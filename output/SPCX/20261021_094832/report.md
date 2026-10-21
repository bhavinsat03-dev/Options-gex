# SPCX gamma exposure report

As of 2026-10-21T13:48:32+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 163.40 | The underlying price used for every calculation in this run. |
| Net GEX | $226.8M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 165.00, 170.00, 162.50 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 160.00, 150.00, 155.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 165.00: 2026-10-21 43%, 2026-10-23 34%, 2026-10-30 9%; 170.00: 2026-10-23 60%, 2026-11-20 18%, 2026-10-30 10%; 162.50: 2026-10-21 55%, 2026-10-23 29%, 2026-10-30 12% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 160.00: 2026-11-20 34%, 2026-10-30 23%, 2026-10-23 22%; 150.00: 2026-11-20 43%, 2026-10-30 25%, 2026-10-23 14%; 155.00: 2026-11-20 38%, 2026-10-23 33%, 2026-10-30 14% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 165.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 152.12 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $4.63B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $20.2M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$164.4M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±4.67 (2.9%) -> 158.73 to 168.06, exp 2026-10-21 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 786,637 calls / 781,345 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 170.00 (61,446); puts 140.00 (65,815) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 165 calls, 43,236 OI: 2026-10-23 32% (14,020), 2026-11-20 21% (9,192), 2026-10-21 17% (7,301); put wall 160 puts, 24,283 OI: 2026-11-20 49% (11,952), 2026-10-30 21% (5,093), 2026-10-23 13% (3,201); max call OI 170 calls, 61,446 OI: 2026-10-23 43% (26,716), 2026-11-20 29% (17,776), 2026-10-30 9% (5,679); max put OI 140 puts, 65,815 OI: 2026-10-23 31% (20,490), 2026-11-20 31% (20,200), 2026-10-21 15% (9,788) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 165.00: 43,236 calls; put wall 160.00: 24,283 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 0.99 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 5.11 vol pts (put 54.1%, call 49.0%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 14.6% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 33.5% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 21.8% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 30.1% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $864.9K net, 0.7% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-21T01:10:11+00:00)

- Call wall: 155.00 -> 165.00 (+10.00)
- Put wall: 140.00 -> 160.00 (+20.00)
- Zero gamma: 150.08 -> 152.12 (+2.04)
- Abs gamma strike: 150.00 -> 165.00 (+15.00)
- Net GEX: -$14.8M -> $226.8M (+$241.6M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
