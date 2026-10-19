# SPY gamma exposure report

As of 2026-10-19T15:31:23+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 769.72 | The underlying price used for every calculation in this run. |
| Net GEX | $716.3M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 770.00, 771.00, 769.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 770.00, 769.00, 760.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 770.00: 2026-10-19 78%, 2026-10-23 7%, 2026-10-20 6%; 771.00: 2026-10-19 80%, 2026-10-20 5%, 2026-10-21 5%; 769.00: 2026-10-19 77%, 2026-10-20 9%, 2026-10-21 5% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 770.00: 2026-10-19 56%, 2026-10-23 12%, 2026-10-30 11%; 769.00: 2026-10-23 57%, 2026-10-19 25%, 2026-10-30 5%; 760.00: 2026-10-30 66%, 2026-10-23 16%, 2026-11-06 5% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 770.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 769.56 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $43.94B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $1.98B | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$3.17B | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±2.50 (0.3%) -> 767.22 to 772.22, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 1,514,940 calls / 3,235,545 puts | Open contracts across all fetched expirations and strikes. |
| OI at main walls | call wall 770.00: 54,195 calls; put wall 770.00: 38,192 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 2.14 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 3.49 vol pts (put 15.3%, call 11.8%, exp 2026-11-13) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 28.2% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 37.4% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 27.9% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 6.5% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $0 net, 0.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T14:20:13+00:00)

- Call wall: 770.00 -> 770.00 (+0.00)
- Put wall: 765.00 -> 770.00 (+5.00)
- Zero gamma: 769.16 -> 769.56 (+0.40)
- Abs gamma strike: 770.00 -> 770.00 (+0.00)
- Net GEX: -$1.80B -> $716.3M (+$2.52B)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
