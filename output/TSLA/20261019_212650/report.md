# TSLA gamma exposure report

As of 2026-10-20T01:26:50+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 368.06 | The underlying price used for every calculation in this run. |
| Net GEX | $125.6M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 400.00, 380.00, 370.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 350.00, 380.00, 360.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 400.00: 2026-11-20 36%, 2026-10-23 27%, 2026-10-30 25%; 380.00: 2026-10-23 50%, 2026-11-20 17%, 2026-10-30 17%; 370.00: 2026-10-23 51%, 2026-11-20 23%, 2026-10-30 10% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 350.00: 2026-11-20 41%, 2026-10-23 23%, 2026-10-30 16%; 380.00: 2026-11-20 44%, 2026-10-30 29%, 2026-10-23 20%; 360.00: 2026-10-23 36%, 2026-11-20 23%, 2026-10-30 23% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 380.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 348.85 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $7.35B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $40.3M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$151.7M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±23.57 (6.4%) -> 344.49 to 391.63, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 529,102 calls / 473,475 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 400.00 (41,360); puts 350.00 (22,428) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 400 calls, 41,360 OI: 2026-11-20 39% (16,094), 2026-10-23 26% (10,628), 2026-10-30 23% (9,685); put wall 350 puts, 22,428 OI: 2026-11-20 49% (10,912), 2026-10-23 18% (4,087), 2026-10-30 15% (3,262); max call OI 400 calls, 41,360 OI: 2026-11-20 39% (16,094), 2026-10-23 26% (10,628), 2026-10-30 23% (9,685); max put OI 350 puts, 22,428 OI: 2026-11-20 49% (10,912), 2026-10-23 18% (4,087), 2026-10-30 15% (3,262) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 400.00: 41,360 calls; put wall 350.00: 22,428 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 0.89 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -0.23 vol pts (put 45.1%, call 45.3%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 37.8% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 21.1% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 41.1% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $3.4M net, 1.3% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-20T01:21:36+00:00)

- Call wall: 400.00 -> 400.00 (+0.00)
- Put wall: 350.00 -> 350.00 (+0.00)
- Zero gamma: 348.85 -> 348.85 (+0.00)
- Abs gamma strike: 380.00 -> 380.00 (+0.00)
- Net GEX: $125.6M -> $125.6M (+$22.4K)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
