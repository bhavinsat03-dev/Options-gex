# TSLA gamma exposure report

As of 2026-10-21T13:48:32+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 388.31 | The underlying price used for every calculation in this run. |
| Net GEX | $427.5M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 400.00, 380.00, 385.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 350.00, 380.00, 370.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 400.00: 2026-10-23 44%, 2026-11-20 24%, 2026-10-30 21%; 380.00: 2026-10-23 58%, 2026-10-30 13%, 2026-11-20 12%; 385.00: 2026-10-23 70%, 2026-11-20 10%, 2026-10-30 8% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 350.00: 2026-11-20 41%, 2026-10-23 22%, 2026-10-30 14%; 380.00: 2026-11-20 40%, 2026-10-23 26%, 2026-10-30 26%; 370.00: 2026-10-23 42%, 2026-11-20 26%, 2026-10-30 19% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 400.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 353.41 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $9.36B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $35.7M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$251.8M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±24.30 (6.3%) -> 364.02 to 412.62, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 650,837 calls / 584,652 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 400.00 (48,135); puts 350.00 (26,413) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 400 calls, 48,135 OI: 2026-11-20 33% (16,082), 2026-10-23 33% (16,076), 2026-10-30 20% (9,712); put wall 350 puts, 26,413 OI: 2026-11-20 41% (10,883), 2026-10-23 23% (6,054), 2026-10-30 13% (3,474); max call OI 400 calls, 48,135 OI: 2026-11-20 33% (16,082), 2026-10-23 33% (16,076), 2026-10-30 20% (9,712); max put OI 350 puts, 26,413 OI: 2026-11-20 41% (10,883), 2026-10-23 23% (6,054), 2026-10-30 13% (3,474) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 400.00: 48,135 calls; put wall 350.00: 26,413 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 0.90 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 6.37 vol pts (put 49.1%, call 42.7%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 45.7% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 22.0% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 32.3% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $5.3M net, 1.4% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-21T01:10:11+00:00)

- Call wall: 400.00 -> 400.00 (+0.00)
- Put wall: 350.00 -> 350.00 (+0.00)
- Zero gamma: 348.16 -> 353.41 (+5.25)
- Abs gamma strike: 400.00 -> 400.00 (+0.00)
- Net GEX: $202.1M -> $427.5M (+$225.4M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
