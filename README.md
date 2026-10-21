# options-gex

A command-line tool that estimates dealer options positioning for QQQ, NDX, SPY or any ticker with listed options. It uses free Yahoo Finance option chains (via `yfinance`).

It reports:
- **gamma exposure (GEX)**: net value, the top call and put walls, the absolute gamma strike, the zero-gamma flip and a gamma profile
- **delta, vanna and charm exposure**
- **expected move**
- **put/call open-interest ratio** and **25-delta skew**
- **expiry concentration**

Each run also writes a plain-English report and compares the results with the previous run.

> Descriptive analytics only. Nothing here is trading advice.

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
| `--max-dte N` | Rolling expiration window in days (default 45): every expiration within the next N days is used |
| `--max-expirations N` | Cap on the number of expirations per ticker (0 = no cap, the default) |
| `--strike-range F` | Keep strikes within spot ± F (for example 0.2 = ±20%) |
| `--no-plots` | Skip PNG charts |
| `--no-history` | Don't save to, or compare against, run history |
| `-v` | Verbose logging |

Index symbols are mapped to Yahoo's caret form automatically (`NDX → ^NDX`, `SPX → ^SPX`, `RUT`, `VIX`, `XSP`). To add more, use the `[aliases]` table in `config.toml`.

### Output

```
output/
├── summary_20261016_100000.csv       # one row per ticker (all headline metrics, errors included)
├── history/
│   ├── QQQ_20261015_100000.json      # every run's summary, used for change tracking
│   └── QQQ_20261016_100000.json
├── latest/
│   ├── QQQ_tradingview.txt           # latest levels string to paste into TradingView
│   └── QQQ_tradingview.pine          # latest indicator with those levels as its default
└── QQQ/20261016_100000/
    ├── report.md                     # every metric, its value and a one-line explanation
    ├── summary.json                  # all metrics, machine-readable
    ├── gex_by_strike.csv             # call/put/net/abs GEX, DEX, vanna, charm, OI per strike
    ├── contracts.csv                 # cleaned contracts with greeks and exposures
    ├── gamma_profile.csv             # total net GEX at each hypothetical spot
    ├── gex.png                       # GEX by strike, with walls, flip and expected-move band
    ├── gamma_profile.png             # net GEX vs. price (-10%..+10%), with flip and spot
    ├── tradingview_levels.txt        # this run's levels string
    └── tradingview.pine              # this run's indicator
```

The terminal shows a combined table, followed by the changes since the previous run:

```
Ticker     Spot Net GEX/1%         Regime Call wall Put wall Abs gamma Zero gamma        Exp. move P/C OI 25d skew           Status
   QQQ   603.00     $1.84B positive gamma    610.00   590.00    600.00     596.40    596.10-609.90   1.31      4.2               ok
  NDX* 24,700.0          - positive gamma  24,987.0 24,168.0  24,577.0   24,430.4  24,417.4-24,982.6  1.31      4.2 derived from QQQ

* derived: levels mapped from a proxy by spot ratio (that ticker's own chain was unavailable)

QQQ changes since 2026-10-15T14:00:00+00:00:
  Call wall: 605.00 -> 610.00 (+5.00)
  Zero gamma: 598.10 -> 596.40 (-1.70)
  Net GEX: $1.20B -> $1.84B (+$640.0M)
```

A ticker that fails is recorded with its error. The remaining tickers still run. The exit code is non-zero only if every ticker fails.

**Derived NDX levels.** Yahoo often has no `^NDX` option chain. When a ticker's chain is unavailable and it has a proxy (`NDX → QQQ` and `SPX → SPY` by default; see `[proxies]` in the config), the tool computes the proxy and multiplies its price levels by `ticker spot / proxy spot`. The scaled levels are walls, the absolute gamma strike, the flip and the expected-move range. The result is clearly marked as derived:
- `*` in the table and `derived from QQQ` in the status column
- `"derived": true` in the JSON
- a banner at the top of the report

Dollar exposures are left empty because they don't carry over from one product to another.

## TradingView

TradingView cannot fetch outside data, so the levels get there through a Pine Script indicator that reads them from a single text setting.

**One-time setup (per chart):**
1. Open `output/latest/<TICKER>_tradingview.pine`, copy all of it, paste it into TradingView's Pine Editor, and click **Add to chart**.

**Each update (once a morning is enough):**
1. Copy the single line in `output/latest/<TICKER>_tradingview.txt`. It looks like:
   ```
   SYM=META;ASOF=2026-10-16 09:00 ET;CW=600,610,620;PW=580,570,560;ZG=591.4;AG=590;EM=583.2,601.8;REG=positive gamma;SRC=chain
   ```
2. On the chart, open the indicator's settings (gear icon), paste the line into **Levels**, and click OK.

