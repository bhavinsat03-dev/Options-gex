from datetime import date

import numpy as np
import pandas as pd
import pytest

from gex import gex
from gex.config import Settings
from gex.data import clean_chain

TODAY = date(2026, 10, 16)  # a Friday; third Friday of October 2026


def _chain(rows):
    return pd.DataFrame(rows, columns=["type", "strike", "t", "iv", "open_interest"])


def _result(raw_chain, now, spot=100.0):
    chain = clean_chain(raw_chain, spot, now, Settings())
    return gex.compute("TEST", chain, spot, TODAY, raw=raw_chain)


# ------------------------------------------------------------ sign conventions

def test_gex_sign_convention():
    chain = _chain([("call", 100, 0.1, 0.2, 10), ("put", 100, 0.1, 0.2, 10)])
    call, put = gex.contract_exposures(chain, spot=100)["gex"]
    assert call > 0 and put < 0
    assert call == pytest.approx(-put)


def test_gex_units():
    out = gex.contract_exposures(_chain([("call", 100, 0.1, 0.2, 10)]), spot=100)
    assert out["gex"].iloc[0] == pytest.approx(out["gamma"].iloc[0] * 10 * 100 * 100**2 * 0.01)


def test_dex_sign_convention():
    # Dealers long calls -> long delta; dealers short puts -> also long delta.
    chain = _chain([("call", 100, 0.1, 0.2, 10), ("put", 100, 0.1, 0.2, 10)])
    out = gex.contract_exposures(chain, spot=100)
    call, put = out.itertuples()
    assert call.delta > 0 and put.delta < 0
    assert call.dex > 0 and put.dex > 0
    assert call.dex == pytest.approx(call.delta * 10 * 100 * 100)
    assert put.dex == pytest.approx(-put.delta * 10 * 100 * 100)


def test_dex_flips_with_dealer_sign():
    # Deep ITM put: delta ~ -1, dealer short it -> ~ +$ notional of delta.
    out = gex.contract_exposures(_chain([("put", 150, 0.1, 0.2, 1)]), spot=100)
    assert out["dex"].iloc[0] == pytest.approx(100 * 100, rel=1e-3)


def test_vanna_and_charm_exposure_signs():
    chain = _chain([("call", 110, 0.1, 0.2, 10), ("put", 90, 0.1, 0.2, 10)])
    out = gex.contract_exposures(chain, spot=100)
    call, put = out.itertuples()
    # OTM call: delta rises with vol (vanna > 0); dealer long -> positive exposure.
    assert call.vanna > 0 and call.vanna_exp > 0
    # OTM put: delta (negative) moves toward -0.5 with vol, so vanna < 0; dealer short -> positive.
    assert put.vanna < 0 and put.vanna_exp > 0
    # OTM call delta decays toward 0 over time -> negative charm.
    assert call.charm < 0 and call.charm_exp < 0
    assert call.charm_exp == pytest.approx(call.charm * 10 * 100 * 100 / 365)


# ------------------------------------------------------------- strikes/walls

def test_walls_and_by_strike(raw_chain, now):
    res = _result(raw_chain, now)
    assert res.call_wall == 110.0 and res.put_wall == 90.0
    assert res.call_walls[0] == 110.0 and len(res.call_walls) == 3
    assert res.put_walls[0] == 90.0 and len(res.put_walls) == 3
    bs = res.by_strike
    assert np.allclose(bs["net_gex"], bs["call_gex"] + bs["put_gex"])
    assert np.allclose(bs["abs_gex"], bs["call_gex"].abs() + bs["put_gex"].abs())
    assert res.total_gex == pytest.approx(bs["net_gex"].sum())
    assert res.contracts["dex"].sum() == pytest.approx(bs["dex"].sum())


def test_top_walls_ordering():
    bs = pd.DataFrame({
        "strike": [90.0, 95.0, 100.0, 105.0, 110.0],
        "call_gex": [0.0, 1.0, 5.0, 3.0, 4.0],
        "put_gex": [-6.0, -2.0, -1.0, 0.0, 0.0],
    })
    assert gex.top_call_walls(bs, 3) == [100.0, 110.0, 105.0]
    assert gex.top_put_walls(bs, 3) == [90.0, 95.0, 100.0]
    assert gex.top_put_walls(bs, 5) == [90.0, 95.0, 100.0]  # only strikes with put GEX


