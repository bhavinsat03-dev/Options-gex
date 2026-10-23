# QQQ gamma exposure report

As of 2026-10-23T16:31:32+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 706.87 | The underlying price used for every calculation in this run. |
| Net GEX | -$3.74B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 710.00, 708.00, 706.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 705.00, 700.00, 707.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 710.00: 2026-10-23 75%, 2026-10-30 15%, 2026-10-26 6%; 708.00: 2026-10-23 95%, 2026-10-26 2%, 2026-10-30 1%; 706.00: 2026-10-23 95%, 2026-10-26 3%, 2026-10-27 1% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 705.00: 2026-10-23 73%, 2026-10-30 19%, 2026-10-26 3%; 700.00: 2026-10-30 84%, 2026-10-26 9%, 2026-10-28 3%; 707.00: 2026-10-23 94%, 2026-10-26 3%, 2026-10-30 2% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 705.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 711.85 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $29.40B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $338.6M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$1.90B | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±3.65 (0.5%) -> 703.21 to 710.51, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 888,009 calls / 1,536,097 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 735.00 (60,659); puts 700.00 (120,420) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 710 calls, 25,689 OI: 2026-10-23 49% (12,480), 2026-10-30 37% (9,627), 2026-10-26 6% (1,662); put wall 705 puts, 40,198 OI: 2026-10-30 58% (23,166), 2026-10-23 28% (11,137), 2026-10-28 4% (1,696); max call OI 735 calls, 60,659 OI: 2026-10-23 47% (28,355), 2026-10-27 29% (17,720), 2026-10-30 19% (11,430); max put OI 700 puts, 120,420 OI: 2026-10-30 73% (88,330), 2026-10-23 18% (21,860), 2026-10-26 4% (4,925) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 710.00: 25,689 calls; put wall 705.00: 40,198 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.73 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 3.82 vol pts (put 28.6%, call 24.8%, exp 2026-10-30) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 40.4% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 0.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 59.6% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 0.0% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $0 net, 0.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
