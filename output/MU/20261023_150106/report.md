# MU gamma exposure report

As of 2026-10-23T19:01:06+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 878.37 | The underlying price used for every calculation in this run. |
| Net GEX | $266.2M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 880.00, 875.00, 900.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 880.00, 900.00, 850.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 880.00: 2026-10-23 95%, 2026-10-30 2%, 2026-10-26 1%; 875.00: 2026-10-23 95%, 2026-10-26 2%, 2026-10-30 2%; 900.00: 2026-10-26 28%, 2026-10-30 25%, 2026-11-20 17% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 880.00: 2026-10-23 51%, 2026-11-20 17%, 2026-10-30 11%; 900.00: 2026-11-20 28%, 2026-10-30 22%, 2026-12-18 17%; 850.00: 2026-11-20 40%, 2026-10-30 17%, 2026-12-18 12% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 880.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 878.94 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $16.92B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $48.5M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$56.7M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±5.97 (0.7%) -> 872.39 to 884.34, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 744,360 calls / 812,670 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 1,000.00 (34,303); puts 800.00 (25,256) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 880 calls, 7,431 OI: 2026-10-23 42% (3,086), 2026-10-30 24% (1,765), 2026-11-20 13% (937); put wall 880 puts, 10,765 OI: 2026-11-20 36% (3,872), 2026-12-18 19% (1,996), 2026-10-23 19% (1,994); max call OI 1000 calls, 34,303 OI: 2026-10-23 25% (8,426), 2026-10-30 21% (7,063), 2026-11-20 20% (6,917); max put OI 800 puts, 25,256 OI: 2026-11-20 26% (6,532), 2026-12-18 25% (6,244), 2026-10-23 17% (4,322) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 880.00: 7,431 calls; put wall 880.00: 10,765 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.09 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -0.36 vol pts (put 53.3%, call 53.6%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 31.6% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 0.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 28.3% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 40.1% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$39.6M net, 13.8% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-23T16:30:16+00:00)

- Call wall: 885.00 -> 880.00 (-5.00)
- Put wall: 890.00 -> 880.00 (-10.00)
- Zero gamma: 874.49 -> 878.94 (+4.45)
- Abs gamma strike: 890.00 -> 880.00 (-10.00)
- Net GEX: $65.6M -> $266.2M (+$200.6M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
