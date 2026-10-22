# SPY gamma exposure report

As of 2026-10-22T19:01:59+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 761.26 | The underlying price used for every calculation in this run. |
| Net GEX | -$7.93B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 770.00, 762.00, 768.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 761.00, 762.00, 760.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 770.00: 2026-10-23 62%, 2026-10-26 17%, 2026-10-28 9%; 762.00: 2026-10-22 58%, 2026-10-23 34%, 2026-10-26 4%; 768.00: 2026-10-23 68%, 2026-10-26 14%, 2026-10-27 12% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 761.00: 2026-10-22 85%, 2026-10-23 14%, 2026-10-26 1%; 762.00: 2026-10-26 50%, 2026-10-23 46%, 2026-10-27 2%; 760.00: 2026-10-23 80%, 2026-10-26 8%, 2026-10-28 5% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 761.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 768.44 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $14.72B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $161.0M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$1.68B | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±2.23 (0.3%) -> 759.04 to 763.50, exp 2026-10-22 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 706,284 calls / 1,084,617 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 790.00 (46,244); puts 745.00 (45,973) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 770 calls, 21,579 OI: 2026-10-23 45% (9,701), 2026-10-22 31% (6,767), 2026-10-26 10% (2,058); put wall 761 puts, 12,084 OI: 2026-10-23 54% (6,532), 2026-10-22 33% (3,942), 2026-10-27 4% (539); max call OI 790 calls, 46,244 OI: 2026-10-23 75% (34,593), 2026-10-29 7% (3,433), 2026-10-22 5% (2,513); max put OI 745 puts, 45,973 OI: 2026-10-23 82% (37,765), 2026-10-22 6% (2,597), 2026-10-26 5% (2,354) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 770.00: 21,579 calls; put wall 761.00: 12,084 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.54 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 1.69 vol pts (put 17.0%, call 15.3%, exp 2026-10-29) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 18.2% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 42.5% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 39.3% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 0.0% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $0 net, 0.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
