"""Plain-English markdown report for one ticker's run."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

NY = ZoneInfo("America/New_York")


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


def _prior_oi(prev: dict | None, side: str, strike: float) -> int | None:
    """OI at ``strike`` in a previous summary, from oi_at or its wall fields."""
    if not prev:
        return None
    at = (prev.get("oi_at") or {}).get(side, {})
    if at:
        return at.get(f"{strike:g}", 0)
    for wall, oi in ((f"{side}_wall", f"{side}_wall_oi"), (f"max_{side}_oi_strike", f"max_{side}_oi")):
        if prev.get(wall) == strike and prev.get(oi) is not None:
            return prev[oi]
    return None


def _date(exp: str) -> str:
    return datetime.strptime(exp, "%Y-%m-%d").strftime("%b %d")


def _sigma(s: dict, level) -> float | None:
    """Distance from spot to ``level`` in expected-move units (1σ = the ATM straddle)."""
    em = s.get("expected_move")
    if level is None or not em or not em.get("move_pct"):
        return None
    return (level / s["spot"] - 1) * 100 / em["move_pct"]


NEAR_FLIP_SIGMA = 1.0


def regime_label(s: dict) -> str:
    """'positive', 'negative', or 'positive, near flip' when spot is within 1σ of it."""
    label = s["regime"].split()[0]
    sigma = _sigma(s, s.get("zero_gamma"))
    if sigma is not None and abs(sigma) < NEAR_FLIP_SIGMA:
        label += ", near flip"
    return label


def _strike_oi_sigma(s: dict, strike, oi) -> str:
    """'770 (53,570; +0.2σ)': wall, its OI and its distance from spot in σ."""
    if strike is None:
        return "-"
    sigma = _sigma(s, strike)
    parts = [] if oi is None else [f"{oi:,}"]
    if sigma is not None:
        parts.append(f"{sigma:+.1f}σ")
    return f"{strike:g} ({'; '.join(parts)})" if parts else f"{strike:g}"


def _contract(c: dict) -> str:
    """'760P Oct 30'"""
    return f"{c['strike']:g}{c['type'][0].upper()} {_date(c['expiration'])}"


def positioning_line(s: dict, prev: dict | None) -> str:
    """OI adds/drops since the previous day and today's high volume-vs-OI contracts."""
    parts = []
    oc = s.get("oi_changes")
    if oc is None:
        parts.append("OI change: no prior day")
    else:
        day = datetime.fromisoformat(prev["as_of"]).astimezone(NY) if prev else None
        label = f" vs {day:%b %d}" if day else ""
        adds = ", ".join(f"{_contract(c)} {c['change']:+,} (OI {c['oi']:,})" for c in oc["adds"] if c["change"] > 0)
        drops = ", ".join(f"{_contract(c)} {c['change']:+,} (OI {c['oi']:,})" for c in oc["drops"] if c["change"] < 0)
        parts.append(f"OI adds{label}: {adds or 'none'}")
        parts.append(f"OI drops{label}: {drops or 'none'}")
    hot = s.get("volume_vs_oi") or []
    parts.append("High volume vs OI today: " + (", ".join(
        f"{_contract(c)} vol {c['volume']:,} ({c['ratio']:.1f}× OI {c['oi']:,})" for c in hot) or "none"))
    return " · ".join(parts)


def key_expiry_line(s: dict, prev: dict | None, show_change: bool = True) -> str:
    """'call wall 770: Nov 20 25%, Oct 23 23% (OI 57,001, +1,234 vs Oct 19) · put wall ...'"""
    parts = []
    for key, side, label in (("call_wall", "call", "call wall"), ("put_wall", "put", "put wall")):
        e = (s.get("oi_expiries") or {}).get(key)
        if not e:
            continue
        exps = ", ".join(f"{_date(x['expiration'])} {x['pct']:.0f}%" for x in e["expiries"][:2])
        before = _prior_oi(prev, side, e["strike"])
        if not show_change:
            parts.append(f"{label} **{e['strike']:g}**: {exps} (OI {e['oi']:,})")
            continue
        if before is None:
            change = "no prior day"
        else:
            day = datetime.fromisoformat(prev["as_of"]).astimezone(NY)
            change = f"{e['oi'] - before:+,} vs {day:%b %d}"
        parts.append(f"{label} **{e['strike']:g}**: {exps} (OI {e['oi']:,}, {change})")
    return " · ".join(parts) or "-"


def render_brief(summaries: list[dict], as_of: str, window: str = "",
                 previous: dict[str, dict] | None = None, title: str = "GEX update") -> str:
    """Two-table markdown update: levels, then dealer positioning and volatility."""
    ok = [s for s in summaries if not str(s.get("status", "ok")).startswith("error")]
    lines = [f"## {title}: {as_of}", ""] + ([window, ""] if window else []) + ["### 1) Levels", "",
             "| Ticker | Spot | Regime | Vs flip | Zero gamma | Net GEX | Call GEX | Put GEX "
             "| Call wall (OI; σ) | Put wall (OI; σ) | Next call walls | Next put walls | Earnings |",
             "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for s in ok:
        zg = s.get("zero_gamma")
        vs_flip = f"{(s['spot'] / zg - 1) * 100:+.2f}%" if zg else "-"
        sigma = _sigma(s, zg)
        if sigma is not None:
            # Spot above the flip is a positive distance; _sigma measures the flip from spot.
            vs_flip += f" ({-sigma:+.1f}σ)"
        lines.append("| " + " | ".join([
            s["ticker"] + (f" (from {s['derived_from']})" if s.get("derived") else ""),
            num(s["spot"]), regime_label(s), vs_flip, num(zg),
            _flow(s.get("net_gex")), _flow(s.get("call_gex")), _flow(s.get("put_gex")),
            _strike_oi_sigma(s, s.get("call_wall"), s.get("call_wall_oi")),
            _strike_oi_sigma(s, s.get("put_wall"), s.get("put_wall_oi")),
            " / ".join(f"{k:g}" for k in s.get("call_walls", [])[1:]) or "-",
            " / ".join(f"{k:g}" for k in s.get("put_walls", [])[1:]) or "-",
            _date(s["earnings_date"]) if s.get("earnings_date") else "-",
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
    # previous=None means history is off: list expiries without the OI change.
    lines += ["", "### 3) Key expiries" + (" and wall OI change" if previous is not None else ""), ""]
    for s in ok:
        prev = (previous or {}).get(s["ticker"])
        lines.append(f"- **{s['ticker']}**: {key_expiry_line(s, prev, previous is not None)}")
    # Positioning changes need the OI snapshots that only history-enabled runs keep.
    if previous is not None:
        lines += ["", "### 4) Positioning changes", ""]
        for s in ok:
            if s.get("derived"):
                continue
            lines.append(f"- **{s['ticker']}**: {positioning_line(s, (previous or {}).get(s['ticker']))}")
        lines += ["", "σ = one expected move (ATM straddle). \"near flip\" = spot within 1σ of the zero-gamma level. "
                  "Earnings shown only when inside the expiry window."]
    failed = [s for s in summaries if str(s.get("status", "")).startswith("error")]
    if failed:
        lines += ["", "Failed: " + ", ".join(f"{s['ticker']} ({s['status']})" for s in failed)]
    lines += ["", "_Descriptive only; not trading advice._", ""]
    return "\n".join(lines)
