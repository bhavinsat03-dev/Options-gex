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


def _new_axes(height: float = 5.5):
    fig, ax = plt.subplots(figsize=(12, height), facecolor=SURFACE)
    return fig, ax


def _save(fig, path: Path) -> Path:
    fig.tight_layout()
    fig.savefig(path, dpi=120, facecolor=SURFACE)
    plt.close(fig)
    return path


def plot_gex_by_strike(result: GexResult, path: Path) -> Path:
    bs = result.by_strike
    fig, ax = _new_axes(6.5)

    em = result.expected_move
    if em:
        ax.axvspan(em["low"], em["high"], color=GRID, alpha=0.6, linewidth=0,
                   label=f"Expected move {em['low']:,.2f}–{em['high']:,.2f} (exp {em['expiration']})")

    width = (bs["strike"].diff().median() if len(bs) > 1 else 1.0) * 0.8
    ax.bar(bs["strike"], bs["call_gex"], width=width, color=CALL, label="Call GEX")
    ax.bar(bs["strike"], bs["put_gex"], width=width, color=PUT, label="Put GEX")
    ax.plot(bs["strike"], bs["net_gex"], color=INK, linewidth=2, label="Net GEX")
    _style(ax)
    _level(ax, result.spot, "Spot", "-")
    _level(ax, result.call_wall, "Call wall", "--", CALL)
    _level(ax, result.put_wall, "Put wall", "--", PUT)
    _level(ax, result.abs_gamma_strike, "Abs gamma", "-.")
    _level(ax, result.zero_gamma, "Zero γ", ":")
    ax.set_title(f"{result.ticker} gamma exposure by strike ($ per 1% move)",
                 loc="left", color=INK, fontsize=12)
    ax.set_xlabel("Strike", color=INK_SECONDARY)
    ax.legend(frameon=False, fontsize=9, loc="upper center", bbox_to_anchor=(0.5, -0.13), ncols=4)
    return _save(fig, path)


def plot_gamma_profile(result: GexResult, path: Path) -> Path:
    prof = result.profile
    fig, ax = _new_axes()
    ax.plot(prof["spot"], prof["net_gex"], color=INK, linewidth=2, label="Net GEX")
    ax.fill_between(prof["spot"], prof["net_gex"], 0, where=prof["net_gex"] >= 0,
                    color=CALL, alpha=0.15, linewidth=0, label="Positive gamma")
    ax.fill_between(prof["spot"], prof["net_gex"], 0, where=prof["net_gex"] < 0,
                    color=PUT, alpha=0.15, linewidth=0, label="Negative gamma")
    _style(ax)
    _level(ax, result.spot, "Spot", "-")
    _level(ax, result.zero_gamma, "Zero γ", ":")
    lo, hi = prof["spot"].iloc[0], prof["spot"].iloc[-1]
    ax.set_title(f"{result.ticker} gamma profile: total net GEX vs. price "
                 f"({lo / result.spot - 1:+.0%} to {hi / result.spot - 1:+.0%})",
                 loc="left", color=INK, fontsize=12)
    ax.set_xlabel("Underlying price", color=INK_SECONDARY)
    ax.legend(frameon=False, fontsize=9, loc="lower right")
    return _save(fig, path)


def plot_result(result: GexResult, out_dir: Path) -> list[Path]:
    out_dir = Path(out_dir)
    return [
        plot_gex_by_strike(result, out_dir / "gex.png"),
        plot_gamma_profile(result, out_dir / "gamma_profile.png"),
    ]
