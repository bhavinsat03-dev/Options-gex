# META gamma exposure report

As of 2026-10-20T01:21:36+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 705.44 | The underlying price used for every calculation in this run. |
| Net GEX | $91.8M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 800.00, 700.00, 750.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 750.00, 680.00, 650.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 800.00: 2026-11-20 65%, 2026-10-23 14%, 2026-11-06 11%; 700.00: 2026-11-20 87%, 2026-10-23 9%, 2026-10-30 3%; 750.00: 2026-11-20 51%, 2026-10-23 34%, 2026-10-30 7% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 750.00: 2026-10-23 80%, 2026-11-20 13%, 2026-10-30 4%; 680.00: 2026-10-30 56%, 2026-10-23 28%, 2026-11-20 13%; 650.00: 2026-10-23 47%, 2026-11-20 33%, 2026-10-30 8% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 750.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 677.05 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $13.23B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $64.4M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$129.4M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±38.40 (5.4%) -> 667.04 to 743.84, exp 2026-10-21 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 402,895 calls / 284,293 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 800.00 (37,856); puts 750.00 (16,333) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 800 calls, 37,856 OI: 2026-11-20 62% (23,359), 2026-10-23 18% (6,655), 2026-11-06 11% (4,017); put wall 750 puts, 16,333 OI: 2026-10-23 77% (12,581), 2026-11-20 16% (2,628), 2026-10-30 4% (620); max call OI 800 calls, 37,856 OI: 2026-11-20 62% (23,359), 2026-10-23 18% (6,655), 2026-11-06 11% (4,017); max put OI 750 puts, 16,333 OI: 2026-10-23 77% (12,581), 2026-11-20 16% (2,628), 2026-10-30 4% (620) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 800.00: 37,856 calls; put wall 750.00: 16,333 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 0.71 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -0.55 vol pts (put 44.0%, call 44.6%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 32.7% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 14.8% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 52.5% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $812.6K net, 0.6% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-20T01:17:50+00:00)

- Call wall: 800.00 -> 800.00 (+0.00)
- Put wall: 750.00 -> 750.00 (+0.00)
- Zero gamma: 660.01 -> 677.05 (+17.04)
- Abs gamma strike: 750.00 -> 750.00 (+0.00)
- Net GEX: $162.3M -> $91.8M (-$70.4M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
