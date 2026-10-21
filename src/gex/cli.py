"""Command-line entry point: ``gex [TICKER ...]``."""

from __future__ import annotations

import argparse
import json
import logging
import sys
import time
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import pandas as pd

from . import data, gex, history, pine, report
from .config import Settings, load_settings

log = logging.getLogger("gex")

SUMMARY_COLUMNS = [
    "ticker", "spot", "net_gex", "regime", "call_wall", "put_wall", "abs_gamma_strike",
    "zero_gamma", "call_walls", "put_walls", "net_dex", "net_vanna", "net_charm",
    "expected_move", "em_low", "em_high", "put_call_oi_ratio", "total_call_oi", "total_put_oi",
    "call_wall_oi", "put_wall_oi", "max_call_oi_strike", "max_call_oi", "max_put_oi_strike", "max_put_oi",
    "skew_25d",
    "pct_0dte", "pct_this_week", "pct_this_month", "pct_beyond", "pct_after_monthly",
    "source", "status",
]


def parse_args(argv=None) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        prog="gex",
        description="Gamma exposure, call/put walls and zero-gamma flip from Yahoo option chains.",
    )
    p.add_argument("tickers", nargs="*", help="tickers to run (overrides the config file)")
    p.add_argument("-c", "--config", default="config.toml", help="TOML config (default: config.toml)")
    p.add_argument("-o", "--output-dir", help="output root directory")
    p.add_argument("--max-dte", type=int, help="only use expirations within this many days")
    p.add_argument("--max-expirations", type=int, help="cap on number of expirations per ticker")
    p.add_argument("--strike-range", type=float, help="keep strikes within spot +/- this fraction")
    p.add_argument("--no-plots", action="store_true", help="skip chart generation")
    p.add_argument("--no-history", action="store_true", help="do not save or compare run history")
    p.add_argument("--title", default="GEX update", help="heading for latest/brief.md")
    p.add_argument("--positioning", action="store_true",
                   help="add the positioning-changes section (OI adds/drops, volume vs OI) to brief.md")
    p.add_argument("-v", "--verbose", action="store_true")
    return p.parse_args(argv)


def build_settings(args: argparse.Namespace) -> Settings:
    settings = load_settings(args.config)
    if args.tickers:
        settings.tickers = [t.upper() for t in args.tickers]
    if args.output_dir:
        settings.output_dir = args.output_dir
    if args.max_dte is not None:
        settings.max_dte = args.max_dte
    if args.max_expirations is not None:
        settings.max_expirations = args.max_expirations
    if args.strike_range is not None:
        settings.strike_range_pct = args.strike_range
    if args.no_plots:
        settings.plots = False
    if args.no_history:
        settings.history = False
    return settings


