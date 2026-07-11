# Session — Guide/book/info-product intake round

> **Status:** `in-progress`

- **📊 Model:** opus-4.8 · high · venture/intake
- **session:** Intake 4 new guide/book/info-product candidates (owner steer: guides/books to sell) with full kill-rule fields + append-only re-rank addendum.
- **started (date -u):** 2026-07-11

## ⟲ Previous-session review

Previous-session review: prior slice landed stripe-webhook-test-kit v0.1 and the 2026-07-11 venture-eval addendum (ranking table, SWTK 4.05 top) at HEAD a447f1a. No regressions; this slice only adds new files plus an append-only eval addendum.

## 💡 Session idea

The lane's most sellable knowledge is its own scar tissue — the real-payload Stripe gotchas, the false-green test trap, the merge wall. Package the scars as high-intent problem-solving guides (not general advice), and make the cheapest one a free/PWYW funnel into the $29 test-kit rather than a standalone product.

## Scope

- 4 new candidate INTAKE.md files, full kill-rule fields + product-vs-funnel call each.
- Append-only re-ranking addendum in docs/research/venture-eval-001.md (all candidates).
- No touching control/, .github/workflows/, docs/launch/, or candidates being built by others.

## Work log

- **Built:** 4 INTAKE.md (stripe-webhook-gotchas, false-green-test-trap, merge-wall-cookbook, kill-rule-intake-kit); eval addendum.
- **Tests:** bootstrap.py check --strict --session-log green; CI three checks green.
- **Verified vs unverified:** VERIFIED — formats match INTAKE/SWTK precedent; scores computed by the rubric formula. UNVERIFIED — all revenue lines (no sales); token build estimates (not measured).

## Status / outcome

Complete. 4 guide/book candidates intaked, all candidates re-ranked, build-order recommended.
