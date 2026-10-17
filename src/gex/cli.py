"""Command-line entry point: ``gex [TICKER ...]``."""

from __future__ import annotations

import argparse
import json
import logging
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

from . import data, gex
from .config import Settings, load_settings

log = logging.getLogger("gex")

SUMMARY_COLUMNS = [
    "ticker", "spot", "total_gex", "call_wall", "put_wall", "zero_gamma",
    "regime", "contracts", "expirations", "status",
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
    return settings


def run_ticker(ticker: str, settings: Settings, now: datetime, stamp: str, fetch=data.fetch_chain) -> dict:
    spot, raw = fetch(ticker, settings, now)
    chain = data.clean_chain(raw, spot, now, settings)
    if chain.empty:
        raise data.DataError("no contracts left after cleaning")

    result = gex.compute(
        ticker, chain, spot,
        r=settings.risk_free_rate, q=settings.dividend_yield,
        sweep_pct=settings.sweep_pct, sweep_steps=settings.sweep_steps,
    )

    out_dir = Path(settings.output_dir) / ticker / stamp
    out_dir.mkdir(parents=True, exist_ok=True)
    result.by_strike.to_csv(out_dir / "gex_by_strike.csv", index=False)
    result.contracts.to_csv(out_dir / "contracts.csv", index=False)
    result.profile.to_csv(out_dir / "gex_profile.csv", index=False)
    summary = result.summary()
    summary["as_of"] = now.isoformat(timespec="seconds")
    (out_dir / "summary.json").write_text(json.dumps(summary, indent=2))
    if settings.plots:
        from .plot import plot_result

        plot_result(result, out_dir / "gex.png")
    log.info("%s: wrote %s", ticker, out_dir)
    return summary


def format_table(df: pd.DataFrame) -> str:
    def money(x):
        if pd.isna(x):
            return "-"
        return f"${x / 1e9:,.2f}B" if abs(x) >= 1e8 else f"${x / 1e6:,.1f}M"

    def num(x):
        return "-" if pd.isna(x) else f"{x:,.2f}"

    shown = pd.DataFrame({
        "Ticker": df["ticker"],
        "Spot": df["spot"].map(num),
        "Net GEX/1%": df["total_gex"].map(money),
        "Call wall": df["call_wall"].map(num),
        "Put wall": df["put_wall"].map(num),
        "Zero gamma": df["zero_gamma"].map(num),
        "Regime": df["regime"].fillna("-"),
        "Status": df["status"],
    })
    return shown.to_string(index=False)


def main(argv=None, fetch=data.fetch_chain, now: datetime | None = None) -> int:
    args = parse_args(argv)
    logging.basicConfig(
        level=logging.INFO if args.verbose else logging.WARNING,
        format="%(levelname)s %(name)s: %(message)s",
    )
    settings = build_settings(args)
    now = now or datetime.now(timezone.utc)
    stamp = now.astimezone(data.NY).strftime("%Y%m%d_%H%M%S")

    rows = []
    for i, ticker in enumerate(settings.tickers):
        if i:
            time.sleep(settings.pause_between_tickers)
        try:
            row = run_ticker(ticker, settings, now, stamp, fetch)
            row["status"] = "ok"
        except Exception as exc:  # one bad ticker must not stop the rest
            log.error("%s: %s", ticker, exc)
            row = {"ticker": ticker, "status": f"error: {exc}"}
        rows.append(row)

    table = pd.DataFrame(rows).reindex(columns=SUMMARY_COLUMNS)
    root = Path(settings.output_dir)
    root.mkdir(parents=True, exist_ok=True)
    table.to_csv(root / f"summary_{stamp}.csv", index=False)

    print(format_table(table))
    print(f"\nOutputs written to {root.resolve()}")
    return 0 if (table["status"] == "ok").any() else 1


if __name__ == "__main__":
    sys.exit(main())
