# SPCX gamma exposure report

As of 2026-10-20T01:26:50+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 147.96 | The underlying price used for every calculation in this run. |
| Net GEX | -$28.4M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 150.00, 155.00, 160.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 140.00, 150.00, 145.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 150.00: 2026-11-20 46%, 2026-10-23 19%, 2026-10-21 12%; 155.00: 2026-10-23 33%, 2026-11-20 25%, 2026-10-21 20%; 160.00: 2026-11-20 35%, 2026-10-23 25%, 2026-10-30 19% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 140.00: 2026-11-20 33%, 2026-10-23 31%, 2026-10-30 13%; 150.00: 2026-11-20 39%, 2026-10-30 25%, 2026-10-23 17%; 145.00: 2026-10-23 31%, 2026-11-20 27%, 2026-10-30 15% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 150.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 154.28 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $4.01B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $12.0M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$75.3M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±10.55 (7.1%) -> 137.41 to 158.51, exp 2026-10-21 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 588,258 calls / 606,692 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 175.00 (35,341); puts 130.00 (44,361) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 150 calls, 32,009 OI: 2026-11-20 58% (18,570), 2026-10-23 13% (4,244), 2026-10-30 10% (3,055); put wall 140 puts, 44,158 OI: 2026-11-20 42% (18,380), 2026-10-23 25% (11,205), 2026-10-30 13% (5,556); max call OI 175 calls, 35,341 OI: 2026-10-30 30% (10,756), 2026-11-20 28% (10,072), 2026-10-23 22% (7,910); max put OI 130 puts, 44,361 OI: 2026-11-20 53% (23,375), 2026-10-30 18% (7,931), 2026-10-23 12% (5,391) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 150.00: 32,009 calls; put wall 140.00: 44,158 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.03 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 0.85 vol pts (put 58.1%, call 57.2%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 39.5% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 20.4% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 40.2% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$514.9K net, 0.8% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-20T01:21:36+00:00)

- Call wall: 150.00 -> 150.00 (+0.00)
- Put wall: 140.00 -> 140.00 (+0.00)
- Zero gamma: 154.28 -> 154.28 (+0.00)
- Abs gamma strike: 150.00 -> 150.00 (+0.00)
- Net GEX: -$28.4M -> -$28.4M (-$4.8K)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
