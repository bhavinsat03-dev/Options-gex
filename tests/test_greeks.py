import math

import numpy as np

from gex.greeks import bs_charm, bs_delta, bs_gamma, bs_vanna


def _bs_call_delta(s, k, t, v, r, q):
    d1 = (math.log(s / k) + (r - q + 0.5 * v * v) * t) / (v * math.sqrt(t))
    return math.exp(-q * t) * 0.5 * (1 + math.erf(d1 / math.sqrt(2)))


def test_known_value():
    # d1 = 0.35, phi(0.35) = 0.375240, gamma = phi / (S * sigma * sqrt(T))
    assert math.isclose(bs_gamma(100, 100, 1.0, 0.2, r=0.05), 0.0187620, rel_tol=1e-5)


def test_matches_finite_difference_of_delta():
    s, k, t, v, r, q = 450.0, 460.0, 0.1, 0.18, 0.04, 0.01
    h = 0.01
    fd = (_bs_call_delta(s + h, k, t, v, r, q) - _bs_call_delta(s - h, k, t, v, r, q)) / (2 * h)
    assert math.isclose(bs_gamma(s, k, t, v, r, q), fd, rel_tol=1e-6)


def test_invalid_inputs_give_zero():
    out = bs_gamma(100, np.array([100, 100, 100, 0]), np.array([0.0, 0.1, 0.1, 0.1]),
                   np.array([0.2, 0.0, 0.2, 0.2]))
    assert out[0] == 0 and out[1] == 0 and out[2] > 0 and out[3] == 0


def test_broadcasts_spot_grid():
    spots = np.array([90.0, 100.0, 110.0])[:, None]
    strikes = np.array([95.0, 100.0, 105.0, 110.0])[None, :]
    assert bs_gamma(spots, strikes, 0.1, 0.2).shape == (3, 4)


def test_peaks_near_the_money():
    strikes = np.arange(80, 121)
    g = bs_gamma(100, strikes, 0.05, 0.2)
    assert abs(strikes[g.argmax()] - 100) <= 1


def test_delta_matches_reference_and_put_call_parity():
    s, k, t, v, r, q = 450.0, 460.0, 0.1, 0.18, 0.04, 0.01
    call = bs_delta(s, k, t, v, True, r, q)
    put = bs_delta(s, k, t, v, False, r, q)
    assert math.isclose(call, _bs_call_delta(s, k, t, v, r, q), rel_tol=1e-9)
    assert math.isclose(call - put, math.exp(-q * t), rel_tol=1e-9)


def test_vanna_matches_finite_difference():
    s, k, t, v, r, q = 100.0, 105.0, 0.25, 0.22, 0.03, 0.0
    h = 1e-5
    fd = (_bs_call_delta(s, k, t, v + h, r, q) - _bs_call_delta(s, k, t, v - h, r, q)) / (2 * h)
    assert math.isclose(bs_vanna(s, k, t, v, r, q), fd, rel_tol=1e-5)


def test_charm_matches_finite_difference():
    s, k, t, v, r, q = 100.0, 95.0, 0.2, 0.3, 0.04, 0.02
    h = 1e-6
    for is_call in (True, False):
        def d(tt):
            return float(bs_delta(s, k, tt, v, is_call, r, q))
        fd = -(d(t + h) - d(t - h)) / (2 * h)  # delta change as time passes
        assert math.isclose(float(bs_charm(s, k, t, v, is_call, r, q)), fd, rel_tol=1e-4)
