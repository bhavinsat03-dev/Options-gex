# BABA gamma exposure report

As of 2026-10-20T01:26:50+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 108.57 | The underlying price used for every calculation in this run. |
| Net GEX | $7.0M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 120.00, 110.00, 115.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 110.00, 105.00, 104.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 120.00: 2026-11-20 76%, 2026-10-30 14%, 2026-10-23 5%; 110.00: 2026-11-20 53%, 2026-10-23 31%, 2026-10-30 12%; 115.00: 2026-10-23 60%, 2026-11-20 23%, 2026-10-30 13% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 110.00: 2026-11-20 60%, 2026-10-23 21%, 2026-10-30 13%; 105.00: 2026-11-20 47%, 2026-10-23 33%, 2026-10-30 13%; 104.00: 2026-10-23 87%, 2026-10-30 11%, 2026-11-06 1% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 110.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 107.37 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $666.2M | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $7.3M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$16.3M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±3.76 (3.5%) -> 104.80 to 112.33, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 244,072 calls / 106,694 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 120.00 (27,879); puts 100.00 (13,862) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 120 calls, 27,879 OI: 2026-11-20 72% (19,952), 2026-10-30 14% (3,957), 2026-10-23 10% (2,793); put wall 110 puts, 12,839 OI: 2026-11-20 75% (9,622), 2026-10-23 10% (1,290), 2026-10-30 9% (1,163); max call OI 120 calls, 27,879 OI: 2026-11-20 72% (19,952), 2026-10-30 14% (3,957), 2026-10-23 10% (2,793); max put OI 100 puts, 13,862 OI: 2026-11-20 67% (9,338), 2026-10-23 15% (2,080), 2026-10-30 7% (976) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 120.00: 27,879 calls; put wall 110.00: 12,839 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 0.44 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -2.77 vol pts (put 40.7%, call 43.4%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 41.1% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 15.7% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 43.2% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$144.6K net, 0.7% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-20T01:21:36+00:00)

- Call wall: 120.00 -> 120.00 (+0.00)
- Put wall: 110.00 -> 110.00 (+0.00)
- Zero gamma: 107.37 -> 107.37 (+0.00)
- Abs gamma strike: 110.00 -> 110.00 (+0.00)
- Net GEX: $7.0M -> $7.0M (-$2.3K)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
