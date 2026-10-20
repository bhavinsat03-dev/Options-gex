# SPCX gamma exposure report

As of 2026-10-20T22:42:21+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 147.79 | The underlying price used for every calculation in this run. |
| Net GEX | -$15.5M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 155.00, 150.00, 160.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 140.00, 145.00, 150.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 155.00: 2026-10-21 37%, 2026-10-23 29%, 2026-11-20 16%; 150.00: 2026-11-20 35%, 2026-10-21 22%, 2026-10-23 22%; 160.00: 2026-11-20 32%, 2026-10-23 30%, 2026-10-30 16% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 140.00: 2026-10-23 37%, 2026-11-20 29%, 2026-10-30 12%; 145.00: 2026-10-23 32%, 2026-11-20 26%, 2026-10-21 16%; 150.00: 2026-11-20 34%, 2026-10-30 22%, 2026-10-23 21% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 150.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 149.72 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $4.25B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $14.4M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$154.5M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±10.52 (7.1%) -> 137.26 to 158.31, exp 2026-10-21 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 667,624 calls / 655,546 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 170.00 (48,407); puts 140.00 (49,948) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 155 calls, 37,588 OI: 2026-10-21 27% (10,280), 2026-10-23 26% (9,930), 2026-11-20 25% (9,546); put wall 140 puts, 49,948 OI: 2026-11-20 38% (19,012), 2026-10-23 29% (14,524), 2026-10-30 12% (5,820); max call OI 170 calls, 48,407 OI: 2026-10-23 44% (21,371), 2026-11-20 31% (15,079), 2026-10-30 10% (4,856); max put OI 140 puts, 49,948 OI: 2026-11-20 38% (19,012), 2026-10-23 29% (14,524), 2026-10-30 12% (5,820) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 155.00: 37,588 calls; put wall 140.00: 49,948 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 0.98 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -0.32 vol pts (put 56.6%, call 56.9%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 45.7% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 18.9% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 35.5% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$499.6K net, 0.8% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-20T22:32:22+00:00)

- Call wall: 155.00 -> 155.00 (+0.00)
- Put wall: 140.00 -> 140.00 (+0.00)
- Zero gamma: 149.73 -> 149.72 (-0.01)
- Abs gamma strike: 150.00 -> 150.00 (+0.00)
- Net GEX: -$15.5M -> -$15.5M (-$8.7K)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
