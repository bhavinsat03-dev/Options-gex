"""Black-Scholes greeks (vectorized, continuous dividend yield q).

All functions broadcast their array arguments against each other, so
``spot`` can be a column vector of hypothetical spots and the rest row
vectors of contracts. Entries with non-positive spot, strike, t or iv
return 0.
"""

from __future__ import annotations

import math

import numpy as np

_SQRT_2PI = np.sqrt(2.0 * np.pi)
_erf = np.vectorize(math.erf, otypes=[float])


def norm_pdf(x):
    return np.exp(-0.5 * np.square(x)) / _SQRT_2PI


def norm_cdf(x):
    return 0.5 * (1.0 + _erf(np.asarray(x, dtype=float) / math.sqrt(2.0)))


def _prepare(spot, strike, t, iv, *extra):
    arrays = np.broadcast_arrays(
        *(np.asarray(a, dtype=float) for a in (spot, strike, t, iv)),
        *(np.asarray(e) for e in extra),
    )
    spot, strike, t, iv = arrays[:4]
    valid = (spot > 0) & (strike > 0) & (t > 0) & (iv > 0)
    return valid, spot.shape, [a[valid] for a in arrays]


def _d1_d2(s, k, t, v, r, q):
    vol_sqrt_t = v * np.sqrt(t)
    d1 = (np.log(s / k) + (r - q + 0.5 * v * v) * t) / vol_sqrt_t
    return d1, d1 - vol_sqrt_t


def bs_gamma(spot, strike, t, iv, r=0.0, q=0.0):
    """Gamma (identical for calls and puts)."""
    valid, shape, (s, k, tt, v) = _prepare(spot, strike, t, iv)
    out = np.zeros(shape)
    if valid.any():
        d1, _ = _d1_d2(s, k, tt, v, r, q)
        out[valid] = np.exp(-q * tt) * norm_pdf(d1) / (s * v * np.sqrt(tt))
    return out


def bs_delta(spot, strike, t, iv, is_call, r=0.0, q=0.0):
    """Delta: e^(-qT) N(d1) for calls, -e^(-qT) N(-d1) for puts."""
    valid, shape, (s, k, tt, v, call) = _prepare(spot, strike, t, iv, is_call)
    out = np.zeros(shape)
    if valid.any():
        d1, _ = _d1_d2(s, k, tt, v, r, q)
        disc = np.exp(-q * tt)
        out[valid] = np.where(call.astype(bool), disc * norm_cdf(d1), -disc * norm_cdf(-d1))
    return out


def bs_vanna(spot, strike, t, iv, r=0.0, q=0.0):
    """Vanna = d(delta)/d(sigma), per 1.00 of vol (same for calls and puts)."""
    valid, shape, (s, k, tt, v) = _prepare(spot, strike, t, iv)
    out = np.zeros(shape)
    if valid.any():
        d1, d2 = _d1_d2(s, k, tt, v, r, q)
        out[valid] = -np.exp(-q * tt) * norm_pdf(d1) * d2 / v
    return out


def bs_charm(spot, strike, t, iv, is_call, r=0.0, q=0.0):
    """Charm = change in delta as calendar time passes (= -d(delta)/dT), per year."""
    valid, shape, (s, k, tt, v, call) = _prepare(spot, strike, t, iv, is_call)
    out = np.zeros(shape)
    if valid.any():
        d1, d2 = _d1_d2(s, k, tt, v, r, q)
        disc = np.exp(-q * tt)
        sqrt_t = np.sqrt(tt)
        common = disc * norm_pdf(d1) * (2 * (r - q) * tt - d2 * v * sqrt_t) / (2 * tt * v * sqrt_t)
        out[valid] = np.where(
            call.astype(bool),
            q * disc * norm_cdf(d1) - common,
            -q * disc * norm_cdf(-d1) - common,
        )
    return out
