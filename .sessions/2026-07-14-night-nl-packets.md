# Session — Night run: the four owed NL-edition follow-throughs, one batch (ORDER 011 items 2/4/7 follow-through)

> **Status:** `complete`

- **📊 Model:** Fable · worker slice · coordinator-authorized night batch (ORDER 011)
- **started (date -u):** Tue Jul 14 00:54:37 UTC 2026
- **closed (date -u):** Tue Jul 14 01:08 UTC 2026
- **branch:** `claude/night-nl-packets` (PR #180)
- **session:** Executes the owed follow-through recorded by the item-2 slice
  (`.sessions/2026-07-13-night-book-variants.md`: "Deliberately deferred
  (owed): the 4 NL vetting packets, their keyword-map C4 rows, and the
  OWNER-QUEUE regen") and its 💡 (batch all four against the merged union,
  ONE regen), plus the night-kiln-3 card's 💡 (un-stale the night-kiln
  packet's §3/§5 "no manuscript exists" lines — three manuscripts now exist,
  PR #174). Under ORDER 011 (`control/inbox.md` @ `d1edd7c`): item 2
  (edition variants — the four NL editions merged tonight as PRs
  #175/#176/#177/#178), item 4 (V057 keyword-map first-claim-wins, approve),
  item 7 ("Queue hygiene: any new packet requires the
  `derive_owner_queue.py` regen + counts-sync same session (the #166 remedy
  class)").
- **plan:** (1) four NL vetting packets in `docs/publishing/vetting/`
  mirroring the de-papieren-sinaasappel / de-waag precedent (PR #131
  structure; §7 rows: EN-first sequencing, NL title ratification,
  native-speaker proofread, availability recheck, cover, price, publish
  click); (2) keyword-map C4 rows — full-map collision scan FIRST,
  first-claim-wins per V057; (3) the-night-kiln.md §3/§5 un-stale with
  citations (15,999w / 15,995w / 23,334w, PRs #96-era Book 1, #145, #174) —
  Book-2 length-band owner question referenced, not altered; (4) ONE
  `derive_owner_queue.py` regen + counts-sync to `docs/current-state.md` +
  `docs/NEXT-SESSION.md`.
- **walls:** no publish, spend, account, or external action — every gate
  queued ⚑ OWNER only; no edits to manuscripts, `control/inbox.md`,
  `control/outbox.md`, workflows, or triggers; one coordinator-authorized
  exception at close: a single ORDER 011 night-progress line in
  `control/status.md`.
- **verify:** `python3 scripts/lint_owner_gates.py` ·
  `python3 scripts/derive_owner_queue.py` ·
  `python3 bootstrap.py check --strict`

## Results (as landed)

- **4 NL vetting packets** (commit `2d61673`):
  `docs/publishing/vetting/de-nachtoven.md` (16,840w, +5.3% vs EN 15,999),
  `de-marmeladepost.md` (15,637w, +4.0% vs EN 15,040),
  `de-glazen-pastorie.md` (15,573w, +3.0% vs EN 15,117),
  `de-driekoningentaart.md` (16,897w, +5.6% vs EN 15,995) — all counts
  re-measured `wc -w` against the merged manuscripts and found identical
  to each NOTES.md; structure mirrors the de-papieren-sinaasappel / de-waag
  precedent; §7 queues EN-first sequencing, NL title ratification,
  native-speaker proofread (blocking), availability recheck, cover, price,
  and the publish click — the seat performed none of them.
- **Keyword-map C4 rows** (same commit): 28 NL keyword rows + 8 browse-node
  first-claims (the C4 inverted case, ×4 — EN packets concept-stage, share
  at graduation); full-map collision scan run FIRST per V057
  first-claim-wins — zero existing claims touched; one watched adjacency
  logged (`moordmysterie Engels dorp` vs De Waag's `moord in de gracht
  roman`, disjoint intent per the C2 pattern); the Terlouw/Oorlogswinter
  no-title-squatting etiquette applied (no "kerstverhaal"/"een
  kerstvertelling" keyword drafted).
- **Night-kiln packet un-staled** (same commit): §3 length-class and §5
  true-length lines no longer say "no manuscript exists" — Books 1–3
  complete on `main` (15,999w / 15,995w PR #145 / 23,334w PR #174), plus
  the verdict footer and §7 intro that restated the same stale park; the
  ⚑ owner-queued Book-2 length-band question referenced, not altered.
- **Queue + counts (the #166 remedy class, ONE regen on the union)**:
  `lint_owner_gates.py` OK 39/39; `derive_owner_queue.py` 39/39 clean —
  **19 decisions / 37 click-run sequences / 213 owner clicks (11
  hard-gated)**, up from 19/33/185 (7 hard-gated) at PR #179; counts-sync
  applied to `docs/current-state.md` and `docs/NEXT-SESSION.md` (incl. the
  vetting-packet tally 34 → 38) in the same commit.
- Heartbeat: one ORDER 011 owed-batch night-progress line appended to
  `control/status.md` (commit `0b866e6`); claim removed in the flip
  commit per convention.

## ⟲ Previous-session review

previous-session review: `.sessions/2026-07-14-night-v020-probe.md`
(ORDER 011 item 5, PR #179) — its protocol §2 discipline paid forward
directly: by recording verbatim WHY the fresh #175–#178 variants were not
probe-eligible ("no NL packets yet + un-graduated EN packets = not
click-ready"), it left this batch a precise spec of what was missing, and
its honest nit (owed work discoverable only by reading cards end to end)
is exactly the debt this batch existed to clear. Honest nit back: its 💡
(make the HARD-GATED annotation name the actual blocking row) got MORE
urgent tonight, not less — the fixed "(a D-item above blocks this
sequence)" suffix now mislabels 5 of the 11 hard-gated groups (the four
new NL sequences are gated by their blocking proofread checkbox, not by
any D-item), so the wording drift it predicted has gone from 1-of-7 to
5-of-11 in one regen.

## 💡 Session idea

💡 **Batch the four EN concept-packet graduations against the merged
union, one session.** Tonight inverted the catalog's usual shape four
times over: The Night Kiln, The Marmalade Post, The Glass Rectory, and
The Twelfth Cake all have complete EN manuscripts on `main` AND fully
vetted NL editions, while their EN packets remain concept-stage
(provisional blurbs, keywords "name-level only, NOT claimed", §3
reservations unretired). Each graduation is now decision-free lookup work
(manuscript measured, nodes already claimed by the NL edition to share
per C4, listing copy rewritable from finished text), and all four move
the same three surfaces (packet + map §1/§3 + OWNER-QUEUE regen) — so one
batched session against merged main, exactly like tonight's NL batch, is
cheaper and drift-free by construction versus four per-title regens.
Deduped against `.sessions/2026-07-1*.md` 💡 lines: the "concept-packet
graduation checker" idea proposes TOOLING to detect graduation debt (a
checker), not the batched execution of these four known graduations; the
night-book-variants 💡 batched the NL follow-throughs (consumed tonight);
no card proposes the EN graduation batch itself.

## Verification

- `python3 scripts/lint_owner_gates.py` — OK, 39/39 inputs clean.
- `python3 scripts/derive_owner_queue.py` — 39/39 clean, 0 manual-review
  rows; regenerated file committed same session (counts grep-verified
  from the generated file: 19 `^### D` decisions, 37 section-2 `###`
  sequences, 213 section-2 unchecked boxes).
- `python3 bootstrap.py check --strict` green at flip (the only prior
  finding was this card's own designed born-red HOLD).
- Claim `control/claims/2026-07-14-night-nl-packets.md` removed in the
  flip commit per convention.