The indicator draws:
- the call walls (blue, dashed) and put walls (red, dashed), with the strongest wall of each drawn thicker
- the zero-gamma flip (dotted)
- the absolute gamma strike
- the expected-move band (shaded)

A small panel in the top-right corner shows the regime and the as-of time. If the levels belong to a different symbol from the chart, the panel shows a red warning. Derived levels (NDX from QQQ) are labelled "(from QQQ)".

## Automatic cloud runs (GitHub Actions)

`.github/workflows/gex.yml` runs the tool on GitHub's servers, so your computer can be off. The schedule is **09:50, 12:30 and 15:00 New York time, Monday to Friday**. The 09:50 run, after the opening quotes have settled, is the main one for the day's levels; the later runs track the regime and same-day expirations. Daylight saving is handled by the workflow, but GitHub may start scheduled runs several minutes late. Scheduled runs only work from the repository's **default branch**.

- **Tickers:** set by `TICKERS` near the top of the workflow file (currently META, SPY, QQQ, TSLA, BABA, MU, AMD, SPCX, IWM).
- **Where results go:** each run commits its reports, JSON, levels strings and history to the **`gex-data` branch**. The latest TradingView line is at `gex-data:output/latest/META_tradingview.txt`, which you can open from the GitHub app. Code and data stay on separate branches.
- **Charts:** charts and `contracts.csv` are not committed. They're attached to each run as a downloadable artifact, kept for 14 days.
- **Quick view:** each run's page in the **Actions** tab shows the summary table and the TradingView line.
- **Manual run:** Actions → GEX levels → **Run workflow**. You can enter other tickers there.
- **Failures:** if every ticker fails (for example, Yahoo blocks the request), the run is marked failed and GitHub emails you.

Market holidays aren't skipped. A holiday run just recalculates from the last session's data.

If you also run the tool on your own computer, avoid splitting the history across two places. Either work from the `gex-data` branch, or pass `--no-history` for local one-off checks.

## Method

### Data cleaning

Contracts are dropped when:
- open interest is zero or missing
- IV is missing or outside `[min_iv, max_iv]`; this removes Yahoo's `0.00001` placeholder IVs
- the strike is outside spot ± `strike_range_pct`
- the contract has expired, meaning it is past 16:00 New York time on the expiration date

Time to expiry runs to 16:00 ET on the expiration date and is floored at `min_t_days` (1 hour by default) so 0DTE gamma stays finite.

### Dealer convention

The usual GEX convention is used: **dealers are long calls and short puts**. The reasoning is that customers write covered calls (selling calls to dealers) and buy puts for protection (buying puts from dealers). Every exposure is computed as

```
exposure = sign × greek × OI × 100 × scaling,    sign = +1 calls, −1 puts
```

| Exposure | Formula | Units |
|---|---|---|
| GEX | sign × γ × OI × 100 × S² × 0.01 | $ of delta to re-hedge per 1% move |
| DEX | sign × Δ × OI × 100 × S | $ of delta held by dealers |
| Vanna | sign × ∂Δ/∂σ × OI × 100 × S × 0.01 | $ delta change per +1 vol point |
| Charm | sign × (−∂Δ/∂T) × OI × 100 × S / 365 | $ delta change per calendar day |

The Greeks come from Black-Scholes with a risk-free rate *r* and a continuous dividend yield *q*:
- d₁ = [ln(S/K) + (r − q + σ²/2)T] / (σ√T), and d₂ = d₁ − σ√T
- γ = e^(−qT) φ(d₁) / (Sσ√T)
- Δ = e^(−qT) N(d₁) for calls, and −e^(−qT) N(−d₁) for puts
- vanna = −e^(−qT) φ(d₁) d₂ / σ
- charm follows the standard closed form

The tests check delta, vanna and charm against finite differences.

### Metrics

- **Call walls / put walls (top 3).** The 3 strikes with the largest positive call GEX, and the 3 with the most negative put GEX.
- **Absolute gamma strike.** The strike where |call GEX| + |put GEX| is largest.
- **Gamma profile and zero-gamma flip.** The tool re-prices every contract's gamma at 201 spot prices from −10% to +10% (`sweep_pct`), holding IV, T and OI fixed. The flip is where total GEX crosses zero, found by linear interpolation; if there are several crossings, the one nearest spot is used.
- **Regime.** `positive gamma` if net GEX at the current spot is ≥ 0, otherwise `negative gamma`. Each label comes with a one-line neutral description.
- **Expiry concentration.** The share of total |GEX| expiring in four buckets that don't overlap:
  - 0DTE (today)
  - the rest of this week (through Sunday)
  - the rest of this calendar month
  - beyond

  It also reports the net GEX, and the share of |GEX|, that expires *after* the next standard monthly expiry (the third Friday).
