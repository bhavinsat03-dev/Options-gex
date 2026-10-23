# SPY gamma exposure report

As of 2026-10-23T19:23:47+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 760.43 | The underlying price used for every calculation in this run. |
| Net GEX | -$16.17B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 770.00, 765.00, 780.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 755.00, 750.00, 760.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 770.00: 2026-10-30 56%, 2026-10-26 18%, 2026-10-28 12%; 765.00: 2026-10-26 53%, 2026-10-30 23%, 2026-10-27 15%; 780.00: 2026-10-30 87%, 2026-10-29 5%, 2026-10-28 4% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 755.00: 2026-10-26 85%, 2026-10-30 13%, 2026-10-27 1%; 750.00: 2026-10-26 59%, 2026-10-30 35%, 2026-10-27 4%; 760.00: 2026-10-23 79%, 2026-10-30 16%, 2026-10-26 2% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 760.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 766.18 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $34.86B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $943.4M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$3.50B | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±6.40 (0.8%) -> 754.03 to 766.83, exp 2026-10-26 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 1,264,051 calls / 2,604,887 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 790.00 (69,551); puts 750.00 (170,028) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 770 calls, 39,092 OI: 2026-10-23 50% (19,503), 2026-10-30 28% (11,140), 2026-10-26 10% (3,961); put wall 755 puts, 132,883 OI: 2026-10-26 64% (84,931), 2026-10-30 18% (23,470), 2026-10-23 16% (21,478); max call OI 790 calls, 69,551 OI: 2026-10-23 49% (34,131), 2026-10-30 38% (26,184), 2026-10-29 5% (3,605); max put OI 750 puts, 170,028 OI: 2026-10-26 51% (86,808), 2026-10-30 33% (55,649), 2026-10-23 11% (18,908) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 770.00: 39,092 calls; put wall 755.00: 132,883 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 2.06 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 2.56 vol pts (put 16.7%, call 14.1%, exp 2026-10-30) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 33.2% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 0.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 66.8% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 0.0% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $0 net, 0.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
