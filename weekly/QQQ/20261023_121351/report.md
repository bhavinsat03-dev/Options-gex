# QQQ gamma exposure report

As of 2026-10-23T16:13:51+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 708.06 | The underlying price used for every calculation in this run. |
| Net GEX | -$4.90B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 710.00, 708.00, 709.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 710.00, 711.00, 700.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 710.00: 2026-10-23 87%, 2026-10-30 8%, 2026-10-26 3%; 708.00: 2026-10-23 96%, 2026-10-26 2%, 2026-10-30 1%; 709.00: 2026-10-23 92%, 2026-10-30 3%, 2026-10-26 2% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 710.00: 2026-10-23 80%, 2026-10-30 13%, 2026-10-26 3%; 711.00: 2026-10-23 98%, 2026-10-30 1%, 2026-10-26 1%; 700.00: 2026-10-30 85%, 2026-10-26 8%, 2026-10-28 3% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 710.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 717.79 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $35.30B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $282.6M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | $359.4M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±3.75 (0.5%) -> 704.31 to 711.81, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 888,009 calls / 1,536,097 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 735.00 (60,659); puts 700.00 (120,420) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 710 calls, 25,689 OI: 2026-10-23 49% (12,480), 2026-10-30 37% (9,627), 2026-10-26 6% (1,662); put wall 710 puts, 53,275 OI: 2026-10-30 48% (25,615), 2026-10-23 38% (20,072), 2026-10-26 5% (2,773); max call OI 735 calls, 60,659 OI: 2026-10-23 47% (28,355), 2026-10-27 29% (17,720), 2026-10-30 19% (11,430); max put OI 700 puts, 120,420 OI: 2026-10-30 73% (88,330), 2026-10-23 18% (21,860), 2026-10-26 4% (4,925) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 710.00: 25,689 calls; put wall 710.00: 53,275 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.73 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 3.92 vol pts (put 28.2%, call 24.3%, exp 2026-10-30) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 50.3% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 0.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 49.7% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 0.0% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $0 net, 0.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
