# MU gamma exposure report

As of 2026-10-23T13:51:27+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 878.51 | The underlying price used for every calculation in this run. |
| Net GEX | $35.9M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 880.00, 875.00, 900.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 900.00, 850.00, 880.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 880.00: 2026-10-23 88%, 2026-10-30 6%, 2026-10-26 2%; 875.00: 2026-10-23 93%, 2026-10-26 3%, 2026-10-30 2%; 900.00: 2026-10-23 25%, 2026-10-30 20%, 2026-10-26 19% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 900.00: 2026-10-23 51%, 2026-11-20 15%, 2026-10-30 10%; 850.00: 2026-10-23 30%, 2026-11-20 29%, 2026-10-30 11%; 880.00: 2026-10-23 56%, 2026-11-20 17%, 2026-10-30 9% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 880.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 876.87 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $17.20B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $59.4M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$272.0M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±23.70 (2.7%) -> 854.81 to 902.21, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 744,363 calls / 812,736 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 1,000.00 (34,303); puts 800.00 (25,256) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 880 calls, 7,431 OI: 2026-10-23 42% (3,086), 2026-10-30 24% (1,765), 2026-11-20 13% (937); put wall 900 puts, 23,108 OI: 2026-11-20 26% (5,983), 2026-10-23 23% (5,288), 2026-12-18 21% (4,795); max call OI 1000 calls, 34,303 OI: 2026-10-23 25% (8,426), 2026-10-30 21% (7,063), 2026-11-20 20% (6,917); max put OI 800 puts, 25,256 OI: 2026-11-20 26% (6,532), 2026-12-18 25% (6,244), 2026-10-23 17% (4,322) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 880.00: 7,431 calls; put wall 900.00: 23,108 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.09 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 9.23 vol pts (put 59.5%, call 50.3%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 37.8% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 0.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 25.6% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 36.6% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$23.1M net, 12.7% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-22T23:53:05+00:00)

- Call wall: 900.00 -> 880.00 (-20.00)
- Put wall: 850.00 -> 900.00 (+50.00)
- Zero gamma: 921.85 -> 876.87 (-44.98)
- Abs gamma strike: 850.00 -> 880.00 (+30.00)
- Net GEX: -$448.3M -> $35.9M (+$484.2M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
