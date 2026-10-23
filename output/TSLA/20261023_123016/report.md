# TSLA gamma exposure report

As of 2026-10-23T16:30:16+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 370.86 | The underlying price used for every calculation in this run. |
| Net GEX | -$69.0M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 370.00, 375.00, 400.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 370.00, 350.00, 360.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 370.00: 2026-10-23 85%, 2026-11-20 5%, 2026-10-26 3%; 375.00: 2026-10-23 46%, 2026-10-30 15%, 2026-11-20 11%; 400.00: 2026-11-20 36%, 2026-10-30 25%, 2026-12-18 21% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 370.00: 2026-10-23 91%, 2026-10-26 2%, 2026-10-30 2%; 350.00: 2026-12-18 33%, 2026-11-20 32%, 2026-10-30 15%; 360.00: 2026-10-30 30%, 2026-11-20 20%, 2026-10-26 20% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 370.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 371.29 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $10.80B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $61.9M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | $12.0M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±3.81 (1.0%) -> 367.05 to 374.67, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 1,177,335 calls / 1,037,317 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 400.00 (72,307); puts 350.00 (44,843) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 370 calls, 24,127 OI: 2026-10-23 30% (7,340), 2026-11-20 28% (6,644), 2026-12-18 17% (4,085); put wall 370 puts, 25,837 OI: 2026-10-23 37% (9,579), 2026-11-20 19% (5,020), 2026-12-18 18% (4,701); max call OI 400 calls, 72,307 OI: 2026-10-23 34% (24,401), 2026-11-20 21% (15,537), 2026-12-18 16% (11,871); max put OI 350 puts, 44,843 OI: 2026-12-18 32% (14,428), 2026-11-20 24% (10,646), 2026-10-23 20% (9,125) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 370.00: 24,127 calls; put wall 370.00: 25,837 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 0.88 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -1.47 vol pts (put 39.3%, call 40.8%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 44.5% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 0.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 22.6% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 32.9% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$15.7M net, 13.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-23T16:12:39+00:00)

- Call wall: 375.00 -> 370.00 (-5.00)
- Put wall: 370.00 -> 370.00 (+0.00)
- Zero gamma: 372.23 -> 371.29 (-0.94)
- Abs gamma strike: 375.00 -> 370.00 (-5.00)
- Net GEX: $19.8M -> -$69.0M (-$88.8M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
