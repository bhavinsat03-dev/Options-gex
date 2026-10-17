# options-gex

A command-line tool that estimates dealer **gamma exposure (GEX)**, the **call wall**, the **put wall** and the **zero-gamma flip** for QQQ, NDX, SPY or any ticker with listed options. It uses free Yahoo Finance option chains (via `yfinance`).

## Install

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pip install -e .            # optional: installs the `gex` command
```

Requires Python 3.11+.

## Usage

```bash
gex                          # tickers from config.toml
gex QQQ NDX                  # override tickers on the command line
python -m gex SPY --max-dte 30 --strike-range 0.1 -v
```

| Option | Meaning |
|---|---|
| `TICKER ...` | Tickers to run. These override `tickers` in the config. |
| `-c, --config` | TOML config file (default `config.toml`) |
| `-o, --output-dir` | Output root (default `output/`) |
| `--max-dte N` | Only use expirations within N days |
| `--max-expirations N` | Cap on the number of expirations per ticker |
| `--strike-range F` | Keep strikes within spot ± F (for example 0.2 = ±20%) |
| `--no-plots` | Skip PNG charts |
| `-v` | Verbose logging |

Index symbols are mapped to Yahoo's caret form automatically (`NDX → ^NDX`, `SPX → ^SPX`, `RUT`, `VIX`, `XSP`). To add more, use the `[aliases]` table in `config.toml`.

### Output

```
output/
├── summary_20261016_100000.csv       # one row per ticker (errors included)
└── QQQ/20261016_100000/
    ├── summary.json                  # spot, net GEX, walls, zero gamma, regime
    ├── gex_by_strike.csv             # call / put / net GEX and OI per strike
    ├── contracts.csv                 # cleaned contracts with gamma and GEX
    ├── gex_profile.csv               # total GEX at each hypothetical spot
    └── gex.png                       # GEX by strike + GEX profile chart
```

The combined summary table is also printed to the terminal:

```
Ticker   Spot Net GEX/1% Call wall Put wall Zero gamma   Regime Status
   QQQ 600.12     $1.84B    610.00   590.00     596.40 positive     ok
   NDX      -          -         -        -          -        -  error: ...
```

A ticker that fails (no options, a network error, or nothing left after cleaning) is recorded with its error. The remaining tickers still run. The exit code is non-zero only if every ticker fails.

## Method

**Data cleaning.** Yahoo chains can be noisy, so contracts are dropped when:
- open interest is missing or zero (below `min_open_interest`)
- IV is missing or outside `[min_iv, max_iv]`; this removes Yahoo's `0.00001` placeholder IVs
- the strike is outside spot ± `strike_range_pct`
- the contract has expired, meaning it is past 16:00 New York time on the expiration date

Time to expiry runs to 16:00 ET on the expiration date and is floored at `min_t_days` (1 hour by default). Without the floor, same-day (0DTE) gamma blows up near the close.

**Gamma.** Black-Scholes gamma with continuous dividend yield *q* and risk-free rate *r*:

γ = e^(−qT) · φ(d₁) / (S σ √T),  d₁ = [ln(S/K) + (r − q + σ²/2)T] / (σ√T)

**GEX per contract.** This uses the common dealer convention: customers are net buyers of calls and net sellers of puts. Dealers are therefore long call gamma and short put gamma.

GEX = sign × γ × OI × 100 × S² × 0.01,  sign = +1 for calls, −1 for puts

The units are dollars of delta that dealers must trade for a 1% move in the underlying. Positive net GEX means dealers hedge against the move, which tends to dampen volatility. Negative net GEX means they hedge with the move, which tends to amplify it.

**Call wall.** The strike with the largest positive call GEX.
**Put wall.** The strike with the largest negative put GEX.

**Zero-gamma flip.** The tool sweeps a grid of hypothetical spot prices (spot ± `sweep_pct`, `sweep_steps` points). At each price it recomputes every contract's gamma, holding IV, T and OI fixed, and sums the net GEX. The flip is where this profile crosses zero, found by linear interpolation; if there are several crossings, the one nearest the current spot is used. If the profile never crosses zero inside the range, the flip is reported as empty. **Regime** is `positive` when spot is above the flip and `negative` when it is below.

**Rate limiting.** The tool pauses between expiration requests (`pause_between_expirations`) and between tickers (`pause_between_tickers`). Failed requests are retried with exponential backoff (`max_retries`).

## Caveats

- Yahoo open interest is updated once a day, so intraday GEX reflects the previous day's positioning.
- The dealer-positioning assumption is a convention, not observed data.
- Yahoo IVs can be stale outside market hours, so results are most reliable during the session.

## Development

```bash
pip install pytest
pytest
```

The tests use synthetic chains and need no network access.

```
src/gex/
├── config.py   # TOML settings and ticker aliases
├── data.py     # yfinance fetching, retries, cleaning, time to expiry
├── greeks.py   # Black-Scholes gamma (vectorized)
├── gex.py      # GEX per contract/strike, walls, profile, zero gamma
├── plot.py     # charts
└── cli.py      # argument parsing, per-ticker runs, outputs
```
