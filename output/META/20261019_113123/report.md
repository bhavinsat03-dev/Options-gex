# META gamma exposure report

As of 2026-10-19T15:31:23+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 703.74 | The underlying price used for every calculation in this run. |
| Net GEX | -$12.8M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 700.00, 800.00, 750.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 700.00, 705.00, 702.50 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 700.00: 2026-11-20 57%, 2026-10-19 18%, 2026-12-18 17%; 800.00: 2026-11-20 50%, 2026-12-18 24%, 2026-10-23 11%; 750.00: 2026-11-20 41%, 2026-10-23 28%, 2026-12-18 19% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 700.00: 2026-10-19 66%, 2026-12-18 11%, 2026-10-23 9%; 705.00: 2026-10-19 83%, 2026-10-23 7%, 2026-10-30 5%; 702.50: 2026-10-19 100%, 2026-10-23 0%, 2026-10-21 0% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 700.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 704.14 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $19.18B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $90.9M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$233.0M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±6.80 (1.0%) -> 696.93 to 710.54, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 669,033 calls / 440,298 puts | Open contracts across all fetched expirations and strikes. |
| OI at main walls | call wall 700.00: 31,444 calls; put wall 700.00: 16,650 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 0.66 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -1.04 vol pts (put 44.3%, call 45.4%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 18.8% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 21.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 9.4% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 50.8% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $65.3M net, 18.2% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T14:20:13+00:00)

- Call wall: 700.00 -> 700.00 (+0.00)
- Put wall: 700.00 -> 700.00 (+0.00)
- Zero gamma: 701.56 -> 704.14 (+2.58)
- Abs gamma strike: 700.00 -> 700.00 (+0.00)
- Net GEX: -$35.7M -> -$12.8M (+$22.9M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
