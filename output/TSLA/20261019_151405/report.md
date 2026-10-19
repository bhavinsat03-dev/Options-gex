# TSLA gamma exposure report

As of 2026-10-19T19:14:05+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 368.84 | The underlying price used for every calculation in this run. |
| Net GEX | $141.0M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 370.00, 400.00, 380.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 350.00, 370.00, 380.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 370.00: 2026-10-19 41%, 2026-10-23 28%, 2026-11-20 12%; 400.00: 2026-11-20 29%, 2026-10-23 22%, 2026-10-30 20%; 380.00: 2026-10-23 43%, 2026-12-18 15%, 2026-11-20 14% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 350.00: 2026-12-18 30%, 2026-11-20 29%, 2026-10-23 16%; 370.00: 2026-10-19 23%, 2026-10-23 20%, 2026-11-20 20%; 380.00: 2026-11-20 34%, 2026-10-30 23%, 2026-12-18 21% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 370.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 353.20 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $12.00B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $51.4M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$210.8M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±1.92 (0.5%) -> 366.92 to 370.75, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 1,071,838 calls / 864,444 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 400.00 (61,407); puts 350.00 (43,131) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| OI at main walls | call wall 370.00: 33,825 calls; put wall 350.00: 43,131 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 0.81 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 0.21 vol pts (put 45.0%, call 44.8%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 4.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 29.6% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 16.2% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 50.3% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$8.3M net, 20.1% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T17:37:37+00:00)

- Call wall: 367.50 -> 370.00 (+2.50)
- Put wall: 367.50 -> 350.00 (-17.50)
- Zero gamma: 355.09 -> 353.20 (-1.89)
- Abs gamma strike: 367.50 -> 370.00 (+2.50)
- Net GEX: $349.9M -> $141.0M (-$208.9M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
