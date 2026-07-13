# Session — Night run: DONE disposition for the derived owner queue (ORDER 008)

> **Status:** `complete`

- **📊 Model:** fable-5 · worker slice · ORDER 008 night-run product lane
- **session:** taught `scripts/derive_owner_queue.py` an already-live/DONE
  disposition (`- [x] ⚑ **Owner:** … — DONE <ISO date>` → read-only
  "## 4. Live / completed" section, never a pending click), wrote the SWTK §7
  packet using it — the queue now shows the one product actually earning with
  ZERO new clicks queued — and upgraded `docs/products/TEMPLATE.md` stage 6
  (buyer-side self-rebuild proof, PR #110's lesson) + stage 8 (post-click
  DONE flip).
- **started (date -u):** Sun Jul 13 01:44 UTC 2026
- **closed (date -u):** Sun Jul 13 01:50:41 UTC 2026

## ⟲ Previous-session review

Previous session (`.sessions/2026-07-13-night-swtk-packet.md`, PR #112): its
verdict discipline held — it correctly REFUSED to write a SWTK packet rather
than queue a duplicate publish click, documented the missing grammar as an
explicit anti-pattern in the click-script, and left a precise 💡 spec ("teach
the script a `- [x] ⚑ **Owner:** … — DONE <date>` checked-box form … checked
boxes are already tolerated by `CHECKBOX_RE` but currently queue as if
unclicked — inspect before relying on it"). This session executed that spec
verbatim, and its parenthetical warning was load-bearing: `CHECKBOX_RE` does
tolerate `[x]` and WOULD have queued the checked rows as pending clicks, so
the implementation requires BOTH marks (checked + DONE) and a regression test
(`test_checked_box_without_done_still_queues`) pins the legacy tolerance.
Its one omission: the spec didn't say the click-script's "deliberately NO
packet" rationale becomes false the moment the disposition lands — that
paragraph had to be retired in the same slice or the docs would contradict
the tree.

## 💡 Session idea

The Live / completed section makes the queue the catalog view, but it is
still binary (pending | DONE). SWTK's LAUNCH-LOG carries a kill clock
(T+7 2026-07-19 checkpoint, T+14 2026-07-26 signal-or-delist) that no derived
surface shows the owner. Cheap next step: a `— DONE <date>` row optionally
followed by `⏲ <ISO date>` (or a `KILL-CHECK <date>` token) that
`derive_owner_queue.py` renders as a "next checkpoint" column in the Live
section — then the owner's one derived file also answers "which live product
needs a look TODAY", and measurement-mode products can't silently outlive
their kill rules. Same tolerant-parser bar: unparsed dates fall back to the
plain DONE rendering, never manual-review noise.

## Scope

- `scripts/derive_owner_queue.py` — DONE disposition (+14 parse lines, +18
  render lines, +7 summary lines; zero changes to legacy paths).
- `scripts/test_derive_owner_queue.py` — NEW, 5 stdlib tests.
- `docs/publishing/vetting/stripe-webhook-test-kit.md` — NEW, first
  LIVE-product packet (all 3 §7 rows DONE 2026-07-12).
- `docs/publishing/OWNER-QUEUE.md` — regenerated.
- `docs/publishing/README.md` — index row; `docs/launch/stripe-webhook-test-kit/publish-owner-action.md`
  — no-packet rationale retired.
- `docs/products/TEMPLATE.md` — stage-6 + stage-8 upgrades.

## Work log — executed evidence (all 2026-07-13)

1. **Baseline (BEFORE the change):** `python3 scripts/derive_owner_queue.py`
   → `parsed 14 of 14 inputs clean (13 packets + keyword map); 9 decisions,
   74 owner clicks across 13 click-run sequences`; regenerated file
   byte-identical to committed. Output + file saved for diffing.
2. **AFTER the script change, same 13-packet tree:** stdout AND
   OWNER-QUEUE.md both byte-identical to the baseline (`diff` empty twice) —
   backward compatibility proven by execution, not inspection.
3. **Tests:** `python3 -m unittest test_derive_owner_queue -v` →
   `Ran 5 tests in 0.004s / OK` (01:47:42Z): legacy unchanged, DONE row lands
   in Live, mixed packet splits, checked-without-DONE still queues, pending
   totals invariant under adding a live packet.
4. **With the SWTK packet:** `parsed 15 of 15 inputs clean (14 packets +
   keyword map); 9 decisions, 74 owner clicks across 13 click-run sequences`
   + `live/completed 3 DONE rows across 1 products (read-only; excluded from
   pending totals)`. Diff vs baseline OWNER-QUEUE.md = purely the appended
   `## 4. Live / completed` section; pending totals 9/74/13 UNCHANGED.
5. Facts in the packet pinned from LAUNCH-LOG.md / publish-owner-action.md:
   live URL, $29 / `price_cents 2900`, sha256 `d3ac5f88620976c4dee15f70801eba5986faa47f4898a1a3bda4907336eeb0d8`
   (19,872 B), HTTP 200 2026-07-12T16:25:16Z + 16:28:47Z, owner test purchase
   18:09:34Z, kill clock 2026-07-19 / 2026-07-26.

## Guard recipe

The DONE disposition requires BOTH marks — checked box AND `— DONE <ISO
date>`; either alone still queues (tested). Never flip a §7 row to DONE
without its durable launch record; never flip a DONE row back to `- [ ]`
(that re-queues a live product's publish click — the documented
anti-pattern). The Live section renders ONLY when DONE rows exist, so
pre-disposition trees regenerate byte-identically.
