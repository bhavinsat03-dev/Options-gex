# SPY gamma exposure report

As of 2026-10-22T19:00:50+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 761.68 | The underlying price used for every calculation in this run. |
| Net GEX | -$16.15B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 770.00, 780.00, 800.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 762.00, 760.00, 765.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 770.00: 2026-10-30 29%, 2026-10-23 27%, 2026-11-20 20%; 780.00: 2026-10-30 43%, 2026-11-20 26%, 2026-11-13 10%; 800.00: 2026-11-20 76%, 2026-10-30 9%, 2026-11-13 7% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 762.00: 2026-10-22 63%, 2026-10-26 16%, 2026-10-23 15%; 760.00: 2026-10-30 43%, 2026-10-23 30%, 2026-11-20 11%; 765.00: 2026-10-30 38%, 2026-10-23 38%, 2026-11-20 11% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 762.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 771.14 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $82.12B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $2.24B | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$1.67B | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±1.93 (0.3%) -> 759.75 to 763.61, exp 2026-10-22 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 2,152,484 calls / 5,927,332 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 800.00 (162,165); puts 750.00 (204,827) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 770 calls, 55,241 OI: 2026-11-20 28% (15,432), 2026-10-30 22% (12,381), 2026-10-23 18% (9,701); put wall 762 puts, 47,491 OI: 2026-10-26 38% (17,890), 2026-10-23 19% (8,898), 2026-11-06 15% (7,204); max call OI 800 calls, 162,165 OI: 2026-11-20 50% (81,279), 2026-10-30 30% (49,118), 2026-10-23 6% (9,453); max put OI 750 puts, 204,827 OI: 2026-11-20 40% (81,348), 2026-10-30 33% (67,250), 2026-11-06 9% (18,272) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 770.00: 55,241 calls; put wall 762.00: 47,491 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 2.75 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 3.34 vol pts (put 17.5%, call 14.2%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 8.4% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 17.4% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 39.7% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 34.5% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$391.2M net, 5.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-22T16:30:29+00:00)

- Call wall: 765.00 -> 770.00 (+5.00)
- Put wall: 765.00 -> 762.00 (-3.00)
- Zero gamma: 773.03 -> 771.14 (-1.89)
- Abs gamma strike: 765.00 -> 762.00 (-3.00)
- Net GEX: -$15.03B -> -$16.15B (-$1.12B)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
