"""Settings loaded from a TOML config file."""

from __future__ import annotations

import tomllib
from dataclasses import dataclass, field, fields
from pathlib import Path

# Index tickers that Yahoo lists with a caret prefix.
DEFAULT_ALIASES = {"NDX": "^NDX", "SPX": "^SPX", "RUT": "^RUT", "VIX": "^VIX", "XSP": "^XSP"}
# If a ticker's chain is unavailable, derive its levels from this proxy by spot ratio.
DEFAULT_PROXIES = {"NDX": "QQQ", "SPX": "SPY"}


@dataclass
class Settings:
    tickers: list[str] = field(default_factory=lambda: ["QQQ", "NDX"])
    output_dir: str = "output"
    risk_free_rate: float = 0.04
    dividend_yield: float = 0.0
    # Chain selection / cleaning
    max_dte: int = 45  # rolling window of expirations, in calendar days
    max_expirations: int = 0  # 0 = every expiration in the window
    strike_range_pct: float = 0.20
    min_open_interest: int = 1
    # Below this much open interest after cleaning, the chain is treated as not
    # available (Yahoo blanks OI and IV before the open) instead of computing junk levels.
    min_total_oi: int = 1000
    min_iv: float = 0.01
    max_iv: float = 5.0
    min_t_days: float = 1.0 / 24.0  # floor time-to-expiry at one hour
    # Zero-gamma sweep / gamma profile
    sweep_pct: float = 0.10
    sweep_steps: int = 201
    # Metrics
    top_walls: int = 3
    skew_target_days: float = 30.0
    # Rate limiting
    pause_between_expirations: float = 0.5
    pause_between_tickers: float = 2.0
    max_retries: int = 3
    plots: bool = True
    history: bool = True
    aliases: dict[str, str] = field(default_factory=lambda: dict(DEFAULT_ALIASES))
    proxies: dict[str, str] = field(default_factory=lambda: dict(DEFAULT_PROXIES))

    def yahoo_symbol(self, ticker: str) -> str:
        return self.aliases.get(ticker.upper(), ticker.upper())


def load_settings(path: str | Path | None) -> Settings:
    """Load settings from ``path``; missing keys keep their defaults."""
    settings = Settings()
    if path is None:
        return settings
    path = Path(path)
    if not path.exists():
        return settings
    with path.open("rb") as fh:
        raw = tomllib.load(fh)

    known = {f.name for f in fields(Settings)}
    unknown = set(raw) - known
    if unknown:
        raise ValueError(f"Unknown config keys in {path}: {', '.join(sorted(unknown))}")
    for key, value in raw.items():
        if key == "aliases":
            settings.aliases.update({k.upper(): v for k, v in value.items()})
        elif key == "proxies":
            settings.proxies.update({k.upper(): v.upper() for k, v in value.items()})
        elif key == "tickers":
            settings.tickers = [t.upper() for t in value]
        else:
            setattr(settings, key, value)
    return settings
