# BABA gamma exposure report

As of 2026-10-21T00:52:34+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 108.61 | The underlying price used for every calculation in this run. |
| Net GEX | $7.5M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 120.00, 110.00, 115.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 110.00, 105.00, 104.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 120.00: 2026-11-20 72%, 2026-10-30 15%, 2026-10-23 5%; 110.00: 2026-11-20 44%, 2026-10-23 40%, 2026-10-30 13%; 115.00: 2026-10-23 57%, 2026-11-20 26%, 2026-10-30 12% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 110.00: 2026-11-20 58%, 2026-10-23 23%, 2026-10-30 13%; 105.00: 2026-11-20 44%, 2026-10-23 34%, 2026-10-30 15%; 104.00: 2026-10-23 86%, 2026-10-30 12%, 2026-11-13 1% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 110.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 107.56 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $714.7M | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $7.4M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$20.9M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±3.25 (3.0%) -> 105.36 to 111.86, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 253,507 calls / 112,645 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 120.00 (30,117); puts 100.00 (13,877) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 120 calls, 30,117 OI: 2026-11-20 66% (20,027), 2026-10-30 15% (4,465), 2026-10-23 11% (3,413); put wall 110 puts, 12,805 OI: 2026-11-20 75% (9,624), 2026-10-23 10% (1,238), 2026-10-30 9% (1,157); max call OI 120 calls, 30,117 OI: 2026-11-20 66% (20,027), 2026-10-30 15% (4,465), 2026-10-23 11% (3,413); max put OI 100 puts, 13,877 OI: 2026-11-20 66% (9,192), 2026-10-23 15% (2,106), 2026-10-30 7% (1,025) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 120.00: 30,117 calls; put wall 110.00: 12,805 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 0.44 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -3.76 vol pts (put 40.7%, call 44.4%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 41.3% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 17.6% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 41.2% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $75.3K net, 1.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-21T00:49:04+00:00)

- Call wall: 120.00 -> 120.00 (+0.00)
- Put wall: 110.00 -> 110.00 (+0.00)
- Zero gamma: 107.56 -> 107.56 (+0.00)
- Abs gamma strike: 110.00 -> 110.00 (+0.00)
- Net GEX: $7.5M -> $7.5M (-$1.5K)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
