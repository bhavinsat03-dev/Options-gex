# SPY gamma exposure report

As of 2026-10-20T01:26:50+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 766.48 | The underlying price used for every calculation in this run. |
| Net GEX | -$8.83B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 770.00, 780.00, 775.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 750.00, 760.00, 765.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 770.00: 2026-10-23 30%, 2026-10-20 20%, 2026-10-30 16%; 780.00: 2026-10-30 31%, 2026-10-23 30%, 2026-11-20 14%; 775.00: 2026-10-23 20%, 2026-10-30 19%, 2026-11-20 14% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 750.00: 2026-10-30 54%, 2026-11-20 25%, 2026-11-06 7%; 760.00: 2026-10-30 52%, 2026-10-23 14%, 2026-11-20 14%; 765.00: 2026-10-30 47%, 2026-10-23 19%, 2026-11-20 13% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 760.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 773.76 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $74.74B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $2.98B | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$3.10B | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±4.40 (0.6%) -> 762.08 to 770.88, exp 2026-10-20 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 1,913,920 calls / 5,671,305 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 800.00 (133,908); puts 750.00 (238,051) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 770 calls, 57,001 OI: 2026-11-20 25% (14,397), 2026-10-23 23% (13,330), 2026-10-30 22% (12,336); put wall 750 puts, 238,051 OI: 2026-10-30 49% (115,566), 2026-11-20 29% (69,729), 2026-11-06 7% (15,956); max call OI 800 calls, 133,908 OI: 2026-11-20 40% (53,761), 2026-10-30 37% (48,886), 2026-10-23 7% (9,516); max put OI 750 puts, 238,051 OI: 2026-10-30 49% (115,566), 2026-11-20 29% (69,729), 2026-11-06 7% (15,956) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 770.00: 57,001 calls; put wall 750.00: 238,051 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 2.96 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 2.98 vol pts (put 15.9%, call 12.9%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 37.9% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 30.8% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 31.3% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$269.0M net, 4.6% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-20T01:21:36+00:00)

- Call wall: 770.00 -> 770.00 (+0.00)
- Put wall: 750.00 -> 750.00 (+0.00)
- Zero gamma: 773.76 -> 773.76 (+0.00)
- Abs gamma strike: 760.00 -> 760.00 (+0.00)
- Net GEX: -$8.83B -> -$8.83B (-$300.3K)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
