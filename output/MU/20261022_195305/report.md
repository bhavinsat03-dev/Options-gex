# MU gamma exposure report

As of 2026-10-22T23:53:05+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 856.49 | The underlying price used for every calculation in this run. |
| Net GEX | -$448.3M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 900.00, 1,000.00, 910.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 850.00, 900.00, 880.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 900.00: 2026-11-20 29%, 2026-10-30 24%, 2026-12-18 18%; 1,000.00: 2026-11-20 34%, 2026-12-18 32%, 2026-10-30 20%; 910.00: 2026-11-20 63%, 2026-12-18 13%, 2026-10-30 10% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 850.00: 2026-10-23 60%, 2026-11-20 15%, 2026-10-30 8%; 900.00: 2026-11-20 26%, 2026-10-23 20%, 2026-10-30 16%; 880.00: 2026-10-23 40%, 2026-11-20 24%, 2026-10-30 14% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 850.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 921.85 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $17.83B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $23.0M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$66.6M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±28.50 (3.3%) -> 827.99 to 884.99, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 678,615 calls / 792,431 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 1,000.00 (31,572); puts 900.00 (23,476) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 900 calls, 13,507 OI: 2026-11-20 32% (4,308), 2026-12-18 27% (3,602), 2026-10-30 16% (2,213); put wall 850 puts, 22,608 OI: 2026-11-20 32% (7,185), 2026-10-23 24% (5,380), 2026-12-18 15% (3,316); max call OI 1000 calls, 31,572 OI: 2026-10-23 28% (8,908), 2026-12-18 20% (6,401), 2026-11-20 20% (6,277); max put OI 900 puts, 23,476 OI: 2026-11-20 26% (6,161), 2026-10-23 24% (5,605), 2026-12-18 20% (4,752) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 900.00: 13,507 calls; put wall 850.00: 22,608 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.17 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 2.24 vol pts (put 56.2%, call 53.9%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 28.4% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 23.3% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 48.3% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$46.4M net, 17.4% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-22T21:56:03+00:00)

- Call wall: 900.00 -> 900.00 (+0.00)
- Put wall: 850.00 -> 850.00 (+0.00)
- Zero gamma: 919.73 -> 921.85 (+2.12)
- Abs gamma strike: 850.00 -> 850.00 (+0.00)
- Net GEX: -$418.9M -> -$448.3M (-$29.4M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
