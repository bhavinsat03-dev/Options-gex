# SPCX gamma exposure report

As of 2026-10-21T15:30:48+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 162.54 | The underlying price used for every calculation in this run. |
| Net GEX | $211.4M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 162.50, 165.00, 170.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 160.00, 150.00, 155.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 162.50: 2026-10-21 70%, 2026-10-23 19%, 2026-10-30 8%; 165.00: 2026-10-23 41%, 2026-10-21 30%, 2026-10-30 12%; 170.00: 2026-10-23 61%, 2026-11-20 20%, 2026-10-30 10% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 160.00: 2026-11-20 32%, 2026-10-23 24%, 2026-10-30 23%; 150.00: 2026-11-20 43%, 2026-10-30 26%, 2026-10-23 14%; 155.00: 2026-11-20 38%, 2026-10-23 34%, 2026-10-30 14% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 162.50 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 149.61 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $5.24B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $20.0M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$139.1M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±2.87 (1.8%) -> 159.68 to 165.41, exp 2026-10-21 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 786,637 calls / 781,345 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 170.00 (61,446); puts 140.00 (65,815) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 162.5 calls, 21,312 OI: 2026-10-23 36% (7,719), 2026-10-30 29% (6,109), 2026-10-21 23% (4,952); put wall 160 puts, 24,283 OI: 2026-11-20 49% (11,952), 2026-10-30 21% (5,093), 2026-10-23 13% (3,201); max call OI 170 calls, 61,446 OI: 2026-10-23 43% (26,716), 2026-11-20 29% (17,776), 2026-10-30 9% (5,679); max put OI 140 puts, 65,815 OI: 2026-10-23 31% (20,490), 2026-11-20 31% (20,200), 2026-10-21 15% (9,788) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 162.50: 21,312 calls; put wall 160.00: 24,283 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 0.99 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 1.52 vol pts (put 52.3%, call 50.8%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 15.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 33.7% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 21.9% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 29.4% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $716.9K net, 0.7% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-21T13:48:32+00:00)

- Call wall: 165.00 -> 162.50 (-2.50)
- Put wall: 160.00 -> 160.00 (+0.00)
- Zero gamma: 152.12 -> 149.61 (-2.51)
- Abs gamma strike: 165.00 -> 162.50 (-2.50)
- Net GEX: $226.8M -> $211.4M (-$15.4M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
