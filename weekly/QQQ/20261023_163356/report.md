# QQQ gamma exposure report

As of 2026-10-23T20:33:56+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 704.40 | The underlying price used for every calculation in this run. |
| Net GEX | -$3.58B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 710.00, 725.00, 730.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 700.00, 690.00, 695.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 710.00: 2026-10-30 60%, 2026-10-26 23%, 2026-10-27 12%; 725.00: 2026-10-30 81%, 2026-10-27 9%, 2026-10-28 4%; 730.00: 2026-10-30 83%, 2026-10-29 7%, 2026-10-28 4% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 700.00: 2026-10-30 83%, 2026-10-26 10%, 2026-10-28 3%; 690.00: 2026-10-30 86%, 2026-10-26 8%, 2026-10-27 2%; 695.00: 2026-10-30 50%, 2026-10-26 42%, 2026-10-29 3% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 700.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 725.65 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $25.93B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $269.0M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$581.6M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±9.89 (1.4%) -> 694.51 to 714.29, exp 2026-10-26 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 888,009 calls / 1,536,097 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 740.00 (36,252); puts 690.00 (98,637) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 710 calls, 13,209 OI: 2026-10-30 73% (9,627), 2026-10-26 13% (1,662), 2026-10-27 8% (1,113); put wall 700 puts, 98,560 OI: 2026-10-30 90% (88,330), 2026-10-26 5% (4,925), 2026-10-28 2% (2,074); max call OI 740 calls, 36,252 OI: 2026-10-30 61% (22,103), 2026-10-27 30% (10,747), 2026-10-26 5% (1,780); max put OI 690 puts, 98,637 OI: 2026-10-30 88% (87,035), 2026-10-26 7% (6,763), 2026-10-27 2% (1,855) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 710.00: 13,209 calls; put wall 700.00: 98,560 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.73 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 3.04 vol pts (put 27.5%, call 24.5%, exp 2026-10-30) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 0.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 100.0% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 0.0% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $0 net, 0.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
