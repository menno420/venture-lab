# Market State Dashboard — intake (owner-directed candidate, spec only)

> A live, **$0-hosted** static website that is a **decision-support screener** for the
> owner's **MANUAL** trading on his existing DEGIRO account. Per watchlist stock it
> surfaces current market **state** (ranging / uptrend / downtrend), an ATR-based
> **expected daily % move**, and — only once earned — whether any lane-vetted strategy
> currently signals. **NOT a bot. NOT automated execution. NOT financial advice.** This
> file is the SPEC only — no site is built in this slice.

## A. What it is (one-liner)

A GitHub-Pages-hosted static screener that reads free/delayed market data on a cron,
computes a small set of **mechanical, descriptive** market-state numbers for a
configurable watchlist of ~20–50 liquid US names, and renders them so the **owner reads
the board and clicks his own trades on DEGIRO**. DEGIRO has no bot API (confirmed —
trading-strategy `docs/research/broker-bot-options-nl-2026-07-12.md`: *"No official API
and no support for automated/bot trading"*), so the only honest model is: **the site
describes state, the human executes**. The site never places an order, never gives
advice, and never claims to predict price.

## B. Phased honesty (CORE DESIGN)

The whole credibility of this tool is that it **never shows a number it cannot defend at
the moment it shows it.** Two hard-separated phases:

### Phase 1 — DESCRIPTIVE screener ONLY (defensible NOW, ships first)

Every Phase-1 field is a **mechanical description of past/observed price**, with **zero
predictive claim**:

- **Regime classification** — ranging vs uptrend vs downtrend, from mechanical inputs
  only: **Bollinger band-width percentile** (band width vs its own trailing history →
  squeeze/expansion) and/or **ADX** (trend strength). No opinion, just the classifier's
  label + the raw inputs behind it.
- **Bollinger band position per timeframe** — where price sits inside its bands on **1h /
  4h / daily** (upper/mid/lower, %B), computed from free data. Purely positional.
- **ATR-based expected daily range, expressed in %** — `ATR(daily) / price` as a
  **typical daily range**, labelled explicitly as *"this is how much it has recently
  moved in a day,"* NOT *"it will move X% today."* It is a volatility descriptor, not a
  forecast.
- **Days-in-current-state** — how many sessions the current regime label has persisted.

All four are backward-looking, reproducible from the raw bars, and survive an honest
"where did this number come from?" audit. **This is the entire product at launch.**

### Phase 2 — SIGNAL overlays (ships EMPTY; each slot must be EARNED)

Phase 2 would overlay *"strategy X currently signals BUY/flat on this ticker."* It is
wired to **exactly one thing**: strategies that have **passed the trading-strategy lane's
pre-registered forward test / one-shot holdout.** No signal is ever shown that isn't
backed by a passed forward test.

**Current status: NONE qualify. Phase 2 ships EMPTY.** As of the 2026-07-12 read of the
trading-strategy lane, the one-shot holdout has been **spent** (its protocol is explicitly
single-use — `docs/p5-holdout-protocol.md`: *"One shot, then final … The holdout is spent
the moment it is read."*) and the result cleared **no strategy for deployment**:

- Of 13 candidates evaluated, the final report records **1 CONFIRMED** (AAPL-donchian),
  **2 HOLDOUT-BEAT** secondaries, and **10 HOLDOUT-MISS** — but the verdict is
  unambiguous: **"No candidate holds a finding label"** (`docs/final-report.md` §Holdout).
  Even the one confirmation is *"a modest, drawdown-shaped, instrument-specific,
  statistically insignificant result"* (t = 0.02, "deep inside noise"). **Zero strategies
  are deployment-ready → zero signal slots exist.**
- **Honest correction to the intake brief:** there is **no landed "Bollinger multi-TF in
  dev" document** in trading-strategy as of this read (the named
  `bollinger-mtf-dev-2026-07-12.md` returns 404 and does not exist in `docs/research/`).
  The only Bollinger evidence on record is negative: the final report states *"The whole
  Bollinger sub-family went 0 for 8"* in the mean-reversion phase. So Phase 2 must **not**
  presuppose a Bollinger multi-TF signal is coming; it ships empty and stays empty until
  some strategy — Bollinger or otherwise — actually clears a fresh, pre-registered forward
  test. If/when a new holdout is opened and a strategy passes, THAT is the trigger to add
  its slot, citing the passing run.

Phase 2 shipping empty is a **feature**: a screener that admits it has no edge yet is more
useful — and far more honest — than one that manufactures signals to fill space.

## C. Architecture ($0 hosting)

```
GitHub Actions cron (hourly, US market hours)
  → fetch delayed/EOD bars for a config watchlist (~20–50 liquid, high-vol US names)
  → compute Phase-1 states (regime, BB positions 1h/4h/daily, ATR% range, days-in-state)
  → emit static JSON + static HTML
  → publish to GitHub Pages
```

- **No server, no database, no runtime backend.** The Action is the only compute; the site
  is static files. Cost = $0 (GitHub Actions + Pages free tiers).
- **No secrets beyond OPTIONAL data-API key NAMES.** The pipeline is designed to run with
  **zero keys** on the primary source. If an optional keyed source is wired, only the env
  var **NAME** is referenced in config/CI (e.g. `FINNHUB_API_KEY`) — **never a value**, and
  the value is an owner-managed GitHub Actions secret, never committed.
- **Watchlist** is a checked-in config file (tickers + timeframe params) the owner edits.

### Data source investigation (honest tradeoffs)

Requirement: cover ~50 tickers **hourly** during US market hours, including enough history
to compute daily Bollinger/ATR/ADX and (ideally) 1h/4h bands.

| Source | Key? | Limits | Covers ~50 tickers hourly? | ToS / notes |
|---|---|---|---|---|
| **yfinance** (Yahoo, unofficial) | No | Unpublished, IP-rate-limited; can throttle/break without notice | **Yes** — one batched call pulls daily + intraday (1h) for the whole list; 4h is resampled from 1h | **Unofficial, ToS grey-area.** Fine-risk for *personal, hourly, non-redistributed* use; do NOT redistribute/sell its data |
| **Stooq** | No | EOD/CSV, generous; intraday coverage thin/unreliable | **Daily: yes.** Intraday 1h/4h: **no** (degrades to daily-only) | Free EOD CSV, no key — rock-solid **daily** fallback |
| **Alpha Vantage** (free) | Yes | **25 requests/day HARD cap** | **No** — 25/day can't cover 50 tickers even once, let alone hourly | Disqualified for this shape |
| **Finnhub** (free) | Yes | 60 req/min; **delayed**; candle/history restricted on free tier | Last-price quotes: yes. Historical candles for BB/ATR: restricted | Optional last-price secondary only (env var NAME `FINNHUB_API_KEY`) |

**RECOMMENDED: PRIMARY = yfinance, FALLBACK = Stooq.**
- **yfinance (primary):** the only free, keyless source that returns **multi-timeframe
  intraday + daily** for all ~50 tickers in a batched pull, which Phase-1's 1h/4h/daily
  Bollinger positions require. Risk owned honestly: unofficial + rate-limited + ToS
  grey-area — acceptable **only** because usage is hourly, personal, and never
  redistributed.
- **Stooq (fallback):** free, keyless, reliable **daily** CSV. If Yahoo throttles/breaks,
  the board **degrades gracefully to daily-only** (regime + daily BB + ATR% + days-in-state
  still compute; the 1h/4h band rows show "intraday unavailable" rather than going stale or
  fabricating). A visibly-degraded board beats a silently-wrong one.
- **Finnhub (optional secondary):** delayed last-price sanity check only, keyed, off by
  default.

**Refresh cadence:** GitHub Actions `cron` **hourly during US market hours**
(~13:30–20:00 UTC ≈ 09:30–16:00 ET) **plus one post-close EOD run** to lock the day's
daily bar. Note GitHub-hosted cron can be delayed several minutes under load — fine for a
decision-support board, and the page must stamp its **last-updated time** so a stale board
is obvious.

**Licensing flag (load-bearing):** 15-min-delayed / EOD data is **fine for personal
decision support** but is **NOT licensed for redistribution or resale.** A **sellable**
version of this dashboard needs a **licensed real-time feed** — a real recurring cost line
(e.g. Polygon or Tiingo paid tiers, roughly tens of USD/month and up). That is an
owner-funded, out-of-scope decision, not a Phase-1 build step.

## D. DEGIRO manual-execution fit (the cost math)

DEGIRO offers no bot API (see §A), so execution is **manual by design** — and at the
owner's account size that is fine, because **costs are not the enemy here:**

- Owner capital: **€5–6K**; typical position **€4–5K**.
- US-stock trade cost: **~€4 total round trip** (per-order fixed fee both ways).
- On a €4–5K position, €4 ≈ **0.08–0.10%** round-trip cost.
- A reliably captured **1–2% move** on €4–5K nets ≈ **€40–100 per trade**, against ~€4 of
  cost — i.e. cost is **~5–10% of a good trade's gross**, not a dealbreaker.
- (Note: DEGIRO's fixed fee makes *small* trades expensive — trading-strategy's broker
  research shows *"single-stock round trips at €100 cost ~4.5% (US)"*. At €4–5K the same
  fixed fee amortizes to ~0.1%. The owner's scale is exactly where the fixed fee stops
  mattering.)

**The edge bar a Phase-2 signal must clear before real use:** a signal is only worth
acting on if its **net expectancy materially exceeds total friction** — round-trip cost
(~0.1%) **+ slippage + a safety margin**. A rule of thumb for this account: a signal must
demonstrate expectancy **well above ~0.1% net per trade** (realistically a multiple of it,
to survive slippage and variance) before it earns a slot on the board. This is exactly why
Phase 2 ships empty: **nothing in the trading-strategy lane has demonstrated even a
statistically significant edge, let alone one that clears costs.**

**Sizing discipline (cited).** Position sizing follows the trading-strategy lane's
allocation discipline, not gut feel. That lane's hybrid allocator
(`docs/hybrid-allocator.md`) fixes a **conservative, non-optimized 70/20/10 split**
(*"B&H core 70% | Rule sleeve 20% | Cash buffer 10%"*, *"chosen conservative, not
optimized"*), and critically **"The sleeve share never grows on paper performance"** — no
adaptive up-sizing off backtest results. The holdout protocol (`docs/p5-holdout-protocol.md`)
further constrains any rule sleeve to **long/flat, no leverage, no shorts**, costed at
**5 bps slippage + 1 bps commission per side.** The dashboard **inherits** this discipline:
any Phase-2 signal maps to the small **rule-sleeve** allocation only, never the core, and
never scales up on a hot streak.

## E. Owner actions + effort

### Owner-action row (six-field grammar) — NOT queued for revenue; one enablement click

> This is the **only** owner action, and it is an **enablement** step (make the future
> site hostable), not a spend or a publish. It is queued only when Phase 1 is actually
> built; at spec stage it is documented, not requested.

#### ⚑ — Enable GitHub Pages for the dashboard (RECOMMENDED host: the trading-strategy repo)

- **WHAT:** Turn on GitHub Pages for the repository that will host the built dashboard.
  **Recommendation: host it on the `menno420/trading-strategy` repo**, not venture-lab.
- **WHERE:** GitHub → the host repo → Settings → Pages → Source = GitHub Actions (or the
  `gh-pages` branch the build Action publishes to).
- **HOW:** One UI toggle: Settings → Pages → set Source; the build Action then publishes the
  static JSON+HTML on each cron run. No custom domain needed (the default
  `menno420.github.io/<repo>` URL is fine).
- **WHY:** GitHub Pages is **per-repository** (each repo can have its own project site), so
  this is **not** about a scarce shared "allotment" — the honest reasons to put it on
  trading-strategy are **cohesion and ownership**: the market data pipeline, the strategy
  definitions, and the forward-test / holdout gating that Phase 2 depends on **all live in
  trading-strategy**, so the dashboard is that repo's natural public face. Keeping
  venture-lab as the **intake/eval lane** (not a hosting surface for a live trading tool)
  keeps its Pages site free for a customer-facing product like **Bababoefoe**, and avoids
  cross-repo data plumbing. (Both repos *could* technically host independently — this is a
  clean-separation recommendation, not a technical constraint.)
- **UNBLOCKS:** A live, auto-refreshing public URL for the Phase-1 board — the entire point
  of "$0-hosted live website."
- **VERIFIED-WHEN:** The Pages URL resolves, shows the watchlist board, and updates after a
  scheduled Action run (last-updated stamp advances).

### Phase 1 build effort / token cap (intake cap — ONE honest number)

**≈ 120k tokens to Phase 1 v0.1, including CI wiring.** Scope inside the cap: the
multi-source fetch module (yfinance primary + Stooq fallback + graceful degrade), the four
descriptive computations (BB-width-percentile/ADX regime, multi-TF %B, ATR% range,
days-in-state), the static JSON+HTML emitter, the GitHub Actions cron workflow, the
watchlist config, a small deterministic test suite over the math, and the CI wiring to keep
it green. Expressed as **complexity/token budget, not wall-clock time.** Over the cap
without a working descriptive board = ledgered negative and re-scoped. (Reference points in
this lane: cc-cost-lens 70k single-file; bababoefoe 150k multi-artifact — this sits between
them.)

### Kill criteria (binding)

- **Owner disuse:** owner stops opening the board for **2 weeks** → **park** it (stop the
  cron, keep the code). A screener nobody reads is pure cost.
- **Data ToS break:** the primary source (yfinance) starts blocking, or its use crosses a
  clear ToS line → **pull** the offending source, fall back to Stooq (daily-only), and if
  no keyless source remains, **park** rather than pay for a feed on spec.
- **No edge ever clears the bar:** if **no** strategy ever passes a fresh forward test at an
  expectancy that clears costs (§D), then **Phase 2 never opens** and the tool stays
  **descriptive-only forever — and that is a fine, honest end state.** A permanently
  Phase-1 screener that correctly describes market state is a legitimate terminal product,
  not a failure.

## F. Ranking / ledger note

**No ranking or ledger update in this slice — by convention.** `docs/research/venture-ledger.md`
tracks **built** candidates (currently only #1 membership-kit and #2 template-packs); other
spec-stage candidates with an INTAKE (cc-cost-lens, bababoefoe) are **not** ledger entries.
This candidate is **spec-only** (nothing built), so it is INTAKE-standalone like them. It
earns a ledger entry (and a six-field ⚑ owner action promoted to `venture-ledger.md`) only
if/when Phase 1 is actually built and the Pages enablement becomes a live ask.

## G. PRIMARY Phase-1 use case — ANCHOR ROTATION (owner-directed)

> This is the **primary** Phase-1 user story the board is built around. It is a
> **descriptive decision-support** flow — the board describes state, the **owner decides and
> clicks his own trades on DEGIRO**. **No predictions, no recommendations, no automated
> execution.** Intel context for this section lives in
> [`intel-context-2026-07.md`](intel-context-2026-07.md), clearly labelled **CONTEXT — NOT A
> RECOMMENDATION**.

**The owner's situation.** The owner holds **Intel (INTC)** shares (~**€5–6K** at DEGIRO). The
**default is HOLD Intel** — the board exists to describe when Intel's *own* mechanical state is
weak enough that he might consider (a) rotating ~€5K into a better-looking name and rebuying Intel
later, or (b) trading Intel itself around a flagged reversal. The board never tells him to do
either; it shows the facts and the cost hurdle, and he decides.

### G.1 — Configurable anchor holding (default INTC)

A **configurable anchor** ticker (default `INTC`) gets a dedicated, prominent panel showing the
anchor's **own** descriptive state:

- **Regime** — trend vs range (from the same mechanical inputs as §B.Phase-1: BB-width percentile
  and/or ADX), with days-in-state.
- **Band position across timeframes** — %B / upper-mid-lower on **daily / 4h / 1h**.
- **ATR-based expected daily range (%)** — `ATR(daily)/price`, labelled *"typical recent daily
  range,"* never *"it will move X% today."* (INTC's ATR% is currently ~5% — see the context file.)
- **Reversal-relevant DESCRIPTIVE facts only** — overnight **gap vs prior close**, **distance to
  the upper/lower bands**, and **band re-entry after a break** (price closed back inside a band it
  had broken). These are *observations of what price did*, with **zero predictive claim**. The
  panel must not say "reversal likely" — only "closed back inside the lower band after breaking it,"
  and let the owner read it.

### G.2 — Rotation trigger (mechanical, ex-ante)

The rotation prompt is defined **ex-ante and mechanically** — no discretion, no fitting:

> **Trigger:** the anchor is **below its lower daily Bollinger band** OR its **daily regime is
> downtrend** (ADX/BB-width classifier). (Config-adjustable, but fixed before the fact.)

When the trigger fires, the board surfaces the **strongest rotation candidates from the watchlist**,
ranked by **DESCRIPTIVE strength ONLY** (e.g. names in a clean uptrend regime / holding above their
bands with rising band-width). **Phase-1 ranking is descriptive, not predictive** — a *predictive*
ranking ("this one will outperform") would require a strategy that **passed the forward test, and
NONE exist**: the trading-strategy lane's one-shot holdout cleared **0 of 13 for deployment**
(1 CONFIRMED at t = 0.02 "deep inside noise" that *trailed* buy-and-hold after costs, 2 HOLDOUT-BEAT,
10 HOLDOUT-MISS; verdict *"No candidate holds a finding label"* — trading-strategy
`docs/final-report.md`, accessed 2026-07-12). So the board ranks *how a name currently looks*, never
*what it will do*.

### G.3 — Rotation hurdle ALWAYS displayed

Next to **every** surfaced rotation candidate, the board **always** shows the **rotation
cost/breakeven hurdle** from §H — the candidate is shown *with the cost of switching into it
attached*, so the owner never sees an attractive-looking name without immediately seeing how much
it must beat "just hold Intel" by to be worth the switch. The hurdle is not a footnote; it rides
alongside the candidate.

### G.4 — "Reversal watch" panel (anchor, descriptive only)

A dedicated **reversal-watch panel for the anchor** surfaces the reversal-relevant descriptive facts
from G.1 — **overnight gap**, **band re-entry after a break**, distance-to-band — as plain
observations. **No predictions.** Purpose: support situation (b) below (trading Intel itself around a
flagged intraday/overnight reversal) with facts, not forecasts. Every tile reads as *"here is what
price did,"* never *"here is what price will do."*

### G.5 — The two situations to support

- **(a) Rotate out of Intel when Intel itself is mechanically weak.** When the anchor trigger (G.2)
  fires, move ~€5K out of Intel into a stronger-*looking* watchlist name, then **rebuy Intel later**.
  The board shows the anchor's weakness, the ranked descriptive candidates, and — crucially — the §H
  round-trip-cycle hurdle each must clear.
- **(b) Trade Intel itself on a flagged reversal.** When the reversal-watch panel (G.4) shows a
  descriptive reversal fact (overnight gap, band re-entry), the owner may trade Intel intraday/overnight
  on his own read. Board's job: surface the fact + the single-round-trip cost, not the call.

## H. ROTATION COST / BREAKEVEN MATH (always shown, honest)

> **This block is prominent by design** and rides next to every rotation candidate (§G.3). A rotation
> only makes sense if the alternative is expected to beat *just holding Intel* by **more than the full
> cost of switching**. Here is that cost, computed honestly.

### H.1 — The full cycle = 4 trade legs

A complete rotation-and-return is **four individual trade legs**:
`sell INTC → buy OTHER → sell OTHER → rebuy INTC`. The cost of the *whole cycle* is what matters,
not a single trade.

### H.2 — DEGIRO fees (verified, cited)

DEGIRO's current **US-stock** cost structure (verified 2026-07-12):

- **€1 commission + €1 handling fee = €2 per order (per leg).** A completed **buy+sell round trip =
  €4** — which matches the owner's stated *"~€4 per completed round trip."*
- **Currency-conversion fee 0.25%** of value on any EUR↔USD auto-conversion (above spot).
- ([brokerchooser.com DEGIRO fees 2026](https://brokerchooser.com/broker-reviews/degiro-review/degiro-fees), accessed 2026-07-12; fee-schedule changes noted Oct 2025 per [quantroutine.com/brokers/degiro](https://quantroutine.com/brokers/degiro/), accessed 2026-07-12.)

### H.3 — Commission for the 4-leg cycle

- **4 legs × €2 = €8 total commission.**
- On a **€5,000** position: **€8 / €5,000 = 0.16%.**

### H.4 — Spread / slippage (conservative)

- Use a conservative **5 bps (0.05%) per leg** — the same per-side slippage the trading-strategy lane
  costs its holdout at (5 bps slippage + 1 bp commission per side, `docs/p5-holdout-protocol.md`).
- **4 legs × 5 bps = 20 bps = 0.20%**, i.e. **~€10** on €5,000.
- *Caveat:* 5 bps is reasonable for **liquid** names; a thinner rotation candidate will cost more, so
  treat 0.20% as a **floor**, not a ceiling.

### H.5 — FX handling (conditional add-on)

DEGIRO's 0.25% conversion applies to EUR↔USD auto-conversions. If proceeds are **kept in USD** between
legs (INTC and the rotation candidate are both USD stocks), only the initial entry and final exit
convert; if **auto-FX converts on every leg**, up to **4 × 0.25% = 1.00%** is added. This depends on
the owner's currency settings, so it is a **conditional add-on**, flagged separately, not baked into
the base hurdle. **Worst case it dominates the whole cost** — a reason to keep proceeds in USD across
the cycle.

### H.6 — TOTAL cycle cost & breakeven (the load-bearing number)

| Component | On €5,000 | % of €5K |
|---|---|---|
| Commission (4 × €2) | €8 | 0.16% |
| Slippage (4 × 5 bps, floor) | €10 | 0.20% |
| **Base cycle cost (USD cash retained)** | **~€18** | **~0.36%** |
| + auto-FX on all 4 legs (worst case) | up to +€50 | up to +1.00% |
| **Worst-case cycle cost** | **up to ~€68** | **up to ~1.36%** |

> **BREAKEVEN, stated plainly:** the alternative trade must be **expected to beat simply HOLDING
> Intel by MORE than ~0.36%** (the base round-trip-cycle friction) just to break even — and
> realistically by a **larger multiple** of that (to survive slippage variance), rising toward
> **~1.0–1.4%** if auto-FX converts every leg. If the switch is not expected to clear Intel by at
> least this margin, **doing nothing (holding Intel) wins.**

### H.7 — GAP RISK (two-sided, quantified)

Transaction cost is **not** the biggest risk — **timing/gap risk is.** While the owner is *out* of
Intel (holding OTHER during the cycle), **Intel can run up.** Intel's **ATR% is ~5%** (ATR(14)≈5.52
on a ~$110 price — see [`intel-context-2026-07.md`](intel-context-2026-07.md) §5). A ~5%-ATR name can
easily move **5–10%+ over even a few sessions**, so if Intel rallies while he's out, the foregone
gain **dwarfs the ~0.36% switching friction by an order of magnitude.** A scheduled catalyst
sharpens this: **Intel reports Q2 earnings 2026-07-23**, a binary event inside any near-term rotation
window. **Implication:** the rotation only makes sense when the anchor's descriptive weakness is
strong enough that the expected relative underperformance of Intel exceeds **both** the friction
(§H.6) **and** this gap risk — a high bar, honestly stated.

### H.8 — NL tax note (general info — NOT tax advice)

Under the Dutch **box 3** regime, tax is levied on **wealth** (a deemed/notional return on net
assets — 2026: an assumed ~7.78% return taxed at 36%, ≈ 2.80% effective), **not on per-trade realized
gains.** So **churn itself carries no direct per-trade tax penalty** — rotating does not trigger a
capital-gains event the way it would in a realization-based system. Note the **pending
werkelijk-rendement (actual-return) reform**: a bill to tax *actual* returns (incl. unrealized gains)
was **adopted by the House of Representatives on 2026-02-12**, aimed at **2028**, but the Minister of
Finance has said amendments are needed and Senate passage is uncertain. **This is general
information, not tax advice.**
([Deloitte NL — Box 3 Actual Return Act](https://www.deloitte.com/nl/en/services/tax/perspectives/wetsvoorstel-wet-werkelijk-rendement-box-3-aangenomen-tweede-kamer.html) · [KPMG — transition to new Box 3](https://kpmg.com/us/en/taxnewsflash/news/2026/02/tnf-netherlands-transition-to-new-box-3-wealth-tax-regime.html), accessed 2026-07-12.)

## Why this might fail

The honest downside: the owner may not sustain the manual-read-and-click habit (kill
criterion #1); the free data sources are unofficial/fragile and could force a park (kill
criterion #2); and — most importantly — **the value ceiling of Phase 1 is "a tidy
description of market state," which does not by itself make money.** The money would come
from Phase 2 signals, and **no strategy in the connected lane has earned one** — the
one-shot holdout cleared nothing deployment-ready (§B). So a realistic read is: this ships
as an honest, defensible **descriptive utility** for the owner's own decisions, with real
revenue **gated behind a forward-test win that has not happened yet and may never.** Scored
that way on purpose — no overstatement.
