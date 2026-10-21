from datetime import date

from gex import report


def test_earnings_cell_flags_next_three_days():
    today = date(2026, 10, 20)
    assert report.earnings_cell("2026-10-20", today) == "⚠️ **today**"
    assert report.earnings_cell("2026-10-23", today) == "⚠️ **Oct 23**"
    assert report.earnings_cell("2026-10-24", today) == "📅 Oct 24"
    assert report.earnings_cell(None, today) == "-"


def test_vol_and_ratio_cells():
    assert report.iv_cell({"call_iv": 0.13, "skew": 2.0}) == "🧊 13%"
    assert report.iv_cell({"call_iv": 0.46, "skew": 0.1}) == "🌡️ 46%"
    assert report.iv_cell({"call_iv": 0.60, "skew": 0.1}) == "🔥 60%"
    assert report.skew_cell({"call_iv": 0.2, "skew": 2.0}) == "⬇️ +2.0"
    assert report.skew_cell({"call_iv": 0.2, "skew": -3.8}) == "⬆️ -3.8"
    assert report.skew_cell({"call_iv": 0.2, "skew": 0.1}) == "➖ +0.1"
    assert report.pc_cell(3.01) == "🟥 3.01" and report.pc_cell(0.44) == "🟩 0.44" and report.pc_cell(1.09) == "⚪ 1.09"
    assert report.iv_cell(None) == report.skew_cell(None) == report.pc_cell(None) == "-"


def test_regime_cell_marks_near_flip():
    s = {"spot": 100.0, "regime": "negative gamma", "zero_gamma": 101.0, "expected_move": {"move_pct": 2.0}}
    assert report.regime_cell(s) == "🔴🟡 negative, near flip"
    s["zero_gamma"] = 110.0
    assert report.regime_cell(s) == "🔴 negative"
