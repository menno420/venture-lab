# The Slow Word — versions

Derived editions of the canonical EN master text ([`../en/`](../en/), ~29,400
words across 12 chapters). Convention per the 2026-07-13 night ORDER's BOOKS
clause ("multiple versions of each — different angles, audiences, lengths —
versions are cheap once the research exists").

## Convention

- **One subdirectory per version.** Each version dir contains its manuscript
  (or, for spec-only versions, a production spec) plus a `NOTES.md`.
- **`NOTES.md` is mandatory and honest:** it states exactly what changed
  versus the canonical `en/` text, at scene level where text was cut, and
  carries a real `wc -w` output for any manuscript it ships — no rounded
  aspirational counts.
- **`en/` stays master.** Versions never edit `en/`; fixes to the story
  itself land in `en/` first, then propagate.
- **Publishing stays owner-gated** for every version, exactly as for the
  master text — see the hard rail in `docs/conventions.md` §13 and the
  existing the-slow-word vetting path under `docs/publishing/`.

## Current versions

| Version | Dir | What it is | Words |
|---------|-----|------------|-------|
| Novella cut | [`novella-cut/`](novella-cut/) | Complete abridged manuscript, self-contained arc, novella-ebook market position | see its `NOTES.md` (`wc -w`) |
| Large print | [`large-print/`](large-print/) | Production spec for a large-print paperback of the FULL novel — spec only, no new manuscript | n/a (uses `en/` text) |
