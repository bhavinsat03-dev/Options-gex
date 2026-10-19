# SPY gamma exposure report

As of 2026-10-19T16:33:15+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 768.06 | The underlying price used for every calculation in this run. |
| Net GEX | -$3.41B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 768.00, 770.00, 769.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 768.00, 767.00, 769.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 768.00: 2026-10-19 86%, 2026-10-20 5%, 2026-10-23 4%; 770.00: 2026-10-19 44%, 2026-10-23 19%, 2026-10-20 14%; 769.00: 2026-10-19 75%, 2026-10-20 8%, 2026-10-21 6% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 768.00: 2026-10-19 77%, 2026-10-21 7%, 2026-10-20 6%; 767.00: 2026-10-19 73%, 2026-10-23 10%, 2026-10-30 5%; 769.00: 2026-10-23 58%, 2026-10-19 23%, 2026-10-20 5% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 768.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 769.13 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $45.42B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $1.89B | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$2.53B | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±2.18 (0.3%) -> 765.88 to 770.24, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 1,514,941 calls / 3,235,545 puts | Open contracts across all fetched expirations and strikes. |
| OI at main walls | call wall 768.00: 20,443 calls; put wall 768.00: 16,697 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 2.14 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 2.48 vol pts (put 14.9%, call 12.4%, exp 2026-11-13) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 25.5% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 37.7% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 29.8% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 7.0% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $0 net, 0.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T16:20:30+00:00)

- Call wall: 768.00 -> 768.00 (+0.00)
- Put wall: 769.00 -> 768.00 (-1.00)
- Zero gamma: 769.73 -> 769.13 (-0.60)
- Abs gamma strike: 768.00 -> 768.00 (+0.00)
- Net GEX: -$3.07B -> -$3.41B (-$344.3M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
