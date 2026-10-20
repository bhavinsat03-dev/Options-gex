"""Exposure calculations: GEX, DEX, vanna, charm and derived levels.

Dealer convention (the common SpotGamma-style assumption): customers are
net sellers of calls (covered-call writing) and net buyers of puts
(protection), so dealers are LONG calls and SHORT puts. Every exposure is

    dealer_sign * greek * open_interest * multiplier * scaling

with dealer_sign = +1 for calls and -1 for puts:

    GEX   = sign * gamma * OI * 100 * S^2 * 0.01   $ delta per 1% move in spot
    DEX   = sign * delta * OI * 100 * S            $ delta held by dealers
    Vanna = sign * vanna * OI * 100 * S * 0.01     $ delta change per +1 vol point
    Charm = sign * charm * OI * 100 * S / 365      $ delta change per calendar day
"""

from __future__ import annotations

import calendar
from dataclasses import dataclass, field
from datetime import date, timedelta

import numpy as np
import pandas as pd

from .greeks import bs_charm, bs_delta, bs_gamma, bs_vanna

CONTRACT_MULTIPLIER = 100
CALL_SIGN = 1.0
PUT_SIGN = -1.0

REGIME_DESCRIPTIONS = {
    "positive gamma": (
        "Dealer hedging tends to offset price moves, a condition historically "
        "associated with lower realized volatility."
    ),
    "negative gamma": (
        "Dealer hedging tends to reinforce price moves, a condition historically "
        "associated with higher realized volatility."
    ),
}


def _signs(option_type: pd.Series) -> np.ndarray:
    return np.where(option_type.to_numpy() == "call", CALL_SIGN, PUT_SIGN)


def _expiry_date(value) -> date:
    return value if isinstance(value, date) else date.fromisoformat(str(value))


# ---------------------------------------------------------------- per contract

def contract_exposures(chain: pd.DataFrame, spot: float, r: float = 0.0, q: float = 0.0) -> pd.DataFrame:
    """Return a copy of ``chain`` with greeks and dealer exposures added.

    ``chain`` needs columns: type ('call'/'put'), strike, t (years), iv,
    open_interest.
    """
    out = chain.copy()
    is_call = out["type"].to_numpy() == "call"
    args = (spot, out["strike"], out["t"], out["iv"])
    out["gamma"] = bs_gamma(*args, r, q)
    out["delta"] = bs_delta(*args, is_call, r, q)
    out["vanna"] = bs_vanna(*args, r, q)
    out["charm"] = bs_charm(*args, is_call, r, q)

    size = _signs(out["type"]) * out["open_interest"].to_numpy(dtype=float) * CONTRACT_MULTIPLIER
    out["gex"] = size * out["gamma"] * spot**2 * 0.01
    out["dex"] = size * out["delta"] * spot
    out["vanna_exp"] = size * out["vanna"] * spot * 0.01
    out["charm_exp"] = size * out["charm"] * spot / 365.0
    return out


# ------------------------------------------------------------------ by strike

def gex_by_strike(contracts: pd.DataFrame) -> pd.DataFrame:
    """Aggregate per-contract exposures by strike."""
    calls = contracts["type"] == "call"
    c = contracts.assign(
        call_gex=contracts["gex"].where(calls, 0.0),
        put_gex=contracts["gex"].where(~calls, 0.0),
        call_oi=contracts["open_interest"].where(calls, 0),
        put_oi=contracts["open_interest"].where(~calls, 0),
    )
    cols = ["call_gex", "put_gex", "dex", "vanna_exp", "charm_exp", "call_oi", "put_oi"]
    by = c.groupby("strike", as_index=False)[cols].sum()
    by.insert(3, "net_gex", by["call_gex"] + by["put_gex"])
    by.insert(4, "abs_gex", by["call_gex"].abs() + by["put_gex"].abs())
    return by.sort_values("strike", ignore_index=True)


def top_call_walls(by_strike: pd.DataFrame, n: int = 3) -> list[float]:
    """Strikes with the largest positive call GEX, strongest first."""
    pos = by_strike[by_strike["call_gex"] > 0]
    return [float(k) for k in pos.nlargest(n, "call_gex")["strike"]]


