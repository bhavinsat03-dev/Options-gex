# MU gamma exposure report

As of 2026-10-19T19:21:22+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 908.55 | The underlying price used for every calculation in this run. |
| Net GEX | -$84.2M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 910.00, 900.00, 1,000.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 910.00, 900.00, 950.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 910.00: 2026-10-19 81%, 2026-11-20 10%, 2026-10-21 3%; 900.00: 2026-10-23 26%, 2026-10-21 24%, 2026-11-20 20%; 1,000.00: 2026-11-20 25%, 2026-12-18 24%, 2026-10-30 19% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 910.00: 2026-10-19 82%, 2026-10-23 5%, 2026-11-20 4%; 900.00: 2026-10-23 41%, 2026-11-20 20%, 2026-12-18 11%; 950.00: 2026-10-23 30%, 2026-10-30 25%, 2026-11-20 22% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 910.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 909.09 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $18.07B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $58.7M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$261.1M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±5.04 (0.6%) -> 903.51 to 913.59, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 655,186 calls / 742,386 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 1,000.00 (27,686); puts 900.00 (21,303) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| OI at main walls | call wall 910.00: 12,128 calls; put wall 910.00: 5,862 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.13 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 1.09 vol pts (put 50.6%, call 49.5%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 16.6% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 28.6% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 16.0% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 38.8% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$26.6M net, 12.8% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T19:14:05+00:00)

- Call wall: 905.00 -> 910.00 (+5.00)
- Put wall: 905.00 -> 910.00 (+5.00)
- Zero gamma: 909.20 -> 909.09 (-0.11)
- Abs gamma strike: 905.00 -> 910.00 (+5.00)
- Net GEX: -$204.5M -> -$84.2M (+$120.4M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
