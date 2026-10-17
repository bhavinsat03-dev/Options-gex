"""Gamma exposure calculations.

Dealer convention (the common SpotGamma-style assumption): customers buy
calls and sell puts, so dealers are long call gamma and short put gamma.

    GEX = sign * gamma * open_interest * multiplier * spot^2 * 0.01

with sign = +1 for calls and -1 for puts. The result is the dollar delta
dealers must trade for a 1% move in the underlying.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
import pandas as pd

from .greeks import bs_gamma

CONTRACT_MULTIPLIER = 100
CALL_SIGN = 1.0
PUT_SIGN = -1.0


def _signs(option_type: pd.Series) -> np.ndarray:
    return np.where(option_type.to_numpy() == "call", CALL_SIGN, PUT_SIGN)


def contract_gex(chain: pd.DataFrame, spot: float, r: float = 0.0, q: float = 0.0) -> pd.DataFrame:
    """Return a copy of ``chain`` with ``gamma`` and ``gex`` columns added.

    ``chain`` needs columns: type ('call'/'put'), strike, t (years), iv,
    open_interest.
    """
    out = chain.copy()
    out["gamma"] = bs_gamma(spot, out["strike"], out["t"], out["iv"], r, q)
    out["gex"] = (
        _signs(out["type"])
        * out["gamma"]
        * out["open_interest"]
        * CONTRACT_MULTIPLIER
        * spot**2
        * 0.01
    )
    return out


def gex_by_strike(contracts: pd.DataFrame) -> pd.DataFrame:
    """Aggregate per-contract GEX into call / put / net GEX per strike."""
    pivot = contracts.pivot_table(
        index="strike", columns="type", values="gex", aggfunc="sum", fill_value=0.0
    )
    by_strike = pd.DataFrame(index=pivot.index)
    by_strike["call_gex"] = pivot["call"] if "call" in pivot else 0.0
    by_strike["put_gex"] = pivot["put"] if "put" in pivot else 0.0
    by_strike["net_gex"] = by_strike["call_gex"] + by_strike["put_gex"]

    oi = contracts.pivot_table(
        index="strike", columns="type", values="open_interest", aggfunc="sum", fill_value=0
    )
    by_strike["call_oi"] = oi["call"] if "call" in oi else 0
    by_strike["put_oi"] = oi["put"] if "put" in oi else 0
    return by_strike.reset_index().sort_values("strike", ignore_index=True)


def call_wall(by_strike: pd.DataFrame) -> float | None:
    """Strike with the largest positive call GEX."""
    if by_strike.empty or not (by_strike["call_gex"] > 0).any():
        return None
    return float(by_strike.loc[by_strike["call_gex"].idxmax(), "strike"])


def put_wall(by_strike: pd.DataFrame) -> float | None:
    """Strike with the largest (most negative) put GEX."""
    if by_strike.empty or not (by_strike["put_gex"] < 0).any():
        return None
    return float(by_strike.loc[by_strike["put_gex"].idxmin(), "strike"])


def gex_profile(
    chain: pd.DataFrame,
    spot: float,
    r: float = 0.0,
    q: float = 0.0,
    sweep_pct: float = 0.15,
    steps: int = 301,
) -> pd.DataFrame:
    """Total net GEX re-evaluated at hypothetical spot levels.

    Gamma is recomputed at each level with IV, T and OI held fixed.
    """
    levels = np.linspace(spot * (1 - sweep_pct), spot * (1 + sweep_pct), steps)
    sign_oi = _signs(chain["type"]) * chain["open_interest"].to_numpy(dtype=float)
    gamma = bs_gamma(
        levels[:, None],
        chain["strike"].to_numpy()[None, :],
        chain["t"].to_numpy()[None, :],
        chain["iv"].to_numpy()[None, :],
        r,
        q,
    )
    total = gamma @ sign_oi * CONTRACT_MULTIPLIER * levels**2 * 0.01
    return pd.DataFrame({"spot": levels, "net_gex": total})


def zero_gamma(profile: pd.DataFrame, spot: float) -> float | None:
    """Spot level where the GEX profile crosses zero, nearest to ``spot``.

    Uses linear interpolation between the bracketing sweep points. Returns
    None when the profile never changes sign within the sweep range.
    """
    x = profile["spot"].to_numpy()
    y = profile["net_gex"].to_numpy()
    crossings = []
    for i in range(len(y) - 1):
        y0, y1 = y[i], y[i + 1]
        if y0 == 0:
            crossings.append(x[i])
        elif y0 * y1 < 0:
            crossings.append(x[i] - y0 * (x[i + 1] - x[i]) / (y1 - y0))
    if len(y) and y[-1] == 0:
        crossings.append(x[-1])
    if not crossings:
        return None
    return float(min(crossings, key=lambda c: abs(c - spot)))


@dataclass
class GexResult:
    ticker: str
    spot: float
    contracts: pd.DataFrame
    by_strike: pd.DataFrame
    profile: pd.DataFrame
    total_gex: float
    call_wall: float | None
    put_wall: float | None
    zero_gamma: float | None
    expirations: list[str] = field(default_factory=list)

    @property
    def regime(self) -> str:
        if self.zero_gamma is None:
            return "positive" if self.total_gex >= 0 else "negative"
        return "positive" if self.spot >= self.zero_gamma else "negative"

    def summary(self) -> dict:
        return {
            "ticker": self.ticker,
            "spot": round(self.spot, 4),
            "total_gex": self.total_gex,
            "call_wall": self.call_wall,
            "put_wall": self.put_wall,
            "zero_gamma": None if self.zero_gamma is None else round(self.zero_gamma, 2),
            "regime": self.regime,
            "contracts": len(self.contracts),
            "expirations": len(self.expirations),
        }


def compute(
    ticker: str,
    chain: pd.DataFrame,
    spot: float,
    r: float = 0.0,
    q: float = 0.0,
    sweep_pct: float = 0.15,
    sweep_steps: int = 301,
) -> GexResult:
    contracts = contract_gex(chain, spot, r, q)
    by_strike = gex_by_strike(contracts)
    profile = gex_profile(chain, spot, r, q, sweep_pct, sweep_steps)
    expirations = sorted({str(e) for e in chain["expiration"]}) if "expiration" in chain else []
    return GexResult(
        ticker=ticker,
        spot=spot,
        contracts=contracts,
        by_strike=by_strike,
        profile=profile,
        total_gex=float(contracts["gex"].sum()),
        call_wall=call_wall(by_strike),
        put_wall=put_wall(by_strike),
        zero_gamma=zero_gamma(profile, spot),
        expirations=expirations,
    )
