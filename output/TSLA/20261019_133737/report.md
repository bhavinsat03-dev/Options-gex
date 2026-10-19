# TSLA gamma exposure report

As of 2026-10-19T17:37:37+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 367.50 | The underlying price used for every calculation in this run. |
| Net GEX | $349.9M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 367.50, 370.00, 400.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 367.50, 350.00, 370.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 367.50: 2026-10-19 98%, 2026-10-23 2%, 2026-10-30 0%; 370.00: 2026-10-19 36%, 2026-10-23 30%, 2026-11-20 13%; 400.00: 2026-11-20 29%, 2026-10-23 22%, 2026-10-30 20% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 367.50: 2026-10-19 95%, 2026-10-23 3%, 2026-10-26 1%; 350.00: 2026-12-18 29%, 2026-11-20 29%, 2026-10-23 17%; 370.00: 2026-10-23 23%, 2026-11-20 23%, 2026-12-18 17% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 367.50 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 355.09 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $11.86B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $52.4M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$166.8M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±2.37 (0.6%) -> 365.12 to 369.86, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 1,071,838 calls / 864,444 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 400.00 (61,407); puts 350.00 (43,131) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| OI at main walls | call wall 367.50: 8,181 calls; put wall 367.50: 2,344 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 0.81 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 0.14 vol pts (put 44.8%, call 44.6%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 31.4% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 20.8% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 11.6% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 36.2% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$10.3M net, 14.6% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T17:29:55+00:00)

- Call wall: 367.50 -> 367.50 (+0.00)
- Put wall: 367.50 -> 367.50 (+0.00)
- Zero gamma: 355.13 -> 355.09 (-0.04)
- Abs gamma strike: 367.50 -> 367.50 (+0.00)
- Net GEX: $354.5M -> $349.9M (-$4.6M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
