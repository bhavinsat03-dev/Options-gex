# QQQ gamma exposure report

As of 2026-10-19T15:31:23+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 723.43 | The underlying price used for every calculation in this run. |
| Net GEX | -$1.82B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 725.00, 724.00, 723.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 720.00, 700.00, 710.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 725.00: 2026-10-19 66%, 2026-10-20 14%, 2026-10-23 9%; 724.00: 2026-10-19 76%, 2026-10-20 13%, 2026-10-21 6%; 723.00: 2026-10-19 76%, 2026-10-20 10%, 2026-10-23 6% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 720.00: 2026-10-30 25%, 2026-10-19 25%, 2026-10-23 22%; 700.00: 2026-10-30 71%, 2026-10-23 11%, 2026-11-06 7%; 710.00: 2026-10-23 46%, 2026-10-30 21%, 2026-11-06 17% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 725.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 727.44 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $41.55B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $861.5M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$1.75B | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±3.23 (0.4%) -> 720.20 to 726.66, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 1,139,605 calls / 1,921,303 puts | Open contracts across all fetched expirations and strikes. |
| OI at main walls | call wall 725.00: 21,916 calls; put wall 720.00: 76,868 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.69 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 5.66 vol pts (put 23.8%, call 18.1%, exp 2026-11-13) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 19.1% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 40.8% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 28.5% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 11.5% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $0 net, 0.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T14:20:13+00:00)

- Call wall: 721.00 -> 725.00 (+4.00)
- Put wall: 720.00 -> 720.00 (+0.00)
- Zero gamma: 724.90 -> 727.44 (+2.54)
- Abs gamma strike: 721.00 -> 725.00 (+4.00)
- Net GEX: -$1.53B -> -$1.82B (-$292.9M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