- **Expected move.** The price of the nearest-expiry ATM straddle (call + put at the strike closest to spot). The tool uses the mid price, or the last trade if the quote is one-sided. It's shown as the range `spot ± move` and drawn as a shaded band on `gex.png`.
- **Put/call OI ratio.** Total put OI divided by total call OI across all fetched expirations.
- **25-delta skew.** IV(25Δ put) − IV(25Δ call) in vol points, using the expiry closest to 30 days. Each IV is interpolated in delta across strikes.

### History

Each run's summary is saved to `<output_dir>/history/<TICKER>_<timestamp>.json`; there is no database. On the next run, the tool finds the most recent earlier file for each ticker. It then prints, and adds to `report.md`, the change in:
- call wall
- put wall
- zero gamma
- absolute gamma strike
- net GEX

Each run also saves a compressed per-contract open-interest snapshot
(`<TICKER>_<timestamp>_oi.csv.gz`). The next day's runs compare against it to
list the largest OI adds and drops by contract in the brief's
**Positioning changes** section.

### Rate limiting

The tool pauses between expiration requests and between tickers. Failed requests are retried with exponential backoff.

## Glossary

| Term | Meaning |
|---|---|
| **GEX (gamma exposure)** | How many dollars of the underlying dealers would need to buy or sell to stay hedged after a 1% price move. Positive: they trade against the move. Negative: they trade with it. |
| **Call wall** | A strike with a large amount of dealer call gamma. Hedging flows there have tended to slow rallies. The tool reports the top three. |
| **Put wall** | A strike with a large amount of dealer put gamma. Hedging flows there have tended to slow declines, or to accelerate them once the strike breaks. The tool reports the top three. |
| **Zero-gamma (flip)** | The price at which total dealer gamma would change sign. It is the boundary between the positive and negative gamma regimes. |
| **Absolute gamma strike** | The single strike with the most total gamma, calls and puts combined, regardless of sign. It often acts as a price magnet. |
| **DEX (delta exposure)** | The dollar delta dealers hold from their options positions, which their stock hedge offsets. |
| **Vanna** | How delta changes when implied volatility changes. Vanna exposure is the dollar delta dealers gain or lose when IV rises one point, so moves in volatility create hedging flows. |
| **Charm** | How delta changes as time passes with price and IV unchanged. Charm exposure is the daily change in dealer dollar delta from time decay alone. It matters most near expiry. |
| **Regime** | "Positive gamma" when net GEX at the current price is positive: dealer hedging tends to offset moves. "Negative gamma" when it is negative: hedging tends to reinforce moves. The brief adds "near flip" when spot is within one expected move of the zero-gamma level, because the label can change on a small move. |
| **σ (sigma) distance** | Distance from spot to a level measured in expected moves (one σ = the nearest-expiry ATM straddle). It makes tickers comparable: 1% is far for SPY but nothing for TSLA. |
| **OI adds / drops** | The contracts (strike, type, expiry) whose open interest rose or fell the most since the previous day. Open interest updates overnight, so this is yesterday's new positioning. Expired contracts are excluded. |
| **High volume vs OI** | Contracts whose volume today is at least 500 and at least half their open interest. Volume is the only intraday sign of positioning that will show up in tomorrow's OI. |
| **Earnings** | The next earnings date, shown only when it falls inside the expiry window. Around earnings, open interest and implied volatility are dominated by the event, so walls and the expected move mean something different. |

## Caveats

- Yahoo open interest is updated once a day, so intraday results reflect the previous day's positioning.
- The dealer-positioning assumption is a convention, not observed data.
- Yahoo IVs and quotes can be stale outside market hours. The expected move and skew are most reliable during the session.

## Development

```bash
pip install pytest
pytest
```

The tests use synthetic chains and need no network access.

```
src/gex/
├── config.py   # TOML settings, ticker aliases, proxies
├── data.py     # yfinance fetching, retries, cleaning, time to expiry
├── greeks.py   # Black-Scholes gamma, delta, vanna, charm (vectorized)
├── gex.py      # exposures, walls, profile, flip, expiry buckets, expected move, skew, proxy mapping
├── history.py  # per-run JSON history and change detection
├── report.py   # plain-English report.md
├── plot.py     # gex.png and gamma_profile.png
└── cli.py      # argument parsing, per-ticker runs, outputs
```

### Brief sections

`latest/brief.md` (and each scheduled post) has four sections: **1) Levels** (regime, flip, GEX, walls with OI and σ distance, earnings flag), **2) Dealer positioning and volatility**, **3) Key expiries and wall OI change**, and **4) Positioning changes** (largest OI adds and drops since the previous day plus today's high volume-vs-OI contracts). Section 4 is omitted with `--no-history`, since it needs the previous day's OI snapshot.

### Weekly SPY/QQQ table

Each scheduled post also includes a second set of tables for SPY and QQQ computed
from only the options expiring in the next 7 days (`WEEKLY_TICKERS` in the
workflow). Locally: `python -m gex SPY QQQ --max-dte 7 --no-history --title "Weekly"`.
