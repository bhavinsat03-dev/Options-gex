# TSLA gamma exposure report

As of 2026-10-23T19:22:31+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 372.04 | The underlying price used for every calculation in this run. |
| Net GEX | $19.9M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 400.00, 380.00, 385.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 350.00, 370.00, 380.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 400.00: 2026-11-20 36%, 2026-10-30 25%, 2026-12-18 21%; 380.00: 2026-10-30 24%, 2026-10-26 21%, 2026-11-20 17%; 385.00: 2026-10-30 35%, 2026-10-26 24%, 2026-11-20 15% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 350.00: 2026-12-18 34%, 2026-11-20 32%, 2026-10-30 15%; 370.00: 2026-10-26 24%, 2026-10-30 23%, 2026-11-20 21%; 380.00: 2026-11-20 32%, 2026-10-30 25%, 2026-12-18 17% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 372.50 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 371.85 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $11.38B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $59.3M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$63.5M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±8.12 (2.2%) -> 363.92 to 380.17, exp 2026-10-26 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 1,177,332 calls / 1,037,317 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 400.00 (72,307); puts 350.00 (44,843) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 400 calls, 72,307 OI: 2026-10-23 34% (24,401), 2026-11-20 21% (15,537), 2026-12-18 16% (11,871); put wall 350 puts, 44,843 OI: 2026-12-18 32% (14,428), 2026-11-20 24% (10,646), 2026-10-23 20% (9,125); max call OI 400 calls, 72,307 OI: 2026-10-23 34% (24,401), 2026-11-20 21% (15,537), 2026-12-18 16% (11,871); max put OI 350 puts, 44,843 OI: 2026-12-18 32% (14,428), 2026-11-20 24% (10,646), 2026-10-23 20% (9,125) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 400.00: 72,307 calls; put wall 350.00: 44,843 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 0.88 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 1.04 vol pts (put 40.5%, call 39.5%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 27.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 0.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 30.4% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 42.6% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$10.3M net, 16.7% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-23T19:01:06+00:00)

- Call wall: 370.00 -> 400.00 (+30.00)
- Put wall: 370.00 -> 350.00 (-20.00)
- Zero gamma: 372.09 -> 371.85 (-0.24)
- Abs gamma strike: 370.00 -> 372.50 (+2.50)
- Net GEX: $112.4M -> $19.9M (-$92.5M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
