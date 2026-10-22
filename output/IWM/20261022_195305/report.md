# IWM gamma exposure report

As of 2026-10-22T23:53:05+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 276.67 | The underlying price used for every calculation in this run. |
| Net GEX | -$1.90B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 280.00, 278.00, 290.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 270.00, 277.00, 275.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 280.00: 2026-10-23 23%, 2026-10-29 21%, 2026-12-18 18%; 278.00: 2026-10-30 44%, 2026-10-23 42%, 2026-10-26 7%; 290.00: 2026-11-20 47%, 2026-12-18 41%, 2026-10-30 8% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 270.00: 2026-11-20 54%, 2026-12-18 19%, 2026-10-30 16%; 277.00: 2026-10-23 92%, 2026-11-20 4%, 2026-10-30 1%; 275.00: 2026-11-20 31%, 2026-10-23 29%, 2026-12-18 21% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 270.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 280.52 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $31.38B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $727.9M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$556.4M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±2.54 (0.9%) -> 274.14 to 279.21, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 1,908,669 calls / 4,000,951 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 290.00 (125,892); puts 260.00 (333,243) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 280 calls, 104,055 OI: 2026-12-18 35% (36,582), 2026-11-20 17% (17,588), 2026-10-29 15% (15,170); put wall 270 puts, 318,813 OI: 2026-11-20 53% (168,381), 2026-12-18 25% (79,912), 2026-10-30 11% (33,986); max call OI 290 calls, 125,892 OI: 2026-12-18 43% (53,569), 2026-11-20 41% (51,975), 2026-10-30 10% (12,295); max put OI 260 puts, 333,243 OI: 2026-12-18 37% (123,079), 2026-11-20 30% (98,572), 2026-10-30 23% (78,256) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 280.00: 104,055 calls; put wall 270.00: 318,813 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 2.10 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 2.65 vol pts (put 21.8%, call 19.2%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 19.4% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 23.2% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 57.4% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$356.4M net, 21.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-22T21:56:03+00:00)

- Call wall: 280.00 -> 280.00 (+0.00)
- Put wall: 270.00 -> 270.00 (+0.00)
- Zero gamma: 279.85 -> 280.52 (+0.67)
- Abs gamma strike: 277.00 -> 270.00 (-7.00)
- Net GEX: -$1.51B -> -$1.90B (-$393.2M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