def top_put_walls(by_strike: pd.DataFrame, n: int = 3) -> list[float]:
    """Strikes with the most negative put GEX, strongest first."""
    neg = by_strike[by_strike["put_gex"] < 0]
    return [float(k) for k in neg.nsmallest(n, "put_gex")["strike"]]


def call_wall(by_strike: pd.DataFrame) -> float | None:
    walls = top_call_walls(by_strike, 1)
    return walls[0] if walls else None


def put_wall(by_strike: pd.DataFrame) -> float | None:
    walls = top_put_walls(by_strike, 1)
    return walls[0] if walls else None


def wall_expiries(contracts: pd.DataFrame, strikes: list[float], option_type: str, top: int = 3) -> list[dict]:
    """For each wall strike, the expirations contributing most of its GEX.

    Returns ``[{"strike", "expiries": [{"expiration", "pct"}, ...]}]`` where
    pct is that expiration's share of the strike's call (or put) |GEX|.
    """
    side = contracts[contracts["type"] == option_type]
    out = []
    for k in strikes:
        at = side[side["strike"] == k]
        by_exp = at.groupby("expiration")["gex"].sum().abs()
        total = by_exp.sum()
        expiries = [
            {"expiration": str(e), "pct": float(v / total * 100)}
            for e, v in by_exp.nlargest(top).items()
        ] if total else []
        out.append({"strike": k, "expiries": expiries})
    return out


def oi_by_expiry(contracts: pd.DataFrame, strike: float | None, option_type: str, top: int = 3) -> dict | None:
    """Open interest at one strike split by expiration, largest first."""
    if strike is None:
        return None
    at = contracts[(contracts["type"] == option_type) & (contracts["strike"] == strike)]
    by_exp = at.groupby("expiration")["open_interest"].sum()
    total = int(by_exp.sum())
    return {
        "strike": strike,
        "type": option_type,
        "oi": total,
        "expiries": [
            {"expiration": str(e), "oi": int(v), "pct": float(v / total * 100)}
            for e, v in by_exp.nlargest(top).items()
        ] if total else [],
    }


def oi_near_spot(by_strike: pd.DataFrame, spot: float, pct: float = 0.15) -> dict:
    """{'call': {'770': oi, ...}, 'put': {...}} for strikes within spot +/- pct."""
    near = by_strike[(by_strike["strike"] - spot).abs() <= spot * pct]
    return {
        side: {f"{k:g}": int(v) for k, v in zip(near["strike"], near[f"{side}_oi"]) if v > 0}
        for side in ("call", "put")
    }


def absolute_gamma_strike(by_strike: pd.DataFrame) -> float | None:
    """Strike with the largest |call GEX| + |put GEX|."""
    if by_strike.empty or not (by_strike["abs_gex"] > 0).any():
        return None
    return float(by_strike.loc[by_strike["abs_gex"].idxmax(), "strike"])


# ---------------------------------------------------------- profile and flip

