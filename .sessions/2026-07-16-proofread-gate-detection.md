# Session — proofread-gate detection fix (three NL editions were shown click-ready when they still need a blocking native-speaker proofread pass)

> **Status:** `complete`

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

- **`scripts/derive_owner_queue.py`** (commit `b9520da`): added a module
  helper `is_blocking_box(text)` and `PROOFREAD_GATE_RE`
  (`native-speaker proofread pass`). Hard-gate detection
  (`blocked = any(is_blocking_box(b) for b in owner_boxes)`) and the
  blocking-row capture now treat a native-speaker proofread pass as
  inherently blocking even when the literal "blocking" keyword is absent,
  while preserving the existing behaviour for boxes that already say
  "blocking". Scoped to the proofread phrase, so ordinary ⚑ Owner rows
  (title ratify, cover, price, the publish click) are NOT mis-flagged.
- **Three packets normalised** (same commit) to the house form used by
  de-nachtoven (+~10 other NL packets): `de-waag.md`,
  `het-trage-woord.md`, `weduwenblauw.md` now append
  `(blocking quality gate for this title)` to the proofread row, so the
  source is unambiguous.
- **`scripts/test_derive_owner_queue.py`** (same commit): +1 case
  (`test_proofread_gate_without_blocking_keyword_is_hard_gated`) — a
  proofread-gate box WITHOUT the literal "blocking" is detected hard-gated
  and names the real proofread blocking row, and a regression battery
  asserts ordinary ⚑ Owner rows (publish click, cover, EN-sequencing, NL
  title-ratify) are NOT treated as gates. `Ran 35 tests … OK`.
- **`docs/publishing/OWNER-QUEUE.md`** regenerated from the script (never
  hand-edited): De Waag, Het trage woord, and Weduwenblauw now render
  **HARD-GATED**; hard-gated sequences **16 → 19**; no other group flipped;
  §3 manual-review stayed empty (47/47 clean). `docs/current-state.md`
  hard-gated count synced 16 → 19.
- **Known nuance (honest):** Weduwenblauw's HARD-GATED suffix renders the
  legacy "(a D-item above blocks this sequence)" variant rather than
  naming the proofread row, because the normalised continuation's word
  "title" (in "…for this title") keyword-overlaps its step-2 "Title
  coupling" ⚑ decision under the pre-existing `linked` heuristic. It IS
  correctly hard-gated; only the explanatory wording differs. De Waag and
  Het trage woord name the proofread row directly. Left as-is — tightening
  the `linked` keyword-overlap heuristic is a separate concern (see 💡).
- **Gates:** `scripts/lint_owner_gates.py` → `OK — 47 input(s) clean`;
  `scripts/test_derive_owner_queue.py` → `Ran 35 tests … OK`;
  `python3 bootstrap.py check --strict` green except this card's own
  designed born-red HOLD (now cleared by this flip); guard-fire telemetry
  delta (9 records) committed with the fix per convention, not reverted.
- **Landed as PR #213**, ⚑ Self-initiated (all inbox ORDERs 011–015
  terminal; nothing owner-queued asked for it). Heartbeat re-stamped
  (`control/status.md`, commit `10e03d3`); `control/inbox.md` untouched.

## ⟲ Previous-session review

previous-session review: `.sessions/2026-07-16-salt-bell.md` (The Salt
Bell concept-#3 write-slice, PR #211, merged `17990a5`) — its central
facts held under re-verification this wake: the merge is on main and
carries the manuscript + DECISIONS + EN packet + one owner-queue regen,
and the "16 hard-gated / 45 sequences / 268 clicks" queue figure it
recorded (via its regen) is exactly the surface this slice audited and
corrected upward to 19 hard-gated (the same three NL proofread rows it
left un-normalised, now fixed at the root).

## 💡 Session idea

💡 **The `linked`/D-item attribution keys on loose keyword overlap and
mis-fires on generic words like "title" — tighten it to a real
same-packet reference.** This slice surfaced it: Weduwenblauw's proofread
blocking row got tagged "executes its D-item above" purely because
"(blocking quality gate for this title)" shares the word "title" with a
"Title coupling" ⚑ decision, so its HARD-GATED suffix reads the D-item
variant instead of naming the proofread row. Cheap next slice: drop
low-signal stopwords (title, edition, cover, price, publish…) from
`lead_keywords`, or require a stronger match (≥2 shared distinctive words,
or an explicit D<n>/step reference) before a click is called "linked" —
so the D-item wording is reserved for rows that genuinely execute a
decision. Deduped against prior `.sessions/*.md` 💡 lines: the previous
owner-queue idea (`owner-queue-blocker-reason`) proposed anchoring the
suffix to its in-place `- [ ]` row; this one is about the accuracy of the
D-item attribution itself, upstream of that anchoring.
