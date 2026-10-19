# BABA gamma exposure report

As of 2026-10-19T14:15:59+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 109.94 | The underlying price used for every calculation in this run. |
| Net GEX | $12.0M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 120.00, 110.00, 115.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 110.00, 100.00, 105.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 120.00: 2026-11-20 52%, 2026-12-18 31%, 2026-10-30 10%; 110.00: 2026-11-20 37%, 2026-10-23 26%, 2026-12-18 24%; 115.00: 2026-10-23 55%, 2026-11-20 17%, 2026-12-18 14% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 110.00: 2026-12-18 47%, 2026-11-20 31%, 2026-10-23 11%; 100.00: 2026-12-18 69%, 2026-11-20 22%, 2026-10-23 3%; 105.00: 2026-12-18 37%, 2026-11-20 31%, 2026-10-23 18% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 110.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 108.22 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $1.62B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $10.1M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$15.8M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±3.78 (3.4%) -> 106.17 to 113.72, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Put/call OI ratio | 0.56 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -0.56 vol pts (put 41.9%, call 42.5%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 28.1% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 10.5% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 61.5% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$5.5M net, 34.3% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T13:56:52+00:00)

- Call wall: 120.00 -> 120.00 (+0.00)
- Put wall: 110.00 -> 110.00 (+0.00)
- Zero gamma: 108.80 -> 108.22 (-0.58)
- Abs gamma strike: 110.00 -> 110.00 (+0.00)
- Net GEX: $3.3M -> $12.0M (+$8.7M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