def gex_profile(
    chain: pd.DataFrame,
    spot: float,
    r: float = 0.0,
    q: float = 0.0,
    sweep_pct: float = 0.10,
    steps: int = 201,
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


def regime(net_gex: float) -> str:
    return "positive gamma" if net_gex >= 0 else "negative gamma"


# ------------------------------------------------------- expiry concentration

def third_friday(year: int, month: int) -> date:
    first = date(year, month, 1)
    first_friday = first + timedelta(days=(calendar.FRIDAY - first.weekday()) % 7)
    return first_friday + timedelta(weeks=2)


def next_monthly_expiry(today: date) -> date:
    """Standard monthly expiry (third Friday) on or after ``today``.

    When the exchange moves it to Thursday for a holiday, contracts
    expiring that Thursday still fall on or before this date.
    """
    tf = third_friday(today.year, today.month)
    if tf >= today:
        return tf
    year, month = (today.year + 1, 1) if today.month == 12 else (today.year, today.month + 1)
    return third_friday(year, month)


def expiry_bucket(expiration: date, today: date) -> str:
    week_end = today + timedelta(days=6 - today.weekday())  # Sunday
    if expiration <= today:
        return "0dte"
    if expiration <= week_end:
        return "this_week"
    if (expiration.year, expiration.month) == (today.year, today.month):
        return "this_month"
    return "beyond"


def expiry_concentration(contracts: pd.DataFrame, today: date) -> dict:
    """Share of total |GEX| by expiry bucket, and GEX left after the next monthly.

    Buckets do not overlap: 0DTE, rest of this week (through Sunday), rest
    of this calendar month, and everything later.
    """
    exps = contracts["expiration"].map(_expiry_date)
    abs_gex = contracts["gex"].abs()
    total_abs = abs_gex.sum()
    buckets = exps.map(lambda e: expiry_bucket(e, today))
    shares = {
        b: (float(abs_gex[buckets == b].sum() / total_abs * 100) if total_abs else 0.0)
        for b in ("0dte", "this_week", "this_month", "beyond")
    }

    monthly = next_monthly_expiry(today)
    after = exps > monthly
    return {
        "pct_abs_gex": shares,
        "next_monthly_expiry": monthly.isoformat(),
        "net_gex_after_monthly": float(contracts.loc[after, "gex"].sum()),
        "pct_abs_gex_after_monthly": (
            float(abs_gex[after].sum() / total_abs * 100) if total_abs else 0.0
        ),
    }


# ---------------------------------------------------------------- vol metrics

def option_price(bid, ask, last) -> float | None:
    """Mid when the quote is two-sided and sane, otherwise last trade."""
    if pd.notna(bid) and pd.notna(ask) and bid > 0 and ask >= bid:
        return float((bid + ask) / 2)
    if pd.notna(last) and last > 0:
        return float(last)
    return None


def expected_move(chain: pd.DataFrame, spot: float) -> dict | None:
    """Expected move from the nearest-expiry at-the-money straddle.

    move = ATM call price + ATM put price; range = spot +/- move. The ATM
    strike is the strike nearest spot that has a priced call and put.
    """
    if chain.empty:
        return None
    nearest = chain.loc[chain["t"].idxmin(), "expiration"]
    exp = chain[chain["expiration"] == nearest]

    priced = {}
    for _, row in exp.iterrows():
        price = option_price(row.get("bid"), row.get("ask"), row.get("last"))
        if price is not None:
            priced[(row["type"], float(row["strike"]))] = price
    strikes = sorted(
        {k for (typ, k) in priced if typ == "call"} & {k for (typ, k) in priced if typ == "put"},
        key=lambda k: abs(k - spot),
    )
    if not strikes:
        return None
    k = strikes[0]
    call, put = priced[("call", k)], priced[("put", k)]
    move = call + put
    return {
        "expiration": str(nearest),
        "strike": k,
        "call_price": call,
        "put_price": put,
        "move": move,
        "move_pct": move / spot * 100,
        "low": spot - move,
        "high": spot + move,
    }


def total_oi(df: pd.DataFrame, option_type: str) -> int:
    oi = pd.to_numeric(df["open_interest"], errors="coerce").fillna(0)
    return int(oi[df["type"] == option_type].sum())


def strike_oi(by_strike: pd.DataFrame, strike: float | None, column: str) -> int | None:
    if strike is None:
        return None
    row = by_strike.loc[by_strike["strike"] == strike, column]
    return int(row.iloc[0]) if len(row) else None


def max_oi_strike(by_strike: pd.DataFrame, column: str) -> tuple[float | None, int | None]:
    """Strike with the most open interest in ``column`` ('call_oi' / 'put_oi')."""
    if by_strike.empty or not (by_strike[column] > 0).any():
        return None, None
    row = by_strike.loc[by_strike[column].idxmax()]
    return float(row["strike"]), int(row[column])


def put_call_oi_ratio(df: pd.DataFrame) -> float | None:
    oi = pd.to_numeric(df["open_interest"], errors="coerce").fillna(0)
    calls = oi[df["type"] == "call"].sum()
    puts = oi[df["type"] == "put"].sum()
    return float(puts / calls) if calls > 0 else None


def skew_25d(
    chain: pd.DataFrame, spot: float, r: float = 0.0, q: float = 0.0, target_days: float = 30
) -> dict | None:
    """25-delta risk reversal skew: IV(25d put) - IV(25d call), in vol points.

    Uses the expiration closest to ``target_days``; each 25-delta IV is
    linearly interpolated in delta across that expiry's strikes.
    """
    if chain.empty:
        return None
    t_by_exp = chain.groupby("expiration")["t"].first()
    exp = (t_by_exp * 365 - target_days).abs().idxmin()
    sub = chain[chain["expiration"] == exp]
    is_call = sub["type"].to_numpy() == "call"
    delta = bs_delta(spot, sub["strike"], sub["t"], sub["iv"], is_call, r, q)

    def iv_at(mask, target):
        d, v = delta[mask], sub["iv"].to_numpy()[mask]
        if len(d) < 2 or not (d.min() <= target <= d.max()):
            return None
        order = np.argsort(d)
        return float(np.interp(target, d[order], v[order]))

    put_iv, call_iv = iv_at(~is_call, -0.25), iv_at(is_call, 0.25)
    if put_iv is None or call_iv is None:
        return None
    return {
        "expiration": str(exp),
        "days": float(t_by_exp[exp] * 365),
        "put_iv": put_iv,
        "call_iv": call_iv,
        "skew": (put_iv - call_iv) * 100,
    }


# ------------------------------------------------------------------- results

@dataclass
class GexResult:
    ticker: str
    spot: float
    today: date
    contracts: pd.DataFrame
    by_strike: pd.DataFrame
    profile: pd.DataFrame
    total_gex: float
    call_walls: list[float]
    put_walls: list[float]
    abs_gamma_strike: float | None
    zero_gamma: float | None
    expected_move: dict | None
    put_call_oi_ratio: float | None
    total_call_oi: int
    total_put_oi: int
    skew_25d: dict | None
    expiry_concentration: dict
    expirations: list[str] = field(default_factory=list)

    @property
    def call_wall(self) -> float | None:
        return self.call_walls[0] if self.call_walls else None

    @property
    def put_wall(self) -> float | None:
        return self.put_walls[0] if self.put_walls else None

    @property
    def regime(self) -> str:
        return regime(self.total_gex)

    def summary(self) -> dict:
        return {
            "ticker": self.ticker,
            "spot": round(self.spot, 4),
            "derived": False,
            "derived_from": None,
            "net_gex": self.total_gex,
            "call_gex": float(self.contracts.loc[self.contracts["type"] == "call", "gex"].sum()),
            "put_gex": float(self.contracts.loc[self.contracts["type"] == "put", "gex"].sum()),
            "regime": self.regime,
            "regime_description": REGIME_DESCRIPTIONS[self.regime],
            "call_wall": self.call_wall,
            "put_wall": self.put_wall,
            "call_walls": self.call_walls,
            "put_walls": self.put_walls,
            "call_wall_expiries": wall_expiries(self.contracts, self.call_walls, "call"),
            "put_wall_expiries": wall_expiries(self.contracts, self.put_walls, "put"),
            "abs_gamma_strike": self.abs_gamma_strike,
            "zero_gamma": None if self.zero_gamma is None else round(self.zero_gamma, 2),
            "net_dex": float(self.contracts["dex"].sum()),
            "net_vanna": float(self.contracts["vanna_exp"].sum()),
            "net_charm": float(self.contracts["charm_exp"].sum()),
            "expected_move": self.expected_move,
            "put_call_oi_ratio": self.put_call_oi_ratio,
            "total_call_oi": self.total_call_oi,
            "total_put_oi": self.total_put_oi,
            "call_wall_oi": strike_oi(self.by_strike, self.call_wall, "call_oi"),
            "oi_at": oi_near_spot(self.by_strike, self.spot),
            "oi_expiries": {
                "call_wall": oi_by_expiry(self.contracts, self.call_wall, "call"),
                "put_wall": oi_by_expiry(self.contracts, self.put_wall, "put"),
                "max_call_oi": oi_by_expiry(self.contracts, max_oi_strike(self.by_strike, "call_oi")[0], "call"),
                "max_put_oi": oi_by_expiry(self.contracts, max_oi_strike(self.by_strike, "put_oi")[0], "put"),
            },
            "max_call_oi_strike": max_oi_strike(self.by_strike, "call_oi")[0],
            "max_call_oi": max_oi_strike(self.by_strike, "call_oi")[1],
            "max_put_oi_strike": max_oi_strike(self.by_strike, "put_oi")[0],
            "max_put_oi": max_oi_strike(self.by_strike, "put_oi")[1],
            "put_wall_oi": strike_oi(self.by_strike, self.put_wall, "put_oi"),
            "skew_25d": self.skew_25d,
            "expiry_concentration": self.expiry_concentration,
            "contracts": len(self.contracts),
            "expirations": len(self.expirations),
        }


def compute(
    ticker: str,
    chain: pd.DataFrame,
    spot: float,
    today: date,
    r: float = 0.0,
    q: float = 0.0,
    sweep_pct: float = 0.10,
    sweep_steps: int = 201,
    n_walls: int = 3,
    skew_target_days: float = 30,
    raw: pd.DataFrame | None = None,
) -> GexResult:
    """Compute every metric for one ticker.

    ``chain`` is the cleaned chain; ``raw`` (optional) is the full fetched
    chain, used only for the put/call open-interest ratio.
    """
    contracts = contract_exposures(chain, spot, r, q)
    by_strike = gex_by_strike(contracts)
    profile = gex_profile(chain, spot, r, q, sweep_pct, sweep_steps)
    return GexResult(
        ticker=ticker,
        spot=spot,
        today=today,
        contracts=contracts,
        by_strike=by_strike,
        profile=profile,
        total_gex=float(contracts["gex"].sum()),
        call_walls=top_call_walls(by_strike, n_walls),
        put_walls=top_put_walls(by_strike, n_walls),
        abs_gamma_strike=absolute_gamma_strike(by_strike),
        zero_gamma=zero_gamma(profile, spot),
        expected_move=expected_move(chain, spot),
        put_call_oi_ratio=put_call_oi_ratio(raw if raw is not None else chain),
        total_call_oi=total_oi(raw if raw is not None else chain, "call"),
        total_put_oi=total_oi(raw if raw is not None else chain, "put"),
        skew_25d=skew_25d(chain, spot, r, q, skew_target_days),
        expiry_concentration=expiry_concentration(contracts, today),
        expirations=sorted({str(e) for e in chain["expiration"]}),
    )


# -------------------------------------------------------------- proxy levels

PRICE_LEVELS = ("call_wall", "put_wall", "abs_gamma_strike", "zero_gamma", "max_call_oi_strike", "max_put_oi_strike")
DOLLAR_EXPOSURES = ("net_gex", "call_gex", "put_gex", "net_dex", "net_vanna", "net_charm")


def derive_summary(proxy: dict, ticker: str, spot: float) -> dict:
    """Map a proxy's levels (e.g. QQQ) onto ``ticker`` (e.g. NDX) by spot ratio.

    Price levels are scaled by spot / proxy_spot. Dollar exposures are not
    transferable and are set to None; ratios and percentages (regime, P/C,
    skew, expiry concentration) are carried over from the proxy as-is.
    """
    ratio = spot / proxy["spot"]
    out = dict(proxy)
    out.update(
        ticker=ticker,
        spot=round(spot, 4),
        derived=True,
        derived_from=proxy["ticker"],
        derived_ratio=ratio,
    )
    for key in PRICE_LEVELS:
        if proxy.get(key) is not None:
            out[key] = round(proxy[key] * ratio, 2)
    out["call_walls"] = [round(k * ratio, 2) for k in proxy.get("call_walls", [])]
    out["put_walls"] = [round(k * ratio, 2) for k in proxy.get("put_walls", [])]
    for key in ("call_wall_expiries", "put_wall_expiries"):
        out[key] = [dict(w, strike=round(w["strike"] * ratio, 2)) for w in proxy.get(key, [])]
    for key in DOLLAR_EXPOSURES + ("total_call_oi", "total_put_oi", "call_wall_oi", "put_wall_oi", "max_call_oi", "max_put_oi"):
        out[key] = None
    em = proxy.get("expected_move")
    if em:
        out["expected_move"] = dict(
            em,
            strike=round(em["strike"] * ratio, 2),
            move=em["move"] * ratio,
            low=em["low"] * ratio,
            high=em["high"] * ratio,
            call_price=None,
            put_price=None,
        )
    out["oi_expiries"] = {}
    out["oi_at"] = {}
    exp_conc = proxy.get("expiry_concentration")
    if exp_conc:
        out["expiry_concentration"] = dict(exp_conc, net_gex_after_monthly=None)
    return out
