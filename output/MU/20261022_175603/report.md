# MU gamma exposure report

As of 2026-10-22T21:56:03+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 856.49 | The underlying price used for every calculation in this run. |
| Net GEX | -$418.9M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 900.00, 910.00, 1,000.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 850.00, 900.00, 840.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 900.00: 2026-11-20 35%, 2026-10-30 29%, 2026-10-23 17%; 910.00: 2026-11-20 71%, 2026-10-30 11%, 2026-10-23 7%; 1,000.00: 2026-11-20 50%, 2026-10-30 30%, 2026-11-06 6% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 850.00: 2026-10-23 62%, 2026-11-20 16%, 2026-10-30 8%; 900.00: 2026-11-20 29%, 2026-10-23 26%, 2026-10-30 19%; 840.00: 2026-10-23 66%, 2026-11-20 11%, 2026-10-30 10% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 850.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 919.73 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $13.62B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $18.6M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$59.6M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±28.50 (3.3%) -> 827.99 to 884.99, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 465,910 calls / 527,695 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 1,000.00 (25,171); puts 850.00 (19,292) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 900 calls, 9,905 OI: 2026-11-20 43% (4,308), 2026-10-30 22% (2,213), 2026-10-23 19% (1,904); put wall 850 puts, 19,292 OI: 2026-11-20 37% (7,185), 2026-10-23 28% (5,380), 2026-11-27 13% (2,597); max call OI 1000 calls, 25,171 OI: 2026-10-23 35% (8,908), 2026-11-20 25% (6,277), 2026-10-30 22% (5,658); max put OI 850 puts, 19,292 OI: 2026-11-20 37% (7,185), 2026-10-23 28% (5,380), 2026-11-27 13% (2,597) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 900.00: 9,905 calls; put wall 850.00: 19,292 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.13 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 2.25 vol pts (put 56.2%, call 53.9%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 33.2% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 27.1% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 39.7% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$19.1M net, 3.8% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-22T19:00:50+00:00)

- Call wall: 900.00 -> 900.00 (+0.00)
- Put wall: 850.00 -> 850.00 (+0.00)
- Zero gamma: 895.45 -> 919.73 (+24.28)
- Abs gamma strike: 850.00 -> 850.00 (+0.00)
- Net GEX: -$370.1M -> -$418.9M (-$48.8M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
