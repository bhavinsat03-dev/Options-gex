# BABA gamma exposure report

As of 2026-10-19T19:14:05+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 108.56 | The underlying price used for every calculation in this run. |
| Net GEX | -$507.4K | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 120.00, 110.00, 115.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 110.00, 100.00, 105.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 120.00: 2026-11-20 53%, 2026-12-18 32%, 2026-10-30 9%; 110.00: 2026-11-20 38%, 2026-12-18 26%, 2026-10-23 24%; 115.00: 2026-10-23 48%, 2026-11-20 20%, 2026-12-18 18% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 110.00: 2026-12-18 46%, 2026-11-20 31%, 2026-10-23 12%; 100.00: 2026-12-18 68%, 2026-11-20 23%, 2026-10-23 3%; 105.00: 2026-12-18 35%, 2026-11-20 30%, 2026-10-23 22% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 110.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 108.63 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $1.60B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $9.6M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$15.8M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±3.70 (3.4%) -> 104.86 to 112.26, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 448,922 calls / 252,877 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 120.00 (42,715); puts 100.00 (48,297) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| OI at main walls | call wall 120.00: 42,715 calls; put wall 110.00: 32,157 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 0.56 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -2.47 vol pts (put 39.6%, call 42.1%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 26.5% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 10.2% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 63.3% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$6.8M net, 35.9% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T17:37:37+00:00)

- Call wall: 120.00 -> 120.00 (+0.00)
- Put wall: 110.00 -> 110.00 (+0.00)
- Zero gamma: 108.57 -> 108.63 (+0.06)
- Abs gamma strike: 110.00 -> 110.00 (+0.00)
- Net GEX: $3.1M -> -$507.4K (-$3.6M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
