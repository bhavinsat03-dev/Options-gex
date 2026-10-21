"""One-image colour summary of a run: a table whose cells are shaded by value."""

from __future__ import annotations

from datetime import date
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
SEQUENTIAL = LinearSegmentedColormap.from_list("gex_seq", [NEUTRAL, "#b7d3f6", "#5598e7", "#1c5cab"])

# (header, sub-header, width in inches)
COLUMNS = [
    ("Ticker", "", 0.9), ("Spot", "", 1.0), ("Regime", "", 1.55), ("Vs flip", "σ from zero-γ", 1.15),
    ("γ balance", "net ÷ gross GEX", 1.35), ("Net GEX", "per 1%", 1.1), ("Call wall", "OI · σ away", 1.45),
    ("Put wall", "OI · σ away", 1.45), ("IV", "25-delta call", 0.85), ("Exp. move", "ATM straddle", 1.0),
    ("P/C OI", "", 0.8), ("Earnings", "", 1.05),
]
ROW_H, HEAD_H = 0.62, 0.9


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
    try:
        today = date.fromisoformat(as_of[:10])
    except ValueError:
        today = None

    width = sum(c[2] for c in COLUMNS)
    top = 0.75
    height = top + HEAD_H + ROW_H * len(rows) + 0.85
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

        cell(0, ri, ticker, bold=True)
        cell(1, ri, f"{s['spot']:,.2f}")
        cell(2, ri, "● positive" if positive else "● negative", fill=POSITIVE if positive else NEGATIVE,
             sub="near flip" if near else None, border=WARN if near else None)
        if vs_flip is None:
            cell(3, ri, "–")
        else:
            cell(3, ri, f"{vs_flip:+.1f}σ", fill=DIVERGING((_clip(vs_flip, -3, 3) + 3) / 6), border=WARN if near else None)
        call_gex, put_gex = s.get("call_gex"), s.get("put_gex")
        if net is not None and call_gex is not None and put_gex is not None and call_gex - put_gex:
            balance = net / (call_gex - put_gex)
            cell(4, ri, f"{balance:+.0%}", fill=DIVERGING(_clip(balance, -0.5, 0.5) + 0.5))
        else:
            cell(4, ri, "–")
        cell(5, ri, _flow(net), fill=None if net is None else DIVERGING(0.8 if net >= 0 else 0.2))
        for ci, strike, oi in ((6, s.get("call_wall"), s.get("call_wall_oi")), (7, s.get("put_wall"), s.get("put_wall_oi"))):
            if strike is None:
                cell(ci, ri, "–")
                continue
            sigma = _sigma(s, strike)
            parts = ([f"{oi:,}"] if oi is not None else []) + ([f"{sigma:+.1f}σ"] if sigma is not None else [])
            cell(ci, ri, f"{strike:g}", sub=" · ".join(parts) or None,
                 fill=SEQUENTIAL(max(0.0, 1 - abs(sigma) / 3)) if sigma is not None else None)
        skew = s.get("skew_25d")
        if skew:
            iv = skew["call_iv"]
            cell(8, ri, f"{iv * 100:.0f}%", fill=SEQUENTIAL(_clip((iv - 0.1) / 0.5, 0, 1)))
        else:
            cell(8, ri, "–")
        em = s.get("expected_move")
        cell(9, ri, f"±{em['move_pct']:.1f}%" if em else "–")
        pc = s.get("put_call_oi_ratio")
        cell(10, ri, "–" if pc is None else f"{pc:.2f}",
             fill=None if pc is None else DIVERGING(_clip(0.5 - (pc - 1) / 3, 0, 1)))
        earnings = s.get("earnings_date")
        if not earnings:
            cell(11, ri, "–")
        else:
            when = date.fromisoformat(earnings)
            if today is not None and 0 <= (when - today).days <= 3:
                cell(11, ri, "▲ " + ("today" if when == today else when.strftime("%b %d")), fill=WARN, bold=True,
                     sub="this week")
            else:
                cell(11, ri, when.strftime("%b %d"), border=MUTED)

    ly = top + HEAD_H + ROW_H * len(rows) + 0.35
    items = [(POSITIVE, "positive gamma / call-heavy"), (NEGATIVE, "negative gamma / put-heavy"),
             ("#1c5cab", "darker blue = wall closer to spot · higher IV"),
             (WARN, "yellow = near flip (<1σ) · earnings within 3 days")]
    lx = 0.1
    for color, label in items:
        outline = color == WARN
        ax.add_patch(FancyBboxPatch((lx, ly - 0.1), 0.22, 0.2, boxstyle="round,pad=0,rounding_size=0.04",
                                    fc="none" if outline else color, ec=color if outline else "none", lw=2))
        ax.text(lx + 0.3, ly, label, fontsize=8, color=INK_SECONDARY, va="center")
        lx += 0.55 + len(label) * 0.075
    note = ("σ = one expected move (ATM straddle). γ balance = net GEX ÷ (call GEX + |put GEX|), "
            "so tickers of different size compare on one scale.")
    if any(s.get("derived") for s in rows):
        note += " * levels derived from a proxy."
    ax.text(0.1, ly + 0.42, note, fontsize=7.5, color=MUTED, va="center")

    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, facecolor=SURFACE, bbox_inches="tight", pad_inches=0.15)
    plt.close(fig)
    return path
