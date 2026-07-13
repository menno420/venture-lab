# 1. The one-session method

## The problem this chapter solves

AI assistants produce excellent *starts*. The failure mode is never
"the prose is bad"; it is that nothing forces the middle and the end
into existence, so the project dies at 2,000 promising words. The
production lane this kit is distilled from shipped 16 complete
manuscripts by treating a book as one deliberate arc with declared
constraints, not an open-ended writing project.

## The unit of work: one book, one arc, one record

Each title lives in its own folder with a fixed anatomy:

```
the-book/
  DECISIONS.md      <- every decision + measurement, written as made
  CANON.md          <- series bible (chapter 2); standalones get one too
  en/               <- the manuscript: one file, or one file per chapter
  versions/         <- derived editions only (chapter 3)
```

Manuscript files use a boring, uniform shape: front matter (title
page, subtitle, content note), `# Chapter N — Name` headings, `⁂`
scene breaks, and an explicit `THE END`. Twelve chapters is the
production default for the ~15k band — long enough for a real arc,
short enough that each chapter has a one-line job you can brief.
Longer works split one-file-per-chapter (`01-the-last-watch.md` …
`12-the-answering.md`) so a single chapter is a single editable,
countable unit.

## Honest counts, single source of length

Word counts are `wc -w` outputs, stated with their measurement basis
("includes front matter and chapter headings"), recorded in
`DECISIONS.md` and cited everywhere else FROM there. The discipline
that matters: when the plan says one length and the delivery is
another, you amend the plan document in the same change and flag the
delta in every surface that repeated it — never let two documents
disagree about how long the book is. A real production example: a
holiday novella was planned at ~20k–30k, delivered at an honest
15,995, and the plan's §3 was amended in the same PR with the delta
flagged three places, expansion recorded as *possibility only*.

## The promise manifest

Before drafting, extract two grep-able lists from your own pitch and
blurb:

- **Required-present** — the promises, verbatim: named phrases, the
  climax image, the subtitle. Each must be findable in the finished
  text (count them).
- **Banned-absent** — register fences: vocabulary this book must not
  contain, because it belongs to another book, another genre pole, or
  an iconography you're deliberately avoiding. Each must hit zero.

Verify mechanically at draft end and after every revision pass, in
BOTH directions. This is cheap and it works: the production run that
originated the banned list caught a stray "alibis" and a "dreading" in
a warm no-crime holiday book — words no human reread had flagged.

## The repair pass is aimed, or it is padding

One full draft straight through, then ONE aimed pass. Aimed means: at
the beats your promise manifest and blurb say matter most, where the
draft is thinnest — not wherever expansion is easiest. The direction
can be negative: the 15,995-word example above came from a 17,599-word
draft, tightened by ~1,750 words of ornamental density with promised
beats untouched. Measure before and after; record the delta and where
it went in `DECISIONS.md`.

## Honesty block — what the method does and doesn't transfer

The production runs behind this kit were executed by coordinated
coding-agent sessions: briefs held in files, commits at chapter
boundaries, a CI gate refusing to merge unfinished work. If you are
one person with one chat window, the *structure* transfers fully
(bands, briefs, manifests, the aimed pass, the decisions record); the
*enforcement* does not — nothing will stop you skipping your own gate.
The templates make the honest path the easy path; they cannot make it
the only path.

---

**Sources:** `candidates/adult-novels/the-twelfth-cake/DECISIONS.md@3b159d9`
(promise manifest with both-directions grep counts, banned-stem
catches, 17,599→15,995 aimed tightening pass, single-source-of-length
amendment) · `candidates/adult-novels/the-slow-word/en/README.md@873d5d9`
(12-chapter one-file-per-chapter structure, front-matter shape,
content note) · `docs/publishing/vetting/the-twelfth-cake.md@3b159d9`
(§3 length amendment recorded plan-side) — word count cited to the
merging PR (#159, squash `3b159d9`), measured `wc -w` 15,995.
