# MU gamma exposure report

As of 2026-10-23T16:12:39+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 886.85 | The underlying price used for every calculation in this run. |
| Net GEX | $111.3M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 890.00, 885.00, 880.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 890.00, 880.00, 885.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 890.00: 2026-10-23 92%, 2026-10-26 3%, 2026-12-18 2%; 885.00: 2026-10-23 96%, 2026-10-26 2%, 2026-10-30 1%; 880.00: 2026-10-23 85%, 2026-10-30 7%, 2026-10-26 2% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 890.00: 2026-10-23 81%, 2026-10-30 6%, 2026-11-20 6%; 880.00: 2026-10-23 62%, 2026-11-20 14%, 2026-10-30 9%; 885.00: 2026-10-23 86%, 2026-10-28 4%, 2026-10-30 4% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 890.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 879.40 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $18.18B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $54.1M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$33.0M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±10.90 (1.2%) -> 875.95 to 897.75, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 744,363 calls / 812,736 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 1,000.00 (34,303); puts 800.00 (25,256) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 890 calls, 6,209 OI: 2026-10-23 44% (2,735), 2026-12-18 23% (1,419), 2026-11-20 9% (532); put wall 890 puts, 7,356 OI: 2026-11-20 30% (2,193), 2026-12-18 20% (1,459), 2026-10-23 19% (1,364); max call OI 1000 calls, 34,303 OI: 2026-10-23 25% (8,426), 2026-10-30 21% (7,063), 2026-11-20 20% (6,917); max put OI 800 puts, 25,256 OI: 2026-11-20 26% (6,532), 2026-12-18 25% (6,244), 2026-10-23 17% (4,322) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 890.00: 6,209 calls; put wall 890.00: 7,356 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.09 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -0.01 vol pts (put 52.9%, call 52.9%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 36.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 0.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 27.1% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 37.0% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$34.8M net, 12.6% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-23T13:51:27+00:00)

- Call wall: 880.00 -> 890.00 (+10.00)
- Put wall: 900.00 -> 890.00 (-10.00)
- Zero gamma: 876.87 -> 879.40 (+2.53)
- Abs gamma strike: 880.00 -> 890.00 (+10.00)
- Net GEX: $35.9M -> $111.3M (+$75.4M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
