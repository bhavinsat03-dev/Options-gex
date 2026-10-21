# SPY gamma exposure report

As of 2026-10-21T01:11:30+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 769.05 | The underlying price used for every calculation in this run. |
| Net GEX | -$2.36B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 770.00, 780.00, 775.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 769.00, 762.00, 765.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 770.00: 2026-10-23 55%, 2026-10-21 29%, 2026-10-22 9%; 780.00: 2026-10-23 63%, 2026-10-26 17%, 2026-10-22 15%; 775.00: 2026-10-23 43%, 2026-10-22 28%, 2026-10-21 17% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 769.00: 2026-10-23 82%, 2026-10-21 12%, 2026-10-22 3%; 762.00: 2026-10-23 55%, 2026-10-26 33%, 2026-10-22 5%; 765.00: 2026-10-23 62%, 2026-10-21 23%, 2026-10-26 6% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 769.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 772.09 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $14.60B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $540.1M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$1.73B | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±4.38 (0.6%) -> 764.67 to 773.42, exp 2026-10-21 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 553,162 calls / 977,620 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 790.00 (44,712); puts 745.00 (45,545) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 770 calls, 19,530 OI: 2026-10-23 64% (12,495), 2026-10-21 18% (3,580), 2026-10-22 9% (1,674); put wall 769 puts, 37,268 OI: 2026-10-23 87% (32,385), 2026-10-21 7% (2,487), 2026-10-26 3% (1,005); max call OI 790 calls, 44,712 OI: 2026-10-23 82% (36,677), 2026-10-26 6% (2,606), 2026-10-27 5% (2,050); max put OI 745 puts, 45,545 OI: 2026-10-23 83% (37,711), 2026-10-22 6% (2,959), 2026-10-21 6% (2,838) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 770.00: 19,530 calls; put wall 769.00: 37,268 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.77 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 0.96 vol pts (put 12.2%, call 11.3%, exp 2026-10-27) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 87.2% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 12.8% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 0.0% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $0 net, 0.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
