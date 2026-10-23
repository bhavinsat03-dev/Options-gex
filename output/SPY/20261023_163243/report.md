# SPY gamma exposure report

As of 2026-10-23T20:32:43+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 759.97 | The underlying price used for every calculation in this run. |
| Net GEX | -$15.20B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 800.00, 780.00, 770.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 755.00, 750.00, 760.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 800.00: 2026-11-20 49%, 2026-12-18 38%, 2026-11-13 4%; 780.00: 2026-12-18 29%, 2026-10-30 27%, 2026-11-20 22%; 770.00: 2026-12-18 28%, 2026-10-30 24%, 2026-11-20 19% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 755.00: 2026-10-26 76%, 2026-10-30 11%, 2026-11-20 4%; 750.00: 2026-10-26 37%, 2026-10-30 22%, 2026-11-20 21%; 760.00: 2026-10-30 55%, 2026-11-20 13%, 2026-10-26 9% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 750.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 773.90 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $109.03B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $3.35B | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$1.90B | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±6.08 (0.8%) -> 753.89 to 766.05, exp 2026-10-26 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 3,057,693 calls / 8,152,062 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 800.00 (212,672); puts 750.00 (306,715) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 800 calls, 212,672 OI: 2026-11-20 40% (85,806), 2026-12-18 26% (55,090), 2026-10-30 23% (49,075); put wall 755 puts, 153,148 OI: 2026-10-26 55% (84,931), 2026-10-30 15% (23,470), 2026-11-20 10% (15,463); max call OI 800 calls, 212,672 OI: 2026-11-20 40% (85,806), 2026-12-18 26% (55,090), 2026-10-30 23% (49,075); max put OI 750 puts, 306,715 OI: 2026-11-20 29% (87,966), 2026-10-26 28% (86,808), 2026-10-30 18% (55,649) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 800.00: 212,672 calls; put wall 755.00: 153,148 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 2.67 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 3.30 vol pts (put 17.1%, call 13.8%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 0.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 51.8% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 48.2% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$275.5M net, 18.7% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-23T19:22:31+00:00)

- Call wall: 800.00 -> 800.00 (+0.00)
- Put wall: 750.00 -> 755.00 (+5.00)
- Zero gamma: 769.96 -> 773.90 (+3.94)
- Abs gamma strike: 760.00 -> 750.00 (-10.00)
- Net GEX: -$20.25B -> -$15.20B (+$5.05B)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
