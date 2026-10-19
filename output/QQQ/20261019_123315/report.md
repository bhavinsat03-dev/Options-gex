# QQQ gamma exposure report

As of 2026-10-19T16:33:15+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 721.23 | The underlying price used for every calculation in this run. |
| Net GEX | -$2.68B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 720.00, 722.00, 721.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 720.00, 710.00, 700.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 720.00: 2026-10-19 73%, 2026-10-20 12%, 2026-10-23 6%; 722.00: 2026-10-19 85%, 2026-10-20 5%, 2026-10-23 3%; 721.00: 2026-10-19 88%, 2026-10-20 6%, 2026-10-23 2% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 720.00: 2026-10-19 49%, 2026-10-30 16%, 2026-10-23 15%; 710.00: 2026-10-23 46%, 2026-10-30 20%, 2026-11-06 16%; 700.00: 2026-10-30 71%, 2026-10-23 11%, 2026-11-06 6% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 720.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 725.81 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $43.14B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $811.8M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$504.5M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±3.00 (0.4%) -> 718.23 to 724.23, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 1,139,605 calls / 1,921,303 puts | Open contracts across all fetched expirations and strikes. |
| OI at main walls | call wall 720.00: 28,569 calls; put wall 720.00: 76,868 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.69 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 3.98 vol pts (put 23.3%, call 19.3%, exp 2026-11-13) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 25.8% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 36.6% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 26.8% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 10.8% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $0 net, 0.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T16:20:30+00:00)

- Call wall: 720.00 -> 720.00 (+0.00)
- Put wall: 720.00 -> 720.00 (+0.00)
- Zero gamma: 726.66 -> 725.81 (-0.85)
- Abs gamma strike: 720.00 -> 720.00 (+0.00)
- Net GEX: -$2.24B -> -$2.68B (-$435.3M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
