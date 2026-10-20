# SPY gamma exposure report

As of 2026-10-20T17:03:25+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 768.70 | The underlying price used for every calculation in this run. |
| Net GEX | -$633.2M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 770.00, 769.00, 768.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 769.00, 768.00, 765.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 770.00: 2026-10-20 66%, 2026-10-23 19%, 2026-10-21 10%; 769.00: 2026-10-20 82%, 2026-10-21 11%, 2026-10-23 4%; 768.00: 2026-10-20 82%, 2026-10-23 7%, 2026-10-21 6% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 769.00: 2026-10-20 49%, 2026-10-23 42%, 2026-10-21 6%; 768.00: 2026-10-20 71%, 2026-10-21 15%, 2026-10-23 8%; 765.00: 2026-10-23 62%, 2026-10-21 23%, 2026-10-26 5% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 769.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 768.90 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $17.30B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $575.0M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$1.53B | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±1.93 (0.3%) -> 766.77 to 770.63, exp 2026-10-20 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 720,796 calls / 1,275,041 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 790.00 (45,999); puts 745.00 (60,324) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 770 calls, 29,373 OI: 2026-10-23 43% (12,495), 2026-10-20 34% (9,843), 2026-10-21 12% (3,580); put wall 769 puts, 40,235 OI: 2026-10-23 80% (32,385), 2026-10-20 7% (2,967), 2026-10-21 6% (2,487); max call OI 790 calls, 45,999 OI: 2026-10-23 80% (36,677), 2026-10-26 6% (2,606), 2026-10-27 4% (2,050); max put OI 745 puts, 60,324 OI: 2026-10-23 63% (37,711), 2026-10-20 24% (14,779), 2026-10-22 5% (2,959) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 770.00: 29,373 calls; put wall 769.00: 40,235 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.77 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 1.10 vol pts (put 12.1%, call 11.0%, exp 2026-10-27) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 34.1% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 57.5% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 8.5% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 0.0% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $0 net, 0.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
