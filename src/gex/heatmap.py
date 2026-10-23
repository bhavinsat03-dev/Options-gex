"""One-image colour summary of a run: a table whose cells are shaded by value."""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.colors import LinearSegmentedColormap, to_rgb  # noqa: E402
from matplotlib.patches import FancyBboxPatch, Rectangle  # noqa: E402

SURFACE = "#fcfcfb"
STRIPE = "#f6f6f4"
INK = "#0b0b0b"
INK_SECONDARY = "#52514e"
MUTED = "#898781"
POSITIVE = "#2a78d6"  # blue: positive gamma, call-heavy (blue/red stays readable for colour-blind viewers)
NEGATIVE = "#e34948"  # red: negative gamma, put-heavy
NEUTRAL = "#f0efec"
WARN = "#fab219"

DIVERGING = LinearSegmentedColormap.from_list("gex_div", [NEGATIVE, "#f2a3a2", NEUTRAL, "#9ec5f4", POSITIVE])
CALL_RAMP = LinearSegmentedColormap.from_list("gex_call", [NEUTRAL, "#b7d3f6", "#5598e7", "#1c5cab"])
PUT_RAMP = LinearSegmentedColormap.from_list("gex_put", [NEUTRAL, "#f6c1c0", "#e86a69", "#b52f2e"])

# Same columns, in the same order, as table 1 of the brief.
# (header, sub-header, width in inches)
COLUMNS = [
    ("Ticker", "", 0.85), ("Spot", "", 0.95), ("Regime", "", 1.5), ("Vs flip", "% · σ", 1.15),
    ("Zero γ", "flip level", 1.05), ("Net GEX", "per 1%", 1.1), ("Call GEX", "", 1.1), ("Put GEX", "", 1.1),
    ("Call wall", "OI · σ away", 1.6), ("Put wall", "OI · σ away", 1.6),
    ("Next call", "walls 2 & 3", 1.25), ("Next put", "walls 2 & 3", 1.25),
]
ROW_H, HEAD_H = 0.62, 0.9
SAME_DAY_PCT = 50  # mark a wall "0DTE" when more than this % of its OI expires today


def _flow(x) -> str:
    if x is None:
        return "–"
    a = abs(x)
    v = f"${a / 1e9:.2f}B" if a >= 1e9 else f"${a / 1e6:.0f}M"
    return ("+" if x >= 0 else "−") + v


def _sigma(s: dict, level) -> float | None:
    em = s.get("expected_move")
    if level is None or not em or not em.get("move_pct"):
        return None
    return (level / s["spot"] - 1) * 100 / em["move_pct"]


def _ink_for(rgb) -> str:
    r, g, b = rgb
    return INK if 0.2126 * r + 0.7152 * g + 0.0722 * b > 0.55 else "#ffffff"


def _clip(x, lo, hi):
    return max(lo, min(hi, x))


