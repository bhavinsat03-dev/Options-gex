# MU gamma exposure report

As of 2026-10-19T17:37:37+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 904.64 | The underlying price used for every calculation in this run. |
| Net GEX | -$112.9M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 900.00, 905.00, 910.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 905.00, 900.00, 850.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 900.00: 2026-10-19 66%, 2026-10-23 9%, 2026-10-21 8%; 905.00: 2026-10-19 87%, 2026-10-23 6%, 2026-10-30 3%; 910.00: 2026-10-19 47%, 2026-11-20 29%, 2026-10-21 8% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 905.00: 2026-10-19 91%, 2026-10-23 4%, 2026-10-21 1%; 900.00: 2026-10-23 31%, 2026-10-19 23%, 2026-11-20 15%; 850.00: 2026-11-20 36%, 2026-10-23 27%, 2026-12-18 12% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 900.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 899.97 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $18.44B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $52.9M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | $50.3M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±7.50 (0.8%) -> 897.15 to 912.15, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 655,183 calls / 742,320 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 1,000.00 (27,686); puts 900.00 (21,303) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| OI at main walls | call wall 900.00: 16,872 calls; put wall 905.00: 3,580 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.13 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 0.65 vol pts (put 50.6%, call 50.0%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 23.6% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 26.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 14.6% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 35.8% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$28.5M net, 11.8% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T17:29:55+00:00)

- Call wall: 900.00 -> 900.00 (+0.00)
- Put wall: 905.00 -> 905.00 (+0.00)
- Zero gamma: 911.41 -> 899.97 (-11.44)
- Abs gamma strike: 900.00 -> 900.00 (+0.00)
- Net GEX: -$122.0M -> -$112.9M (+$9.1M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