def test_absolute_gamma_strike():
    bs = pd.DataFrame({"strike": [90.0, 100.0, 110.0], "call_gex": [1.0, 4.0, 6.0], "put_gex": [-7.0, -5.0, 0.0]})
    bs["abs_gex"] = bs["call_gex"].abs() + bs["put_gex"].abs()
    # 100 has the largest combined |GEX| (9) though it is neither wall.
    assert gex.absolute_gamma_strike(bs) == 100.0


# ------------------------------------------------------------ profile / flip

def test_zero_gamma_interpolation():
    profile = pd.DataFrame({"spot": [90.0, 95.0, 100.0, 105.0], "net_gex": [-2.0, -1.0, 1.0, 3.0]})
    assert gex.zero_gamma(profile, 100.0) == pytest.approx(97.5)


def test_zero_gamma_picks_crossing_nearest_spot():
    profile = pd.DataFrame({"spot": [80.0, 90.0, 100.0, 110.0, 120.0], "net_gex": [1.0, -1.0, -1.0, 1.0, 1.0]})
    assert gex.zero_gamma(profile, 108.0) == pytest.approx(105.0)
    assert gex.zero_gamma(profile, 86.0) == pytest.approx(85.0)


def test_zero_gamma_none_when_no_crossing():
    profile = pd.DataFrame({"spot": [90.0, 100.0, 110.0], "net_gex": [1.0, 2.0, 3.0]})
    assert gex.zero_gamma(profile, 100.0) is None


def test_profile_range_and_flip(raw_chain, now):
    res = _result(raw_chain, now)
    assert res.profile["spot"].iloc[0] == pytest.approx(90.0)
    assert res.profile["spot"].iloc[-1] == pytest.approx(110.0)
    assert res.put_wall < res.zero_gamma < res.call_wall
    chain = clean_chain(raw_chain, 100.0, now, Settings())
    at_spot = gex.gex_profile(chain, 100.0, sweep_pct=0.0, steps=1)["net_gex"].iloc[0]
    assert at_spot == pytest.approx(res.total_gex)


def test_regime_label():
    assert gex.regime(1.0) == "positive gamma"
    assert gex.regime(-1.0) == "negative gamma"
    for text in gex.REGIME_DESCRIPTIONS.values():
        words = set(text.lower().replace(",", " ").replace(".", " ").split())
        assert not words & {"buy", "sell", "should", "long", "short"}  # neutral, no advice
        assert text.count(".") == 1  # one line


def test_only_calls():
    chain = _chain([("call", 100, 0.1, 0.2, 10)]).assign(expiration="2026-10-23")
    res = gex.compute("X", chain, 100.0, TODAY)
    assert res.put_wall is None and res.call_wall == 100.0
    assert res.put_call_oi_ratio == 0.0


# ------------------------------------------------------ expiry concentration

def test_third_friday_and_next_monthly():
    assert gex.third_friday(2026, 10) == date(2026, 10, 16)
    assert gex.next_monthly_expiry(date(2026, 10, 16)) == date(2026, 10, 16)
    assert gex.next_monthly_expiry(date(2026, 10, 19)) == date(2026, 11, 20)
    assert gex.next_monthly_expiry(date(2026, 12, 21)) == date(2027, 1, 15)


def test_expiry_buckets():
    today = date(2026, 10, 14)  # Wednesday
    assert gex.expiry_bucket(date(2026, 10, 14), today) == "0dte"
    assert gex.expiry_bucket(date(2026, 10, 16), today) == "this_week"
    assert gex.expiry_bucket(date(2026, 10, 18), today) == "this_week"  # Sunday
    assert gex.expiry_bucket(date(2026, 10, 30), today) == "this_month"
    assert gex.expiry_bucket(date(2026, 11, 2), today) == "beyond"


