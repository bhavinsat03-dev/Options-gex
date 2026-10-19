"""TradingView output: a one-line levels string and a Pine Script indicator.

The indicator reads every level from a single text input, so after adding
it to a chart once, updating it is a matter of pasting the latest levels
string into its settings. The generated .pine file also has that run's
levels baked in as the default, for a fresh add.
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

NY = ZoneInfo("America/New_York")

LEVELS_TOKEN = "__LEVELS__"


def _n(x) -> str:
    return f"{x:.2f}".rstrip("0").rstrip(".")


def levels_string(summary: dict) -> str:
    """Compact ``KEY=value;...`` string the Pine indicator parses.

    SYM ticker, ASOF timestamp, CW call walls, PW put walls, ZG zero gamma,
    AG absolute gamma strike, OC/OP max call/put OI strikes, EM expected-move low,high, REG regime,
    SRC 'chain' or the proxy ticker the levels were derived from.
    """
    parts = [f"SYM={summary['ticker']}"]
    as_of = summary.get("as_of")
    if as_of:
        parts.append("ASOF=" + datetime.fromisoformat(as_of).astimezone(NY).strftime("%Y-%m-%d %H:%M ET"))
    if summary.get("call_walls"):
        parts.append("CW=" + ",".join(_n(k) for k in summary["call_walls"]))
    if summary.get("put_walls"):
        parts.append("PW=" + ",".join(_n(k) for k in summary["put_walls"]))
    if summary.get("zero_gamma") is not None:
        parts.append(f"ZG={_n(summary['zero_gamma'])}")
    if summary.get("abs_gamma_strike") is not None:
        parts.append(f"AG={_n(summary['abs_gamma_strike'])}")
    if summary.get("max_call_oi_strike") is not None:
        parts.append(f"OC={_n(summary['max_call_oi_strike'])}")
    if summary.get("max_put_oi_strike") is not None:
        parts.append(f"OP={_n(summary['max_put_oi_strike'])}")
    em = summary.get("expected_move")
    if em:
        parts.append(f"EM={_n(em['low'])},{_n(em['high'])}")
    if summary.get("regime"):
        parts.append(f"REG={summary['regime']}")
    parts.append(f"SRC={summary['derived_from'] if summary.get('derived') else 'chain'}")
    return ";".join(parts)


PINE_TEMPLATE = """//@version=6
// GEX levels from options-gex. Paste the latest line from
// output/latest/<TICKER>_tradingview.txt into the "Levels" setting.
indicator("GEX levels", overlay = true, max_lines_count = 50, max_labels_count = 50)

levels     = input.string("__LEVELS__", "Levels (paste from <TICKER>_tradingview.txt)")
showLabels = input.bool(true, "Show labels")
showEM     = input.bool(true, "Show expected move band")
callCol    = input.color(#2a78d6, "Call walls")
putCol     = input.color(#e34948, "Put walls")
flipCol    = input.color(#52514e, "Zero gamma")
absCol     = input.color(#6250d6, "Absolute gamma strike")
emCol      = input.color(color.new(#888888, 88), "Expected move band")

field(string src, string key) =>
    string result = ""
    for part in str.split(src, ";")
        kv = str.split(part, "=")
        if kv.size() == 2 and kv.get(0) == key
            result := kv.get(1)
    result

numbers(string s) =>
    array<float> out = array.new_float()
    if s != ""
        for p in str.split(s, ",")
            v = str.tonumber(p)
            if not na(v)
                out.push(v)
    out

var array<line> drawnLines = array.new_line()
var array<label> drawnLabels = array.new_label()
var array<linefill> drawnFills = array.new_linefill()

drawLevel(float price, color col, string txt, string style, int width) =>
    drawnLines.push(line.new(bar_index - 1, price, bar_index, price, extend = extend.both, color = col, style = style, width = width))
    if showLabels
        drawnLabels.push(label.new(bar_index + 3, price, txt + " " + str.tostring(price, format.mintick), style = label.style_label_left, color = color(na), textcolor = col, size = size.small))

if barstate.islast
    // Redraw from scratch on every realtime update.
    while drawnLines.size() > 0
        drawnLines.pop().delete()
    while drawnLabels.size() > 0
        drawnLabels.pop().delete()
    while drawnFills.size() > 0
        drawnFills.pop().delete()

    sym = field(levels, "SYM")
    src = field(levels, "SRC")
    tag = src != "" and src != "chain" ? " (from " + src + ")" : ""

    callWalls = numbers(field(levels, "CW"))
    for [i, k] in callWalls
        drawLevel(k, callCol, "Call wall " + str.tostring(i + 1) + tag, line.style_dashed, i == 0 ? 2 : 1)
    putWalls = numbers(field(levels, "PW"))
    for [i, k] in putWalls
        drawLevel(k, putCol, "Put wall " + str.tostring(i + 1) + tag, line.style_dashed, i == 0 ? 2 : 1)

    zg = str.tonumber(field(levels, "ZG"))
    if not na(zg)
        drawLevel(zg, flipCol, "Zero gamma" + tag, line.style_dotted, 2)
    oc = str.tonumber(field(levels, "OC"))
    if not na(oc)
        drawLevel(oc, callCol, "Max call OI" + tag, line.style_dotted, 1)
    op = str.tonumber(field(levels, "OP"))
    if not na(op)
        drawLevel(op, putCol, "Max put OI" + tag, line.style_dotted, 1)
    ag = str.tonumber(field(levels, "AG"))
    if not na(ag)
        drawLevel(ag, absCol, "Abs gamma" + tag, line.style_dashed, 1)

    em = numbers(field(levels, "EM"))
    if showEM and em.size() == 2
        lo = line.new(bar_index - 1, em.get(0), bar_index, em.get(0), extend = extend.both, color = color(na))
        hi = line.new(bar_index - 1, em.get(1), bar_index, em.get(1), extend = extend.both, color = color(na))
        drawnLines.push(lo)
        drawnLines.push(hi)
        drawnFills.push(linefill.new(lo, hi, emCol))

    var table info = table.new(position.top_right, 1, 3, bgcolor = color.new(color.white, 10), border_width = 0)
    mismatch = sym != "" and sym != syminfo.ticker
    info.cell(0, 0, "GEX " + sym + tag, text_color = color.black, text_size = size.small)
    info.cell(0, 1, field(levels, "REG") + "  |  as of " + field(levels, "ASOF"), text_color = color.black, text_size = size.small)
    info.cell(0, 2, mismatch ? "Levels are for " + sym + ", chart is " + syminfo.ticker : "", text_color = color.red, text_size = size.small)
"""


def render_pine(summary: dict) -> str:
    return PINE_TEMPLATE.replace(LEVELS_TOKEN, levels_string(summary))


def write(out_dir: Path, latest_dir: Path, summary: dict) -> None:
    """Write tradingview.pine and tradingview_levels.txt for this run, and
    refresh output/latest/<TICKER>_tradingview.{txt,pine}."""
    line = levels_string(summary)
    pine = render_pine(summary)
    out_dir, latest_dir = Path(out_dir), Path(latest_dir)
    (out_dir / "tradingview_levels.txt").write_text(line + "\n")
    (out_dir / "tradingview.pine").write_text(pine)
    latest_dir.mkdir(parents=True, exist_ok=True)
    (latest_dir / f"{summary['ticker']}_tradingview.txt").write_text(line + "\n")
    (latest_dir / f"{summary['ticker']}_tradingview.pine").write_text(pine)
