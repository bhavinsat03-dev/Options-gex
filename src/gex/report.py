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


def wall_expiry_text(walls) -> str:
    """'800: 2026-11-20 62%, 2026-10-23 20%; 750: ...'"""
    if not walls:
        return "n/a"
    return "; ".join(
        f"{num(w['strike'])}: " + (", ".join(f"{e['expiration']} {e['pct']:.0f}%" for e in w["expiries"]) or "n/a")
        for w in walls
    )


def oi_expiry_text(entry) -> str:
    """'750 puts, 18,780 OI: 2026-11-20 61% (11,456), 2026-10-23 20% (3,756)'"""
    if not entry:
        return "n/a"
    parts = ", ".join(f"{e['expiration']} {e['pct']:.0f}% ({e['oi']:,})" for e in entry["expiries"])
    return f"{entry['strike']:g} {entry['type']}s, {entry['oi']:,} OI: {parts or 'n/a'}"


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
        ("Call wall expiries", wall_expiry_text(s.get("call_wall_expiries")),
         "For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire."),
        ("Put wall expiries", wall_expiry_text(s.get("put_wall_expiries")),
         "For each put wall, the expirations holding most of its gamma and their share."),
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
        ("Total call / put OI",
         "n/a" if s.get("total_call_oi") is None else f"{s['total_call_oi']:,} calls / {s['total_put_oi']:,} puts",
         "Open contracts across all fetched expirations and strikes."),
        ("Strongest OI strikes",
         "n/a" if s.get("max_call_oi_strike") is None and s.get("max_put_oi_strike") is None
         else f"calls {num(s.get('max_call_oi_strike'))}"
         + (f" ({s['max_call_oi']:,})" if s.get("max_call_oi") is not None else "")
         + f"; puts {num(s.get('max_put_oi_strike'))}"
         + (f" ({s['max_put_oi']:,})" if s.get("max_put_oi") is not None else ""),
         "The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls."),
        ("Wall OI by expiry",
         "; ".join(f"{label} {oi_expiry_text((s.get('oi_expiries') or {}).get(key))}"
                   for key, label in (("call_wall", "call wall"), ("put_wall", "put wall"),
                                      ("max_call_oi", "max call OI"), ("max_put_oi", "max put OI"))),
         "Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date."),
        ("OI at main walls",
         "n/a" if s.get("call_wall_oi") is None and s.get("put_wall_oi") is None
         else f"call wall {num(s.get('call_wall'))}: {s.get('call_wall_oi') or 0:,} calls; put wall {num(s.get('put_wall'))}: {s.get('put_wall_oi') or 0:,} puts",
         "Open contracts at the strongest call and put wall strikes, summed across expirations."),
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


def _flow(x) -> str:
    """Signed compact dollars for the brief: '+$1.23B', '−$45.6M'."""
    if x is None:
        return "-"
    sign = "−" if x < 0 else "+"
    x = abs(x)
    return f"{sign}${x / 1e9:.2f}B" if x >= 1e9 else f"{sign}${x / 1e6:.1f}M"


def _strike_oi(strike, oi) -> str:
    if strike is None:
        return "-"
    return f"{strike:g}" if oi is None else f"{strike:g} ({oi:,})"


def render_brief(summaries: list[dict], as_of: str) -> str:
    """Two-table markdown update: levels, then dealer positioning and volatility."""
    ok = [s for s in summaries if not str(s.get("status", "ok")).startswith("error")]
    lines = [f"## GEX update: {as_of}", "", "### 1) Levels", "",
             "| Ticker | Spot | Regime | Vs flip | Zero gamma | Call wall (OI) | Put wall (OI) "
             "| Next call walls | Next put walls | Abs gamma | Expected move |",
             "|---|---|---|---|---|---|---|---|---|---|---|"]
    for s in ok:
        zg, em = s.get("zero_gamma"), s.get("expected_move")
        vs_flip = f"{(s['spot'] / zg - 1) * 100:+.2f}%" if zg else "-"
        lines.append("| " + " | ".join([
            s["ticker"] + (f" (from {s['derived_from']})" if s.get("derived") else ""),
            num(s["spot"]), s["regime"].split()[0], vs_flip, num(zg),
            _strike_oi(s.get("call_wall"), s.get("call_wall_oi")),
            _strike_oi(s.get("put_wall"), s.get("put_wall_oi")),
            " / ".join(f"{k:g}" for k in s.get("call_walls", [])[1:]) or "-",
            " / ".join(f"{k:g}" for k in s.get("put_walls", [])[1:]) or "-",
            num(s.get("abs_gamma_strike")),
            f"{num(em['low'])}–{num(em['high'])}" if em else "-",
        ]) + " |")
    lines += ["", "### 2) Dealer positioning and volatility", "",
              "| Ticker | Net GEX (per 1%) | Net DEX | Vanna (per vol pt) | Charm (per day) "
              "| Expected move | 25d skew | IV | P/C OI |",
              "|---|---|---|---|---|---|---|---|---|"]
    for s in ok:
        em, sk = s.get("expected_move"), s.get("skew_25d")
        lines.append("| " + " | ".join([
            s["ticker"], _flow(s.get("net_gex")), _flow(s.get("net_dex")),
            _flow(s.get("net_vanna")), _flow(s.get("net_charm")),
            f"±{em['move_pct']:.1f}%" if em else "-",
            f"{sk['skew']:+.1f}" if sk else "-",
            f"{sk['call_iv'] * 100:.0f}%" if sk else "-",
            num(s.get("put_call_oi_ratio")),
        ]) + " |")
    failed = [s for s in summaries if str(s.get("status", "")).startswith("error")]
    if failed:
        lines += ["", "Failed: " + ", ".join(f"{s['ticker']} ({s['status']})" for s in failed)]
    lines += ["", "_Descriptive only; not trading advice._", ""]
    return "\n".join(lines)
