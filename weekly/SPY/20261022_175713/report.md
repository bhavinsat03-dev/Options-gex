# SPY gamma exposure report

As of 2026-10-22T21:57:13+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 763.96 | The underlying price used for every calculation in this run. |
| Net GEX | -$6.20B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 770.00, 768.00, 765.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 767.00, 765.00, 766.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 770.00: 2026-10-23 69%, 2026-10-26 14%, 2026-10-27 7%; 768.00: 2026-10-23 74%, 2026-10-26 12%, 2026-10-27 9%; 765.00: 2026-10-23 88%, 2026-10-26 5%, 2026-10-27 3% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 767.00: 2026-10-27 62%, 2026-10-23 30%, 2026-10-26 6%; 765.00: 2026-10-23 86%, 2026-10-26 6%, 2026-10-27 3%; 766.00: 2026-10-26 77%, 2026-10-23 17%, 2026-10-28 2% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 767.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 773.66 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $18.08B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $180.0M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$489.1M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±5.71 (0.7%) -> 758.25 to 769.67, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 706,284 calls / 1,084,617 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 790.00 (43,731); puts 767.00 (51,675) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 770 calls, 14,812 OI: 2026-10-23 65% (9,701), 2026-10-26 14% (2,058), 2026-10-28 9% (1,294); put wall 767 puts, 51,675 OI: 2026-10-27 72% (37,241), 2026-10-23 18% (9,302), 2026-10-26 6% (3,035); max call OI 790 calls, 43,731 OI: 2026-10-23 79% (34,593), 2026-10-29 8% (3,433), 2026-10-27 5% (2,384); max put OI 767 puts, 51,675 OI: 2026-10-27 72% (37,241), 2026-10-23 18% (9,302), 2026-10-26 6% (3,035) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 770.00: 14,812 calls; put wall 767.00: 51,675 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.54 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 2.43 vol pts (put 16.3%, call 13.8%, exp 2026-10-29) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 56.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 44.0% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 0.0% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $0 net, 0.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
