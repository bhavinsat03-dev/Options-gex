# SPY gamma exposure report

As of 2026-10-23T19:02:24+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 760.59 | The underlying price used for every calculation in this run. |
| Net GEX | -$16.70B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 761.00, 760.00, 770.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 760.00, 761.00, 755.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 761.00: 2026-10-23 95%, 2026-10-26 2%, 2026-10-30 1%; 760.00: 2026-10-23 82%, 2026-10-30 12%, 2026-10-26 2%; 770.00: 2026-10-30 55%, 2026-10-26 19%, 2026-10-28 11% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 760.00: 2026-10-23 75%, 2026-10-30 20%, 2026-10-26 3%; 761.00: 2026-10-23 97%, 2026-10-26 1%, 2026-10-30 1%; 755.00: 2026-10-26 85%, 2026-10-30 13%, 2026-10-27 1% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 760.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 769.95 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $39.96B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $942.4M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$2.87B | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±1.64 (0.2%) -> 758.95 to 762.22, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 1,264,051 calls / 2,604,887 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 790.00 (69,551); puts 750.00 (170,028) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 761 calls, 3,629 OI: 2026-10-23 52% (1,888), 2026-10-30 19% (672), 2026-10-26 13% (464); put wall 760 puts, 109,650 OI: 2026-10-30 71% (78,081), 2026-10-23 17% (19,072), 2026-10-26 5% (5,093); max call OI 790 calls, 69,551 OI: 2026-10-23 49% (34,131), 2026-10-30 38% (26,184), 2026-10-29 5% (3,605); max put OI 750 puts, 170,028 OI: 2026-10-26 51% (86,808), 2026-10-30 33% (55,649), 2026-10-23 11% (18,908) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 761.00: 3,629 calls; put wall 760.00: 109,650 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 2.06 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 3.27 vol pts (put 17.3%, call 14.0%, exp 2026-10-30) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 34.9% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 0.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 65.1% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 0.0% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $0 net, 0.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
