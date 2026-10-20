# META gamma exposure report

As of 2026-10-20T22:42:21+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 694.25 | The underlying price used for every calculation in this run. |
| Net GEX | $63.5M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 700.00, 800.00, 750.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 750.00, 680.00, 650.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 700.00: 2026-11-20 79%, 2026-10-23 12%, 2026-10-30 5%; 800.00: 2026-11-20 69%, 2026-11-06 11%, 2026-10-23 10%; 750.00: 2026-11-20 52%, 2026-10-23 31%, 2026-10-30 8% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 750.00: 2026-10-23 79%, 2026-11-20 14%, 2026-10-30 4%; 680.00: 2026-10-30 54%, 2026-10-23 28%, 2026-11-20 14%; 650.00: 2026-10-23 48%, 2026-11-20 30%, 2026-10-30 9% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 700.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 677.52 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $13.51B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $66.3M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$162.5M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±37.70 (5.4%) -> 656.55 to 731.95, exp 2026-10-21 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 440,778 calls / 299,935 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 800.00 (39,747); puts 750.00 (16,285) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 700 calls, 24,884 OI: 2026-11-20 86% (21,313), 2026-10-23 7% (1,866), 2026-10-30 4% (1,015); put wall 750 puts, 16,285 OI: 2026-10-23 77% (12,525), 2026-11-20 16% (2,621), 2026-10-30 4% (627); max call OI 800 calls, 39,747 OI: 2026-11-20 60% (23,653), 2026-10-23 19% (7,550), 2026-11-06 11% (4,259); max put OI 750 puts, 16,285 OI: 2026-10-23 77% (12,525), 2026-11-20 16% (2,621), 2026-10-30 4% (627) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 700.00: 24,884 calls; put wall 750.00: 16,285 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 0.68 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 0.10 vol pts (put 45.0%, call 44.9%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 33.1% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 16.5% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 50.4% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $689.4K net, 0.7% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-20T22:32:22+00:00)

- Call wall: 700.00 -> 700.00 (+0.00)
- Put wall: 750.00 -> 750.00 (+0.00)
- Zero gamma: 677.48 -> 677.52 (+0.04)
- Abs gamma strike: 700.00 -> 700.00 (+0.00)
- Net GEX: $63.6M -> $63.5M (-$111.4K)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
