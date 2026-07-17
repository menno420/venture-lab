# The Night Kiln — EN omnibus / box-set edition spec

Production spec for a **single-volume omnibus** (a.k.a. box-set / "complete
trilogy") edition of the finished **EN** *Night Kiln* series — the three
already-complete, already-verified novellas bound as **one book**. This is a
**recombination spec only — no new prose**; the three EN masters are set into
one volume **unchanged**, byte-for-byte, and a version NEVER edits a master
(`../README.md` convention). Structure and rigor mirror the sibling
`../large-print/EDITION-SPEC.md` and the just-merged Paper Orange
audiobook spec
(`candidates/adult-novels/the-paper-orange/versions/audio/EDITION-SPEC.md`,
PR #225). Publishing is owner-gated
([`docs/publishing/vetting/the-night-kiln.md`](../../../../../docs/publishing/vetting/the-night-kiln.md) §7).

**Scope: EN only.** A Dutch omnibus (*De Nachtoven* / *De Morgendeur* /
*De Oogstslag*, all three NL editions complete under `../nl/`, `../nl-book-2/`,
`../nl-book-3/`) is a natural mirror of this spec but is **deferred**: it turns
on the owner's still-open one-word length-band ratify in
[`../../LENGTH-BAND-PREP.md`](../../LENGTH-BAND-PREP.md) (De Morgendeur at ~16k
parity vs the packet's ~20k–30k band). The **EN omnibus does not depend on that
ratify** and does not touch it — the EN masters are final as written. When the
owner ratifies, an `omnibus-nl/` spec is a one-slice follow-up.

Provenance: created 2026-07-17 (night run, ORDER 016 — improve an existing
sellable by adding a new gate-free edition, extending the "versions are cheap
once the research exists" line the `versions/` index carries from ORDER 008
item 1). Source manuscripts pinned in the *Word count* section and the
provenance footer with their measured `wc -w`.

## Edition identity

- **Series title (canonical):** ***The Night Kiln*** — the series name carried
  by every book's front matter (Book Two's subtitle: *"…The Night Kiln,
  Book Two"*; Book Three: *"…The Night Kiln, Book Three"*). Book One's title and
  the series title are the same words, which the omnibus title must disambiguate
  so a shopper doesn't mistake the omnibus for Book One alone.
- **Proposed omnibus title (⚑ PROPOSED — DECISIONS names none):**
  ***The Night Kiln: The Complete Trilogy***.
  Rationale: keeps the established series brand as the lead word; *The Complete
  Trilogy* is the standard box-set signal buyers scan for and resolves the
  Book-One-vs-omnibus collision above. **`../../DECISIONS.md` records no omnibus
  title** (it names the three book titles and the three NL titles only), so this
  is proposed per the sibling specs' decide-and-flag habit and is the **owner's
  to ratify** at listing time. Alternatives considered: *The Wenholt Kiln
  Trilogy* (foregrounds the village, weakens the established series brand);
  *The Night Kiln Omnibus* (accurate, flatter retail signal); *Three Firings*
  / *The Kiln Keeps* (thematic but off-brand — discards the series name a repeat
  buyer searches for). Recommend *The Complete Trilogy*.
- **Proposed subtitle (⚑ PROPOSED):** *Three Cozy Fantasy Novellas of Wenholt*
  — carries the genre promise every book's own subtitle makes (*A Cozy Fantasy
  Novella*) and the shared setting; the "three novellas" count sets the
  single-volume expectation honestly.
- **What it is:** one book, three novellas, read in series order, with unified
  front/back matter — a higher-AOV listing that sells the whole arc in one
  click instead of three. **Not** a bundle of three separate files (that is the
  storefront-bundle pattern, `candidates/BUNDLE-LISTING.md`); this is a single
  bound interior.

## The three books, in reading order

Fixed series order (planted-hook chain is strictly linear — see *Inter-book
continuity*); each is a complete standalone arc ("THE END") that also advances
the series.

| # | Book | EN master | Chapters | Words (`wc -w`) |
|---|------|-----------|:--------:|----------------:|
| One | *The Night Kiln* | `../../en/the-night-kiln.md` | 12 | 15,999 |
| Two | *The Morning Door* | `../../en/the-morning-door.md` | 12 | 15,995 |
| Three | *The Harvest Rows* | `../../en/the-harvest-rows.md` | 12 | 23,334 |
| | **Omnibus total** | (three masters, unchanged) | **36** | **55,328** |

Reading order is **not** interchangeable: Book Two's spine is the Stonebeck
letter that arrives on Book One's last page; Book Three's spine is the harvest
dish Book Two hooks on its last page; the craft's catechism grows one line per
book (see below). The omnibus presents them One → Two → Three and nowhere
signals that a reader may start mid-series (each book's own "it stands alone"
content note is kept, but the volume's front matter orders them).

## Unified front matter (single-volume read order)

What the bound omnibus presents, top to bottom. The per-book front matter is
**consolidated** so the reader meets the volume once, then each book in turn.

1. **Omnibus title page (single):** proposed title *The Night Kiln: The
   Complete Trilogy* / subtitle *Three Cozy Fantasy Novellas of Wenholt* /
   author. One title page for the whole volume — the three per-book `# TITLE`
   lines become interior **half-title dividers** (step 6), not competing title
   pages.
2. **Copyright / colophon (single):** one combined copyright page for the whole
   volume — author, edition line ("Omnibus edition"), the three novellas listed
   by title with their original standing, one rights/ISBN block (ISBN is
   owner-gated, see *NOT included*), colophon/typeface note. Replaces three
   separate copyright pages with one.
3. **Consolidated content note (single, read once up front):** all three
   masters carry a **near-identical** content note (adult cozy fantasy; grief,
   remembered bereavement offpage/in the past, a beloved character living with
   memory loss, all handled gently; no violence, no explicit content). The
   omnibus prints **one** volume-level content note up front rather than
   repeating it three times. Verbatim source text lives in each master's front
   block; the consolidated note must not soften or drop any element (Book Two/
   Three add "long in the past"/"in the past" and the "stands alone" line — keep
   the union, lose nothing).
4. **Combined Table of Contents** — the full 36-chapter TOC below, grouped under
   three book headings. This is the omnibus's one genuinely new front-matter
   artifact; it is derived mechanically from the masters' `# Chapter …` lines
   (grep shown in *Provenance*), not rewritten.
5. **Optional series note / "About this edition"** (recommended, ≤1 page): one
   short paragraph telling the reader these are three linked novellas best read
   in order, and that each also stands alone — the single place the volume
   speaks in its own voice. Content is editorial; not drafted here.
6. **Book One → Two → Three**, each opened by a **half-title divider** (recto:
   the book's `# TITLE` + its `*A Cozy Fantasy Novella · …*` subtitle line, and
   optionally its back-cover teaser `>` quote as divider copy), then that book's
   twelve chapters read in sequence from the master unchanged.
7. **Back matter** — see *Back matter*.

### Combined Table of Contents (all 36 chapters — derived, not rewritten)

**Book One — *The Night Kiln***
1. Moonrise Custom
2. The Telling Shelf
3. The Long Fire
4. The Stranger at Moonrise
5. Bread and Opinions
6. The Mason's Hands
7. What the Kiln Kept
8. The Quarrel Told
9. Two on the Rope
10. The Keystone
11. The Proving Fire
12. Wintermark, and the Morning Cup

**Book Two — *The Morning Door***
1. The Wedding Cup
2. A Nice Jar
3. The Ledger and the Lime
4. The Careful Hand
5. Things in the Room
6. How a Fire Opens
7. The Unclaimed Cup
8. What It Costs
9. The Apprentice's Bowl
10. The Short Night
11. The Morning, Told
12. A House with a Morning in It

**Book Three — *The Harvest Rows***
1. Harvest Weather
2. The Short Entry
3. What the Frost Took
4. The Third Temper
5. Boats and Opinions
6. The Race Told
7. The Colour of the Ler
8. Load-Bearing Breaks
9. My Stroke and Not Mine
10. The Harvest Rows
11. The Level Fire
12. Harvest Home

Chapter numbering **restarts at One inside each book** (they are three
novellas, not a 36-chapter novel). At typeset time the TOC entries carry page
numbers; a running head of *book title · chapter title* keeps the reader
oriented across the ~55k words.

## Inter-book continuity / transition note

How the single volume flows book to book — the omnibus's job is to make three
separately-published arcs read as one continuous sit-down without editing a
word.

- **Half-title dividers carry the seams.** Between books, a recto half-title
  (the next book's title + subtitle) gives the reader the same "new book" beat a
  separate cover would — a deliberate pause, not a hard stop. Each book's own
  opening re-establishes the craft's rule in its first paragraph (the
  byte-identical "The rule in Wenholt was older than anyone who kept it…"), so
  the transition is self-healing: a reader crossing from Book One's last page to
  Book Two's first is re-grounded by the text itself.
- **The planted-hook chain is linear and already in the prose** — the omnibus
  needs to add nothing, only preserve order:
  - **One → Two:** Book One's final page delivers the Stonebeck letter asking
    "whether what a fire had shut, another fire might ever, gently, open." Book
    Two IS the answer to that letter. In one volume the letter and its answer sit
    a half-title apart — a stronger hand-off than the original standalone gap.
  - **Two → Three:** Book Two closes on Edda saying *"Wash the dust off. That's a
    harvest story,"* naming the dunted race-dish. Book Three IS that harvest
    story. Same immediate hand-off across the divider.
  - **Three → (Book Four):** Book Three plants Ilsabet's-first-pot hook
    (*"That's a winter story"*) — the omnibus preserves it as the series' open
    door; it is **not** a loose end to trim.
- **The growing catechism is the volume's spine and its best continuity payoff.**
  Read in one sitting the reader watches the craft's creed accrete one line per
  book, each line taught to the fire *in* the book that adds it:
  - Book One establishes: *"The kiln keeps. It does not take. Say it back."*
  - Book Two ends adding: *"And what it keeps, asked kindly, it can give back."*
  - Book Three ends adding: *"And what breaks, told together, it can mend."*
  The three-line catechism standing complete on the omnibus's last page (Book
  Three's ending prints all three lines together) is the single-volume edition's
  emotional argument for existing — a payoff only the omnibus delivers in one
  breath. Do not annotate or gloss it; the accretion speaks for itself.
- **Consistent world detail across the seam** (kept intact, not edited): Edda
  Marren and the crooked cup, Perrin's apprentice arc (elbows → first carry →
  steady wedging-bench hand across the three books), Wenholt / the Ler ferry
  (Wim & Griet) / Stonebeck, the telling shelf's nine bowls, the kiln "bearing
  all it kept and keeping all it bore." These recur verbatim; the omnibus's value
  is letting a reader feel the accumulation without a between-books wait.

## Back matter

- **Single "THE END" per book is retained** — each book keeps its own closing
  and `⁂` dinkus; the omnibus does not merge them into one ending. Book Three's
  ending (the full three-line catechism) is the volume's true close.
- **Volume back matter (single):** optional "About the author," a "The Night
  Kiln series" list (the three titles + any owner-approved forthcoming Book
  Four line — Book Four is only a planted hook, so list it only if the owner
  wants a teaser), and — if the owner runs the standalone editions in parallel —
  a short "also available separately / large-print / audiobook / Dutch editions"
  cross-reference to the sibling `versions/` products. Content is editorial and
  owner-approved; not drafted here.
- **No new story material** goes in back matter. Any excerpt, bonus scene, or
  author's note would be **new prose** and is out of scope for a
  recombination-only spec.

## Word count (honest, measured)

Per-book counts by `wc -w` on the EN masters, 2026-07-17 (command reproduced in
*Provenance*); the three sum to the omnibus body total:

```
15999  ../../en/the-night-kiln.md
15995  ../../en/the-morning-door.md
23334  ../../en/the-harvest-rows.md
55328  total
```

- **Omnibus body: 55,328 words** (three masters, unchanged). This is the honest
  read-length; the combined TOC, one consolidated content note, three
  half-title dividers, and volume front/back matter add a small non-story
  overhead on top (a few hundred words at most, unmeasured until typeset).
- These are the **same measured counts** the `../README.md` index and
  `../../LENGTH-BAND-PREP.md` carry (15,999 / 15,995 / 23,334) — no re-count
  drift. The Book-Two ~16k length-band question stays the owner's and is
  **untouched** here: the omnibus binds the books **as written**.

## Trim size + page estimate (standard trade edition — NOT large-print)

Unlike the sibling `../large-print/` spec (6×9, 16pt, deliberately low
words-per-page), the omnibus is a **standard trade paperback** — the point is a
comfortable single volume at a sane page count, not enlarged type. Nothing below
is measured: **no interior has been typeset**, so every figure is an estimate
from density, to be replaced by the real page count at production.

- **Recommended trim:** **5.5" × 8.5"** (KDP standard trade; roomier than 5×8
  for a 55k-word omnibus, keeps the spine and page count reasonable). 6×9 is the
  alternative if the standalone editions use it and shelf-parity matters.
- **Body face:** ~10.5–11pt high-legibility book serif, 1.2–1.3× leading,
  justified with hyphenation — standard trade norms (this is **not** the
  large-print edition; that accessibility format is specced separately in
  `../large-print/`). Inline emphasis italics (the kiln's law, the catechism)
  stay inline; never set whole paragraphs italic.
- **Density band (estimate):** ~**300–370 words/page** at 5.5×8.5 / 11pt
  (typical trade density; contrast the large-print spec's deliberate
  160–200 wpp). Body: 55,328 ÷ 300–370 ≈ **150–185 pages**.
- **Plus front/back matter + dividers + chapter openers:** combined TOC
  (~2–3 pp), title/copyright/content-note/series-note (~4–5 pp), 3 half-title
  dividers (~3–6 pp), 36 chapter-opener pages starting fresh (~18–36 pp
  depending on whether openers force a recto), back matter (~2–4 pp) ≈
  **30–55 pp** of non-body.
- **Working estimate: ~185–235 pages; midpoint ~210 pages.** This **crosses the
  110-page KDP flat-band boundary decisively** — where each standalone novella
  (~90–115 pp) sat in or near KDP's $2.30 flat band, the omnibus lands in the
  **per-page band** ($1.00 fixed + $0.012/page; source: the large-print spec's
  cited KDP printing-cost table, verify live at production). Indicative print
  cost at ~210 pp ≈ $1.00 + 210×$0.012 ≈ **$3.52** (black ink; recompute at the
  real page count).

**Indicative economics (analysis only — the price/publish click is the
owner's).** The AOV case for the omnibus: three standalone **ebooks** at the
packet's recommended $4.99 each (`docs/publishing/vetting/the-night-kiln.md` §4)
total **$14.97**; an omnibus ebook priced in the low-teens (e.g. ~$9.99–$12.99)
reads as a series discount while lifting the single-order value above any one
$4.99 book — the standard "buy the box set" lift. A print omnibus at ~210 pp
sits in CHECKLIST §4's verified paperback band ($12.99–$14.99) with print
royalty = 60% of list − print cost (≈ $4.27–$5.47/unit at ~$3.52 cost). **These
are indicative bands, not a recommendation to list at any number** — the actual
list price, the ebook/print split, and the click are **owner decisions**
(see *NOT included*).

## Production steps (when owner green-lights)

*Listed for planning only — none executed or authorized here.*

1. Ratify (or replace) the proposed omnibus title/subtitle; set the volume
   copyright/edition line.
2. Typeset the three masters unchanged into one interior at the trim/typography
   above; build the combined TOC with real page numbers; set running heads
   (*book · chapter*); record the actual page count.
3. Recompute print cost + royalty at the real page count (formula above; confirm
   it is in the per-page band, not the flat band).
4. Cover: a **new omnibus cover** (a box-set cover is its own design — the three
   standalone covers do not compose into one); any art spend is an owner
   decision.
5. Assign the omnibus its **own ISBN** (a distinct product from the three
   standalones).
6. Run the full `docs/publishing/CHECKLIST.md` pass for the new SKU.

## NOT included / owner-gated

This file is a **recombination spec only**. Every item below is an **owner
decision**, explicitly **out of scope** for this slice — nothing here authorizes
any of them:

- **The component manuscripts** — untouched. No new prose, no edits, no
  re-count; the three EN masters are byte-for-byte the canonical texts.
- **Omnibus cover design** — a box-set cover is a new art asset; any spend is
  owner-gated.
- **ISBN** — the omnibus is a distinct product needing its own ISBN; assignment
  is owner-gated.
- **Title/subtitle ratification** — the omnibus title above is **proposed**, not
  decided.
- **Print / KDP publish** — trim/list/price selection, the KDP upload, category
  and keyword choices, KDP Select enrollment, the publish click, and any spend
  or account action all stay owner-gated.
- **The NL omnibus** — deferred pending the owner's length-band ratify
  (`../../LENGTH-BAND-PREP.md`); not built here.

⚑ **Cover, ISBN, title ratification, price, and publish clicks stay
owner-gated** (vetting packet §7; `docs/publishing/CHECKLIST.md` §7 /
CONSTITUTION rail 13) — nothing in this spec creates a listing, sets a price,
commissions art, or spends. Omnibus **production remains a future owner-gated
step**; this slice ships only the preparatory recombination spec.

---

**Provenance footer.** Derived from the three EN masters, unchanged:
`../../en/the-night-kiln.md@aa04700` (blob `e8abb0e`, `wc -w` = **15,999**);
`../../en/the-morning-door.md@aa04700` (blob `f1a5476`, `wc -w` = **15,995**);
`../../en/the-harvest-rows.md@0d9335d` (blob `b691050`, `wc -w` = **23,334**).
Omnibus body total **55,328** words. Counts measured 2026-07-17 via
`wc -w candidates/adult-novels/the-night-kiln/en/{the-night-kiln,the-morning-door,the-harvest-rows}.md`;
combined TOC derived via `grep -n '^# Chapter' …` on the same three files (36
chapter headings, 12 per book). Canonical series/title/order facts from
[`../../DECISIONS.md`](../../DECISIONS.md); length-band context from
[`../../LENGTH-BAND-PREP.md`](../../LENGTH-BAND-PREP.md). No manuscript text was
altered.
