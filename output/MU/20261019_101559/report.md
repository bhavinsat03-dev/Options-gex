# MU gamma exposure report

As of 2026-10-19T14:15:59+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 913.84 | The underlying price used for every calculation in this run. |
| Net GEX | $53.4M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 920.00, 910.00, 915.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 900.00, 920.00, 950.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 920.00: 2026-10-19 83%, 2026-10-23 5%, 2026-12-18 5%; 910.00: 2026-10-19 61%, 2026-11-20 20%, 2026-10-21 6%; 915.00: 2026-10-19 87%, 2026-10-23 8%, 2026-10-21 3% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 900.00: 2026-10-23 34%, 2026-11-20 19%, 2026-10-19 12%; 920.00: 2026-10-19 51%, 2026-11-20 14%, 2026-10-23 12%; 950.00: 2026-10-23 29%, 2026-10-30 23%, 2026-11-20 22% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 920.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 911.15 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $18.00B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $63.5M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$302.8M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±15.68 (1.7%) -> 898.17 to 929.52, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Put/call OI ratio | 1.13 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 3.99 vol pts (put 52.4%, call 48.4%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 23.9% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 26.3% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 14.6% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 35.2% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$21.1M net, 11.6% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T13:56:52+00:00)

- Call wall: 900.00 -> 920.00 (+20.00)
- Put wall: 900.00 -> 900.00 (+0.00)
- Zero gamma: 912.42 -> 911.15 (-1.27)
- Abs gamma strike: 900.00 -> 920.00 (+20.00)
- Net GEX: -$10.9M -> $53.4M (+$64.3M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
