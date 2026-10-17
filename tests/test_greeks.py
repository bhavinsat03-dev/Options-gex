import math

import numpy as np

from gex.greeks import bs_gamma


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
