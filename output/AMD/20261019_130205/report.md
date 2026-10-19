# AMD gamma exposure report

As of 2026-10-19T17:02:05+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 543.33 | The underlying price used for every calculation in this run. |
| Net GEX | $6.1M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 542.50, 535.00, 540.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 542.50, 550.00, 540.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 542.50: 2026-10-19 93%, 2026-10-23 5%, 2026-10-21 1%; 535.00: 2026-10-19 73%, 2026-10-23 22%, 2026-10-21 2%; 540.00: 2026-10-19 63%, 2026-10-23 18%, 2026-11-20 7% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 542.50: 2026-10-19 96%, 2026-10-21 2%, 2026-10-23 1%; 550.00: 2026-10-23 30%, 2026-11-20 27%, 2026-10-30 17%; 540.00: 2026-10-19 28%, 2026-10-23 24%, 2026-10-30 14% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 542.50 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 543.15 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $8.74B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $38.0M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | $83.3M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±5.86 (1.1%) -> 537.47 to 549.19, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 565,327 calls / 582,418 puts | Open contracts across all fetched expirations and strikes. |
| OI at main walls | call wall 542.50: 1,843 calls; put wall 542.50: 1,250 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.03 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -2.51 vol pts (put 56.1%, call 58.6%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 23.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 32.8% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 12.2% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 32.0% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$904.3K net, 8.6% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T16:33:15+00:00)

- Call wall: 550.00 -> 542.50 (-7.50)
- Put wall: 550.00 -> 542.50 (-7.50)
- Zero gamma: 545.30 -> 543.15 (-2.15)
- Abs gamma strike: 550.00 -> 542.50 (-7.50)
- Net GEX: $36.2M -> $6.1M (-$30.1M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
