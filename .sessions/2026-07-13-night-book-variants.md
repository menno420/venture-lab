# Session — Night run: book catalog edition variants — large-print specs, 8-title bundle (ORDER 011 item 2, BOOKS lane)

> **Status:** `complete`

- **📊 Model:** fable-5 · worker slice · ORDER 011 item 2 (edition variants, night run)
- **started (date -u):** Mon Jul 13 23:13:07 UTC 2026
- **closed (date -u):** Tue Jul 14 00:20 UTC 2026
- **branch:** `claude/night-book-variants` — anchor PR (#172) of the slice; the
  four NL editions are sibling branches of this card
  (`claude/night-book-variants-2` through `-5`), each opened and merged as its
  own PR tonight while this anchor stayed born-red.
- **session:** Run under ORDER 011 item 2 (control/inbox.md: "New book titles
  + edition variants — EN adult catalog (11 manuscripts) still has unexecuted
  variants; versions are cheap per ORDER 008 item 1"). This slice writes
  LARGE-PRINT EDITION SPECS (production spec docs only, no new manuscripts)
  for the eight coordinator-assigned adult manuscripts with no large-print
  coverage — *The Glass Rectory*, *The Marmalade Post*, *The Night Kiln*
  (Book One), *The Morning Door* (Night Kiln Book Two, specced AS WRITTEN at
  its honest 15,995 words — the ⚑ owner length-band question in
  `the-night-kiln/DECISIONS.md` is not touched), *The Paper Orange*, *The
  Salvage Orchard*, *The Seed Catalogue Courtship*, *The Twelfth Cake* — as
  `versions/large-print*/EDITION-SPEC.md` per manuscript, mirroring the
  merged the-slow-word spec (PR #111) and the 2026-07-13 4-title bundle
  (`.sessions/2026-07-13-large-print-spec-bundle.md`), plus a
  `versions/README.md` index per touched title.
- **walls:** `docs/publishing/**` (vetting packets, keyword-map, OWNER-QUEUE)
  deliberately untouched — that surface is held by the concurrent
  night-product-slice session; the packet/C4/queue follow-through for these
  editions is recorded as owed. No edits to manuscripts, `control/inbox.md`,
  `control/outbox.md`, workflows, or triggers; no publish, spend, or external
  action. (One coordinator-authorized exception executed at flip: the single
  ORDER 011 item 2 night-progress line in `control/status.md`.)

## Results (as landed)

- **8 large-print EDITION-SPECs** (anchor #172, commit `e7eb57f`), one per
  uncovered adult manuscript: `the-glass-rectory`, `the-marmalade-post`,
  `the-night-kiln` (`large-print/` Book One + `large-print-book-2/` *The
  Morning Door*, specced AS WRITTEN, ⚑ length-band question untouched),
  `the-paper-orange`, `the-salvage-orchard`, `the-seed-catalogue-courtship`,
  `the-twelfth-cake` — each `versions/large-print*/EDITION-SPEC.md` with
  measured `wc -w` source counts, 6×9 16pt+ trim/typography, page estimate,
  and KDP cost/royalty math per the PR #111 convention.
- **7 `versions/README.md` indexes** created/extended in the anchor; the
  night-kiln and marmalade-post indexes were union-merged with their `nl/`
  rows at merge `7732bb7`; the glass-rectory and twelfth-cake `nl/` rows
  added at flip (commit `19c244c`) once #177/#178 merged with measured
  counts.
- **4 complete NL editions merged tonight on this card's sibling branches**
  (each a full literary translation, all 12 chapters, finished prose, own
  NOTES.md with honest counts): *De Nachtoven* 16,840w (PR #175, branch
  `-2`), *De Marmeladepost* 15,637w (PR #176, branch `-3`), *De glazen
  pastorie* 15,573w (PR #177, branch `-4`), *De Driekoningentaart* 16,897w
  (PR #178, branch `-5`). All counts re-verified by `wc -w` on the merged
  files from main before the index rows were written.
- Heartbeat: one night-progress line for item 2 appended to
  `control/status.md` (commit `30e4b8c`), dated, stating only what this
  slice did — per the night-verdicts card's aging-progress-lines nit.
- **Deliberately deferred (owed):** the 4 NL vetting packets, their
  keyword-map C4 rows, and the OWNER-QUEUE regen — `docs/publishing/**` was
  held tonight by the item-1 session; owed to a follow-up session (see 💡).

## ⟲ Previous-session review

previous-session review: `.sessions/2026-07-13-night-verdicts.md` (ORDER 011
item 4, PR #173) — its minimal-diff decide-and-flag discipline (apply the
ruling where the verdict's own `target:` points, refuse the mass edit that
would force an OWNER-QUEUE regen) is the same shape this slice used for its
docs/publishing wall, and its honest nit about per-item progress lines aging
fast was consumed directly: this card's heartbeat line states only what this
slice did, dated, with the deferral named instead of implied. Honest nit: its
verdicts-ledger 💡 adds a fourth proposed advisory checker to a lane whose
unbuilt-💡 backlog is itself already flagged as compounding — the ledger idea
is good, but it will need the sweep it implicitly assumes.

## 💡 Session idea

💡 **Batch the four owed NL follow-throughs into ONE session against the
merged union.** Tonight left four NL editions (#175–#178) each owing the same
three artifacts: an NL vetting packet, keyword-map C4 rows, and an
OWNER-QUEUE regen. Running those as four per-title sessions means four
queue regens against four different packet sets — exactly the
counts-drift/merge-conflict class PR #166 had to remedy and the
night-membership-ready review predicted ("every subsequent packet session
regenerates OWNER-QUEUE from a different packet set"). One follow-up session
against merged main writes all four packets, adds all C4 rows in one
keyword-map edit, and runs `derive_owner_queue.py` ONCE on the union —
cheaper by construction and drift-free by construction. Deduped against
`.sessions/2026-07-1*.md` 💡 lines: the ledger/checker/glossary ideas are
tooling; nl-editions-vetting's shared-click hoisting is queue mechanics for
packets that already exist; no existing card proposes batching owed
follow-through work by shared regen surface.

## Verification

- `python3 bootstrap.py check --strict --session-log
  .sessions/2026-07-13-night-book-variants.md` and bare
  `python3 bootstrap.py check --strict` both green at flip (outputs in the
  session report).
- Claim `control/claims/2026-07-13-night-book-variants.md` removed in the
  flip commit per convention.
