# 2026-07-12 — Market State Dashboard: anchor-rotation primary use case + rotation cost math + Intel context

> **Status:** `in-progress`

## 💡 Session idea
Extend the existing `candidates/market-state-dashboard/` spec with the owner's PRIMARY
Phase-1 use case: an **anchor holding** (default INTC — the owner holds ~€5–6K of Intel at
DEGIRO, default = HOLD). Spec (A) the anchor's own descriptive state panel + a mechanical,
ex-ante **rotation trigger** that surfaces DESCRIPTIVE-strength rotation candidates from a
watchlist (Phase-1 ranks by descriptive strength ONLY — no predictive ranking, since no
strategy has cleared the forward test); (B) a prominent, honest **rotation cost / breakeven**
block (4-leg cycle: sell INTC → buy OTHER → sell OTHER → rebuy INTC), with real DEGIRO US-stock
fees + slippage + gap-risk + an NL box-3 tax note; and (C) a NEW `intel-context-2026-07.md`
file — current, fully-cited web research on Intel, headed **CONTEXT — NOT A RECOMMENDATION**.
RAILS: research/spec only — no accounts, no trades, no financial recommendations. Cross-repo
READS of menno420/trading-strategy only; the PR touches venture-lab ONLY; control/ untouched.

## Previous-session review
The prior slice (`2026-07-12-candidate-market-state-dashboard.md`) wrote
`candidates/market-state-dashboard/INTAKE.md` — a spec-only intake for a $0-hosted static
DECISION-SUPPORT SCREENER for the owner's MANUAL DEGIRO trading (no bot, no advice), with
PHASED HONESTY (Phase 1 descriptive-only; Phase 2 signal overlays ship EMPTY, gated on a passed
forward test). That card also recorded the correct standing result from the trading-strategy
lane: the one-shot holdout was SPENT and cleared **no strategy for deployment** — of 13
candidates, 1 CONFIRMED (AAPL-donchian, t=0.02, "deep inside noise"), 2 HOLDOUT-BEAT, 10
HOLDOUT-MISS, verdict **"No candidate holds a finding label"**. This slice extends the SAME
candidate with the anchor-rotation use case; it touches only files under
`candidates/market-state-dashboard/` plus this card. It does NOT touch `control/`,
`.github/workflows/`, other candidates, or the ledger (spec-only candidate → INTAKE-standalone
per repo convention).

## Model
- **📊 Model:** opus-4.8 · worker · venture/intake

## Deliverables
- candidates/market-state-dashboard/INTAKE.md — new §G anchor-rotation use case + §H rotation
  cost/breakeven math (edit of existing spec)
- candidates/market-state-dashboard/intel-context-2026-07.md — NEW cited research file
  (CONTEXT — NOT A RECOMMENDATION)

## Outcome
_(pending — flipped to complete as the last content commit)_