def test_expiry_concentration():
    contracts = pd.DataFrame({
        "expiration": ["2026-10-14", "2026-10-16", "2026-10-30", "2026-11-20"],
        "gex": [10.0, -30.0, 20.0, 40.0],
    })
    conc = gex.expiry_concentration(contracts, date(2026, 10, 14))
    shares = conc["pct_abs_gex"]
    assert shares == pytest.approx({"0dte": 10.0, "this_week": 30.0, "this_month": 20.0, "beyond": 40.0})
    assert sum(shares.values()) == pytest.approx(100.0)
    assert conc["next_monthly_expiry"] == "2026-10-16"
    assert conc["net_gex_after_monthly"] == pytest.approx(60.0)
    assert conc["pct_abs_gex_after_monthly"] == pytest.approx(60.0)


# ---------------------------------------------------------------- vol metrics

def _priced(rows):
    return pd.DataFrame(rows, columns=["type", "expiration", "strike", "t", "bid", "ask", "last"])


def test_expected_move_from_atm_straddle():
    chain = _priced([
        ("call", "2026-10-23", 100.0, 0.02, 2.00, 2.20, 2.5),   # mid 2.10
        ("put", "2026-10-23", 100.0, 0.02, 1.80, 2.00, 1.0),    # mid 1.90
        ("call", "2026-10-23", 105.0, 0.02, 0.50, 0.60, 0.5),
        ("put", "2026-10-23", 105.0, 0.02, 5.00, 5.20, 5.1),
        ("call", "2026-11-20", 101.0, 0.10, 9.0, 9.0, 9.0),     # later expiry ignored
        ("put", "2026-11-20", 101.0, 0.10, 9.0, 9.0, 9.0),
    ])
    em = gex.expected_move(chain, spot=101.0)
    assert em["expiration"] == "2026-10-23"
    assert em["strike"] == 100.0
    assert em["move"] == pytest.approx(4.0)
    assert em["move_pct"] == pytest.approx(4.0 / 101.0 * 100)
    assert (em["low"], em["high"]) == pytest.approx((97.0, 105.0))


def test_expected_move_falls_back_to_last_and_skips_unpriced():
    chain = _priced([
        ("call", "2026-10-23", 100.0, 0.02, 0.0, 0.0, 3.0),     # no quote -> last 3.0
        ("put", "2026-10-23", 100.0, 0.02, 0.0, 0.0, 0.0),      # unpriced -> strike skipped
        ("call", "2026-10-23", 95.0, 0.02, 6.0, 6.2, 0.0),
        ("put", "2026-10-23", 95.0, 0.02, 0.9, 1.1, 0.0),
    ])
    em = gex.expected_move(chain, spot=100.0)
    assert em["strike"] == 95.0
    assert em["move"] == pytest.approx(6.1 + 1.0)


def test_option_price():
    assert gex.option_price(1.0, 1.2, 5.0) == pytest.approx(1.1)
    assert gex.option_price(0.0, 1.2, 5.0) == 5.0
    assert gex.option_price(1.3, 1.2, 5.0) == 5.0  # crossed quote
    assert gex.option_price(np.nan, np.nan, np.nan) is None


def test_put_call_oi_ratio():
    df = pd.DataFrame({"type": ["call", "call", "put"], "open_interest": [100, 300, 600]})
    assert gex.put_call_oi_ratio(df) == pytest.approx(1.5)


def test_skew_25d_flat_vs_skewed():
    strikes = np.arange(80.0, 121.0, 1.0)
    rows = []
    for k in strikes:
        rows.append(("call", "2026-11-13", k, 28 / 365, 0.20, 100))
        rows.append(("put", "2026-11-13", k, 28 / 365, 0.20 + (100 - k) * 0.004, 100))
    chain = pd.DataFrame(rows, columns=["type", "expiration", "strike", "t", "iv", "open_interest"])
    sk = gex.skew_25d(chain, 100.0)
    assert sk["expiration"] == "2026-11-13"
    assert sk["call_iv"] == pytest.approx(0.20)
    assert sk["skew"] > 0  # puts priced richer

    flat = chain.assign(iv=0.20)
    assert gex.skew_25d(flat, 100.0)["skew"] == pytest.approx(0.0, abs=1e-9)


