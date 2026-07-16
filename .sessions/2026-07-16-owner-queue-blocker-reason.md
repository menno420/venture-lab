# Session — owner-queue blocker-reason fix (hard-gated sequences show their REAL blocking row)

> **Status:** `in-progress`

- **📊 Model:** Claude Opus · medium · runtime bugfix (owner-queue generator)
- **started (date -u):** Thu Jul 16 15:43:37 UTC 2026
- **branch:** `claude/owner-queue-blocker-reason` (PR TBD)
- **session:** ⚑ Self-initiated slice (all ORDER 011/014 inbox items
  terminal — nothing owner-queued asked for this; it improves the accuracy
  of the owner-click-ready surface with no owner click required). What/why:
  `scripts/derive_owner_queue.py` renders EVERY hard-gated click-run with
  the fixed suffix `(a D-item above blocks this sequence)`. But `blocked`
  is set purely by the word "blocking" appearing in an owner checkbox
  (`derive_owner_queue.py` line 258) — and for the ~16 hard-gated
  sequences (12 NL editions + others) the actual blocking row is a
  per-title "native-speaker proofread pass … (blocking quality gate for
  this title)" checkbox, a length-band ruling, an originals handoff, or a
  prerequisite publish click — NOT any D-item. There is NO D-item gating
  them. The suffix misleads the owner about WHY each sequence is blocked,
  in the single file that drives every publish decision.
- **scope:** `scripts/derive_owner_queue.py` — capture the first actual
  blocking row per hard-gated group at parse time and render
  `HARD-GATED — blocking row: <clipped ~80 chars>`, keeping the old
  D-item wording ONLY as a fallback when the blocking row genuinely links
  to a same-packet D-item (Painted Stones / Puddle Museum / Windmill Mouse
  illustration money-decision). Extend `scripts/test_derive_owner_queue.py`
  with a proofread-gated case + a D-item-linked case. Regenerate
  `docs/publishing/OWNER-QUEUE.md` from the script (never hand-edited).
  Plus this card, the claim, and a heartbeat re-stamp.
- **walls:** no publish, spend, or external action; no edits to
  `control/inbox.md`; no merge or auto-merge from this seat; the generated
  file is only ever written by the script; family-level model names only.
- **verify plan:** run `scripts/test_derive_owner_queue.py` (must pass);
  run `scripts/lint_owner_gates.py` if present; regenerate the queue and
  diff it — the ONLY changes must be the corrected blocker-reason
  suffixes, no drift; `python3 bootstrap.py check --strict` must exit 0
  (its born-red HOLD on this card is the designed exception until flip).
- **done-when:** the fix + extended test + regenerated queue land on a
  READY PR, CI green (kit-tests + substrate-gate), heartbeat re-stamped,
  and this card flipped `complete` as the last commit (clearing the
  born-red HOLD).

## Results (as landed)

[[fill: results as landed at flip]]

## ⟲ Previous-session review

[[fill: previous-session review — 2026-07-16 state-restamp / main-verify session, PR #209]]

## 💡 Session idea

[[fill: one genuine session idea at flip]]