class Runner:
    """Runs tickers for one timestamped invocation and writes their outputs."""

    def __init__(self, settings: Settings, now: datetime, fetch=data.fetch_chain,
                 fetch_spot=data.fetch_spot_only, fetch_earnings=data.fetch_earnings_date):
        self.settings = settings
        self.now = now
        self.stamp = now.astimezone(data.NY).strftime("%Y%m%d_%H%M%S")
        self.today = now.astimezone(data.NY).date()
        self.root = Path(settings.output_dir)
        self.history_dir = self.root / "history"
        self.fetch = fetch
        self.fetch_spot = fetch_spot
        self.fetch_earnings = fetch_earnings
        self.summaries: dict[str, dict] = {}
        self.changes: dict[str, tuple[str, list[dict]]] = {}

    def compute(self, ticker: str) -> dict:
        """Full calculation from the ticker's own option chain."""
        if ticker in self.summaries:
            return self.summaries[ticker]
        s = self.settings
        spot, raw = self.fetch(ticker, s, self.now)
        chain = data.clean_chain(raw, spot, self.now, s)
        if chain.empty:
            raise data.DataError("no contracts left after cleaning")

        result = gex.compute(
            ticker, chain, spot, self.today,
            r=s.risk_free_rate, q=s.dividend_yield,
            sweep_pct=s.sweep_pct, sweep_steps=s.sweep_steps,
            n_walls=s.top_walls, skew_target_days=s.skew_target_days, raw=raw,
        )
        out_dir = self._out_dir(ticker)
        result.by_strike.to_csv(out_dir / "gex_by_strike.csv", index=False)
        result.contracts.to_csv(out_dir / "contracts.csv", index=False)
        result.profile.to_csv(out_dir / "gamma_profile.csv", index=False)
        if s.plots:
            from .plot import plot_result

            plot_result(result, out_dir)
        summary = result.summary()
        summary["earnings_date"] = self._earnings_in_window(ticker)
        return self._finish(summary, out_dir, result.contracts)

    def _earnings_in_window(self, ticker: str) -> str | None:
        """Next earnings date if it falls inside the expiry window, else None."""
        earnings = self.fetch_earnings(ticker, self.settings, self.today)
        if not earnings:
            return None
        days = (date.fromisoformat(earnings) - self.today).days
        return earnings if 0 <= days <= self.settings.max_dte else None

    def derive(self, ticker: str, proxy: str) -> dict:
        """Levels for ``ticker`` mapped from ``proxy`` by spot ratio."""
        proxy_summary = self.compute(proxy)
        spot = self.fetch_spot(ticker, self.settings)
        summary = gex.derive_summary(proxy_summary, ticker, spot)
        return self._finish(summary, self._out_dir(ticker))

    def run(self, ticker: str) -> dict:
        try:
            summary = self.compute(ticker)
            return dict(summary, status="ok")
        except Exception as exc:  # one bad ticker must not stop the rest
            proxy = self.settings.proxies.get(ticker)
            if not proxy or proxy == ticker:
                log.error("%s: %s", ticker, exc)
                return {"ticker": ticker, "status": f"error: {exc}"}
            log.warning("%s: %s; deriving levels from %s", ticker, exc, proxy)
            try:
                summary = self.derive(ticker, proxy)
                return dict(summary, status=f"derived from {proxy}")
            except Exception as exc2:
                log.error("%s: %s; derivation from %s failed: %s", ticker, exc, proxy, exc2)
                return {"ticker": ticker, "status": f"error: {exc}; derive failed: {exc2}"}

    def _out_dir(self, ticker: str) -> Path:
        out_dir = self.root / ticker / self.stamp
        out_dir.mkdir(parents=True, exist_ok=True)
        return out_dir

    def _finish(self, summary: dict, out_dir: Path, contracts: pd.DataFrame | None = None) -> dict:
        ticker = summary["ticker"]
        summary["as_of"] = self.now.isoformat(timespec="seconds")
        changes, previous_as_of = [], None
        if self.settings.history:
            previous = history.load_previous(self.history_dir, ticker, self.stamp)
            if previous:
                changes = history.diff(previous, summary)
                previous_as_of = previous.get("as_of")
                self.changes[ticker] = (previous_as_of, changes)
            if contracts is not None:
                # OI is published once a day, so compare against the previous day's snapshot.
                summary["oi_changes"] = gex.oi_changes(
                    contracts, history.load_previous_day_oi(self.history_dir, ticker, self.stamp))
                history.save_oi(self.history_dir, ticker, self.stamp, contracts)
            history.save(self.history_dir, summary, self.stamp)
        (out_dir / "summary.json").write_text(json.dumps(summary, indent=2))
        report.write(out_dir / "report.md", summary, changes, previous_as_of)
        pine.write(out_dir, self.root / "latest", summary)
        log.info("%s: wrote %s", ticker, out_dir)
        self.summaries[ticker] = summary
        return summary


def flat_row(summary: dict) -> dict:
    """Flatten a summary into one row of the combined table."""
    row = {k: summary.get(k) for k in SUMMARY_COLUMNS}
    if summary.get("status", "").startswith("error"):
        return row
    row["call_walls"] = " ".join(f"{k:g}" for k in summary.get("call_walls", []))
    row["put_walls"] = " ".join(f"{k:g}" for k in summary.get("put_walls", []))
    em = summary.get("expected_move")
    if em:
        row.update(expected_move=em["move"], em_low=em["low"], em_high=em["high"])
    skew = summary.get("skew_25d")
    row["skew_25d"] = skew["skew"] if skew else None
    conc = summary.get("expiry_concentration") or {}
    shares = conc.get("pct_abs_gex", {})
    row.update(
        pct_0dte=shares.get("0dte"), pct_this_week=shares.get("this_week"),
        pct_this_month=shares.get("this_month"), pct_beyond=shares.get("beyond"),
        pct_after_monthly=conc.get("pct_abs_gex_after_monthly"),
    )
    row["source"] = f"derived from {summary['derived_from']}" if summary.get("derived") else "chain"
    return row


