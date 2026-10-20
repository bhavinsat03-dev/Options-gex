# META gamma exposure report

As of 2026-10-20T13:50:37+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 683.83 | The underlying price used for every calculation in this run. |
| Net GEX | $18.8M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 700.00, 800.00, 750.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 680.00, 650.00, 700.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 700.00: 2026-11-20 80%, 2026-10-23 11%, 2026-10-30 5%; 800.00: 2026-11-20 69%, 2026-11-06 11%, 2026-10-23 10%; 750.00: 2026-11-20 54%, 2026-10-23 30%, 2026-10-30 8% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 680.00: 2026-10-30 54%, 2026-10-23 28%, 2026-11-20 14%; 650.00: 2026-10-23 50%, 2026-11-20 29%, 2026-10-30 9%; 700.00: 2026-10-23 37%, 2026-11-20 27%, 2026-10-30 19% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 700.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 678.29 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $12.36B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $62.5M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$193.4M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±36.35 (5.3%) -> 647.48 to 720.18, exp 2026-10-21 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 440,778 calls / 299,935 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 800.00 (39,747); puts 650.00 (13,026) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 700 calls, 24,884 OI: 2026-11-20 86% (21,313), 2026-10-23 7% (1,866), 2026-10-30 4% (1,015); put wall 680 puts, 12,420 OI: 2026-10-30 54% (6,738), 2026-10-23 23% (2,828), 2026-11-20 18% (2,268); max call OI 800 calls, 39,747 OI: 2026-11-20 60% (23,653), 2026-10-23 19% (7,550), 2026-11-06 11% (4,259); max put OI 650 puts, 13,026 OI: 2026-10-23 43% (5,554), 2026-11-20 36% (4,721), 2026-10-30 9% (1,121) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 700.00: 24,884 calls; put wall 680.00: 12,420 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 0.68 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -4.76 vol pts (put 42.3%, call 47.1%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 29.5% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 17.7% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 52.8% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$666.9K net, 0.6% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-20T01:26:50+00:00)

- Call wall: 800.00 -> 700.00 (-100.00)
- Put wall: 750.00 -> 680.00 (-70.00)
- Zero gamma: 677.07 -> 678.29 (+1.22)
- Abs gamma strike: 750.00 -> 700.00 (-50.00)
- Net GEX: $91.8M -> $18.8M (-$73.0M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
