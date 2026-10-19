# AMD gamma exposure report

As of 2026-10-19T17:26:38+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 542.22 | The underlying price used for every calculation in this run. |
| Net GEX | -$15.5M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 542.50, 540.00, 545.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 542.50, 540.00, 545.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 542.50: 2026-10-19 96%, 2026-10-23 3%, 2026-10-21 0%; 540.00: 2026-10-19 72%, 2026-10-23 14%, 2026-11-20 5%; 545.00: 2026-10-19 60%, 2026-10-23 25%, 2026-10-21 7% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 542.50: 2026-10-19 96%, 2026-10-21 2%, 2026-10-23 1%; 540.00: 2026-10-19 64%, 2026-10-23 12%, 2026-10-30 7%; 545.00: 2026-10-19 50%, 2026-10-23 18%, 2026-10-21 17% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 542.50 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 546.32 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $9.73B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $35.3M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | $5.4M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±4.50 (0.8%) -> 537.71 to 546.72, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 565,327 calls / 582,418 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 620.00 (28,308); puts 440.00 (23,765) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| OI at main walls | call wall 542.50: 1,843 calls; put wall 542.50: 1,250 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.03 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -0.36 vol pts (put 57.2%, call 57.6%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 27.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 31.8% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 11.5% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 29.8% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $282.7K net, 8.1% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T17:16:17+00:00)

- Call wall: 542.50 -> 542.50 (+0.00)
- Put wall: 542.50 -> 542.50 (+0.00)
- Zero gamma: 546.47 -> 546.32 (-0.15)
- Abs gamma strike: 542.50 -> 542.50 (+0.00)
- Net GEX: -$6.4M -> -$15.5M (-$9.1M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
