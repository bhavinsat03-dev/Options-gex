# SPY gamma exposure report

As of 2026-10-23T20:33:56+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 759.97 | The underlying price used for every calculation in this run. |
| Net GEX | -$10.72B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 770.00, 765.00, 780.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 755.00, 750.00, 760.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 770.00: 2026-10-30 57%, 2026-10-26 16%, 2026-10-28 12%; 765.00: 2026-10-26 53%, 2026-10-30 24%, 2026-10-27 15%; 780.00: 2026-10-30 87%, 2026-10-29 5%, 2026-10-28 4% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 755.00: 2026-10-26 85%, 2026-10-30 13%, 2026-10-27 1%; 750.00: 2026-10-26 58%, 2026-10-30 35%, 2026-10-27 4%; 760.00: 2026-10-30 77%, 2026-10-26 13%, 2026-10-28 5% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 755.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 772.59 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $31.68B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $884.3M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$1.24B | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±6.07 (0.8%) -> 753.90 to 766.04, exp 2026-10-26 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 1,264,052 calls / 2,604,887 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 800.00 (51,688); puts 750.00 (151,120) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 770 calls, 19,589 OI: 2026-10-30 57% (11,140), 2026-10-26 20% (3,961), 2026-10-28 10% (1,986); put wall 755 puts, 111,405 OI: 2026-10-26 76% (84,931), 2026-10-30 21% (23,470), 2026-10-27 1% (1,132); max call OI 800 calls, 51,688 OI: 2026-10-30 95% (49,075), 2026-10-27 2% (1,127), 2026-10-26 2% (990); max put OI 750 puts, 151,120 OI: 2026-10-26 57% (86,808), 2026-10-30 37% (55,649), 2026-10-27 4% (5,672) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 770.00: 19,589 calls; put wall 755.00: 111,405 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 2.06 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 1.83 vol pts (put 16.3%, call 14.5%, exp 2026-10-30) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 0.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 100.0% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 0.0% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $0 net, 0.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
