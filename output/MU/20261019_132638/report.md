# MU gamma exposure report

As of 2026-10-19T17:26:38+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 905.82 | The underlying price used for every calculation in this run. |
| Net GEX | -$117.6M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 900.00, 910.00, 905.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 905.00, 900.00, 850.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 900.00: 2026-10-19 62%, 2026-10-23 10%, 2026-10-21 9%; 910.00: 2026-10-19 64%, 2026-11-20 19%, 2026-10-21 5%; 905.00: 2026-10-19 83%, 2026-10-23 8%, 2026-10-30 4% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 905.00: 2026-10-19 92%, 2026-10-23 4%, 2026-10-21 1%; 900.00: 2026-10-23 37%, 2026-11-20 18%, 2026-12-18 10%; 850.00: 2026-11-20 37%, 2026-10-23 27%, 2026-12-18 12% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 905.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 911.52 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $17.87B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $55.6M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$78.0M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±8.13 (0.9%) -> 897.69 to 913.96, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 655,186 calls / 742,386 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 1,000.00 (27,686); puts 900.00 (21,303) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| OI at main walls | call wall 900.00: 16,872 calls; put wall 905.00: 3,580 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.13 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -0.21 vol pts (put 50.1%, call 50.3%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 23.6% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 25.8% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 14.7% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 35.9% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$29.8M net, 11.9% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T17:16:17+00:00)

- Call wall: 910.00 -> 900.00 (-10.00)
- Put wall: 905.00 -> 905.00 (+0.00)
- Zero gamma: 915.24 -> 911.52 (-3.72)
- Abs gamma strike: 910.00 -> 905.00 (-5.00)
- Net GEX: -$101.2M -> -$117.6M (-$16.4M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
