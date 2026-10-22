from datetime import date, datetime, timedelta, timezone

import numpy as np
import pandas as pd
import pytest

from gex.config import Settings, load_settings
from gex.data import clean_chain, select_expirations, time_to_expiry


def test_clean_drops_bad_rows(raw_chain, now):
    bad = pd.DataFrame([
        ("call", "2026-10-23", 100.0, 0, 0.2, 0, 0, 0),        # zero OI
        ("call", "2026-10-23", 100.0, np.nan, 0.2, 0, 0, 0),   # missing OI
        ("call", "2026-10-23", 100.0, 10, 0.00001, 0, 0, 0),   # placeholder IV
        ("call", "2026-10-23", 100.0, 10, 9.0, 0, 0, 0),       # absurd IV
        ("call", "2026-10-23", 300.0, 10, 0.2, 0, 0, 0),       # far OTM
        ("call", "2026-10-16", 100.0, 10, 0.2, 0, 0, 0),       # expires today, still live at 10:00 ET
        ("call", "2026-10-15", 100.0, 10, 0.2, 0, 0, 0),       # already expired
    ], columns=raw_chain.columns)
    out = clean_chain(pd.concat([raw_chain, bad]), 100.0, now, Settings())
    assert len(out) == len(raw_chain) + 1
    assert (out["open_interest"] > 0).all()
    assert out["iv"].between(0.01, 5.0).all()
    assert out["strike"].between(80, 120).all()
    assert (out["t"] > 0).all()


def test_time_to_expiry_floor(now):
    exp = pd.Series(["2026-10-16", "2026-10-23"])
    t = time_to_expiry(exp, now, min_days=1 / 24)
    assert t.iloc[0] == pytest.approx(6 / (365 * 24))  # 10:00 -> 16:00 ET
    assert t.iloc[1] == pytest.approx((7 * 24 + 6) / (365 * 24))
    late = datetime(2026, 10, 16, 19, 59, tzinfo=timezone.utc)  # 15:59 ET
    assert time_to_expiry(exp, late, min_days=1 / 24).iloc[0] == pytest.approx(1 / (365 * 24))


def test_select_expirations():
    exps = ["2026-10-15", "2026-10-16", "2026-11-20", "2027-06-18", "2026-10-23"]
    s = Settings(max_dte=60, max_expirations=2)
    assert select_expirations(exps, date(2026, 10, 16), s) == ["2026-10-16", "2026-10-23"]


def test_load_settings(tmp_path):
    p = tmp_path / "c.toml"
    p.write_text('tickers = ["qqq", "ndx"]\nmax_dte = 30\n[aliases]\nnq = "NQ=F"\n')
    s = load_settings(p)
    assert s.tickers == ["QQQ", "NDX"] and s.max_dte == 30
    assert s.yahoo_symbol("NDX") == "^NDX" and s.yahoo_symbol("nq") == "NQ=F"
    assert s.yahoo_symbol("qqq") == "QQQ"


def test_load_settings_rejects_unknown_keys(tmp_path):
    p = tmp_path / "c.toml"
    p.write_text("max_dtee = 30\n")
    with pytest.raises(ValueError):
        load_settings(p)


def test_select_expirations_rolling_window_without_cap():
    today = date(2026, 10, 20)
    exps = [(today + timedelta(days=d)).isoformat() for d in range(0, 80, 2)]
    sel = select_expirations(exps, today, Settings())  # defaults: 60 days, no cap
    assert sel[0] == "2026-10-20" and sel[-1] == "2026-12-19"  # day 60 is inside; day 62 is not
    assert len(sel) == 31


def test_select_expirations_weekly_window():
    today = date(2026, 10, 20)
    exps = [(today + timedelta(days=d)).isoformat() for d in range(0, 30)]
    sel = select_expirations(exps, today, Settings(max_dte=7))
    assert sel[0] == "2026-10-20" and sel[-1] == "2026-10-27" and len(sel) == 8


def test_next_earnings_date_picks_first_upcoming():
    from datetime import date
    import pandas as pd
    from gex.data import next_earnings_date
    today = date(2026, 10, 20)
    cal = {"Earnings Date": [date(2026, 7, 29), pd.Timestamp("2026-10-28"), date(2026, 10, 29)]}
    assert next_earnings_date(cal, today) == "2026-10-28"
    assert next_earnings_date({}, today) is None
    assert next_earnings_date(None, today) is None
    assert next_earnings_date({"Earnings Date": []}, today) is None


def test_clean_chain_fills_missing_volume(raw_chain, now):
    from gex.config import Settings
    from gex.data import clean_chain
    df = clean_chain(raw_chain, 100.0, now, Settings())
    assert (df["volume"] == 0).all()
    raw = raw_chain.assign(volume=[float("nan")] * (len(raw_chain) - 1) + [12.0])
    assert clean_chain(raw, 100.0, now, Settings())["volume"].max() == 12
