# SPY gamma exposure report

As of 2026-10-19T13:42:08+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 767.30 | The underlying price used for every calculation in this run. |
| Net GEX | $1.91B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 770.00, 768.00, 767.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 767.00, 769.00, 765.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 770.00: 2026-10-19 46%, 2026-10-23 19%, 2026-10-20 13%; 768.00: 2026-10-19 79%, 2026-10-20 7%, 2026-10-23 6%; 767.00: 2026-10-19 83%, 2026-10-20 9%, 2026-10-21 4% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 767.00: 2026-10-19 75%, 2026-10-23 12%, 2026-10-20 5%; 769.00: 2026-10-23 68%, 2026-10-19 18%, 2026-10-21 5%; 765.00: 2026-10-19 60%, 2026-10-23 21%, 2026-10-21 5% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 770.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 765.98 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $31.50B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $1.10B | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$2.50B | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±3.40 (0.4%) -> 763.89 to 770.70, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Put/call OI ratio | 2.14 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 3.10 vol pts (put 15.6%, call 12.5%, exp 2026-11-13) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 34.4% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 45.5% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 15.1% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 4.9% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $0 net, 0.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T13:38:14+00:00)

- Call wall: 770.00 -> 770.00 (+0.00)
- Put wall: 765.00 -> 767.00 (+2.00)
- Zero gamma: 769.75 -> 765.98 (-3.77)
- Abs gamma strike: 770.00 -> 770.00 (+0.00)
- Net GEX: -$4.65B -> $1.91B (+$6.56B)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
