"""Black-Scholes greeks."""

from __future__ import annotations

import numpy as np

_SQRT_2PI = np.sqrt(2.0 * np.pi)


def norm_pdf(x):
    return np.exp(-0.5 * np.square(x)) / _SQRT_2PI


def bs_gamma(spot, strike, t, iv, r=0.0, q=0.0):
    """Black-Scholes gamma (identical for calls and puts).

    Arguments broadcast against each other, so ``spot`` can be a column
    vector of hypothetical spots and the rest row vectors of contracts.
    Entries with non-positive t, iv, spot or strike return 0.
    """
    spot, strike, t, iv = np.broadcast_arrays(
        np.asarray(spot, dtype=float),
        np.asarray(strike, dtype=float),
        np.asarray(t, dtype=float),
        np.asarray(iv, dtype=float),
    )
    valid = (spot > 0) & (strike > 0) & (t > 0) & (iv > 0)
    out = np.zeros(spot.shape, dtype=float)
    if not valid.any():
        return out

    s, k, tt, v = spot[valid], strike[valid], t[valid], iv[valid]
    vol_sqrt_t = v * np.sqrt(tt)
    d1 = (np.log(s / k) + (r - q + 0.5 * v * v) * tt) / vol_sqrt_t
    out[valid] = np.exp(-q * tt) * norm_pdf(d1) / (s * vol_sqrt_t)
    return out
