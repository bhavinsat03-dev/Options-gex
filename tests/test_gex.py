import numpy as np
import pandas as pd
import pytest

from gex import gex
from gex.config import Settings
from gex.data import clean_chain


def _chain(rows):
    return pd.DataFrame(rows, columns=["type", "strike", "t", "iv", "open_interest"])


def test_dealer_sign_convention():
    chain = _chain([("call", 100, 0.1, 0.2, 10), ("put", 100, 0.1, 0.2, 10)])
    out = gex.contract_gex(chain, spot=100)
    call, put = out["gex"]
    assert call > 0 and put < 0
    assert call == pytest.approx(-put)


def test_gex_units():
    chain = _chain([("call", 100, 0.1, 0.2, 10)])
    out = gex.contract_gex(chain, spot=100)
    g = out["gamma"].iloc[0]
    assert out["gex"].iloc[0] == pytest.approx(g * 10 * 100 * 100**2 * 0.01)


def test_walls_and_by_strike(raw_chain, now):
    chain = clean_chain(raw_chain, 100.0, now, Settings())
    res = gex.compute("TEST", chain, 100.0)
    assert res.call_wall == 110.0
    assert res.put_wall == 90.0
    bs = res.by_strike
    assert np.allclose(bs["net_gex"], bs["call_gex"] + bs["put_gex"])
    assert res.total_gex == pytest.approx(bs["net_gex"].sum())


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


def test_flip_between_put_and_call_walls(raw_chain, now):
    chain = clean_chain(raw_chain, 100.0, now, Settings())
    res = gex.compute("TEST", chain, 100.0)
    assert res.zero_gamma is not None
    assert res.put_wall < res.zero_gamma < res.call_wall
    # Profile at the actual spot equals the direct total.
    at_spot = gex.gex_profile(chain, 100.0, sweep_pct=0.0, steps=1)["net_gex"].iloc[0]
    assert at_spot == pytest.approx(res.total_gex)


def test_regime(raw_chain, now):
    chain = clean_chain(raw_chain, 100.0, now, Settings())
    res = gex.compute("TEST", chain, 100.0)
    assert res.regime == ("positive" if res.spot >= res.zero_gamma else "negative")


def test_only_calls():
    chain = _chain([("call", 100, 0.1, 0.2, 10)])
    res = gex.compute("X", chain, 100.0)
    assert res.put_wall is None and res.call_wall == 100.0