def render(summaries: list[dict], path: Path, as_of: str, title: str = "GEX heatmap") -> Path | None:
    """Draw the heatmap for the summaries that computed, or return None if there are none."""
    rows = [s for s in summaries if not str(s.get("status", "ok")).startswith("error")]
    if not rows:
        return None
    width = sum(c[2] for c in COLUMNS)
    top = 0.75
    height = top + HEAD_H + ROW_H * len(rows) + 1.1
    fig, ax = plt.subplots(figsize=(width, height), dpi=150)
    fig.patch.set_facecolor(SURFACE)
    ax.set_facecolor(SURFACE)
    ax.set_xlim(0, width)
    ax.set_ylim(height, 0)
    ax.axis("off")

    ax.text(0.05, 0.3, title, fontsize=15, weight="bold", color=INK, va="center")
    ax.text(0.05, 0.62, f"{as_of} · descriptive only, not trading advice", fontsize=8.5, color=INK_SECONDARY, va="center")

    xs, x = [], 0.0
    for head, sub, w in COLUMNS:
        xs.append(x)
        ax.text(x + 0.08, top + 0.3, head, fontsize=9.5, weight="bold", color=INK, va="center")
        if sub:
            ax.text(x + 0.08, top + 0.6, sub, fontsize=7, color=MUTED, va="center")
        x += w
    ax.plot([0, width], [top + HEAD_H - 0.05] * 2, color=MUTED, lw=0.8)

    def cell(ci, ri, text, fill=None, bold=False, sub=None, border=None):
        x0, w = xs[ci], COLUMNS[ci][2]
        y0 = top + HEAD_H + ri * ROW_H
        color = INK
        if fill is not None or border:
            rgb = (to_rgb(fill) if isinstance(fill, str) else fill[:3]) if fill is not None else None
            ax.add_patch(FancyBboxPatch(
                (x0 + 0.04, y0 + 0.05), w - 0.08, ROW_H - 0.1, boxstyle="round,pad=0,rounding_size=0.06",
                fc=rgb if rgb else "none", ec=border or "none", lw=2.2 if border else 0))
            if rgb:
                color = _ink_for(rgb)
        yy = y0 + ROW_H / 2 - (0.09 if sub else 0)
        ax.text(x0 + 0.1, yy, text, fontsize=9, color=color, va="center", weight="bold" if bold else "normal")
        if sub:
            ax.text(x0 + 0.1, yy + 0.2, sub, fontsize=7, color=color if fill is not None else INK_SECONDARY, va="center")

    for ri, s in enumerate(rows):
        if ri % 2:
            ax.add_patch(Rectangle((0, top + HEAD_H + ri * ROW_H), width, ROW_H, fc=STRIPE, ec="none", zorder=-1))
        net = s.get("net_gex")
        positive = s.get("regime", "").startswith("positive")
        flip_sigma = _sigma(s, s.get("zero_gamma"))
        vs_flip = -flip_sigma if flip_sigma is not None else None
        near = vs_flip is not None and abs(vs_flip) < 1
        ticker = s["ticker"] + ("*" if s.get("derived") else "")

        call_gex, put_gex = s.get("call_gex"), s.get("put_gex")
        gross = (call_gex - put_gex) if call_gex is not None and put_gex is not None else 0

        cell(0, ri, ticker, bold=True)
        cell(1, ri, f"{s['spot']:,.2f}")
        cell(2, ri, "● positive" if positive else "● negative", fill=POSITIVE if positive else NEGATIVE,
             sub="near flip" if near else None, border=WARN if near else None)
        zg = s.get("zero_gamma")
        if vs_flip is None or not zg:
            cell(3, ri, "–")
        else:
            cell(3, ri, f"{(s['spot'] / zg - 1) * 100:+.2f}%", sub=f"{vs_flip:+.1f}σ",
                 fill=DIVERGING((_clip(vs_flip, -3, 3) + 3) / 6), border=WARN if near else None)
        cell(4, ri, "–" if zg is None else f"{zg:,.2f}")
        # Net GEX is shaded by net ÷ gross GEX, so tickers of very different size share one scale.
        cell(5, ri, _flow(net), fill=DIVERGING(_clip(net / gross, -0.5, 0.5) + 0.5) if net is not None and gross else None)
        # Call and put GEX are shaded by their share of gross GEX: darker = that side dominates.
        cell(6, ri, _flow(call_gex), fill=CALL_RAMP(_clip((call_gex / gross - 0.3) / 0.4, 0, 1)) if gross else None)
        cell(7, ri, _flow(put_gex), fill=PUT_RAMP(_clip((-put_gex / gross - 0.3) / 0.4, 0, 1)) if gross else None)
        for ci, strike, oi, same_day, ramp in (
                (8, s.get("call_wall"), s.get("call_wall_oi"), s.get("call_wall_0dte_pct"), CALL_RAMP),
                (9, s.get("put_wall"), s.get("put_wall_oi"), s.get("put_wall_0dte_pct"), PUT_RAMP)):
            if strike is None:
                cell(ci, ri, "–")
                continue
            sigma = _sigma(s, strike)
            parts = ([f"{oi:,}"] if oi is not None else []) + ([f"{sigma:+.1f}σ"] if sigma is not None else [])
            if same_day is not None and same_day > SAME_DAY_PCT:
                parts.append("0DTE")
            cell(ci, ri, f"{strike:g}", sub=" · ".join(parts) or None,
                 fill=ramp(max(0.0, 1 - abs(sigma) / 3)) if sigma is not None else None)
        cell(10, ri, " / ".join(f"{k:g}" for k in s.get("call_walls", [])[1:]) or "–")
        cell(11, ri, " / ".join(f"{k:g}" for k in s.get("put_walls", [])[1:]) or "–")

    ly = top + HEAD_H + ROW_H * len(rows) + 0.35
    items = [(POSITIVE, "positive gamma / calls dominate"), (NEGATIVE, "negative gamma / puts dominate"),
             ("#1c5cab", "darker = wall closer to spot"),
             (WARN, "yellow outline = near flip (spot within 1σ of zero gamma)")]
    lx = 0.1
    for color, label in items:
        outline = color == WARN
        ax.add_patch(FancyBboxPatch((lx, ly - 0.1), 0.22, 0.2, boxstyle="round,pad=0,rounding_size=0.04",
                                    fc="none" if outline else color, ec=color if outline else "none", lw=2))
        ax.text(lx + 0.3, ly, label, fontsize=8, color=INK_SECONDARY, va="center")
        lx += 0.55 + len(label) * 0.075
    note = ("σ = one expected move (ATM straddle). Net GEX shading = net ÷ (call GEX + |put GEX|); "
            "call and put GEX shading = each side's share of that total, so tickers of different size compare.")
    if any(s.get("derived") for s in rows):
        note += " * levels derived from a proxy."
    ax.text(0.1, ly + 0.42, note, fontsize=7.5, color=MUTED, va="center")
    late = "0DTE = most of the wall's open interest expires today."
    if any(s.get("walls_skip_expiry") for s in rows):
        late += " Late session: same-day expiries are left out of walls and σ (they expire at the close)."
    ax.text(0.1, ly + 0.7, late, fontsize=7.5, color=MUTED, va="center")

    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, facecolor=SURFACE, bbox_inches="tight", pad_inches=0.15)
    plt.close(fig)
    return path
