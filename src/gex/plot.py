"""Charts for a GEX result."""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402

from .gex import GexResult  # noqa: E402

SURFACE = "#fcfcfb"
INK = "#0b0b0b"
INK_SECONDARY = "#52514e"
GRID = "#e4e3df"
CALL = "#2a78d6"
PUT = "#e34948"


def _fmt_dollars(x, _pos=None) -> str:
    sign = "\u2212" if x < 0 else ""
    x = abs(x)
    for div, suffix in ((1e9, "B"), (1e6, "M"), (1e3, "K")):
        if x >= div:
            return f"{sign}${x / div:,.1f}{suffix}"
    return f"{sign}${x:,.0f}"


def _style(ax):
    ax.set_facecolor(SURFACE)
    ax.grid(axis="y", color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(GRID)
    ax.tick_params(colors=INK_SECONDARY, labelsize=9)
    ax.yaxis.set_major_formatter(FuncFormatter(_fmt_dollars))
    ax.axhline(0, color=INK_SECONDARY, linewidth=0.8)


def _level(ax, x, label, style, color=INK_SECONDARY):
    """Vertical reference line, identified (with its value) in the legend."""
    if x is None:
        return
    ax.axvline(x, color=color, linestyle=style, linewidth=1.5, label=f"{label} {x:,.2f}")


def plot_result(result: GexResult, path: Path) -> Path:
    bs = result.by_strike
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 9), facecolor=SURFACE)

    width = (bs["strike"].diff().median() if len(bs) > 1 else 1.0) * 0.8
    ax1.bar(bs["strike"], bs["call_gex"], width=width, color=CALL, label="Call GEX")
    ax1.bar(bs["strike"], bs["put_gex"], width=width, color=PUT, label="Put GEX")
    ax1.plot(bs["strike"], bs["net_gex"], color=INK, linewidth=2, label="Net GEX")
    _style(ax1)
    _level(ax1, result.spot, "Spot", "-")
    _level(ax1, result.call_wall, "Call wall", "--", CALL)
    _level(ax1, result.put_wall, "Put wall", "--", PUT)
    _level(ax1, result.zero_gamma, "Zero γ", ":")
    ax1.set_title(
        f"{result.ticker} gamma exposure by strike ($ per 1% move)",
        loc="left", color=INK, fontsize=12,
    )
    ax1.set_xlabel("Strike", color=INK_SECONDARY)
    ax1.legend(frameon=False, fontsize=9, loc="lower left", ncols=2)

    prof = result.profile
    ax2.plot(prof["spot"], prof["net_gex"], color=INK, linewidth=2, label="Net GEX")
    ax2.fill_between(prof["spot"], prof["net_gex"], 0, where=prof["net_gex"] >= 0,
                     color=CALL, alpha=0.15, linewidth=0)
    ax2.fill_between(prof["spot"], prof["net_gex"], 0, where=prof["net_gex"] < 0,
                     color=PUT, alpha=0.15, linewidth=0)
    _style(ax2)
    _level(ax2, result.spot, "Spot", "-")
    _level(ax2, result.zero_gamma, "Zero γ", ":")
    ax2.set_title("Total net GEX vs. underlying price", loc="left", color=INK, fontsize=12)
    ax2.set_xlabel("Underlying price", color=INK_SECONDARY)
    ax2.legend(frameon=False, fontsize=9, loc="lower right")

    fig.tight_layout()
    fig.savefig(path, dpi=120, facecolor=SURFACE)
    plt.close(fig)
    return path
