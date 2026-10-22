# MU gamma exposure report

As of 2026-10-22T13:50:59+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 893.41 | The underlying price used for every calculation in this run. |
| Net GEX | -$199.6M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 900.00, 910.00, 950.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 900.00, 850.00, 880.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 900.00: 2026-10-23 45%, 2026-11-20 21%, 2026-10-30 20%; 910.00: 2026-11-20 47%, 2026-10-23 34%, 2026-10-30 8%; 950.00: 2026-10-23 32%, 2026-10-30 27%, 2026-11-20 23% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 900.00: 2026-10-23 58%, 2026-11-20 16%, 2026-10-30 11%; 850.00: 2026-10-23 32%, 2026-11-20 31%, 2026-10-30 14%; 880.00: 2026-10-23 46%, 2026-11-20 25%, 2026-10-30 14% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 900.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 915.45 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $13.55B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $52.9M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$276.2M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±29.60 (3.3%) -> 863.81 to 923.01, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 465,910 calls / 527,695 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 1,000.00 (25,171); puts 850.00 (19,292) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 900 calls, 9,905 OI: 2026-11-20 43% (4,308), 2026-10-30 22% (2,213), 2026-10-23 19% (1,904); put wall 900 puts, 18,724 OI: 2026-11-20 33% (6,161), 2026-10-23 30% (5,605), 2026-10-30 13% (2,486); max call OI 1000 calls, 25,171 OI: 2026-10-23 35% (8,908), 2026-11-20 25% (6,277), 2026-10-30 22% (5,658); max put OI 850 puts, 19,292 OI: 2026-11-20 37% (7,185), 2026-10-23 28% (5,380), 2026-11-27 13% (2,597) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 900.00: 9,905 calls; put wall 900.00: 18,724 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.13 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -0.74 vol pts (put 50.9%, call 51.7%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 36.8% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 27.5% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 35.8% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$17.9M net, 3.3% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-21T19:00:04+00:00)

- Call wall: 910.00 -> 900.00 (-10.00)
- Put wall: 910.00 -> 900.00 (-10.00)
- Zero gamma: 911.68 -> 915.45 (+3.77)
- Abs gamma strike: 910.00 -> 900.00 (-10.00)
- Net GEX: -$82.0M -> -$199.6M (-$117.6M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
