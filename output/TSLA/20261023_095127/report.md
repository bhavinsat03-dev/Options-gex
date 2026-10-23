# TSLA gamma exposure report

As of 2026-10-23T13:51:27+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 367.20 | The underlying price used for every calculation in this run. |
| Net GEX | -$19.6M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 370.00, 365.00, 375.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 365.00, 367.50, 360.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 370.00: 2026-10-23 71%, 2026-11-20 9%, 2026-10-30 5%; 365.00: 2026-10-23 82%, 2026-11-20 6%, 2026-10-30 4%; 375.00: 2026-10-23 51%, 2026-10-30 13%, 2026-11-20 11% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 365.00: 2026-10-23 73%, 2026-10-26 12%, 2026-10-30 7%; 367.50: 2026-10-23 88%, 2026-10-26 6%, 2026-10-30 3%; 360.00: 2026-10-30 23%, 2026-10-23 22%, 2026-10-26 19% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 365.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 367.47 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $10.46B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $61.1M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$338.0M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±6.54 (1.8%) -> 360.66 to 373.74, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 1,177,335 calls / 1,037,317 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 400.00 (72,307); puts 350.00 (44,843) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 370 calls, 24,127 OI: 2026-10-23 30% (7,340), 2026-11-20 28% (6,644), 2026-12-18 17% (4,085); put wall 365 puts, 19,059 OI: 2026-10-23 35% (6,584), 2026-10-30 16% (3,002), 2026-10-26 14% (2,640); max call OI 400 calls, 72,307 OI: 2026-10-23 34% (24,401), 2026-11-20 21% (15,537), 2026-12-18 16% (11,871); max put OI 350 puts, 44,843 OI: 2026-12-18 32% (14,428), 2026-11-20 24% (10,646), 2026-10-23 20% (9,125) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 370.00: 24,127 calls; put wall 365.00: 19,059 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 0.88 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -5.23 vol pts (put 37.7%, call 43.0%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 35.4% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 0.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 25.6% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 39.0% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$25.3M net, 15.5% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-22T23:53:05+00:00)

- Call wall: 380.00 -> 370.00 (-10.00)
- Put wall: 375.00 -> 365.00 (-10.00)
- Zero gamma: 366.76 -> 367.47 (+0.71)
- Abs gamma strike: 380.00 -> 365.00 (-15.00)
- Net GEX: $181.2M -> -$19.6M (-$200.8M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
