# META gamma exposure report

As of 2026-10-20T19:30:24+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 688.79 | The underlying price used for every calculation in this run. |
| Net GEX | $34.7M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 700.00, 750.00, 800.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 680.00, 750.00, 650.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 700.00: 2026-11-20 80%, 2026-10-23 12%, 2026-10-30 5%; 750.00: 2026-11-20 53%, 2026-10-23 30%, 2026-10-30 8%; 800.00: 2026-11-20 69%, 2026-11-06 11%, 2026-10-23 10% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 680.00: 2026-10-30 54%, 2026-10-23 28%, 2026-11-20 14%; 750.00: 2026-10-23 78%, 2026-11-20 15%, 2026-10-30 4%; 650.00: 2026-10-23 49%, 2026-11-20 30%, 2026-10-30 9% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 700.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 678.78 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $13.46B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $62.2M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$148.3M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±38.45 (5.6%) -> 650.34 to 727.24, exp 2026-10-21 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 440,778 calls / 299,935 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 800.00 (39,747); puts 750.00 (16,285) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 700 calls, 24,884 OI: 2026-11-20 86% (21,313), 2026-10-23 7% (1,866), 2026-10-30 4% (1,015); put wall 680 puts, 12,420 OI: 2026-10-30 54% (6,738), 2026-10-23 23% (2,828), 2026-11-20 18% (2,268); max call OI 800 calls, 39,747 OI: 2026-11-20 60% (23,653), 2026-10-23 19% (7,550), 2026-11-06 11% (4,259); max put OI 750 puts, 16,285 OI: 2026-10-23 77% (12,525), 2026-11-20 16% (2,621), 2026-10-30 4% (627) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 700.00: 24,884 calls; put wall 680.00: 12,420 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 0.68 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -0.98 vol pts (put 44.4%, call 45.4%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 32.4% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 16.7% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 50.8% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $454.5K net, 0.7% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-20T17:02:06+00:00)

- Call wall: 700.00 -> 700.00 (+0.00)
- Put wall: 680.00 -> 680.00 (+0.00)
- Zero gamma: 678.19 -> 678.78 (+0.59)
- Abs gamma strike: 700.00 -> 700.00 (+0.00)
- Net GEX: $41.2M -> $34.7M (-$6.5M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
