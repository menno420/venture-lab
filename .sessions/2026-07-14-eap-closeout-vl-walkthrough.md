# Session — ORDER 014(b): EAP close-out walkthrough + owner actions

> **Status:** `in-progress`

- **📊 Model:** Claude Fable 5 (family-level)
- **started (date -u):** Tue Jul 14 10:07:52 UTC 2026
- **branch:** `claude/eap-closeout-walkthrough-014b` — READY PR (born-red:
  this card holds the substrate gate red until it flips `complete`; the
  close-out surfaces — `control/status.md` / `control/outbox.md` — land in a
  later pass on this same branch)
- **session:** ORDER 014(b) (`control/inbox.md` @ `37e3c05`) — land
  `docs/eap-closeout-walkthrough-2026-07-14.md` with sections A–E (what the
  seat did · current state + verify commands · OWNER ACTIONS checklist with
  every pending decision/click · 5-minute verify tour · handoff notes), a
  docs-gate Status badge in the first 12 lines, and a real markdown link
  from `docs/AGENT_ORIENTATION.md`'s planted-doc-set list (precedent: the
  EAP audit doc entry).
- **walls:** no publish, no spend, no external action; no self-merge or
  auto-merge arm (classifier wall, `docs/CAPABILITIES.md` append log); the
  262 owner clicks / 16 hard-gated sequences stay parked-cited; grading is
  time-gated to 2026-07-17T09:05Z and untouched.
- **verify:** `python3 bootstrap.py check --strict`

## ⟲ Previous-session review

previous-session review: `.sessions/2026-07-14-eap-audit.md` (+ its
follow-up `.sessions/2026-07-14-eap-audit-s8-fix.md`) — the EAP audit
session shipped PR #192 (the 11-section measured audit, honest nulls kept
in §11) and PR #193 (the §8 attribution fix, every corrected cite verified
against the trading-strategy tree before the doc was touched), and its
refuse-to-invent posture is exactly what makes this walkthrough cheap to
write: section A can link the audit instead of re-deriving it — the one
cost is that the audit's own nit (bare PR numbers colliding across repos)
had to be fixed by a second session instead of being caught pre-merge.

## 💡 Session idea

💡 **A machine-parseable owner-answers intake file to close the decision
loop.** The queue's OUTPUT direction is fully mechanized
(`scripts/derive_owner_queue.py` regenerates `docs/publishing/OWNER-QUEUE.md`
from packet §7 blocks), but the INPUT direction is not: owner replies
("go with defaults", "D13: A", "NK2: 16k") arrive as free chat text and
must be hand-applied to packets by whichever session sees them — chat
evaporates, and a missed reply is invisible. Recipe: a one-writer
`control/owner-answers.md` with a claim-bullet-style grammar
(`` - `D13` · **C (Park)** · YYYY-MM-DD ``), parsed by the same module
`derive_owner_queue.py` already exposes (the kill-clock checker's
import-not-fork precedent); the derive script renders answered D-items as
RESOLVED with the owner's letter, and `check` nags (advisory) on any
answer older than ~72h not yet applied to its packet. Deduped against
`docs/ideas/` (the 2026-07-14 batch is title concepts) and the prior 💡
set on the 2026-07-14 cards (counts-drift nag, NL pre-naming, series
glossary, per-concept outcome rows, HARD-GATED rendering, hoisted shared
clicks, wall-anchor citing, repo-qualified PR cites): no prior idea
mechanizes the owner-reply INTAKE direction.

## Scope

- FIRST commit: this born-red card + claim
  `control/claims/2026-07-14-eap-closeout-walkthrough.md`, pushed
  immediately.
- Deliverable: `docs/eap-closeout-walkthrough-2026-07-14.md` (sections A–E
  per ORDER 014(b)) + the reachability link in `docs/AGENT_ORIENTATION.md`.
- NOT this session: arming/merging the PR, flipping this badge,
  `control/status.md` / `control/outbox.md` (a later pass on this branch
  carries the close-out surfaces per the coordinator dispatch).
