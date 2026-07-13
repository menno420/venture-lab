# Session — Night run: ⏲/KILL-CHECK column in the derived owner queue (ORDER 008)

> **Status:** `complete`

- **📊 Model:** fable-5 · worker slice · ORDER 008 night-run product-infra lane
- **session:** paid down THE top backlog debt (named by three consecutive
  cards: photo-packs → bundle-packet → candidate-sweep): the derived owner
  queue's "Live / completed" section could not show kill-clock
  checkpoints, so the owner couldn't see "which live product needs a look
  today". Design chosen: a **packet-level `KILL-CHECK:` line** inside §7
  carrying one-or-more `⏲ <ISO date> <label>` tokens — packet-level (not
  per-DONE-row) because the kill clock is a product-level fact, one clock
  per launch; the line reuses the existing `collect_items` continuation
  grammar unchanged. Rendered earliest-first in the Live section as
  `⏲ Next checkpoint: <date> — <label>` (+ a stdout line). Malformed dates
  are skipped with a manual-review note, matching the script's documented
  tolerant-parser/advisory contract (exits 0 on every path) — a hard error
  would have been the wrong philosophy for this file.
- **started (date -u):** Sun Jul 13 02:38:59 UTC 2026
- **closed (date -u):** Sun Jul 13 02:47 UTC 2026

## ⟲ Previous-session review

Previous session (`.sessions/2026-07-13-night-candidate-sweep.md`, PR #125,
merged): the sweep held the honesty bar well — it ranked all four
unpacketed candidates by distance-to-READY, drove only the one whose
content genuinely pre-existed in-repo (Kill-Rule Intake Kit $15, floor
6/6 executed with a proper zero-runtime honest null), and recorded the
other three as honestly unbuilt rather than asserting progress. Its
baseline-then-delta queue-regen proof pattern was reused here verbatim
and worked exactly as designed: baseline byte-identical at HEAD, then
post-script-change regen on the untouched tree ALSO byte-identical (the
strongest possible backward-compat evidence), then the SWTK delta =
exactly two ⏲ lines. Its 💡 (a greppable `source-material:` intake field)
did not apply to this infra slice but remains a good sweep-cost reducer.
It named this slice's debt as "THE top backlog debt (three consecutive
cards name it)" — that call was correct and this slice closes it; the
streak stops at three.

## 💡 Session idea

The queue now shows each live product's next checkpoint, but nothing
computes "is a checkpoint DUE?" — the owner still has to compare ⏲ dates
against today. Since the generator is deliberately timestamp-free
(determinism: output depends only on input file content), the comparison
belongs in a separate advisory checker à la `check_ledger_drift.py`: a
`check_kill_clocks.py` that reuses `derive_owner_queue.parse_packet`,
takes today's date, and prints DUE/OVERDUE checkpoints (exit 0 always).
Wired into the night-run wake ritual, "SWTK T+7 is due today" becomes a
printed fact on every wake from 2026-07-19 onward instead of a date the
coordinator must remember to compare.

## Scope

- `scripts/derive_owner_queue.py` — KILL-CHECK grammar (packet-level,
  §7), earliest-first Live-section rendering, stdout next-checkpoint
  line, malformed-date manual-review note.
- `scripts/test_derive_owner_queue.py` — 4 new tests (parse +
  earliest-first, absent-token unchanged, malformed date skipped with
  note + valid sibling renders, pending-packet token renders nothing);
  suite 9/9 OK.
- `docs/publishing/vetting/stripe-webhook-test-kit.md` — KILL-CHECK line
  with the real LAUNCH-LOG checkpoints (⏲ 2026-07-19 T+7 funnel
  checkpoint · ⏲ 2026-07-26 T+14 kill-rule deadline).
- `docs/publishing/OWNER-QUEUE.md` — regenerated (18/18 inputs clean).
- `docs/products/TEMPLATE.md` — stage-8: post-click KILL-CHECK token
  documented.
- `docs/current-state.md` — checked: no "⏲ column missing" debt line
  exists there (the debt lived in session cards only), so no edit.

## Executed evidence (all 2026-07-13, 02:38–02:47Z)

1. **Backward-compat (byte-identity), executed both sides of the change
   on the untouched packet tree:** regen at HEAD → `git diff` empty vs
   committed OWNER-QUEUE.md; after the script change, regen again →
   stdout diff AND file diff vs the saved baseline both empty
   ("STDOUT-DIFF: byte-identical" / "FILE-DIFF: byte-identical").
2. **Tests:** `python3 -m unittest discover -s scripts -p "test_*.py"`
   → `Ran 9 tests in 0.006s / OK` (4 new + 5 pre-existing).
3. **SWTK regen:** `parsed 18 of 18 inputs clean … manual-review — none`;
   new stdout line `⏲ [Stripe Webhook Test Kit] next checkpoint
   2026-07-19 — T+7 funnel checkpoint (2 armed)`; file delta vs baseline
   = exactly the two ⏲ lines in the SWTK Live entry (`252a253,254`).
