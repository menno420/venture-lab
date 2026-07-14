# Session — Night run: the four owed NL-edition follow-throughs, one batch (ORDER 011 items 2/4/7 follow-through)

> **Status:** in-progress

- **📊 Model:** Fable · worker slice · coordinator-authorized night batch (ORDER 011)
- **started (date -u):** Tue Jul 14 00:54:37 UTC 2026
- **branch:** `claude/night-nl-packets`
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
