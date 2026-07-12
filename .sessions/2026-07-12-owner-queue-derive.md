# 2026-07-12 — Derive owner queue from vetting packet §7 blocks (PR #91 card idea)

> **Status:** in-progress

## Scope

One work increment, self-initiated from the 💡 idea on PR #91's session card
(`.sessions/2026-07-12-slow-word-vetting.md`): the ⚑ owner queue should be a
DERIVED fact, not a hand-maintained list. Deliverables: NEW
`scripts/derive_owner_queue.py` (stdlib-only, always-exit-0, tolerant parser
in the `check_ledger_drift.py` convention) that parses the §7 / ⚑ OWNER-GATE
blocks across `docs/publishing/vetting/*.md` plus ⚑ OWNER-flagged conflicts
in `docs/publishing/keyword-map.md`, and regenerates
`docs/publishing/OWNER-QUEUE.md` deterministically (decisions first with
bolded defaults, then pure click-run items; unparseable packets listed under
Manual review, never edited); + an index row in `docs/publishing/README.md`.
No publish, spend, account, or external action; packets NOT normalized this
slice; `control/status.md`, `control/outbox.md`, and triggers untouched.

## 💡 Session idea
💡 (to be filled at flip)

## Previous-session review
previous-session review: (to be filled at flip)

## Model
- **📊 Model:** Fable 5 · worker · venture/publishing

## Outcome
(in progress)
