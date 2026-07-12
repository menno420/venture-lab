# 2026-07-12 — Venture candidate: Market State Dashboard (owner decision-support screener)

> **Status:** `complete`

## 💡 Session idea
Write the INTAKE/SPEC (spec doc only — no site build) for a "Market State Dashboard":
a live, $0-hosted, static website that is a DECISION-SUPPORT SCREENER for the owner's
MANUAL trading on his existing DEGIRO account (NOT a bot, NOT automated execution,
NOT financial advice). Per watchlist stock it surfaces current market state
(ranging / uptrend / downtrend), an ATR-based expected daily % move, and — later —
whether any lane-vetted strategy currently signals. Core design is PHASED HONESTY:
Phase 1 is a purely descriptive, defensible-now screener; Phase 2 ships EMPTY and only
gains a signal overlay when a strategy passes the trading-strategy lane's pre-registered
forward test. Cross-repo READS of menno420/trading-strategy via raw.githubusercontent.com;
one PR touches venture-lab only.

## Previous-session review
Prior venture-lab slices intook the digital-artifact candidates (membership-kit,
template-packs, cc-cost-lens, agent-fleet-field-manual) and the owner-directed physical
candidate Bababoefoe, each as a standalone `candidates/<slug>/INTAKE.md` with kill-rule
fields and (where a revenue action was ready) a six-field owner-action row in
`docs/research/venture-ledger.md`. This slice mirrors that INTAKE convention for a NEW
digital candidate rooted in the owner's trading interest; it touches only NEW files under
`candidates/market-state-dashboard/` plus this card. It does NOT touch `control/`,
`.github/workflows/`, other candidates, or the ledger (spec-only candidates are
INTAKE-standalone per repo convention — cc-cost-lens / bababoefoe are not ledger entries).

## Model
- **📊 Model:** opus-4.8 · worker · venture/intake

## Deliverables
- candidates/market-state-dashboard/INTAKE.md (the spec)

## Outcome
Wrote `candidates/market-state-dashboard/INTAKE.md` — a spec-only intake for a $0-hosted
static decision-support screener for the owner's MANUAL DEGIRO trading (no bot, no advice).
Sections: one-liner; PHASED HONESTY (Phase 1 descriptive-only: BB-width/ADX regime,
multi-TF %B, ATR% range, days-in-state — all defensible-now; Phase 2 signal overlays ship
EMPTY, gated on a passed forward test); $0 architecture (Actions cron → fetch → static
JSON+HTML → Pages) with a data-source tradeoff table; DEGIRO cost math + the edge bar; a
six-field ⚑ owner-action row (enable Pages, RECOMMENDED on trading-strategy repo); Phase-1
build cap ≈120k tokens incl. CI; and binding kill criteria.

Cross-repo READS of menno420/trading-strategy (raw + github MCP). HONEST CORRECTIONS to the
intake brief, documented in-spec so no fabrication landed: (1) the named
`position-sizing-vet-2026-07-12.md` and `bollinger-mtf-dev-2026-07-12.md` docs do NOT exist
(404); I cited the REAL anchors instead — `docs/hybrid-allocator.md` (70/20/10 conservative
split, sleeve never grows on paper performance), `docs/p5-holdout-protocol.md` (one-shot,
long/flat, spent-when-read), `docs/final-report.md` §Holdout, and
`docs/research/broker-bot-options-nl-2026-07-12.md` (DEGIRO "No official API / no automated
trading"). (2) The holdout did NOT go "0/13"; it recorded 1 CONFIRMED (AAPL-donchian, t=0.02,
insignificant) / 2 HOLDOUT-BEAT / 10 MISS with verdict "No candidate holds a finding label"
— net zero deployment-ready, so Phase 2 still ships empty. (3) There is NO landed "Bollinger
multi-TF in dev" doc; the only Bollinger evidence is "the whole Bollinger sub-family went 0
for 8" — so the spec does NOT presuppose a Bollinger signal is coming.

Also corrected the Pages recommendation's reasoning: Pages is per-repo (not a scarce shared
allotment), so the real justification to host on trading-strategy is cohesion/ownership
(data + strategy defs + holdout gating live there) and keeping venture-lab as the intake
lane — kept the recommendation, fixed the premise. No ledger/ranking update (spec-only
candidates are INTAKE-standalone per repo convention). No spend, no accounts, no publishing,
no secrets (env var NAMES only). `python bootstrap.py check --strict` green. First commit was
the born-red card; this final commit flips it complete.

