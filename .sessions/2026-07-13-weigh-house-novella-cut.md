# 2026-07-13 — Night run: The Weigh House novella cut (BOOKS lane, versions slice)

> **Status:** `complete`

Started 2026-07-13T01:09:44Z · closed 2026-07-13T01:58Z (`date -u`).
**Run under ORDER 008** (control/inbox.md, 2026-07-13T00:46:54Z — owner
night-run DIRECT ORDER; seat clause 1: "BOOKS: multiple new book ideas AND
multiple versions of each (different angles, audiences, lengths) — versions
are cheap once the research exists"): this slice delivers a VERSION of an
existing finished manuscript — a complete novella-cut abridgement of
**The Weigh House** (36,434-word Amsterdam police procedural).

## Outcome

- `candidates/adult-novels/the-weigh-house/versions/README.md` — versions
  convention (one subdir per version, manuscript + honest-`wc` NOTES.md);
  verified compatible with the slow-word sibling's convention that landed
  on main mid-run (PR merged at `d01dacd`-era HEAD).
- `versions/novella-cut/the-weigh-house-novella.md` — **complete abridged
  manuscript, 18,984 words** (`wc -w`, honest count), 16 chapters, finished
  prose only, self-contained arc, no placeholders.
- `versions/novella-cut/NOTES.md` — scene-level cut list with reasons,
  **clue-chain audit table** (every resolution clue → where planted in the
  cut; result: airtight, no resolution element relies on cut material),
  continuity smoothing log (4 master inconsistencies resolved: houseboat
  vs flat, lead-block counts, half-hitch naming, evidence-securing timing;
  1 fair-play plant added: the comms backup SD card now planted in Ch13),
  market position (crime novella ebook $3.99–$5.99 band per
  docs/publishing/CHECKLIST.md §4; suggested $3.99 for this shorter
  edition; base case ≈ $0, honest null), and the ⚑ owner gate.
- Positioning check: read `docs/publishing/vetting/the-weigh-house.md`
  before cutting; the novella keeps the master's title page line ("An
  Amsterdam crime novel"), content note verbatim, and contradicts nothing
  in the packet; the pending D2 subtitle decision ("An Amsterdam Crime
  Novel") is untouched and one new owner sub-decision (edition strategy)
  is flagged in NOTES.md, routed through the existing §7 OWNER-GATE.
- No spend, no accounts, no publishing; control/status.md, outbox, inbox,
  workflows untouched.

## 💡 Session idea
💡 **Clue-chain audit as a reusable NOTES.md section.** The cut-list +
"each resolution clue → where planted" table turned out to be the whole
quality gate for abridging a procedural — it caught the master's own
unplanted SD-card reveal and the dangling poste-restante thread. Making
that table a named convention in versions/README.md (required for any
`*-cut` version of a mystery/procedural, optional elsewhere) would let the
next versions session audit mechanically instead of re-deriving the method.

## Previous-session review
previous-session review: `.sessions/2026-07-13-night-book-idea-packets.md`
(PR #105) — genuinely strong: its six concept packets explicitly "queued
versions-of-each as the natural next slice," and this session plus the
sibling versions PRs (slow-word, ultramarine, large-print bundle) executed
exactly that handoff same-night, which is the packet-to-versions pipeline
working as designed; honest nit: its 💡 (concept-packet graduation checker)
is still unbuilt, and tonight's versions wave widens the same unchecked
surface — versions dirs now exist that no script cross-references against
vetting packets.

## Model
- **📊 Model:** fable-5 · worker · BOOKS lane, night run
