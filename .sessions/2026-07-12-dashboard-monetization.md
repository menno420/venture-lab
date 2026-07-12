# 2026-07-12 — Market State Dashboard: monetization posture (tiers, compliance copy rules, paid-euro gates, conservative revenue)

> **Status:** `complete`

## 💡 Session idea
Extend the existing `candidates/market-state-dashboard/` spec with a **MONETIZATION**
posture that does NOT contradict the anchor-rotation additions (§G/§H). Four required
pieces, written tightly in ANALYTICS voice: (1) **tier design** — FREE = the owner-dogfood
Phase 1 (limited watchlist, core market states); PREMIUM (€5–15/mo, **feature-gated NOT
advice-gated**) = larger/custom watchlists, advanced/custom indicators, email/push ping
alerts, anchor-rotation tooling; Phase 1 stays **auth-ready** (static now + a simple gate
later, no over-engineered auth). (2) **Compliance posture as BINDING COPY RULES** — a
checklist the site/marketing must pass: analytics voice only, full denominators + published
methodology, never imperative buy/sell, per-item methodology links, standing disclaimer on
every surface, out-of-sample + full-denominator backtest claims (house rule), with the EU
MAR / MiFID rationale stated. (3) **Gates before the first paid euro** as six-field
OWNER-ACTION rows (WHAT/WHERE/HOW/WHY/UNBLOCKS/VERIFIED-WHEN): (a) licensed COMMERCIAL data
feed (~€25–100/mo — current free feeds are personal-use only), (b) one-off NL legal/compliance
copy check, (c) the existing 2-week dogfood KILL CRITERION stands. (4) **Conservative revenue
line** — base case €0 without distribution, stated assumption chain, no overstatement.
RAILS: spec/copy only — no accounts, no spend, no trades, no financial recommendations;
touches only `candidates/market-state-dashboard/` + this card; `control/` untouched.

## Previous-session review
Two prior slices built this candidate. `2026-07-12-candidate-market-state-dashboard.md`
wrote `candidates/market-state-dashboard/INTAKE.md` — the spec-only intake for a $0-hosted
static DECISION-SUPPORT SCREENER for the owner's MANUAL DEGIRO trading (no bot, no advice),
with PHASED HONESTY (Phase 1 descriptive-only; Phase 2 signal overlays ship EMPTY, gated on a
passed forward test) and recorded the standing trading-strategy result (one-shot holdout
SPENT, 0 of 13 deployment-ready). `2026-07-12-dashboard-anchor-rotation.md` then extended it
with **§G** (anchor-rotation PRIMARY Phase-1 use case, default INTC, mechanical ex-ante
rotation trigger, descriptive-only candidate ranking) and **§H** (4-leg rotation cost /
breakeven math, verified DEGIRO US fees, gap risk, NL box-3 note), plus a cited
`intel-context-2026-07.md` (headed CONTEXT — NOT A RECOMMENDATION). This slice adds a NEW
`MONETIZATION.md` supplementary doc (repo convention = per-candidate supplementary `.md`
alongside INTAKE, e.g. photo-packs `MARKET-PLAN.md`, bababoefoe `MAKE-IT-REAL-PLAN.md`; no
prior `MONETIZATION.md` exists) linked from INTAKE, and EXTENDS the existing §E owner-action
grammar rather than contradicting §G/§H. It touches only files under
`candidates/market-state-dashboard/` plus this card. It does NOT touch `control/`,
`.github/workflows/`, other candidates, or the ledger (spec-only candidate → INTAKE-standalone
per repo convention).

## Model
- **📊 Model:** opus-4.8 · worker · venture/intake

## Deliverables
- candidates/market-state-dashboard/MONETIZATION.md — NEW supplementary doc: tier design,
  compliance copy rules, six-field paid-euro gates, conservative revenue line
- candidates/market-state-dashboard/INTAKE.md — one-line link to MONETIZATION.md (edit)

## Outcome
Added `candidates/market-state-dashboard/MONETIZATION.md` (NEW supplementary doc, per the
per-candidate `.md`-alongside-INTAKE convention — no prior `MONETIZATION.md` existed) and
linked it from `INTAKE.md`'s intro "Related docs" pointer. All four required pieces, written
in ANALYTICS voice and explicitly non-contradicting §B PHASED HONESTY and the §G/§H
anchor-rotation additions.

**§B Tier design** — **FREE** = the owner-dogfood Phase 1 (limited watchlist, core market
states, with the disclaimer + per-item methodology as free-tier *obligations*). **PREMIUM
€5–15/mo, feature-gated NOT advice-gated** = larger/custom watchlists, advanced/custom
indicators, email/push "ping" alerts (that state *what price did*, never *what to do*), and
the **anchor-rotation tooling** (§G/§H machinery — configurable anchor, ex-ante trigger,
descriptive-only ranking, always-attached rotation-cost hurdle). Advice-gating forbidden at
any price. **Architecture note:** Phase 1 stays a $0 static site but keeps an **auth-ready
seam** (compute/presentation split; premium emitted as a separately-gate-able bundle) — the
seam *exists* but is deliberately **not wired**; no login/DB/billing in Phase 1.

**§C Compliance posture = BINDING COPY RULES** — a pass/fail checklist every surface must
pass: analytics voice only; full denominators + published methodology; never imperative
buy/sell; per-item methodology links; standing "historical data, no guarantee of future
results" disclaimer on every surface; backtest claims OUT-OF-SAMPLE + full denominator (house
rule). **Rationale stated:** EU **MAR** can treat even generic instrument-specific "suggested
strategies" as investment recommendations (disclosure duties); personalized advice is
**MiFID**-licensed territory — the rules keep the product on the analytics side of BOTH lines.

**§D Gates before the first paid euro** — three **six-field OWNER-ACTION rows**
(WHAT/WHERE/HOW/WHY/UNBLOCKS/VERIFIED-WHEN, schema replicated from
`docs/research/venture-ledger.md` § ⚑ needs-owner / INTAKE §E): **⚑M1** licensed COMMERCIAL
data feed (~€25–100/mo — free yfinance/Stooq are personal-use-only; candidates **Polygon.io**
/ **Tiingo**, key NAME only as an Actions secret); **⚑M2** one-off **NL** legal/compliance
counsel check of the premium copy (small fixed cost); **⚑M3** the existing **2-week owner
dogfood KILL CRITERION** stands as the go/no-go before any premium spend/build. None performed
— documented, not requested.

**§E Conservative revenue line** — **base case €0** without distribution, with the explicit
unproven assumption chain (no audience → visits unproven → visit→checkout unproven →
checkout→paid unproven). No figure projected; consistent with INTAKE's own "does not by itself
make money" read. No overstatement.

RAILS honoured: spec/posture only — no accounts, no spend, no trades, no recommendations;
touched only `candidates/market-state-dashboard/` (MONETIZATION.md + INTAKE link) + this card;
`control/` untouched; ledger untouched (spec-only candidate → INTAKE-standalone per convention).
First commit = born-red card (`in-progress`); content committed next; this final commit flips
the card `complete`. `python3 bootstrap.py check --strict` green.
