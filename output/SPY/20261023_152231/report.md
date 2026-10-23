# SPY gamma exposure report

As of 2026-10-23T19:22:31+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 760.49 | The underlying price used for every calculation in this run. |
| Net GEX | -$20.25B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 800.00, 770.00, 780.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 750.00, 755.00, 760.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 800.00: 2026-11-20 50%, 2026-12-18 38%, 2026-11-13 4%; 770.00: 2026-12-18 28%, 2026-10-30 25%, 2026-11-20 19%; 780.00: 2026-12-18 29%, 2026-10-30 27%, 2026-11-20 22% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 750.00: 2026-10-26 37%, 2026-10-30 22%, 2026-11-20 21%; 755.00: 2026-10-26 75%, 2026-10-30 12%, 2026-11-20 4%; 760.00: 2026-10-23 69%, 2026-10-30 17%, 2026-11-20 4% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 760.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 769.96 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $116.10B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $3.41B | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$3.60B | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±6.36 (0.8%) -> 754.12 to 766.84, exp 2026-10-26 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 3,057,666 calls / 8,152,062 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 800.00 (222,046); puts 750.00 (325,623) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 800 calls, 222,046 OI: 2026-11-20 39% (85,806), 2026-12-18 25% (55,090), 2026-10-30 22% (49,075); put wall 750 puts, 325,623 OI: 2026-11-20 27% (87,966), 2026-10-26 27% (86,808), 2026-10-30 17% (55,649); max call OI 800 calls, 222,046 OI: 2026-11-20 39% (85,806), 2026-12-18 25% (55,090), 2026-10-30 22% (49,075); max put OI 750 puts, 325,623 OI: 2026-11-20 27% (87,966), 2026-10-26 27% (86,808), 2026-10-30 17% (55,649) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 800.00: 222,046 calls; put wall 750.00: 325,623 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 2.67 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 3.98 vol pts (put 17.5%, call 13.6%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 19.9% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 0.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 41.4% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 38.7% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$206.0M net, 15.1% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-23T19:01:06+00:00)

- Call wall: 760.00 -> 800.00 (+40.00)
- Put wall: 760.00 -> 750.00 (-10.00)
- Zero gamma: 770.80 -> 769.96 (-0.84)
- Abs gamma strike: 760.00 -> 760.00 (+0.00)
- Net GEX: -$21.32B -> -$20.25B (+$1.07B)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
