# 2026-07-12 — Venture candidate: Market State Dashboard (owner decision-support screener)

> **Status:** `in-progress`

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
_(filled at close-out)_
