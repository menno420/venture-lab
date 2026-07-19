# Self-Edit / Proofreading Pass — *The Mirror City* (Lull · Book Two)

> **Status:** `draft`
>
> Record of a genuine proofreading read across all 12 chapters (`book2/ch01.md`–
> `ch12.md`) made while compiling `MANUSCRIPT-KDP.md`. The canonical source
> chapter files were **not modified**; every change below was applied only to the
> compiled KDP file. This is an editorial aid, not a substitute for a
> professional proofread (see the closing caveat).

---

## (a) Mechanical fixes APPLIED (to the compiled `MANUSCRIPT-KDP.md` only)

**Mechanical typos found: ZERO.** A full read plus programmatic checks across all
12 chapters found no spelling errors, no doubled words, no double spaces, no
trailing whitespace, and no stray tabs. The prose is clean and internally
consistent (British spellings — *colour, centimetre, neighbourhood, metre* —
throughout; straight quotes/apostrophes throughout, which matches the house style
of the KDP exemplar `the-paper-orange.md`). Nothing was "corrected," because there
was nothing to correct.

- **Checked and deliberately NOT changed:** `ch09` — *"so nobody ever gets to tell
  you you did it for a bad reason."* The doubled **"you you"** is grammatically
  correct (object of *tell* + subject of the subordinate clause: *tell you [that]
  you did it*). Left as written.

**One structural normalization APPLIED (not a typo fix):** each source chapter
opened with a draft marker line — `*Lull, Book Two · draft*` — on line 3, under the
chapter heading. All **12** of these draft sublines (and their trailing blank line)
were removed from the compiled manuscript, because a published KDP edition should
not carry an internal "draft" marker, and the compiled front-matter page now
carries the title/series/subtitle instead. This is a documented KDP-build decision
(prep source-pack §3, Book D build note: *"drop the sublines for KDP"*). Chapter
**bodies were preserved byte-for-byte** — verified by diffing each source chapter
(with only its subline removed) against the compiled output: identical.

---

## (b) Continuity & consistency questions FLAGGED (not auto-fixed)

Raised for author/owner judgement; none were changed in the manuscript.

**1. ⚑ Genre-scoping mismatch (required flag).** The manuscript is unambiguously a
fast, cliff-ended **middle-grade / YA portal-fantasy adventure** in the
Percy-Jackson register (dream-walkers, two secret factions, a magic-adjacent
apprenticeship in Venice, real peril, a 12-year-old first-person narrator). The
book's own `book2-listing.md` is scoped correctly for this. **However**, the
series' reservation row in `docs/publishing/keyword-map.md` §3 scopes "Lull" as a
*"Quiet/literary novella — stillness, small-town hush"* — which **does not match**
the actual content, and its drafted keywords (`middle grade fantasy`, `portal
fantasy`, `Percy Jackson readalike`, `Venice fantasy`) contradict that literary
scoping. All metadata in `KDP-METADATA.md` follows the manuscript (MG
portal-fantasy), not the §3 register. **This mismatch must be reconciled**
(re-scope the §3 row, or resolve the possible "Lull" title collision) before any
keyword is claimed as a §1 ownership row. Owner / keyword-map follow-up.

**2. Character names vs `bible/names.md`.** The core in-world name set is used
consistently and matches the bible's recommended set: **the Palimpsest** (faction),
**Vivid** (elite tier), **Anchoring** (big-mass ability), **the Lull** (perception
filter), **the Vigil** (keeper faction); the *Sleeper → Waker → Vivid* ladder and
the *darn / darner / darning* craft verb are all used consistently. Terms that
appear in Book 2 but are **not defined in `bible/names.md`** (verify they match Book
1 / `world.md` usage, since names.md only covers the four "blank" picks + the
Vigil):
   - **"The First Draft"** — the Palimpsest's leader / master entity (the
     many-voiced "weight"), central to ch06–ch10. Internally consistent here;
     confirm it is the established Book-1 term.
   - **"Scrivener(s)"** — the Palimpsest's grey-coated agents (ch06, ch08). Confirm
     against Book 1.
   - **"snag"** — the in-world word for a loud/undreamt dreamer like Sam. Consistent
     use; confirm it's the Book-1 term.
   - **Fenna's surname "Bakker"** — appears exactly once (ch09, *"Fenna Bakker"*) and
     is not in the bible. Confirm it matches Book 1.

**3. Timeline / age (checked — consistent, noted for confirmation).** Sam is
*"twelve years and one day old"* at the open (ch01), with six years of nightmares
dating to *"the night I turned six."* The withheld **date** is his thirteenth
birthday (per `series-arc.md` / Book 3), i.e. roughly a year ahead — consistent with
Wessel expecting the factions to circle *"months, maybe a year"* (ch12) and with
ch12's *"Twelve years old."* No contradiction found; flagged only so a copyeditor
knows the age math is intentional.

**4. Serafina's "four hundred years" vs "forty years" of grief (checked —
INTENTIONAL, do not "fix").** In ch04 Serafina calls the forbidden mirror *"four
hundred years of my grief,"* but in ch10 she explicitly retracts this: *"That's the
lie I tell… it isn't four hundred years old, my grief, it's forty. That mirror is
your father's."* The earlier line is a deliberate in-story deflection, resolved
on-page. This is **not** a continuity error — flagged so a proofreader doesn't
"reconcile" the numbers and break the reveal.

**5. Two distinct mirrors (checked — kept distinct, noted).** The **1630-plague
mirror** (a cloudy oval; the heist door; cracks corner-to-corner in ch09) is a
different object from the **forbidden floor-to-ceiling mirror** (Joris's / Pompeii,
covered until ch11, shipped to Amsterdam in ch12). ch07 is explicit: *"not the
forbidden one; a different one, an old cloudy oval."* Consistent; flagged only
because the two are easy to conflate on a fast read.

**6. World-rule consistency (checked — consistent).** The Venice tell-inversion (a
*late* reflection = awake; a *true/smooth* mirror = the trap) is established (ch03)
and paid off (ch05, ch10); Anchoring-vs-pulling (ch04 → ch09) and the backwash-cost
escalation (father's face in Book 1 → mother's face in ch09) all hold together and
match `outline.md` / `series-arc.md`. No issues.

---

## (c) Caveat

**This pass does NOT replace a professional proofread.** It is a single careful
editorial read by the compiling worker, aimed at (i) applying only safe, logged
mechanical/structural changes and (ii) surfacing continuity questions for the
author. It has not been checked by a native-speaker proofreader or a line editor,
and the current `OWNER-START-HERE` guidance keeps the whole book catalogue
hard-gated on exactly such a native-speaker proofread pass before publish. A
professional proofread remains a required pre-publish step.
