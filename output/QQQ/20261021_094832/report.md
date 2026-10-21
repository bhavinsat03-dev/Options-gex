# QQQ gamma exposure report

As of 2026-10-21T13:48:32+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 722.78 | The underlying price used for every calculation in this run. |
| Net GEX | -$2.03B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 725.00, 720.00, 722.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 720.00, 700.00, 710.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 725.00: 2026-10-21 57%, 2026-10-23 17%, 2026-10-30 11%; 720.00: 2026-10-21 44%, 2026-10-23 19%, 2026-11-20 18%; 722.00: 2026-10-22 53%, 2026-10-21 33%, 2026-10-23 8% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 720.00: 2026-11-20 26%, 2026-10-23 20%, 2026-10-21 18%; 700.00: 2026-10-30 50%, 2026-11-20 27%, 2026-10-23 9%; 710.00: 2026-10-23 51%, 2026-10-30 17%, 2026-11-06 14% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 720.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 726.49 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $69.74B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $1.48B | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$2.98B | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±5.63 (0.8%) -> 717.15 to 728.42, exp 2026-10-21 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 1,765,179 calls / 2,857,484 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 760.00 (94,772); puts 700.00 (216,208) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 725 calls, 37,970 OI: 2026-10-30 26% (9,691), 2026-11-20 23% (8,809), 2026-10-21 19% (7,375); put wall 720 puts, 123,115 OI: 2026-11-20 45% (55,576), 2026-10-30 19% (22,850), 2026-10-23 11% (13,981); max call OI 760 calls, 94,772 OI: 2026-11-20 35% (33,265), 2026-11-06 27% (25,566), 2026-10-30 18% (17,251); max put OI 700 puts, 216,208 OI: 2026-10-30 42% (89,867), 2026-11-20 30% (64,757), 2026-10-23 8% (18,177) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 725.00: 37,970 calls; put wall 720.00: 123,115 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.62 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 4.73 vol pts (put 24.0%, call 19.2%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 14.1% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 28.4% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 24.9% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 32.6% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$58.4M net, 2.7% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-21T09:59:32+00:00)

- Call wall: 613.00 -> 725.00 (+112.00)
- Abs gamma strike: 613.00 -> 720.00 (+107.00)
- Net GEX: $995 -> -$2.03B (-$2.03B)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
