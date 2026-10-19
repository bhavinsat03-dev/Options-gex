# TSLA gamma exposure report

As of 2026-10-19T19:21:22+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 368.23 | The underlying price used for every calculation in this run. |
| Net GEX | $316.9M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 367.50, 400.00, 380.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 350.00, 380.00, 360.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 367.50: 2026-10-19 97%, 2026-10-23 2%, 2026-10-30 0%; 400.00: 2026-11-20 29%, 2026-10-23 22%, 2026-10-30 20%; 380.00: 2026-10-23 43%, 2026-12-18 15%, 2026-11-20 14% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 350.00: 2026-12-18 29%, 2026-11-20 29%, 2026-10-23 16%; 380.00: 2026-11-20 34%, 2026-10-30 23%, 2026-12-18 21%; 360.00: 2026-10-23 29%, 2026-12-18 19%, 2026-10-30 19% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 367.50 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 365.02 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $11.84B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $49.5M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | $376.0M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±2.05 (0.6%) -> 366.18 to 370.28, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 1,071,841 calls / 864,444 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 400.00 (61,407); puts 350.00 (43,131) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| OI at main walls | call wall 367.50: 8,181 calls; put wall 350.00: 43,131 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 0.81 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -1.31 vol pts (put 44.1%, call 45.4%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 22.6% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 23.6% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 13.1% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 40.8% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$12.0M net, 16.4% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T19:14:05+00:00)

- Call wall: 370.00 -> 367.50 (-2.50)
- Put wall: 350.00 -> 350.00 (+0.00)
- Zero gamma: 353.20 -> 365.02 (+11.82)
- Abs gamma strike: 370.00 -> 367.50 (-2.50)
- Net GEX: $141.0M -> $316.9M (+$175.9M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
