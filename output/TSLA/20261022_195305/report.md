# TSLA gamma exposure report

As of 2026-10-22T23:53:05+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 374.58 | The underlying price used for every calculation in this run. |
| Net GEX | $181.2M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 380.00, 370.00, 375.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 375.00, 370.00, 380.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 380.00: 2026-10-23 67%, 2026-10-30 8%, 2026-11-20 7%; 370.00: 2026-10-23 70%, 2026-11-20 10%, 2026-10-30 6%; 375.00: 2026-10-23 67%, 2026-10-30 9%, 2026-11-20 8% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 375.00: 2026-10-23 76%, 2026-10-30 6%, 2026-11-20 5%; 370.00: 2026-10-23 63%, 2026-10-30 10%, 2026-11-20 10%; 380.00: 2026-10-23 54%, 2026-11-20 16%, 2026-10-30 15% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 380.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 366.76 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $11.92B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $58.1M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$170.5M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±8.60 (2.3%) -> 365.98 to 383.18, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 1,119,541 calls / 995,266 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 400.00 (63,432); puts 350.00 (43,206) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 380 calls, 32,513 OI: 2026-10-23 34% (11,041), 2026-12-18 23% (7,504), 2026-11-20 16% (5,343); put wall 375 puts, 16,309 OI: 2026-10-23 40% (6,585), 2026-11-20 17% (2,848), 2026-12-18 15% (2,421); max call OI 400 calls, 63,432 OI: 2026-10-23 31% (19,583), 2026-11-20 24% (15,090), 2026-12-18 19% (11,976); max put OI 350 puts, 43,206 OI: 2026-12-18 34% (14,563), 2026-11-20 25% (10,753), 2026-10-23 21% (8,927) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 380.00: 32,513 calls; put wall 375.00: 16,309 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 0.89 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 0.16 vol pts (put 40.6%, call 40.4%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 45.3% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 18.8% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 35.9% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$10.1M net, 14.2% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-22T21:56:03+00:00)

- Call wall: 380.00 -> 380.00 (+0.00)
- Put wall: 375.00 -> 375.00 (+0.00)
- Zero gamma: 366.17 -> 366.76 (+0.59)
- Abs gamma strike: 380.00 -> 380.00 (+0.00)
- Net GEX: $192.5M -> $181.2M (-$11.3M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
