# MU gamma exposure report

As of 2026-10-19T19:14:05+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 906.68 | The underlying price used for every calculation in this run. |
| Net GEX | -$204.5M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 905.00, 900.00, 1,000.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 905.00, 900.00, 850.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 905.00: 2026-10-19 86%, 2026-10-23 6%, 2026-10-30 3%; 900.00: 2026-10-23 26%, 2026-10-21 24%, 2026-11-20 20%; 1,000.00: 2026-11-20 25%, 2026-12-18 24%, 2026-10-30 19% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 905.00: 2026-10-19 91%, 2026-10-23 4%, 2026-10-21 1%; 900.00: 2026-10-23 41%, 2026-11-20 20%, 2026-12-18 11%; 850.00: 2026-11-20 37%, 2026-10-23 27%, 2026-12-18 12% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 905.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 909.20 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $18.51B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $56.1M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$246.5M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±4.95 (0.5%) -> 901.73 to 911.63, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 655,183 calls / 742,320 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 1,000.00 (27,686); puts 900.00 (21,303) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| OI at main walls | call wall 905.00: 2,595 calls; put wall 905.00: 3,580 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.13 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 0.70 vol pts (put 50.4%, call 49.7%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 14.8% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 29.2% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 16.3% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 39.7% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$28.2M net, 13.1% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T17:37:37+00:00)

- Call wall: 900.00 -> 905.00 (+5.00)
- Put wall: 905.00 -> 905.00 (+0.00)
- Zero gamma: 899.97 -> 909.20 (+9.23)
- Abs gamma strike: 900.00 -> 905.00 (+5.00)
- Net GEX: -$112.9M -> -$204.5M (-$91.7M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
