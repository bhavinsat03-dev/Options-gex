# AMD gamma exposure report

As of 2026-10-19T16:20:30+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 548.30 | The underlying price used for every calculation in this run. |
| Net GEX | $39.2M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 550.00, 620.00, 545.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 550.00, 545.00, 560.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 550.00: 2026-10-19 64%, 2026-10-23 16%, 2026-11-20 7%; 620.00: 2026-11-20 46%, 2026-10-30 29%, 2026-10-23 9%; 545.00: 2026-10-19 59%, 2026-10-23 26%, 2026-10-21 8% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 550.00: 2026-10-19 44%, 2026-10-23 16%, 2026-11-20 15%; 545.00: 2026-10-19 53%, 2026-10-23 17%, 2026-10-21 15%; 560.00: 2026-11-20 37%, 2026-10-23 23%, 2026-10-30 12% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 550.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 544.11 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $9.89B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $37.1M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$16.3M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±5.71 (1.0%) -> 542.60 to 554.01, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 565,327 calls / 582,418 puts | Open contracts across all fetched expirations and strikes. |
| OI at main walls | call wall 550.00: 11,610 calls; put wall 550.00: 14,957 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.03 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -0.00 vol pts (put 57.2%, call 57.2%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 20.2% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 35.1% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 12.8% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 32.0% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $1.3M net, 8.6% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T16:05:44+00:00)

- Call wall: 550.00 -> 550.00 (+0.00)
- Put wall: 550.00 -> 550.00 (+0.00)
- Zero gamma: 545.72 -> 544.11 (-1.61)
- Abs gamma strike: 550.00 -> 550.00 (+0.00)
- Net GEX: $65.0M -> $39.2M (-$25.8M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
