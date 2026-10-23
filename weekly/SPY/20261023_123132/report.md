# SPY gamma exposure report

As of 2026-10-23T16:31:32+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 761.69 | The underlying price used for every calculation in this run. |
| Net GEX | -$13.16B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 762.00, 763.00, 764.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 762.00, 760.00, 755.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 762.00: 2026-10-23 87%, 2026-10-30 8%, 2026-10-26 3%; 763.00: 2026-10-23 84%, 2026-10-26 7%, 2026-10-30 4%; 764.00: 2026-10-23 72%, 2026-10-26 12%, 2026-10-30 7% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 762.00: 2026-10-23 77%, 2026-10-26 15%, 2026-10-27 5%; 760.00: 2026-10-23 47%, 2026-10-30 41%, 2026-10-26 6%; 755.00: 2026-10-26 83%, 2026-10-30 15%, 2026-10-27 1% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 762.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 766.46 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $33.77B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $1.04B | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$3.19B | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±2.82 (0.4%) -> 758.87 to 764.52, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 1,264,052 calls / 2,604,887 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 790.00 (69,551); puts 750.00 (170,028) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 762 calls, 14,987 OI: 2026-10-23 43% (6,456), 2026-10-30 40% (5,940), 2026-10-26 7% (1,057); put wall 762 puts, 34,577 OI: 2026-10-26 37% (12,854), 2026-10-23 30% (10,293), 2026-10-27 16% (5,367); max call OI 790 calls, 69,551 OI: 2026-10-23 49% (34,131), 2026-10-30 38% (26,184), 2026-10-29 5% (3,605); max put OI 750 puts, 170,028 OI: 2026-10-26 51% (86,808), 2026-10-30 33% (55,649), 2026-10-23 11% (18,908) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 762.00: 14,987 calls; put wall 762.00: 34,577 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 2.06 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 1.96 vol pts (put 16.4%, call 14.5%, exp 2026-10-30) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 34.8% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 0.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 65.2% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 0.0% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $0 net, 0.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
