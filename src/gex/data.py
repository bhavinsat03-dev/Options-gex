"""Fetching and cleaning option chains from Yahoo Finance via yfinance."""

from __future__ import annotations

import logging
import time
from datetime import date, datetime, time as dtime, timezone
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

from .config import Settings

log = logging.getLogger(__name__)

NY = ZoneInfo("America/New_York")
SECONDS_PER_YEAR = 365.0 * 24 * 3600

RAW_COLUMNS = ["type", "expiration", "strike", "open_interest", "volume", "iv", "bid", "ask", "last"]


class DataError(RuntimeError):
    pass


def _retry(fn, what: str, settings: Settings):
    """Call ``fn`` with exponential backoff (rate limits, flaky network)."""
    delay = 2.0
    for attempt in range(1, settings.max_retries + 1):
        try:
            return fn()
        except Exception as exc:  # yfinance raises a variety of types
            if attempt == settings.max_retries:
                raise DataError(f"{what} failed after {attempt} attempts: {exc}") from exc
            log.warning("%s failed (%s); retrying in %.0fs", what, exc, delay)
            time.sleep(delay)
            delay *= 2


def fetch_spot(tk, symbol: str, settings: Settings) -> float:
    def get():
        price = None
        try:
            price = tk.fast_info["last_price"]
        except Exception:
            pass
        if price is None or not np.isfinite(price) or price <= 0:
            hist = tk.history(period="5d")
            if hist.empty:
                raise DataError(f"no price history for {symbol}")
            price = hist["Close"].iloc[-1]
        return float(price)

    return _retry(get, f"spot price for {symbol}", settings)


def fetch_spot_only(ticker: str, settings: Settings) -> float:
    """Spot price for ``ticker`` without touching its option chain."""
    import yfinance as yf

    symbol = settings.yahoo_symbol(ticker)
    return fetch_spot(yf.Ticker(symbol), symbol, settings)


def select_expirations(expirations, today: date, settings: Settings) -> list[str]:
    selected = []
    for exp in expirations:
        dte = (date.fromisoformat(exp) - today).days
        if 0 <= dte <= settings.max_dte:
            selected.append(exp)
    selected.sort()
    return selected[: settings.max_expirations] if settings.max_expirations > 0 else selected


def _normalize(df: pd.DataFrame, option_type: str, expiration: str) -> pd.DataFrame:
    return pd.DataFrame(
        {
            "type": option_type,
            "expiration": expiration,
            "strike": df.get("strike"),
            "open_interest": df.get("openInterest"),
            "volume": df.get("volume"),
            "iv": df.get("impliedVolatility"),
            "bid": df.get("bid"),
            "ask": df.get("ask"),
            "last": df.get("lastPrice"),
        }
    )


def fetch_chain(ticker: str, settings: Settings, now: datetime | None = None):
    """Download spot and the raw option chain for ``ticker``.

    Returns ``(spot, raw_chain)`` where raw_chain has RAW_COLUMNS.
    """
    import yfinance as yf

    symbol = settings.yahoo_symbol(ticker)
    tk = yf.Ticker(symbol)
    spot = fetch_spot(tk, symbol, settings)

    expirations = _retry(lambda: tk.options, f"expirations for {symbol}", settings)
    if not expirations:
        raise DataError(f"no listed options for {symbol}")
    today = (now or datetime.now(timezone.utc)).astimezone(NY).date()
    selected = select_expirations(expirations, today, settings)
    if not selected:
        raise DataError(f"no expirations for {symbol} within {settings.max_dte} days")

    frames = []
    for i, exp in enumerate(selected):
        if i:
            time.sleep(settings.pause_between_expirations)
        chain = _retry(lambda: tk.option_chain(exp), f"{symbol} chain {exp}", settings)
        frames.append(_normalize(chain.calls, "call", exp))
        frames.append(_normalize(chain.puts, "put", exp))
        log.info("%s: fetched %s (%d calls, %d puts)", ticker, exp, len(chain.calls), len(chain.puts))

    return spot, pd.concat(frames, ignore_index=True)


