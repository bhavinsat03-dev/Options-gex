# TSLA gamma exposure report

As of 2026-10-21T16:30:50+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 386.42 | The underlying price used for every calculation in this run. |
| Net GEX | $371.0M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 400.00, 380.00, 385.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 380.00, 370.00, 350.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 400.00: 2026-10-23 44%, 2026-11-20 24%, 2026-10-30 20%; 380.00: 2026-10-23 57%, 2026-10-30 13%, 2026-11-20 13%; 385.00: 2026-10-23 69%, 2026-11-20 10%, 2026-10-30 8% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 380.00: 2026-11-20 38%, 2026-10-23 28%, 2026-10-30 27%; 370.00: 2026-10-23 43%, 2026-11-20 25%, 2026-10-30 19%; 350.00: 2026-11-20 43%, 2026-10-23 19%, 2026-10-30 14% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 400.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 352.76 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $9.86B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $41.1M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$240.1M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±22.35 (5.8%) -> 364.07 to 408.77, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 650,837 calls / 584,652 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 400.00 (48,135); puts 350.00 (26,413) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 400 calls, 48,135 OI: 2026-11-20 33% (16,082), 2026-10-23 33% (16,076), 2026-10-30 20% (9,712); put wall 380 puts, 14,234 OI: 2026-11-20 50% (7,073), 2026-10-30 24% (3,439), 2026-10-23 18% (2,590); max call OI 400 calls, 48,135 OI: 2026-11-20 33% (16,082), 2026-10-23 33% (16,076), 2026-10-30 20% (9,712); max put OI 350 puts, 26,413 OI: 2026-11-20 41% (10,883), 2026-10-23 23% (6,054), 2026-10-30 13% (3,474) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 400.00: 48,135 calls; put wall 380.00: 14,234 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 0.90 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 0.09 vol pts (put 44.0%, call 43.9%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 46.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 21.7% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 32.3% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $4.3M net, 1.4% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-21T15:30:48+00:00)

- Call wall: 400.00 -> 400.00 (+0.00)
- Put wall: 380.00 -> 380.00 (+0.00)
- Zero gamma: 352.11 -> 352.76 (+0.65)
- Abs gamma strike: 400.00 -> 400.00 (+0.00)
- Net GEX: $378.6M -> $371.0M (-$7.6M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