# ------------------------------------------------------------- proxy levels

def test_derive_summary_scales_levels(raw_chain, now):
    proxy = _result(raw_chain, now).summary()
    derived = gex.derive_summary(proxy, "NDX", spot=4100.0)
    ratio = 41.0
    assert derived["derived"] is True and derived["derived_from"] == "TEST"
    assert derived["derived_ratio"] == pytest.approx(ratio)
    assert derived["call_wall"] == pytest.approx(proxy["call_wall"] * ratio)
    assert derived["put_walls"] == pytest.approx([k * ratio for k in proxy["put_walls"]])
    assert derived["zero_gamma"] == pytest.approx(proxy["zero_gamma"] * ratio, abs=0.01)
    assert derived["expected_move"]["low"] == pytest.approx(proxy["expected_move"]["low"] * ratio)
    assert derived["net_gex"] is None and derived["net_dex"] is None
    assert derived["regime"] == proxy["regime"]
    assert proxy["call_wall"] == 110.0  # proxy untouched


def test_wall_expiries():
    contracts = pd.DataFrame({
        "type": ["call", "call", "call", "put", "call"],
        "strike": [110.0, 110.0, 110.0, 110.0, 105.0],
        "expiration": ["2026-10-23", "2026-11-20", "2026-10-23", "2026-10-23", "2026-10-23"],
        "gex": [30.0, 60.0, 20.0, -999.0, 5.0],
    })
    (w,) = gex.wall_expiries(contracts, [110.0], "call")
    assert w["strike"] == 110.0
    # 2026-10-23 rows sum to 50 of 110; the put and the 105 strike are excluded.
    assert [(e["expiration"], round(e["pct"], 1)) for e in w["expiries"]] == [("2026-11-20", 54.5), ("2026-10-23", 45.5)]
    (p,) = gex.wall_expiries(contracts, [110.0], "put")
    assert p["expiries"] == [{"expiration": "2026-10-23", "pct": 100.0}]


def test_wall_expiries_in_summary(raw_chain, now):
    s = _result(raw_chain, now).summary()
    assert [w["strike"] for w in s["call_wall_expiries"]] == s["call_walls"]
    for w in s["call_wall_expiries"] + s["put_wall_expiries"]:
        assert sum(e["pct"] for e in w["expiries"]) == pytest.approx(100.0)


def test_open_interest_fields(raw_chain, now):
    s = _result(raw_chain, now).summary()
    assert s["total_call_oi"] == int(raw_chain.loc[raw_chain["type"] == "call", "open_interest"].sum())
    assert s["total_put_oi"] == int(raw_chain.loc[raw_chain["type"] == "put", "open_interest"].sum())
    assert s["call_wall_oi"] == 5000 * 2  # 110 strike, two expirations
    assert s["put_wall_oi"] == 6000 * 2   # 90 strike
    assert s["put_call_oi_ratio"] == pytest.approx(s["total_put_oi"] / s["total_call_oi"])


def test_max_oi_strikes(raw_chain, now):
    s = _result(raw_chain, now).summary()
    assert (s["max_call_oi_strike"], s["max_call_oi"]) == (110.0, 10000)
    assert (s["max_put_oi_strike"], s["max_put_oi"]) == (90.0, 12000)
    d = gex.derive_summary(s, "NDX", 4100.0)
    assert d["max_call_oi_strike"] == pytest.approx(110.0 * 41) and d["max_call_oi"] is None


def test_oi_by_expiry(raw_chain, now):
    s = _result(raw_chain, now).summary()
    e = s["oi_expiries"]["call_wall"]
    assert e["strike"] == 110.0 and e["type"] == "call" and e["oi"] == 10000
    assert sorted(x["expiration"] for x in e["expiries"]) == ["2026-10-23", "2026-11-20"]
    assert sum(x["pct"] for x in e["expiries"]) == pytest.approx(100.0)
    assert s["oi_expiries"]["max_put_oi"]["strike"] == 90.0
