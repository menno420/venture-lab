# Market State Dashboard — MONETIZATION (spec only, no spend in this slice)

> Supplementary to [`INTAKE.md`](INTAKE.md). This file specifies **how the dashboard could
> earn**, without contradicting the intake's core design (PHASED HONESTY — §B) or the
> anchor-rotation additions (§G/§H). It is **copy and posture only**: no accounts are
> created, no feed is purchased, no listing is published, and nothing here is a financial
> recommendation. The base case is **€0** (§E) — this document exists so that *if* the owner
> ever pursues revenue, the compliance rails and the real cost gates are written down **before**
> the first euro, not after.

## A. Scope & non-contradiction

Monetization sits **on top of** the free descriptive screener, never in place of its honesty.
Every rule below is downstream of two facts already established in the intake:

- **Phase 2 ships EMPTY** — no strategy in the trading-strategy lane has cleared a
  pre-registered forward test (one-shot holdout SPENT, 0 of 13 deployment-ready; INTAKE §B).
  So **nothing sold here is a signal, a prediction, or advice.** The product monetizes
  **descriptive tooling and convenience**, not edge.
- **The value ceiling of Phase 1 is "a tidy description of market state"** (INTAKE §"Why this
  might fail"). Revenue therefore rides on *breadth, customization, and delivery* of that
  description — not on a claim that it makes money.

## B. Tier design

Two tiers, split on **features**, never on **advice**. The premium tier unlocks *more of the
same descriptive tooling*, delivered more conveniently — it never unlocks a "better call."

### FREE — the owner-dogfood Phase 1

The exact Phase-1 board the owner already builds and reads for himself:

- **Limited watchlist** (a small fixed cap — the ~20–50 liquid US names of the intake, or a
  smaller public default).
- **Core market states** — regime (BB-width percentile / ADX), multi-timeframe %B, ATR%
  typical-daily-range, days-in-state (INTAKE §B Phase 1).
- The **standing disclaimer** and **per-item methodology** on every surface (§C) — these are
  free-tier obligations, not premium features.

FREE is the honest, defensible product on its own. It is also the **dogfood and the funnel**:
the owner uses it for real (the 2-week kill criterion, §D gate c) before any premium build.

### PREMIUM — €5–15/mo, **feature-gated, NOT advice-gated**

Premium gates **capacity, customization, and delivery** — every premium feature is still a
*descriptive* surface under the same §C copy rules:

- **Larger / custom watchlists** — raise or remove the free cap; let the subscriber define
  their own ticker set and timeframe params.
- **Advanced / custom indicators** — additional mechanical descriptors and user-tunable
  parameters (e.g. custom BB/ADX/ATR windows, extra timeframes) — all still backward-looking,
  reproducible-from-bars descriptors, never forecasts.
- **Email / push "ping" alerts** — notify when a *descriptive state changes* (e.g. "AAPL
  regime flipped range→uptrend," "INTC closed back inside its lower daily band"). Alerts state
  **what price did**, never **what to do** — the same wording constraint as the board (§C).
- **Anchor-rotation tooling** — the §G/§H machinery as a configurable, subscriber-owned
  feature: a **configurable anchor** (INTAKE §G.1), the mechanical **ex-ante rotation trigger**
  (§G.2), the **descriptive-only** candidate ranking (§G.2 — ranks *how a name currently looks*,
  never *what it will do*), and — always attached — the **rotation cost / breakeven hurdle**
  (§G.3/§H). Selling this tooling does **not** loosen its honesty: it still surfaces facts +
  the cost hurdle and leaves every decision to the user.

**Advice-gating is forbidden.** No tier, at any price, unlocks a buy/sell instruction, a
prediction, a "recommended" name, or a signal that has not passed a forward test. Money buys
**more descriptors, more tickers, and delivery** — never a call.

### Architecture note — auth-ready, not over-built

Phase 1 stays a **$0 static site now**, but structured so a paywall can be *added* later
without a rewrite:

- Keep the compute (GitHub Actions) and the presentation (static JSON+HTML) separated as in
  INTAKE §C, so a gate can wrap the *delivery* of premium JSON without touching the math.
- Treat the free board as the public artifact and premium data as a **separately-emitted,
  gate-able bundle** — the seam a future auth layer clips onto.
- **Do NOT build auth now.** No login, no user DB, no billing integration in Phase 1 — that is
  premature and off the $0 path. "Auth-ready" means *the seam exists*; it does not mean the
  seam is wired. Wiring waits until the §D gates clear and the kill criterion passes.

## C. COMPLIANCE POSTURE — BINDING COPY RULES

> **Load-bearing.** This is a **checklist every site and marketing surface MUST pass** before
> it ships — free or paid, landing page or alert email. A surface that fails any line does not
> ship. The product lives or dies on staying on the **analytics** side of the regulatory line;
> these rules are what keep it there.

**The checklist (each line is pass/fail):**

- [ ] **Analytics voice only.** Every claim is an **indicator state** or a **historical
      frequency** — never a suggestion to act. Describe what price *did*; never instruct.
- [ ] **Full denominators, always.** Any frequency/statistic ships with its **full
      denominator** and a link to its **published methodology** (e.g. "closed back inside the
      lower band on 34 of 512 observed daily sessions" — never a bare "closes back inside 7%
      of the time").
- [ ] **Never imperative buy/sell language.** No "buy," "sell," "take profit," "enter,"
      "exit," "target," or any instruction to trade — on the board, in alerts, or in
      marketing. (An alert says "regime flipped to downtrend," never "sell.")
- [ ] **Per-item methodology links required.** Every descriptor on every surface links to how
      it is computed (definition + inputs + window). No number appears without its method one
      click away.
- [ ] **Standing disclaimer on every surface.** Every page, email, and alert carries: *this is
      historical/descriptive market data, not financial advice, and there is no guarantee of
      future results.* No surface is exempt — including marketing.
- [ ] **Backtest claims are OUT-OF-SAMPLE + full denominator (house rule).** Any performance
      or backtest claim in marketing is **out-of-sample** and stated with its **full
      denominator and methodology**. In-sample / cherry-picked / denominator-free performance
      claims are banned outright — stricter than the law requires, on purpose.

**Rationale (state it plainly):** Under the EU **Market Abuse Regulation (MAR)**, even
*generic*, non-personalized material that proposes an investment strategy for a specific
instrument (e.g. "suggested strategy: buy X when Y") can count as an **investment
recommendation**, carrying disclosure/objectivity duties. Cross the further line into
**personalized** advice and you are in **MiFID II**-licensed investment-advice territory
entirely. The copy rules above keep the product **on the analytics side of BOTH lines**: pure
descriptive indicator states and honestly-denominated historical frequencies are market
*analysis/data*, not a recommendation and not advice. The moment copy drifts toward "you
should" or "this will," it risks reclassification — which is exactly why "never imperative"
and "no predictions" are hard, checkable rules rather than aspirations.

> This is a house compliance posture, not legal advice. Gate (b) in §D queues a one-off
> professional review of the actual premium copy against these rules before any paid launch.

## D. Gates before the first paid euro

> Three gates stand between the free dogfood board and the first paid subscription. Each is a
> **six-field OWNER-ACTION row** in the repo's standard grammar
> (WHAT / WHERE / HOW / WHY / UNBLOCKS / VERIFIED-WHEN — see
> [`docs/research/venture-ledger.md`](../../docs/research/venture-ledger.md) § ⚑ needs-owner and
> INTAKE §E). **None have been performed.** They are documented here, not requested — a paid
> build is not queued until the kill criterion (gate c) passes.

### ⚑M1 — License a COMMERCIAL market-data feed (the free feeds are personal-use only)

- **WHAT:** Replace the personal-use free sources (yfinance/Stooq — INTAKE §C: unofficial /
  personal, non-redistributed use only) with a **commercially-licensed** feed whose terms
  permit powering a **paid, redistributed** product. Est. cost line **~€25–100/mo** depending
  on ticker count and cadence.
- **WHERE:** A reputable market-data API with an explicit **commercial** tier — candidates:
  **Polygon.io** (Stocks paid tiers) or **Tiingo** (paid commercial plan); both already named
  as the sellable-version feed in INTAKE §C. Sign-up + billing on the vendor's site; the key
  is an owner-managed GitHub Actions **secret** (env var NAME only in config — never a value).
- **HOW:** Create the vendor account, choose the commercial tier that covers ~50 tickers at
  the intake's hourly + EOD cadence, confirm the **licence explicitly permits a paid /
  redistributed product**, and wire the key NAME into the pipeline config (e.g.
  `POLYGON_API_KEY` / `TIINGO_API_KEY`) as an Actions secret.
- **WHY:** yfinance/Stooq are fine for the owner's **personal** board but are **not licensed
  for redistribution or resale** (INTAKE §C licensing flag). Charging subscribers for data
  served off a personal-use feed is a ToS and licensing breach — a paid product **must** sit
  on a commercial feed.
- **UNBLOCKS:** A legally-sellable data layer — the precondition for any premium tier to exist
  at all.
- **VERIFIED-WHEN:** The commercial plan is active, its licence text is on record as
  permitting a paid product, the board renders off the licensed feed, and the free-feed
  personal-use path is no longer what serves paying subscribers.

### ⚑M2 — One-off NL legal/compliance counsel check of the premium copy

- **WHAT:** A single, fixed-cost review by qualified **Netherlands** legal/compliance counsel
  of the premium site + marketing copy against the §C copy rules and the MAR/MiFID lines.
- **WHERE:** A Dutch law/compliance firm with financial-promotions / MAR-MiFID experience
  (NL/EU jurisdiction, as this is the owner's jurisdiction). Engaged directly by the owner;
  the copy under review is this repo's `MONETIZATION.md` §C plus the actual landing/alert/
  marketing text once drafted.
- **HOW:** Package the §C checklist + the drafted premium copy, commission a one-off written
  opinion confirming the product reads as **market analysis/data** (not an investment
  recommendation under MAR, not advice under MiFID), and apply any required copy edits before
  launch. Small fixed cost, not a retainer.
- **WHY:** §C is a **house** posture, not a legal opinion. Before charging money on copy that
  deliberately walks a regulatory line, a professional confirmation that the line is not
  crossed is cheap insurance against reclassification / disclosure-duty exposure.
- **UNBLOCKS:** Confidence to publish paid copy — the compliance sign-off gate for a paid
  launch.
- **VERIFIED-WHEN:** Written NL counsel sign-off is on record, and every edit it required has
  landed in the shipped copy.

### ⚑M3 — Existing KILL CRITERION stands: 2-week owner dogfood before any premium build

- **WHAT:** Enforce the intake's binding kill criterion (INTAKE §E / §"Kill criteria") as the
  first monetization gate: the **owner uses the Phase-1 board for 2 weeks** before any premium
  build begins or any spend on ⚑M1/⚑M2 is authorized.
- **WHERE:** The live Phase-1 board (the owner's own dogfood instance); the disuse check is
  the same one already specified in INTAKE §E ("owner stops opening the board for 2 weeks →
  park it").
- **HOW:** Owner opens and reads the board over a **2-week** window. Sustained real use →
  proceed to authorize ⚑M1/⚑M2. Board goes unread for 2 weeks → **park** the candidate (stop
  the cron, keep the code) and **spend nothing** on a premium build. This gate is an
  owner-action only in that it is the owner's **go/no-go** on committing money — the action is
  *withholding* spend until dogfood proves the tool earns its own attention.
- **WHY:** A screener the owner himself won't open is worth nothing to strangers. Proving
  **self-use first** is the cheapest possible validation and prevents paying for a commercial
  feed + legal review on a tool that has not earned even one real user (its author).
- **UNBLOCKS:** Permission to spend on ⚑M1/⚑M2 and to start the premium build — *only* after
  self-use is demonstrated.
- **VERIFIED-WHEN:** 2 weeks of sustained owner use is on record (board opened/read across the
  window, not parked) — and only then are the paid gates authorized.

## E. Conservative revenue line

**Base case: €0.** Honestly, with **no distribution and no audience**, this earns nothing —
and that is the number to plan around, not a hopeful projection.

**The assumption chain (every link is unproven):**

1. **Traffic is unproven.** There is **no audience** — no list, no channel, no inbound. A
   live URL is not visitors; visitors must be *acquired*, and no acquisition path is built.
2. **Visit → checkout is unproven.** Even given visitors, the fraction who start a paid
   checkout for a *descriptive screener that explicitly makes no predictions* is unknown and
   plausibly tiny — the honest product deliberately refuses the "get rich" hook that converts.
3. **Checkout → paid is unproven.** Free-tier-to-paid conversion for a €5–15/mo descriptive
   tool, with no track record and no signals to sell, is a guess — and guesses are not revenue.

Because **every** link (visits → checkout → purchase) is unproven and the front of the chain
(any audience at all) does not yet exist, the defensible forecast is **€0 until distribution
is built and measured.** Any positive number requires *first* solving distribution, *then*
observing real conversion — neither of which this slice does. **No figure is projected here;
the honest base case is zero, stated plainly and not overstated** — consistent with the
intake's own read that Phase 1 "does not by itself make money" and real revenue is "gated
behind a forward-test win that has not happened yet and may never" (INTAKE §"Why this might
fail").
