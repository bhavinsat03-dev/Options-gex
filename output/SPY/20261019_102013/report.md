# SPY gamma exposure report

As of 2026-10-19T14:20:13+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 768.69 | The underlying price used for every calculation in this run. |
| Net GEX | -$1.80B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 770.00, 769.00, 768.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 765.00, 760.00, 750.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 770.00: 2026-10-19 53%, 2026-10-23 15%, 2026-10-20 13%; 769.00: 2026-10-19 81%, 2026-10-20 7%, 2026-10-21 4%; 768.00: 2026-10-19 66%, 2026-10-20 13%, 2026-10-23 8% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 765.00: 2026-10-30 40%, 2026-10-19 30%, 2026-10-23 14%; 760.00: 2026-10-30 64%, 2026-10-23 16%, 2026-11-06 5%; 750.00: 2026-10-30 74%, 2026-11-06 9%, 2026-10-23 8% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 770.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 769.16 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $44.73B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $1.96B | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$3.93B | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±3.57 (0.5%) -> 765.12 to 772.26, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 1,514,940 calls / 3,235,545 puts | Open contracts across all fetched expirations and strikes. |
| OI at main walls | call wall 770.00: 54,195 calls; put wall 765.00: 77,767 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 2.14 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 5.12 vol pts (put 16.6%, call 11.5%, exp 2026-11-13) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 23.9% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 39.1% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 30.1% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 7.0% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $0 net, 0.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T14:15:59+00:00)

- Call wall: 768.00 -> 770.00 (+2.00)
- Put wall: 765.00 -> 765.00 (+0.00)
- Zero gamma: 769.16 -> 769.16 (+0.00)
- Abs gamma strike: 768.00 -> 770.00 (+2.00)
- Net GEX: -$1.98B -> -$1.80B (+$179.6M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
