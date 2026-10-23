# MU gamma exposure report

As of 2026-10-23T16:30:16+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 886.45 | The underlying price used for every calculation in this run. |
| Net GEX | $65.6M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 885.00, 890.00, 880.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 890.00, 900.00, 880.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 885.00: 2026-10-23 97%, 2026-10-26 1%, 2026-10-30 1%; 890.00: 2026-10-23 92%, 2026-10-26 3%, 2026-10-30 2%; 880.00: 2026-10-23 82%, 2026-10-30 9%, 2026-10-26 3% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 890.00: 2026-10-23 77%, 2026-11-20 7%, 2026-10-30 7%; 900.00: 2026-10-23 37%, 2026-11-20 18%, 2026-10-30 14%; 880.00: 2026-10-23 68%, 2026-11-20 12%, 2026-10-30 7% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 890.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 874.49 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $18.55B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $53.3M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | $86.4M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±9.90 (1.1%) -> 876.55 to 896.35, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 744,363 calls / 812,736 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 1,000.00 (34,303); puts 800.00 (25,256) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 885 calls, 2,989 OI: 2026-10-23 75% (2,248), 2026-10-26 7% (222), 2026-10-30 7% (216); put wall 890 puts, 7,356 OI: 2026-11-20 30% (2,193), 2026-12-18 20% (1,459), 2026-10-23 19% (1,364); max call OI 1000 calls, 34,303 OI: 2026-10-23 25% (8,426), 2026-10-30 21% (7,063), 2026-11-20 20% (6,917); max put OI 800 puts, 25,256 OI: 2026-11-20 26% (6,532), 2026-12-18 25% (6,244), 2026-10-23 17% (4,322) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 885.00: 2,989 calls; put wall 890.00: 7,356 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.09 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 2.26 vol pts (put 54.2%, call 51.9%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 37.4% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 0.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 26.5% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 36.1% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$32.7M net, 12.4% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-23T16:12:39+00:00)

- Call wall: 890.00 -> 885.00 (-5.00)
- Put wall: 890.00 -> 890.00 (+0.00)
- Zero gamma: 879.40 -> 874.49 (-4.91)
- Abs gamma strike: 890.00 -> 890.00 (+0.00)
- Net GEX: $111.3M -> $65.6M (-$45.6M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
