"""Plain-English markdown report for one ticker's run."""

from __future__ import annotations

from pathlib import Path


def money(x) -> str:
    if x is None:
        return "n/a"
    sign = "-" if x < 0 else ""
    x = abs(x)
    if x >= 1e9:
        return f"{sign}${x / 1e9:,.2f}B"
    if x >= 1e6:
        return f"{sign}${x / 1e6:,.1f}M"
    if x >= 1e3:
        return f"{sign}${x / 1e3:,.1f}K"
    return f"{sign}${x:,.0f}"


def num(x, digits: int = 2) -> str:
    return "n/a" if x is None else f"{x:,.{digits}f}"


def pct(x) -> str:
    return "n/a" if x is None else f"{x:.1f}%"


def levels(xs) -> str:
    return ", ".join(num(x) for x in xs) if xs else "n/a"


def _signed(x, money_fmt: bool) -> str:
    text = money(x) if money_fmt else num(x)
    return text if x < 0 else "+" + text


def format_changes(changes: list[dict]) -> list[str]:
    out = []
    for c in changes:
        is_money = c["field"] == "net_gex"
        fmt = money if is_money else num
        out.append(f"{c['label']}: {fmt(c['old'])} -> {fmt(c['new'])} ({_signed(c['change'], is_money)})")
    return out


def metric_rows(s: dict) -> list[tuple[str, str, str]]:
    """(metric, value, explanation) rows for the report."""
    em = s.get("expected_move")
    skew = s.get("skew_25d")
    conc = s.get("expiry_concentration") or {}
    shares = conc.get("pct_abs_gex", {})
    return [
        ("Spot", num(s["spot"]),
         "The underlying price used for every calculation in this run."),
        ("Net GEX", money(s.get("net_gex")),
         "Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it."),
        ("Regime", s["regime"],
         s["regime_description"]),
        ("Call walls (top 3)", levels(s.get("call_walls")),
         "Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies."),
        ("Put walls (top 3)", levels(s.get("put_walls")),
         "Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines."),
        ("Absolute gamma strike", num(s.get("abs_gamma_strike")),
         "The single strike with the most total gamma (calls plus puts), often the strongest price magnet."),
        ("Zero-gamma flip", num(s.get("zero_gamma")),
         "The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them."),
        ("Net DEX", money(s.get("net_dex")),
         "Dollar delta dealers hold from these options; it is what their stock hedge must offset."),
        ("Net vanna", money(s.get("net_vanna")),
         "How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow."),
        ("Net charm", money(s.get("net_charm")),
         "How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged."),
        ("Expected move",
         "n/a" if not em else f"±{num(em['move'])} ({pct(em['move_pct'])}) -> {num(em['low'])} to {num(em['high'])}, exp {em['expiration']}",
         "The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry."),
        ("Put/call OI ratio", num(s.get("put_call_oi_ratio")),
         "Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding."),
        ("25-delta skew",
         "n/a" if not skew else f"{num(skew['skew'])} vol pts (put {pct(skew['put_iv'] * 100)}, call {pct(skew['call_iv'] * 100)}, exp {skew['expiration']})",
         "Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside."),
        ("|GEX| from 0DTE", pct(shares.get("0dte")),
         "Share of total gamma expiring today, which disappears at today's close."),
        ("|GEX| from rest of this week", pct(shares.get("this_week")),
         "Share of total gamma expiring later this week."),
        ("|GEX| from rest of this month", pct(shares.get("this_month")),
         "Share of total gamma expiring after this week but within this calendar month."),
        ("|GEX| beyond this month", pct(shares.get("beyond")),
         "Share of total gamma expiring in later months, the most persistent part of positioning."),
        (f"GEX after monthly expiry ({conc.get('next_monthly_expiry', 'n/a')})",
         f"{money(conc.get('net_gex_after_monthly'))} net, {pct(conc.get('pct_abs_gex_after_monthly'))} of |GEX|",
         "The gamma that will still be in place once the next standard monthly options expire."),
    ]


def _cell(text: str) -> str:
    return str(text).replace("|", "\\|")


def render(summary: dict, changes: list[dict] | None = None, previous_as_of: str | None = None) -> str:
    s = summary
    lines = [f"# {s['ticker']} gamma exposure report", "", f"As of {s.get('as_of', 'n/a')}.", ""]
    if s.get("derived"):
        lines += [
            f"> **Derived levels.** {s['ticker']} option chains were unavailable, so price levels "
            f"are {s['derived_from']} levels multiplied by the spot ratio "
            f"({s['ticker']} spot / {s['derived_from']} spot = {num(s['derived_ratio'], 4)}). "
            f"Dollar exposures are not transferable and are omitted; "
            f"ratios and percentages are {s['derived_from']}'s.",
            "",
        ]
    lines += ["| Metric | Value | What it means |", "|---|---|---|"]
    lines += [f"| {_cell(m)} | {_cell(v)} | {_cell(e)} |" for m, v, e in metric_rows(s)]
    lines.append("")
    if changes:
        lines += [f"## Changes since previous run ({previous_as_of})", ""]
        lines += [f"- {c}" for c in format_changes(changes)]
        lines.append("")
    lines += [
        "_Positioning estimates assume dealers are long calls and short puts and use "
        "Yahoo open interest, which updates once per day. Descriptive only; not trading advice._",
        "",
    ]
    return "\n".join(lines)


def write(path: Path, summary: dict, changes=None, previous_as_of=None) -> Path:
    Path(path).write_text(render(summary, changes, previous_as_of))
    return Path(path)