def next_earnings_date(calendar, today: date) -> str | None:
    """First earnings date on or after ``today`` from a yfinance calendar.

    ``calendar`` is the dict yfinance returns (``{"Earnings Date": [...]}``);
    older versions return a DataFrame, which is handled too. Returns an ISO
    date or None when nothing usable is listed.
    """
    try:
        dates = calendar["Earnings Date"] if isinstance(calendar, dict) else calendar.loc["Earnings Date"]
    except (KeyError, TypeError, AttributeError):
        return None
    if not isinstance(dates, (list, tuple, pd.Series, np.ndarray)):
        dates = [dates]
    upcoming = []
    for d in dates:
        try:
            d = pd.Timestamp(d).date()
        except (TypeError, ValueError):
            continue
        if d >= today:
            upcoming.append(d)
    return min(upcoming).isoformat() if upcoming else None


def fetch_earnings_date(ticker: str, settings: Settings, today: date) -> str | None:
    """Next earnings date for ``ticker``, or None (ETFs, indexes, lookup failure).

    Never raises: an earnings flag is not worth failing a run over.
    """
    import yfinance as yf

    try:
        return next_earnings_date(yf.Ticker(settings.yahoo_symbol(ticker)).calendar, today)
    except Exception as exc:
        log.warning("%s: earnings date lookup failed: %s", ticker, exc)
        return None


def time_to_expiry(expiration: pd.Series, now: datetime, min_days: float) -> pd.Series:
    """Years until 16:00 New York time on each expiration date, floored."""
    now_utc = now.astimezone(timezone.utc)
    seconds = [
        (datetime.combine(date.fromisoformat(str(e)), dtime(16, 0), NY) - now_utc).total_seconds()
        for e in expiration
    ]
    floor = min_days * 24 * 3600
    return pd.Series(np.maximum(seconds, floor) / SECONDS_PER_YEAR, index=expiration.index)


def clean_chain(raw: pd.DataFrame, spot: float, now: datetime, settings: Settings) -> pd.DataFrame:
    """Apply cleaning rules and add a ``t`` (years to expiry) column.

    Drops rows with missing strike / OI / IV, OI below the minimum, IV
    outside [min_iv, max_iv], strikes outside spot +/- strike_range_pct, and
    contracts that have already expired.
    """
    df = raw.copy()
    for col in ("strike", "open_interest", "iv"):
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.dropna(subset=["strike", "open_interest", "iv"])
    df = df[df["open_interest"] >= max(settings.min_open_interest, 1)]
    df = df[(df["iv"] >= settings.min_iv) & (df["iv"] <= settings.max_iv)]
    lo, hi = spot * (1 - settings.strike_range_pct), spot * (1 + settings.strike_range_pct)
    df = df[(df["strike"] >= lo) & (df["strike"] <= hi)]
    # Volume is optional in the raw chain (missing in synthetic data) and
    # often NaN on Yahoo; treat both as zero.
    volume = pd.to_numeric(df["volume"], errors="coerce") if "volume" in df else pd.Series(0, index=df.index)
    df["volume"] = volume.fillna(0).astype(int)

    if df.empty:
        return df.assign(t=pd.Series(dtype=float)).reset_index(drop=True)

    # Drop expirations whose 16:00 ET close has passed.
    now_utc = now.astimezone(timezone.utc)
    close = df["expiration"].map(
        lambda e: datetime.combine(date.fromisoformat(str(e)), dtime(16, 0), NY)
    )
    df = df[close.map(lambda c: c > now_utc).astype(bool)]

    df = df.assign(t=time_to_expiry(df["expiration"], now, settings.min_t_days))
    df["open_interest"] = df["open_interest"].astype(int)
    return df.reset_index(drop=True)
