# SPY gamma exposure report

As of 2026-10-23T13:51:27+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 760.71 | The underlying price used for every calculation in this run. |
| Net GEX | -$15.94B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 762.00, 765.00, 800.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 760.00, 750.00, 755.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 762.00: 2026-10-23 74%, 2026-10-30 11%, 2026-10-26 4%; 765.00: 2026-10-23 41%, 2026-10-26 19%, 2026-12-18 10%; 800.00: 2026-11-20 49%, 2026-12-18 36%, 2026-10-30 5% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 760.00: 2026-10-23 42%, 2026-10-30 32%, 2026-11-20 8%; 750.00: 2026-10-26 41%, 2026-10-30 20%, 2026-11-20 20%; 755.00: 2026-10-26 63%, 2026-10-23 14%, 2026-10-30 10% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 760.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 770.14 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $120.15B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $3.45B | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$2.67B | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±4.61 (0.6%) -> 756.10 to 765.32, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 3,057,693 calls / 8,152,062 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 800.00 (222,046); puts 750.00 (325,623) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 762 calls, 23,842 OI: 2026-10-23 27% (6,456), 2026-10-30 25% (5,940), 2026-12-18 20% (4,793); put wall 760 puts, 190,984 OI: 2026-10-30 41% (78,081), 2026-11-20 18% (34,688), 2026-12-18 12% (22,942); max call OI 800 calls, 222,046 OI: 2026-11-20 39% (85,806), 2026-12-18 25% (55,090), 2026-10-30 22% (49,075); max put OI 750 puts, 325,623 OI: 2026-11-20 27% (87,966), 2026-10-26 27% (86,808), 2026-10-30 17% (55,649) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 762.00: 23,842 calls; put wall 760.00: 190,984 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 2.67 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 4.76 vol pts (put 18.5%, call 13.7%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 20.9% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 0.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 39.8% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 39.3% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$82.2M net, 15.5% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-22T23:53:05+00:00)

- Call wall: 770.00 -> 762.00 (-8.00)
- Put wall: 760.00 -> 760.00 (+0.00)
- Zero gamma: 774.73 -> 770.14 (-4.59)
- Abs gamma strike: 760.00 -> 760.00 (+0.00)
- Net GEX: -$13.04B -> -$15.94B (-$2.90B)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
