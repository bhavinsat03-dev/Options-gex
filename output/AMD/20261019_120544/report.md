# AMD gamma exposure report

As of 2026-10-19T16:05:44+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 548.28 | The underlying price used for every calculation in this run. |
| Net GEX | $65.0M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 550.00, 620.00, 600.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 550.00, 545.00, 560.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 550.00: 2026-10-19 54%, 2026-10-23 20%, 2026-11-20 9%; 620.00: 2026-11-20 45%, 2026-10-30 29%, 2026-10-23 10%; 600.00: 2026-11-20 27%, 2026-10-23 22%, 2026-12-18 21% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 550.00: 2026-10-23 30%, 2026-11-20 26%, 2026-10-30 17%; 545.00: 2026-10-19 34%, 2026-10-23 24%, 2026-10-21 23%; 560.00: 2026-11-20 38%, 2026-10-23 26%, 2026-10-30 14% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 550.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 545.72 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $8.78B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $40.0M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | $63.1M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±7.00 (1.3%) -> 541.28 to 555.29, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 565,327 calls / 582,418 puts | Open contracts across all fetched expirations and strikes. |
| OI at main walls | call wall 550.00: 11,610 calls; put wall 550.00: 14,363 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.03 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -4.19 vol pts (put 54.4%, call 58.6%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 17.5% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 34.8% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 13.5% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 34.2% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$1.1M net, 9.2% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T15:31:23+00:00)

- Call wall: 550.00 -> 550.00 (+0.00)
- Put wall: 550.00 -> 550.00 (+0.00)
- Zero gamma: 541.37 -> 545.72 (+4.35)
- Abs gamma strike: 550.00 -> 550.00 (+0.00)
- Net GEX: $63.1M -> $65.0M (+$1.9M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
