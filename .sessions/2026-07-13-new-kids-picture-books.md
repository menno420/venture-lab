# 2026-07-13 — New kids picture books: The Windmill Mouse + The Puddle Museum, first complete trilingual manuscripts

> **Status:** `complete`

- **📊 Model:** fable-5 · worker slice · BOOKS lane, 2026-07-13 night run
- **Started:** 2026-07-13T01:58:16Z (`date -u`)
- **Closed:** 2026-07-13T02:09:30Z (`date -u`)
- **⚑ Order basis:** run under **ORDER 008** (owner night-run DIRECT ORDER, carried verbatim in `control/inbox.md`, verified present at origin/main `873d5d9` before the born-red commit) — BOOKS clause: "BOOKS: multiple new book ideas AND multiple versions of each (different angles, audiences, lengths) — versions are cheap once the research exists." Not self-initiated.

**What landed:** the FIRST COMPLETE picture-book texts for the two kids concepts vetted tonight in PR #105, trilingual EN/NL/DE, mirroring the `painted-stones` file/front-matter convention (13 spreads, one italic art-direction note per spread, honest body `wc -w` in front matter):

1. `candidates/childrens-books/the-windmill-mouse/` — **The Windmill Mouse / Het Molenmuisje / Die Mühlenmaus** (ages 3–6). Body word counts: EN **581**, NL **585**, DE **577**. Heroine anglicized EN Millie / NL Mies (packet name) / DE Minna. Packet's Moderate-collision differentiator honored: zero "old Amsterdam" phrasing in any language, no clogs, no song-adjacent rhyme; no "bedtime" phrasing per the kids-cluster rule. `DECISIONS.md` records premise fidelity, localization, and the ⚑ §5 illustration + §7 publish owner-gates (packet and seat recommend Park).
2. `candidates/childrens-books/the-puddle-museum/` — **The Puddle Museum / Het Regenplassenmuseum / Das Pfützenmuseum** (ages 4–8). Body word counts: EN **584**, NL **587**, DE **578**. NL title deliberately non-literal ("Het Plassenmuseum" reads as the peeing museum in Dutch); all three packet exhibits + whale treasure + "the best kind" answer delivered verbatim-faithful. `DECISIONS.md` carries the packet's reflection-heavy AI-art risk flag forward (worst catalog candidate for a cheap AI pilot) plus the ⚑ owner-gates.

Illustration stays parked (text-only lane; art notes are direction, not generation); every publish click stays a queued owner action per each packet's §7. No `docs/publishing/**`, control ledgers, workflows, or triggers touched.

## previous-session review

Previous BOOKS-lane session (`.sessions/2026-07-13-slow-word-novella-cut.md`, PR landed as part of tonight's run): its budget-first-abridgment lesson — compute per-chapter word targets BEFORE writing and `wc -w` as you go — was applied here as spread-level budgeting (~45 words/spread against a 550–650 body target), and all six manuscripts landed inside the band on the first count, no trim pass needed. Its honest-`wc` discipline (commit the measured number, not the aspirational one) is reproduced in every front-matter count here.

## 💡 Session idea

Title-collision checks are run for English only, but localization creates NEW collisions vetting never sees: bare NL "Het Plassenmuseem/Plassenmuseum" would have shipped a pee joke as a title — caught here only because the translator happened to be paying attention. Cheap guard: add a "per-language title drift" row to the vetting CHECKLIST (one line per target language: homophone/vulgarity/autocorrect check on the *translated* title), so the trilingual pipeline vets all three shelf-facing titles, not just the master.

## Work log

1. Premise check at origin/main `873d5d9`: neither `candidates/childrens-books/the-windmill-mouse/` nor `the-puddle-museum/` exists; only live claim (`2026-07-13-order-night-run.md`) covers `control/inbox.md`, not these paths.
2. Born-red card + claim `control/claims/claude-new-kids-picture-books.md` (`180c6fd`), pushed before content work.
3. Read both vetting packets in full; studied `painted-stones` (all three languages + DECISIONS.md) as the convention master.
4. The Windmill Mouse EN/NL/DE + DECISIONS.md (`c2df4fd`).
5. The Puddle Museum EN/NL/DE + DECISIONS.md (`c5bec18`).
6. `python3 bootstrap.py check --strict`: only findings are this card's designed born-red hold + its missing close-out markers — both resolved by this flip commit. Claim file deleted in this same commit.
