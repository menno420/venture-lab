# Session — EAP closeout: ORDER 013 conventions rules 2–3 → enabler doctrine

> **Status:** `in-progress`

- **📊 Model:** Claude Fable 5 · docs-only ORDER 013 slice · EAP final day 2026-07-14
- **started (date -u):** Tue Jul 14 10:05:04 UTC 2026
- **branch:** `claude/eap-closeout-conventions-013`
- **session:** Execute ORDER 013 (INC-44) — rewrite `docs/conventions.md`
  rules 2–3 to the enabler doctrine: the `auto-merge-enabler.yml` workflow
  arms squash auto-merge on non-draft `claude/*` PRs; agent-side arming and
  direct self-merge are classifier-DENIED per this repo's own
  `docs/PLATFORM-LIMITS.md` / `docs/CAPABILITIES.md` walls. Rule 3's
  merge-then-flag review posture is KEPT. Same PR updates
  `docs/review-queue.md`'s "self-merge grant (conventions.md rule 3)"
  citation to match the new wording. Premise re-verified live at HEAD
  `37e3c05` before any edit: rule 2 still read "arm it **at creation, in
  the checks-pending window**".
- **walls:** docs-only — no workflow, trigger, `control/status.md`,
  `control/inbox.md`, or `control/outbox.md` edits; no auto-merge arming,
  no self-merge (the wall this very rewrite documents); PR left READY on a
  `claude/*` head for the enabler.
- **verify:** `python3 bootstrap.py check --strict`

## Work log

- 2026-07-14T10:05Z — Worktree from origin/main (`37e3c05`); ORDER 013
  premise re-verified at HEAD (rule 2 verbatim unchanged since recon).
  Claim `control/claims/2026-07-14-eap-closeout-conventions.md` + this
  born-red card committed first and pushed.

## ⟲ Previous-session review

previous-session review: `.sessions/2026-07-14-eap-audit.md` (the EAP
project audit, PR #192, plus its #193 attribution correction). What held
up: the audit's citation discipline — every finding carrying
`path:line@ref` or a PR number — is exactly what makes THIS slice cheap:
INC-44's premise ("rule 2 still instructs agent-side arming") was
re-checkable in one grep because the audit and the walls ledger keep
verbatim quotes, not paraphrases. Honest nit: the audit's §8 needed a
same-day correction PR (#193) because attributions were written
repo-unqualified — the same drift class INC-44 itself is (binding prose
lagging verified reality), which argues for citing refs at write time,
every time.

## 💡 Session idea

💡 **Advisory doctrine-drift check for binding docs.** INC-44 existed
because a binding rule (`docs/conventions.md` rule 2) kept instructing an
action the walls ledger records as classifier-DENIED — two sources of
truth, one stale, and only a human diff caught it. Guard recipe: an
advisory checker (alongside `scripts/check_ledger_drift.py`, exits 0)
that greps binding docs for a small denial-list of instruction stems
recorded as walls in `docs/CAPABILITIES.md` (e.g. "arm auto-merge",
"REST merge") and nags when a `binding`-badged doc instructs a
documented-denied action; test target alongside the existing
ledger-drift tests. Deduped against prior 💡 set: the wire-garden-packet
card proposes counts-drift nagging (numbers prose vs derived counts) —
this is instruction-vs-walls drift, a different surface.
