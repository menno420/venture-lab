# Versions convention — children's books track

> **Status:** `reference` — seeded 2026-07-13 with the first board-book cuts (ORDER 008 "multiple versions of each").

How a title grows versions beyond its base picture-book manuscripts (`<slug>.{en,nl,de}.md` flat in the title folder):

- **One subdir per version** under `candidates/childrens-books/<title>/versions/<version-name>/` (e.g. `versions/board-book/`). Files named `<slug>.<version>.{en,nl,de}.md`.
- **Multi-book titles** name the book in the filename — `<slug>-<book-number>.<version>.<lang>.md` — with one shared `NOTES.md` per version dir carrying a per-book count table.
- **`NOTES.md` is required** in every version dir: honest `wc -w` per language (state the exact count command), what was kept vs dropped against the source manuscript, and the version's format/fulfillment ⚑ OWNER items.
- **Honest word counts, always** — real `wc -w` output, never estimates. If a count misses a stated target, the miss is recorded, not rounded.
- **A version is a standalone work**, not a summary: it must read complete on its own for its audience. NL/DE are native-quality parallel versions on the same spread grid, not literal translations of the EN cut.
- **Owner gates carry over:** illustration, layout, print, ISBN, pricing, and distribution stay parked/⚑ OWNER exactly as for base manuscripts.
