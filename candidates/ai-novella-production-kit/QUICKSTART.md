# Quickstart — your first production run in ~20 minutes

No build step, no dependencies. You are copying five templates and
adopting four habits. The goal of run #1 is a FINISHED manuscript in a
deliberately modest band — not your magnum opus.

## 1. Copy the templates

From `templates/` into your book's folder:

```
your-book/
  CANON.md            <- templates/CANON-template.md   (series bible; even standalones get one)
  PLAN.md             <- templates/chapter-plan.md     (band, chapters, promise manifest)
  DECISIONS.md        <- start empty; filled as you decide (chapter 1)
  RECOVERY.md         <- templates/recovery-checklist.md
  en/
    01-<chapter>.md   <- one file per chapter, or one file with chapter headings
vetting/
  your-book.md        <- templates/vetting-packet.md   (the publish gate, chapter 4)
versions/             <- created later, per edition (templates/edition-variant-matrix.md)
```

## 2. Pick the band BEFORE the first word (chapter 3)

Fill `PLAN.md`'s band line, e.g. **15,000–16,000 words, 12 chapters,
~1,300 words each**. The band is a contract: the production runs this
kit is distilled from landed manuscript after manuscript inside a
15k–16k band because the band was declared first and measured honestly
(`wc -w`, front matter included, stated as such) — and when a draft
missed the band, the fix was an *aimed* pass (cut density, expand the
thinnest promised beat), never silent re-planning.

## 3. Write the promise manifest before drafting (chapter 1)

In `PLAN.md`, two lists:

- **Required-present:** the exact phrases your pitch/blurb promises
  ("the sale papers signed," "no appeals") — each must appear in the
  finished text; verify by search, not memory.
- **Banned-absent:** the registers this book must NOT drift into
  (crime stems in a warm holiday book; another series' vocabulary) —
  each must appear zero times.

Run both greps at the end of the draft AND after every revision pass.
This is the cheapest quality gate in the kit and the production runs
caught real defects with it.

## 4. Draft in one deliberate arc (chapter 1)

Chapter brief → full draft straight through → one aimed repair pass →
measure → record. After each work block, fill one `DECISIONS.md`
bullet: what you decided, what you measured, what you cut. If your
session/tool dies mid-draft, `RECOVERY.md` (chapter 5) is the path
back — the worked case went from zero words pushed to a merged
15,995-word manuscript because the state was recoverable by design.

## 5. Gate it before you call it done (chapter 4)

Copy `templates/vetting-packet.md`, work it top to bottom: title +
collision scan → market + length class → price band → packaging →
listing copy → the publish-click checklist. A manuscript that hasn't
passed the packet is *written*, not *publishable* — keep the two words
separate and the gate stays honest.

## 6. Only then: book N+1 (chapters 2 and 7)

Update `CANON.md` in the same sitting the book is finished (laws
byte-exact, hooks with coordinates). Then read chapter 7 before
starting the sequel: the kill rules exist because "write the next one"
is always more fun than checking whether anyone bought the last one.

## Optional hardening

- Keep the book in git; commit at every chapter boundary and push
  after every commit — the recovery chapter's worked case turns on
  exactly this habit.
- Derive editions (novella cut, serial, translation, large print)
  only from the base manuscript, never from another edition —
  chapter 3's one rule of variants.
