# SPCX gamma exposure report

As of 2026-10-22T13:50:59+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 152.16 | The underlying price used for every calculation in this run. |
| Net GEX | -$72.8M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 160.00, 155.00, 150.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 155.00, 150.00, 145.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 160.00: 2026-10-23 38%, 2026-11-20 25%, 2026-10-30 20%; 155.00: 2026-10-23 52%, 2026-11-20 17%, 2026-10-30 15%; 150.00: 2026-11-20 37%, 2026-10-23 34%, 2026-10-30 14% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 155.00: 2026-10-23 69%, 2026-10-30 11%, 2026-11-20 9%; 150.00: 2026-10-23 48%, 2026-10-30 23%, 2026-11-20 17%; 145.00: 2026-10-23 33%, 2026-11-20 28%, 2026-10-30 20% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 155.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 156.66 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $4.59B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $18.9M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$93.4M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±5.46 (3.6%) -> 146.69 to 157.62, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 755,348 calls / 780,998 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 170.00 (66,439); puts 140.00 (57,330) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 160 calls, 45,233 OI: 2026-11-20 36% (16,201), 2026-10-23 30% (13,375), 2026-10-30 18% (8,091); put wall 155 puts, 50,343 OI: 2026-10-23 45% (22,501), 2026-11-20 23% (11,775), 2026-10-30 17% (8,715); max call OI 170 calls, 66,439 OI: 2026-10-23 43% (28,600), 2026-11-20 25% (16,492), 2026-10-30 19% (12,325); max put OI 140 puts, 57,330 OI: 2026-11-20 36% (20,468), 2026-10-23 35% (19,896), 2026-10-30 14% (8,003) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 160.00: 45,233 calls; put wall 155.00: 50,343 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.03 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -2.52 vol pts (put 49.1%, call 51.6%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 40.6% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 27.9% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 31.4% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$79.5K net, 0.9% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-21T19:00:04+00:00)

- Call wall: 160.00 -> 160.00 (+0.00)
- Put wall: 150.00 -> 155.00 (+5.00)
- Zero gamma: 148.43 -> 156.66 (+8.23)
- Abs gamma strike: 160.00 -> 155.00 (-5.00)
- Net GEX: $149.4M -> -$72.8M (-$222.2M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
