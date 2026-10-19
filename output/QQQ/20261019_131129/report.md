# QQQ gamma exposure report

As of 2026-10-19T17:11:29+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 719.69 | The underlying price used for every calculation in this run. |
| Net GEX | -$3.55B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 720.00, 721.00, 719.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 720.00, 710.00, 700.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 720.00: 2026-10-19 81%, 2026-10-20 8%, 2026-10-23 4%; 721.00: 2026-10-19 86%, 2026-10-20 8%, 2026-10-23 2%; 719.00: 2026-10-19 84%, 2026-10-20 9%, 2026-10-23 3% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 720.00: 2026-10-19 71%, 2026-10-30 9%, 2026-10-23 8%; 710.00: 2026-10-23 47%, 2026-10-30 20%, 2026-11-06 15%; 700.00: 2026-10-30 70%, 2026-10-23 12%, 2026-11-06 6% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 720.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 725.66 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $44.34B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $752.2M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$893.5M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±2.47 (0.3%) -> 717.22 to 722.17, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 1,139,605 calls / 1,921,303 puts | Open contracts across all fetched expirations and strikes. |
| OI at main walls | call wall 720.00: 28,569 calls; put wall 720.00: 76,868 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.69 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 4.62 vol pts (put 23.9%, call 19.3%, exp 2026-11-13) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 29.1% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 34.9% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 25.7% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 10.3% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $0 net, 0.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T17:02:05+00:00)

- Call wall: 720.00 -> 720.00 (+0.00)
- Put wall: 720.00 -> 720.00 (+0.00)
- Zero gamma: 725.61 -> 725.66 (+0.05)
- Abs gamma strike: 720.00 -> 720.00 (+0.00)
- Net GEX: -$3.32B -> -$3.55B (-$230.7M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
