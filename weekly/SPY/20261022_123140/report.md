# SPY gamma exposure report

As of 2026-10-22T16:31:40+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 764.75 | The underlying price used for every calculation in this run. |
| Net GEX | -$8.34B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 765.00, 770.00, 766.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 765.00, 766.00, 767.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 765.00: 2026-10-22 81%, 2026-10-23 17%, 2026-10-26 1%; 770.00: 2026-10-23 73%, 2026-10-26 12%, 2026-10-27 6%; 766.00: 2026-10-22 47%, 2026-10-23 41%, 2026-10-27 5% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 765.00: 2026-10-22 62%, 2026-10-23 32%, 2026-10-26 3%; 766.00: 2026-10-26 46%, 2026-10-22 41%, 2026-10-23 10%; 767.00: 2026-10-27 61%, 2026-10-23 29%, 2026-10-26 6% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 765.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 770.06 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $17.80B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $260.9M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$1.00B | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±2.82 (0.4%) -> 761.93 to 767.57, exp 2026-10-22 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 706,284 calls / 1,084,617 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 790.00 (46,244); puts 767.00 (55,440) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 765 calls, 8,345 OI: 2026-10-22 47% (3,928), 2026-10-23 40% (3,363), 2026-10-26 4% (351); put wall 765 puts, 27,865 OI: 2026-10-23 55% (15,378), 2026-10-22 25% (6,944), 2026-10-26 8% (2,126); max call OI 790 calls, 46,244 OI: 2026-10-23 75% (34,593), 2026-10-29 7% (3,433), 2026-10-22 5% (2,513); max put OI 767 puts, 55,440 OI: 2026-10-27 67% (37,241), 2026-10-23 17% (9,302), 2026-10-22 7% (3,765) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 765.00: 8,345 calls; put wall 765.00: 27,865 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.54 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 1.34 vol pts (put 15.2%, call 13.8%, exp 2026-10-29) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 26.9% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 40.7% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 32.4% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 0.0% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $0 net, 0.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
