# META gamma exposure report

As of 2026-10-19T17:11:29+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 701.12 | The underlying price used for every calculation in this run. |
| Net GEX | -$121.9M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 700.00, 800.00, 750.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 700.00, 702.50, 750.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 700.00: 2026-11-20 47%, 2026-10-19 32%, 2026-12-18 14%; 800.00: 2026-11-20 50%, 2026-12-18 24%, 2026-10-23 10%; 750.00: 2026-11-20 41%, 2026-10-23 27%, 2026-12-18 19% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 700.00: 2026-10-19 86%, 2026-12-18 5%, 2026-10-23 4%; 702.50: 2026-10-19 100%, 2026-10-23 0%, 2026-10-21 0%; 750.00: 2026-10-23 72%, 2026-11-20 12%, 2026-12-18 10% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 700.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 703.16 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $18.98B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $91.5M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$241.5M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±5.08 (0.7%) -> 696.05 to 706.20, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 669,033 calls / 440,298 puts | Open contracts across all fetched expirations and strikes. |
| OI at main walls | call wall 700.00: 31,444 calls; put wall 700.00: 16,650 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 0.66 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -1.61 vol pts (put 43.5%, call 45.2%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 23.1% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 19.6% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 9.0% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 48.3% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $63.3M net, 17.3% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T17:02:05+00:00)

- Call wall: 700.00 -> 700.00 (+0.00)
- Put wall: 700.00 -> 700.00 (+0.00)
- Zero gamma: 703.32 -> 703.16 (-0.16)
- Abs gamma strike: 700.00 -> 700.00 (+0.00)
- Net GEX: -$107.2M -> -$121.9M (-$14.6M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
