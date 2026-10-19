# AMD gamma exposure report

As of 2026-10-19T16:33:15+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 547.48 | The underlying price used for every calculation in this run. |
| Net GEX | $36.2M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 550.00, 545.00, 620.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 550.00, 545.00, 530.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 550.00: 2026-10-19 58%, 2026-10-23 19%, 2026-11-20 8%; 545.00: 2026-10-19 63%, 2026-10-23 23%, 2026-10-21 7%; 620.00: 2026-11-20 46%, 2026-10-30 29%, 2026-10-23 9% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 550.00: 2026-10-19 25%, 2026-10-23 22%, 2026-11-20 20%; 545.00: 2026-10-19 59%, 2026-10-23 15%, 2026-10-21 14%; 530.00: 2026-10-23 34%, 2026-11-20 19%, 2026-11-06 14% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 550.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 545.30 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $9.68B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $37.3M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$36.8M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±5.42 (1.0%) -> 542.05 to 552.90, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 565,327 calls / 582,418 puts | Open contracts across all fetched expirations and strikes. |
| OI at main walls | call wall 550.00: 11,610 calls; put wall 550.00: 14,957 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.03 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -0.99 vol pts (put 56.7%, call 57.7%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 18.9% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 35.2% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 13.1% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 32.8% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $592.6K net, 8.8% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T16:20:30+00:00)

- Call wall: 550.00 -> 550.00 (+0.00)
- Put wall: 550.00 -> 550.00 (+0.00)
- Zero gamma: 544.11 -> 545.30 (+1.19)
- Abs gamma strike: 550.00 -> 550.00 (+0.00)
- Net GEX: $39.2M -> $36.2M (-$3.0M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
