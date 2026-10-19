# QQQ gamma exposure report

As of 2026-10-19T21:59:34+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 718.36 | The underlying price used for every calculation in this run. |
| Net GEX | -$4.39B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 720.00, 740.00, 735.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 710.00, 700.00, 720.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 720.00: 2026-10-20 49%, 2026-10-23 21%, 2026-10-30 13%; 740.00: 2026-10-30 62%, 2026-10-23 26%, 2026-11-06 4%; 735.00: 2026-10-23 72%, 2026-10-30 11%, 2026-11-06 5% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 710.00: 2026-10-23 47%, 2026-10-30 19%, 2026-11-06 15%; 700.00: 2026-10-30 70%, 2026-10-23 12%, 2026-11-06 6%; 720.00: 2026-10-30 32%, 2026-10-23 29%, 2026-11-06 9% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 720.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 731.64 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $41.58B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $698.5M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$1.19B | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±6.76 (0.9%) -> 711.60 to 725.12, exp 2026-10-20 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 1,139,605 calls / 1,921,303 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 740.00 (56,452); puts 700.00 (152,133) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| OI at main walls | call wall 720.00: 20,212 calls; put wall 710.00: 96,311 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.69 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 4.62 vol pts (put 24.3%, call 19.7%, exp 2026-11-13) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 49.5% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 36.2% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 14.3% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $0 net, 0.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T19:21:22+00:00)

- Call wall: 720.00 -> 720.00 (+0.00)
- Put wall: 720.00 -> 710.00 (-10.00)
- Zero gamma: 724.46 -> 731.64 (+7.18)
- Abs gamma strike: 720.00 -> 720.00 (+0.00)
- Net GEX: -$3.05B -> -$4.39B (-$1.34B)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
