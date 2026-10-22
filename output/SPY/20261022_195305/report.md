# SPY gamma exposure report

As of 2026-10-22T23:53:05+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 763.96 | The underlying price used for every calculation in this run. |
| Net GEX | -$13.04B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 770.00, 800.00, 780.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 760.00, 765.00, 767.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 770.00: 2026-10-23 27%, 2026-12-18 21%, 2026-10-30 21%; 800.00: 2026-11-20 50%, 2026-12-18 34%, 2026-10-30 6%; 780.00: 2026-10-30 33%, 2026-12-18 26%, 2026-11-20 18% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 760.00: 2026-10-30 43%, 2026-10-23 25%, 2026-11-20 11%; 765.00: 2026-10-23 43%, 2026-10-30 34%, 2026-11-20 10%; 767.00: 2026-10-27 55%, 2026-10-23 27%, 2026-10-26 5% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 760.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 774.73 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $110.30B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $3.32B | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$1.79B | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±5.71 (0.7%) -> 758.25 to 769.67, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 3,021,926 calls / 7,977,595 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 800.00 (214,898); puts 750.00 (226,142) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 770 calls, 82,350 OI: 2026-12-18 41% (33,876), 2026-11-20 19% (15,432), 2026-10-30 15% (12,381); put wall 760 puts, 183,049 OI: 2026-10-30 41% (75,291), 2026-11-20 19% (34,886), 2026-12-18 12% (22,711); max call OI 800 calls, 214,898 OI: 2026-11-20 38% (81,279), 2026-12-18 25% (53,042), 2026-10-30 23% (49,118); max put OI 750 puts, 226,142 OI: 2026-11-20 36% (81,348), 2026-10-30 30% (67,250), 2026-12-18 11% (24,409) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 770.00: 82,350 calls; put wall 760.00: 183,049 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 2.64 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 3.21 vol pts (put 16.7%, call 13.5%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 18.7% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 36.7% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 44.7% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $74.3M net, 17.5% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-22T21:56:03+00:00)

- Call wall: 770.00 -> 770.00 (+0.00)
- Put wall: 760.00 -> 760.00 (+0.00)
- Zero gamma: 775.29 -> 774.73 (-0.56)
- Abs gamma strike: 760.00 -> 760.00 (+0.00)
- Net GEX: -$13.40B -> -$13.04B (+$352.4M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
