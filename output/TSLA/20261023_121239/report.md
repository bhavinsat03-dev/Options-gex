# TSLA gamma exposure report

As of 2026-10-23T16:12:39+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 372.88 | The underlying price used for every calculation in this run. |
| Net GEX | $19.8M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 375.00, 370.00, 372.50 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 370.00, 375.00, 372.50 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 375.00: 2026-10-23 77%, 2026-10-30 6%, 2026-10-26 5%; 370.00: 2026-10-23 68%, 2026-11-20 9%, 2026-10-26 7%; 372.50: 2026-10-23 93%, 2026-10-30 3%, 2026-10-26 2% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 370.00: 2026-10-23 73%, 2026-10-30 6%, 2026-10-26 6%; 375.00: 2026-10-23 78%, 2026-10-26 6%, 2026-10-30 4%; 372.50: 2026-10-23 93%, 2026-10-26 4%, 2026-10-30 2% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 375.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 372.23 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $12.20B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $59.8M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$63.5M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±3.70 (1.0%) -> 369.18 to 376.58, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 1,177,335 calls / 1,037,317 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 400.00 (72,307); puts 350.00 (44,843) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 375 calls, 20,959 OI: 2026-10-23 30% (6,277), 2026-11-20 21% (4,393), 2026-10-30 14% (2,959); put wall 370 puts, 25,837 OI: 2026-10-23 37% (9,579), 2026-11-20 19% (5,020), 2026-12-18 18% (4,701); max call OI 400 calls, 72,307 OI: 2026-10-23 34% (24,401), 2026-11-20 21% (15,537), 2026-12-18 16% (11,871); max put OI 350 puts, 44,843 OI: 2026-12-18 32% (14,428), 2026-11-20 24% (10,646), 2026-10-23 20% (9,125) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 375.00: 20,959 calls; put wall 370.00: 25,837 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 0.88 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 0.48 vol pts (put 40.3%, call 39.8%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 37.6% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 0.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 26.0% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 36.4% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$10.6M net, 14.3% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-23T13:51:27+00:00)

- Call wall: 370.00 -> 375.00 (+5.00)
- Put wall: 365.00 -> 370.00 (+5.00)
- Zero gamma: 367.47 -> 372.23 (+4.76)
- Abs gamma strike: 365.00 -> 375.00 (+10.00)
- Net GEX: -$19.6M -> $19.8M (+$39.4M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
