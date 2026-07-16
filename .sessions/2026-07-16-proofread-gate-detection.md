# Session — proofread-gate detection fix (three NL editions were shown click-ready when they still need a blocking native-speaker proofread pass)

> **Status:** `in-progress`

- **📊 Model:** Claude Opus · medium · runtime bugfix
- **started (date -u):** Thu Jul 16 16:40:00 UTC 2026
- **branch:** `claude/proofread-gate-detection` (PR TBD)
- **session:** ⚑ Self-initiated slice (surfaced by the #210/#211 follow-on
  investigation into the owner-queue surface; all inbox ORDERs 011–015
  terminal, nothing owner-queued asked for this). What/why:
  `scripts/derive_owner_queue.py` decides a click-run is HARD-GATED purely
  by whether the literal word "blocking" appears in an owner checkbox
  (`blocked = any("blocking" in b.lower() for b in owner_boxes)`, ~line
  265). Three NL titles — **De Waag**, **Het trage woord**,
  **Weduwenblauw** — carry the SAME owner native-speaker proofread quality
  gate as the correctly-gated packets (e.g. de-nachtoven), but their
  checkbox reads `native-speaker proofread pass approved/commissioned.`
  with NO `(blocking quality gate for this title)` continuation, so the
  literal "blocking" keyword is absent and the generator renders all three
  as NOT hard-gated. The owner-facing queue therefore tells the owner these
  three are click-ready to publish when they actually require the same
  blocking human proofread pass. **Publishing an un-proofread NL edition is
  a real quality/reputation risk** — this protects the owner from
  mis-publishing.
- **scope:** ROOT-CAUSE fix in the generator — hard-gate detection now
  recognises an `⚑ Owner:` native-speaker proofread-pass checkbox as
  inherently blocking even when the literal "blocking" keyword is absent,
  while preserving existing behaviour for boxes that already say "blocking"
  and NOT mis-flagging unrelated ⚑ Owner rows (title ratify, cover, price,
  publish clicks). Additionally normalise the three packets' proofread
  rows to the established house form (append `(blocking quality gate for
  this title)`, matching de-nachtoven and ~10 other NL packets) so the
  source is unambiguous. Extend `scripts/test_derive_owner_queue.py`:
  a proofread-gate box WITHOUT the literal "blocking" is detected
  hard-gated; a regression case that an ordinary ⚑ Owner publish-click box
  is NOT mis-flagged. Regenerate `docs/publishing/OWNER-QUEUE.md` from the
  script (never hand-edited). Plus this card, the claim, and a heartbeat
  re-stamp.
- **walls:** no publish, spend, or external action; no edits to
  `control/inbox.md`; no merge or auto-merge from this seat; the generated
  file is only ever written by the script; family-level model names only.
- **verify plan:** run `scripts/test_derive_owner_queue.py` (must pass);
  run `scripts/lint_owner_gates.py` (must pass); regenerate the queue and
  diff it — the ONLY new HARD-GATED entries must be the three titles (plus
  their corrected suffixes), no other drift; `python3 bootstrap.py check
  --strict` must exit 0 (its born-red HOLD on this card is the designed
  exception until the completion flip).
- **done-when:** the fix + extended test + regenerated queue land on a
  READY PR, CI green (kit-tests + substrate-gate), heartbeat re-stamped,
  and this card flipped `complete` as the last commit (clearing the
  born-red HOLD).

## Results (as landed)

[[fill: script fix + test + regenerated queue + packet normalisation, with commit SHAs]]

## ⟲ Previous-session review

[[fill: one-line review of the 2026-07-16 Salt Bell slice, PR #211, merge 17990a5]]

## 💡 Session idea

[[fill: one genuine forward idea, deduped against prior .sessions/*.md]]
