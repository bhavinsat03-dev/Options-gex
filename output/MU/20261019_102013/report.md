# MU gamma exposure report

As of 2026-10-19T14:20:13+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 916.56 | The underlying price used for every calculation in this run. |
| Net GEX | $197.4M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 920.00, 915.00, 900.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 900.00, 950.00, 850.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 920.00: 2026-10-19 88%, 2026-10-23 3%, 2026-12-18 3%; 915.00: 2026-10-19 91%, 2026-10-23 5%, 2026-10-21 2%; 900.00: 2026-10-23 27%, 2026-10-21 25%, 2026-11-20 19% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 900.00: 2026-10-23 33%, 2026-11-20 20%, 2026-10-19 11%; 950.00: 2026-10-23 27%, 2026-10-30 23%, 2026-11-20 22%; 850.00: 2026-11-20 37%, 2026-10-23 26%, 2026-12-18 13% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 920.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 912.21 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $17.48B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $66.0M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$307.6M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±18.07 (2.0%) -> 898.49 to 934.64, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 655,183 calls / 742,320 puts | Open contracts across all fetched expirations and strikes. |
| OI at main walls | call wall 920.00: 7,361 calls; put wall 900.00: 21,303 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.13 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 7.69 vol pts (put 54.6%, call 46.9%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 26.2% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 25.5% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 14.2% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 34.1% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$15.9M net, 11.2% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T14:15:59+00:00)

- Call wall: 920.00 -> 920.00 (+0.00)
- Put wall: 900.00 -> 900.00 (+0.00)
- Zero gamma: 911.15 -> 912.21 (+1.06)
- Abs gamma strike: 920.00 -> 920.00 (+0.00)
- Net GEX: $53.4M -> $197.4M (+$144.0M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
