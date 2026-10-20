# TSLA gamma exposure report

As of 2026-10-20T01:17:50+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 368.06 | The underlying price used for every calculation in this run. |
| Net GEX | $112.2M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 400.00, 380.00, 370.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 350.00, 380.00, 360.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 400.00: 2026-11-20 29%, 2026-10-23 22%, 2026-10-30 20%; 380.00: 2026-10-23 42%, 2026-12-18 15%, 2026-11-20 15%; 370.00: 2026-10-23 46%, 2026-11-20 21%, 2026-12-18 10% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 350.00: 2026-12-18 30%, 2026-11-20 29%, 2026-10-23 16%; 380.00: 2026-11-20 35%, 2026-10-30 22%, 2026-12-18 21%; 360.00: 2026-10-23 29%, 2026-12-18 20%, 2026-11-20 19% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 400.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 352.04 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $10.89B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $51.1M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$155.3M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±23.57 (6.4%) -> 344.49 to 391.63, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 931,373 calls / 800,365 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 400.00 (54,592); puts 350.00 (36,086) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 400 calls, 54,592 OI: 2026-11-20 29% (16,094), 2026-12-18 24% (13,232), 2026-10-23 19% (10,628); put wall 350 puts, 36,086 OI: 2026-12-18 38% (13,658), 2026-11-20 30% (10,912), 2026-10-23 11% (4,087); max call OI 400 calls, 54,592 OI: 2026-11-20 29% (16,094), 2026-12-18 24% (13,232), 2026-10-23 19% (10,628); max put OI 350 puts, 36,086 OI: 2026-12-18 38% (13,658), 2026-11-20 30% (10,912), 2026-10-23 11% (4,087) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 400.00: 54,592 calls; put wall 350.00: 36,086 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 0.86 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -0.23 vol pts (put 45.1%, call 45.3%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 30.2% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 16.8% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 53.0% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$10.0M net, 21.3% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T21:59:34+00:00)

- Call wall: 400.00 -> 400.00 (+0.00)
- Put wall: 350.00 -> 350.00 (+0.00)
- Zero gamma: 352.89 -> 352.04 (-0.85)
- Abs gamma strike: 400.00 -> 400.00 (+0.00)
- Net GEX: $116.7M -> $112.2M (-$4.4M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
