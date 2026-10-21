# QQQ gamma exposure report

As of 2026-10-21T15:30:48+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 724.98 | The underlying price used for every calculation in this run. |
| Net GEX | -$835.9M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 725.00, 730.00, 722.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 720.00, 700.00, 710.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 725.00: 2026-10-21 75%, 2026-10-23 10%, 2026-10-30 6%; 730.00: 2026-10-23 35%, 2026-10-22 22%, 2026-11-20 15%; 722.00: 2026-10-22 68%, 2026-10-21 13%, 2026-10-23 10% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 720.00: 2026-11-20 29%, 2026-10-23 25%, 2026-10-30 20%; 700.00: 2026-10-30 51%, 2026-11-20 28%, 2026-11-06 8%; 710.00: 2026-10-23 48%, 2026-10-30 19%, 2026-11-06 16% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 725.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 726.97 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $67.71B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $1.53B | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$2.31B | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±3.56 (0.5%) -> 721.41 to 728.54, exp 2026-10-21 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 1,765,179 calls / 2,857,484 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 760.00 (94,772); puts 700.00 (216,208) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 725 calls, 37,970 OI: 2026-10-30 26% (9,691), 2026-11-20 23% (8,809), 2026-10-21 19% (7,375); put wall 720 puts, 123,115 OI: 2026-11-20 45% (55,576), 2026-10-30 19% (22,850), 2026-10-23 11% (13,981); max call OI 760 calls, 94,772 OI: 2026-11-20 35% (33,265), 2026-11-06 27% (25,566), 2026-10-30 18% (17,251); max put OI 700 puts, 216,208 OI: 2026-10-30 42% (89,867), 2026-11-20 30% (64,757), 2026-10-23 8% (18,177) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 725.00: 37,970 calls; put wall 720.00: 123,115 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.62 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 3.98 vol pts (put 23.1%, call 19.1%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 12.9% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 29.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 25.2% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 32.8% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$51.5M net, 2.7% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-21T13:48:32+00:00)

- Call wall: 725.00 -> 725.00 (+0.00)
- Put wall: 720.00 -> 720.00 (+0.00)
- Zero gamma: 726.49 -> 726.97 (+0.48)
- Abs gamma strike: 720.00 -> 725.00 (+5.00)
- Net GEX: -$2.03B -> -$835.9M (+$1.19B)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