def _strike_oi(strike, oi) -> str:
    """'800 (51,793)'; the OI part is omitted when unknown (derived tickers)."""
    if pd.isna(strike):
        return "-"
    return f"{strike:g}" if pd.isna(oi) else f"{strike:g} ({oi:,.0f})"


def format_table(df: pd.DataFrame) -> str:
    def opt(fn):
        return lambda x: "-" if pd.isna(x) else fn(x)

    def em(r):
        if pd.isna(r["em_low"]):
            return "-"
        return f"{r['em_low']:,.2f}-{r['em_high']:,.2f}"

    shown = pd.DataFrame({
        "Ticker": df["ticker"] + df["source"].map(lambda s: "*" if str(s).startswith("derived") else ""),
        "Spot": df["spot"].map(opt(report.num)),
        "Net GEX/1%": df["net_gex"].map(opt(report.money)),
        "Regime": df["regime"].fillna("-"),
        "Call wall": df["call_wall"].map(opt(report.num)),
        "Put wall": df["put_wall"].map(opt(report.num)),
        "Abs gamma": df["abs_gamma_strike"].map(opt(report.num)),
        "Zero gamma": df["zero_gamma"].map(opt(report.num)),
        "Exp. move": df.apply(em, axis=1),
        "Max call OI": df.apply(lambda r: _strike_oi(r["max_call_oi_strike"], r["max_call_oi"]), axis=1),
        "Max put OI": df.apply(lambda r: _strike_oi(r["max_put_oi_strike"], r["max_put_oi"]), axis=1),
        "P/C OI": df["put_call_oi_ratio"].map(opt(report.num)),
        "25d skew": df["skew_25d"].map(opt(lambda x: f"{x:.1f}")),
        "Status": df["status"],
    })
    return shown.to_string(index=False)


def main(argv=None, fetch=data.fetch_chain, fetch_spot=data.fetch_spot_only,
         fetch_earnings=data.fetch_earnings_date, now: datetime | None = None) -> int:
    args = parse_args(argv)
    logging.basicConfig(
        level=logging.INFO if args.verbose else logging.WARNING,
        format="%(levelname)s %(name)s: %(message)s",
    )
    settings = build_settings(args)
    runner = Runner(settings, now or datetime.now(timezone.utc), fetch, fetch_spot, fetch_earnings)

    rows, results = [], []
    for i, ticker in enumerate(settings.tickers):
        if i:
            time.sleep(settings.pause_between_tickers)
        result = runner.run(ticker)
        results.append(result)
        rows.append(flat_row(result))

    table = pd.DataFrame(rows).reindex(columns=SUMMARY_COLUMNS)
    runner.root.mkdir(parents=True, exist_ok=True)
    table.to_csv(runner.root / f"summary_{runner.stamp}.csv", index=False)

    latest = runner.root / "latest"
    latest.mkdir(parents=True, exist_ok=True)
    as_of = runner.now.astimezone(data.NY).strftime("%Y-%m-%d %H:%M ET")
    window_end = runner.today + timedelta(days=settings.max_dte)
    window = f"Options expiring {runner.today:%b %d} to {window_end:%b %d} (rolling {settings.max_dte} days)."
    previous = {
        r["ticker"]: history.load_previous_day(runner.history_dir, r["ticker"], runner.stamp)
        for r in results if not str(r.get("status", "")).startswith("error")
    } if settings.history else None
    (latest / "brief.md").write_text(report.render_brief(results, as_of, window, previous, args.title, args.positioning))

    print(format_table(table))
    if table["source"].astype(str).str.startswith("derived").any():
        print("\n* derived: levels mapped from a proxy by spot ratio (that ticker's own chain was unavailable)")
    for ticker, (previous_as_of, changes) in runner.changes.items():
        if ticker in settings.tickers and changes:
            print(f"\n{ticker} changes since {previous_as_of}:")
            for line in report.format_changes(changes):
                print(f"  {line}")
    for summary in runner.summaries.values():
        if summary["ticker"] in settings.tickers and summary.get("call_wall_expiries"):
            print(f"\n{summary['ticker']} wall expiries:")
            print(f"  Calls: {report.wall_expiry_text(summary['call_wall_expiries'])}")
            print(f"  Puts:  {report.wall_expiry_text(summary.get('put_wall_expiries'))}")
    print(f"\nOutputs written to {runner.root.resolve()}")
    return 0 if table["status"].astype(str).map(lambda s: not s.startswith("error")).any() else 1


if __name__ == "__main__":
    sys.exit(main())
