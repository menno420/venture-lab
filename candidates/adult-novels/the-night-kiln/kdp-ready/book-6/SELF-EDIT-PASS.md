# Self-Edit Pass — The Summer Ember (The Night Kiln, Book Six)

> A genuine proofreading read of the full manuscript
> (`candidates/adult-novels/the-night-kiln/en/the-summer-ember.md`, ~15,660 words,
> 12 chapters) made while building the KDP package. Line numbers below refer to
> the **canonical source** `en/the-summer-ember.md` (the KDP manuscript adds 33
> lines of front matter, so its body line numbers = source + 33).
>
> **⚠ This pass does NOT replace a professional native-speaker proofread.** It
> is a build-time editorial read by the packaging worker, not a copy-edit of
> record. A human proofreader should still pass the finished text before
> publication — this is the series hard-gate.

## (a) Mechanical fixes — APPLIED

**None at package time. Zero mechanical corrections were needed, and none were
made here.** The manuscript body is preserved **byte-for-byte** in
`MANUSCRIPT-KDP.md` (verified by diff against source lines 13–307 — identical). No
`sed` fix step was run.

Checked and found clean across the whole text:

- **Doubled words** (`the the`, `and and`, etc.) — none (regex scan, zero hits).
- **Double spaces / spacing before punctuation** — none (zero of each).
- **Common misspellings** (recieve, seperate, definately, occured, thier, untill, begining, …) — none.
- **Quote / apostrophe consistency** — consistent straight ASCII quotes (U+0022) and apostrophes (U+0027) throughout; **zero** curly/smart quotes (verified). House style for the series; deliberately left as-is, since it is uniform.
- **Dashes** — consistent em-dashes (U+2014, 195 of them); no hyphen-as-dash (` - `) anywhere.
- **Scene breaks** — seven `⁂` marks, consistent with the series glyph.
- **Byte-locked refrain** — the five inherited catechism lines are **byte-identical** to their form in `the-spring-cup.md` (copied verbatim, not retyped); the new sixth line appears byte-identical at all three of its occurrences (ch. 7 draft, ch. 10 firing, ch. 12 recital). The rule-sentence opening (first sentence) is byte-identical to Books 1–5.

This is an unusually clean manuscript; the honest result is that there was
nothing mechanical to fix at packaging time.

## (b) Continuity questions — FLAGGED, not auto-fixed

These are editorial questions for the author/owner. As Book 6 the manuscript was
read specifically for consistency with Books 1–5; the threads it picks up (see the
positive checks below) are consistent, with the following notes.

### B1. Glaze chemistry — Book 6 deliberately avoids Book 5's flagged celadon/reduction issue (author's eye welcome)

Book 5's self-edit (`kdp-ready/book-5/SELF-EDIT-PASS.md` B1) flagged that *The
Spring Cup* four times describes a red/red-brown result from an **iron celadon
under reduction**, which contradicts Books 1 & 4 (where iron celadon + reduction =
**winter-glass blue**) and real practice. Book 6's **new** vessels — the old
Stonebeck pot (src L129) and the new far-bank pot (src L245) — are deliberately
described instead as *"the … breathing brown of an old wood-ash over iron"*, which
is chemically consistent (wood-ash/iron in oxidation reads warm brown/amber) and
sidesteps the Book-5 contradiction entirely. The one place Book 6 uses the Book-5
phrase — *"the small footed wedding cup, red as an iron celadon gone rich under a
good reduction"* (src L33) — is a **deliberate callback** to Book 5's existing cup
on the shelf, carrying that book's own (separately flagged) wording forward
verbatim, **not** a new independent glaze claim. **Question for the author:** if
Book 5's celadon wording is ever revised, the single L33 callback here should be
revised in lockstep; the two new Book-6 vessels need no change.

### B2. Internal timeline anchors (confirmed consistent; noted for the copy-editor)

The book pins its far-side history on two intervals, kept internally consistent:
the far fire / bridge / Sabra's death are **"thirty years and more"** ago
(matching the Book-5→6 hook in `series-arc.md`), while the *memory* Sabra kept —
the midsummer bridge night with young Ilsabet — is **"fifty years"** old (a memory
older than the pot that holds it: fired ~30 yrs ago, of a night ~50 yrs past; the
give-back calls it *"thirty-years-fresh and fifty-years-young,"* src ~L227). Old
Tam's ages track this (a boy at Sabra's knee ~60 yrs ago when the fire burned; a
grown man when it went cold ~30 yrs ago). **No inconsistency found**; flagged only
so a copy-editor can confirm the intended intervals. Note this book does **not**
depend on Book 5's own latent "Nesta at nineteen vs. died at eighty-one" gap (that
is a Book-5 question, untouched here) — Book 6 leaves Nesta's exact age at the
receiving of the pot unstated on purpose.

### B3. Two kilns / two catechisms — new series geography (owner note, not a fix)

Book 6 introduces a **second kiln** (the relit Stonebeck hearth) and refers to
**"the far-side words"** of the catechism (a Stonebeck rendering Sabra taught Old
Tam), distinct from the Wenholt catechism whose six English lines are byte-locked.
The far-side words are never quoted (only the Wenholt catechism is spoken), so no
new byte-locked text is created. **Owner note:** if the series ever renders the
far-side catechism on the page (e.g. a Book 7), it becomes a *new* byte-locked
artifact to hold consistent — track it the way the Wenholt six lines are tracked.

### Positive continuity checks (verified consistent with Books 1–5 — no action needed)

- **Perrin Loft**, made a witch at Wintermark (*The Winter Wheel*) and co-witch in *The Spring Cup* ("these three months," spring), is here "a witch of Wenholt half a year and more" (summer) — consistent; still seventeen.
- **Griet** (memory loss; the two lamps at the ferry — the porridge bowl and the mended dish) gets her one clear-evening beat and blesses the fire's crossing; she *counts* the far hill's new light — no living memory-loss is touched by fire (series border held).
- The **private shelf** callbacks — Sorrel's honey-jar lid ajar (Bk 2), the race-dish's empty board / lamp at the ferry (Bk 3), Ilsabet's first-pot board returned to clay (Bk 4), and **the stilled wedding cup** at the far end (Bk 5, heard/given-back) — are all present and consistent (src L33), and the shelf is correctly left **unchanged** (Book 6's vessels stay on the far bank).
- The **two-rook mark / Ansel Rooke / Rooke Brothers** lineage matches Bks 4–5 (the far pot's foot, src ~L233), plus a new **pressed lantern** for the bridge.
- **Grams Ilsabet's seventh ledger** (Bks 4–5) is used again, now for her *young-hand* record of Sabra and the two fires — consistent with Ilsabet being Edda's teacher, a generation older.
- The **Stonebeck bridge** "went in a flood thirty years back" matches Books 1 & 5 (the flood that also stopped Nesta's wedding).
- The **catechism grows to a sixth line** here, exactly as the five-book progression sets up (keep → give back → mend → hand on → keep the love → *wake the far fire*).

## (c) Caveat

**This self-edit pass is a build-time editorial read only. It is NOT a substitute
for a professional native-speaker proofread**, which remains the series' hard gate
before any publication. The body is preserved byte-for-byte; the continuity items
above are questions/notes for the author, deliberately left unchanged in the text.
