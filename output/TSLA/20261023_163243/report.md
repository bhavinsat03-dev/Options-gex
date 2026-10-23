# TSLA gamma exposure report

As of 2026-10-23T20:32:43+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 372.22 | The underlying price used for every calculation in this run. |
| Net GEX | $31.3M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 400.00, 380.00, 385.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 350.00, 370.00, 360.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 400.00: 2026-11-20 36%, 2026-10-30 24%, 2026-12-18 21%; 380.00: 2026-10-30 24%, 2026-10-26 21%, 2026-11-20 17%; 385.00: 2026-10-30 36%, 2026-10-26 23%, 2026-11-20 15% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 350.00: 2026-12-18 34%, 2026-11-20 33%, 2026-10-30 14%; 370.00: 2026-10-26 25%, 2026-10-30 23%, 2026-11-20 21%; 360.00: 2026-10-30 31%, 2026-11-20 20%, 2026-10-26 17% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 380.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 370.01 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $9.62B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $59.9M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$90.6M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±7.85 (2.1%) -> 364.37 to 380.07, exp 2026-10-26 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 1,177,335 calls / 1,037,317 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 400.00 (47,906); puts 300.00 (37,274) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 400 calls, 47,906 OI: 2026-11-20 32% (15,537), 2026-12-18 25% (11,871), 2026-10-30 22% (10,383); put wall 350 puts, 35,718 OI: 2026-12-18 40% (14,428), 2026-11-20 30% (10,646), 2026-10-30 11% (3,752); max call OI 400 calls, 47,906 OI: 2026-11-20 32% (15,537), 2026-12-18 25% (11,871), 2026-10-30 22% (10,383); max put OI 300 puts, 37,274 OI: 2026-12-18 43% (16,107), 2026-11-20 26% (9,609), 2026-10-30 20% (7,510) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 400.00: 47,906 calls; put wall 350.00: 35,718 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 0.88 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 0.52 vol pts (put 39.6%, call 39.1%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 0.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 41.9% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 58.1% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$11.5M net, 22.7% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-23T19:22:31+00:00)

- Call wall: 400.00 -> 400.00 (+0.00)
- Put wall: 350.00 -> 350.00 (+0.00)
- Zero gamma: 371.85 -> 370.01 (-1.84)
- Abs gamma strike: 372.50 -> 380.00 (+7.50)
- Net GEX: $19.9M -> $31.3M (+$11.4M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
