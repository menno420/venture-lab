# 2. The series bible: CANON.md

## Why a one-page bible beats a reread

Book N+1's real cost is not writing — it is *recovering canon*: what
were the rules, who is everyone, what did book N promise? Without a
bible that recovery is a full reread (hours, and lossy: you re-derive
the rules from instances and get them subtly wrong). The production
convention: every series — and every standalone that might grow —
carries a one-page `CANON.md`, updated **in the same change that lands
each book**, so canon recovery for the next book is an O(1) lookup.

## The five sections that earn their place

The production CANON files converged on this anatomy (the template in
`templates/CANON-template.md` mirrors it):

1. **Laws — byte-exact.** The series' load-bearing rules, quoted
   verbatim from the page, not paraphrased. If a rule is series text
   (a ferry that runs on the law "Always count the passengers twice"
   — one of three such laws in the production example), the bible
   carries the exact wording, because a paraphrase WILL drift and the
   drifted version will get written into book N+1.
2. **Mechanics.** How the world's machinery actually behaves —
   documented as behavior ("the box is the fog's ear"), with chapter
   coordinates for where each mechanic was established.
3. **Geography / setting facts.** Named places with the small
   concrete details that recur (how many jetties, which clock runs 11
   minutes fast) — the details readers notice when book N+1 gets them
   wrong.
4. **Cast.** Names, ages, roles, and the *constraints* on each
   character — including negative constraints. The production example
   carries one that a paraphrasing bible would lose entirely: a
   captain who is "never given a pronoun on the page (deliberate;
   hold this line series-wide)."
5. **Open hooks — planted → for future books.** Every deliberate
   loose end, WITH the coordinate where it was planted ("ch. 13") and
   what was promised about when it pays off. Hooks without
   coordinates rot into vague obligations; hooks with coordinates are
   a sequel outline you already wrote.

## The update discipline

The bible is updated in the same sitting/PR as the book that changes
it — never "later." A bible that trails its books by one volume is
worse than none: it authoritatively states stale canon. For
multi-file bibles (a longer work in the production catalog splits
into `bible/characters.md`, `bible/world.md`, `bible/style.md`), the
same rule applies per file, and the base manuscript remains the story
canon's source of truth — the bible is the index, not the master
(chapter 3 applies the same rule to editions).

## Honesty block

A bible is only as good as its byte-exactness. The convention's real
cost is the discipline of quoting rather than paraphrasing, and of
writing the update while the book is still in your head. The
production evidence is one lane's usage across a 16-manuscript
catalog with multi-book series in flight; no external writing team
has run these exact templates.

---

**Sources:** `candidates/middle-grade/the-halfway-ferry/CANON.md@abf1f23`
(the worked one-page bible: byte-exact laws, mechanics with chapter
coordinates, cast constraints incl. the pronoun line, open hooks with
plant locations; quotes above are single lines from that committed
file, shown for shape) ·
`candidates/adult-novels/ultramarine/bible/characters.md@873d5d9`
(multi-file bible variant: characters/world/style split) ·
`candidates/adult-novels/ultramarine/versions/README.md@873d5d9`
(base manuscript = source of truth for canon; editions never silently
change it).
