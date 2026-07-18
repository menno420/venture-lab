# The Night Kiln — audiobook / narration edition spec (trilogy audio program)

Production spec for a single-narrator **audiobook program** of the **completed
EN *Night Kiln* trilogy** — the three already-finished, already-verified
novellas (Book One *The Night Kiln* `../../en/the-night-kiln.md`, **15,999
words**; Book Two *The Morning Door* `../../en/the-morning-door.md`, **15,995
words**; Book Three *The Harvest Rows* `../../en/the-harvest-rows.md`, **23,334
words** — `wc -w`, 2026-07-18, reproduced in *Word count & runtime*). **Spec
only — no recording, no narrator hire, no audio file, no distribution**; a
narrator/producer reads the base manuscripts unchanged. This spec covers the
three books as **one trilogy audio program** — three per-book audiobooks
narrated to a single continuous voicing brief (recommended), plus an **optional
single omnibus audio program** (all three in one product; see that section).
The **component manuscripts stay UNTOUCHED**; a version NEVER edits a master
(`../README.md` convention).

Structure and rigor mirror the just-merged **Paper Orange** audiobook spec
(`candidates/adult-novels/the-paper-orange/versions/audio/EDITION-SPEC.md`,
PR #225 — the template this follows: narration script order, pronunciation
guide, honest per-chapter `wc -w`, WPM runtime + ACX finished-hours, tone
notes, owner-gated NOT-included section, `file@sha` provenance footer) and the
sibling `../large-print/EDITION-SPEC.md` + `../omnibus-en/EDITION-SPEC.md`
(PR #226). Publishing/production is owner-gated
([`docs/publishing/vetting/the-night-kiln.md`](../../../../../docs/publishing/vetting/the-night-kiln.md) §7).

Provenance: created 2026-07-18 (night run, ORDER 016 — improve an existing
sellable by adding a new gate-free format edition, extending the "versions are
cheap once the research exists" line the `versions/` index carries from
ORDER 008 item 1). Source manuscripts pinned in *Word count & runtime* and the
provenance footer with their measured `wc -w`.

## Edition identity

- **What it is:** a **trilogy audio program** — the three finished EN novellas
  narrated by a **single narrator** to **one voicing brief**, so Edda, Perrin,
  Wim & Griet, and the recurring village voices sound **identical across all
  three books** (the whole point of a series audiobook — the *Tone / pacing /
  character-voice* and *Voice-consistency guide* sections exist to enforce
  this). Delivered as **three per-book audiobooks** (Book One / Two / Three,
  each its own ACX/Findaway title), read in series order.
- **Optional single omnibus audio program:** the same three recordings can also
  be issued as **one combined audiobook** ("The Night Kiln: The Complete
  Trilogy" — proposed title, see `../omnibus-en/EDITION-SPEC.md`), a higher-AOV
  single listing. Same audio, different packaging; specced in its own section
  below. Either way the three books are recorded **once** to the same brief.
- **Source of truth:** the three **EN masters**, read verbatim. Nothing in this
  spec changes a word of the prose.
- **Voicing:** single narrator, all parts (no full-cast dramatization). Close
  third person on **Edda Marren** throughout all three books — the narrator IS
  the narrative voice, and differentiates the small cast by light shading, not
  impersonation (see *Tone / pacing / character-voice notes*).
- **Language:** English. The setting (Wenholt) is an **invented cozy-fantasy
  world**; the text is entirely English (grep-verified — see
  *Voice-consistency & pronunciation guide*). There are **no** real
  Dutch/foreign-language terms to translate or gloss; the only work the guide
  does is **proper-name consistency across three books**.
- **NL narration is a separate future edition — deferred.** All three books have
  complete NL translations (*De Nachtoven* `../nl/`, *De Morgendeur*
  `../nl-book-2/`, *De Oogstslag* `../nl-book-3/`), so a Dutch audio program is
  a natural mirror of this spec — but it needs a **Dutch narrator**, native
  pronunciation, and separate ACX/Findaway listings, and it rides the owner's
  still-open **one-word length-band ratify** in
  [`../../LENGTH-BAND-PREP.md`](../../LENGTH-BAND-PREP.md) (Book Two/Three at
  ~16k/23k vs the packet band). This EN audio program **does not depend on that
  ratify and does not touch it** — the EN masters are final as written. When the
  owner ratifies, an NL narration spec is a one-slice follow-up.

## Narration script order (per book)

Each book is a **self-contained audiobook** with its own opening/closing
credits, and each is read in the same order. The manuscript's markdown is a
print convention; the narrator reads the *text*, not the markup.

For **every** book, in order:

1. **Opening credits** (producer-supplied boilerplate, spoken): *"[Book title],
   The Night Kiln [Book N], written by [author], narrated by [narrator]."* —
   exact wording set at production; not in the manuscript. (Book One has no
   "Book One" line in its own front matter — the series numbering lives in
   Books Two/Three subtitles — so the credit adds "Book One" for series clarity
   at production.)
2. **Title + subtitle** — the manuscript's `#` title line and the `*A Cozy
   Fantasy Novella · The Night Kiln, Book N*` subtitle (Book One's subtitle is
   just *A Cozy Fantasy Novella*; Books Two/Three carry the series number).
3. **Content note** — read in full, unhurried, before the story. All three
   masters carry a near-identical adult-cozy content note (grief; remembered
   bereavement offpage/in the past; a beloved character living with memory loss;
   *no violence, no explicit content*). Books Two/Three add "this stands alone."
   Read it verbatim; it is the listener's informed-consent moment. ACX/retailer
   listings should also carry it in text.
4. **Chapters One–Twelve, in sequence** — announce each chapter by its spoken
   title (e.g. *"Chapter One. Moonrise Custom."*), then read the chapter body.
   A short held silence (~1.5–2 s) at each chapter opener and at any scene-break
   rule (`---`) inside a chapter; a longer beat between chapters. **Note:** each
   book opens with the byte-identical rule-sentence — *"The rule in Wenholt was
   older than anyone who kept it…"* — deliver it the **same way every time**
   across all three books; it is the series' recurring incantation, not a fresh
   line.
5. **"THE END" + the `⁂` dinkus** — the closing "THE END" is spoken plainly;
   the `⁂` asterism is voiced as a **held silence**, not a word. The final
   catechism (see below) is inside Chapter Twelve's body and is read as body.
6. **Closing credits** (producer-supplied): *"You have been listening to [Book
   title]… This recording is copyright…"* — set at production.

**SKIP (do not voice), every book:**
- The **back-cover blurb** — the `>` block-quote near the top of each master
  ("Everyone in Wenholt knows the rule…"). It is marketing copy for the listing
  page and the retail sample, not body text; reading it doubles the opening.
  (If the producer wants a spoken teaser for the retail sample clip, this is the
  text to use — but it is NOT part of the book body. Blurb lengths, skipped:
  Book One 59 w, Book Two 96 w, Book Three 86 w.)
- All **markdown markup**: the `#` heading hashes, the `---` horizontal rules
  (voiced as a silence, not a word), the `>` quote marker, the `·` middot in the
  subtitle line, and the `*…*` italic asterisks. Italics are read as
  **emphasis / interior thought**, never announced.
- Any **page numbers, running heads, or file metadata** — none exist in the
  manuscripts, but if a typeset PDF is used as the read-from copy, ignore them.

**The growing catechism (read identically where it recurs).** The craft's creed
accretes one line per book and each book *ends* on the lines it has earned —
these are body text, read plainly and unhurried, never dramatized:
- Book One ends on: *"The kiln keeps. It does not take. Say it back."*
- Book Two ends adding: *"And what it keeps, asked kindly, it can give back."*
- Book Three ends on all three lines together, the trilogy's true close:
  *"The kiln keeps. It does not take. Say it back. / And what it keeps, asked
  kindly, it can give back. / And what breaks, told together, it can mend."*
The line the narrator has spoken before must sound the same when it returns — a
recognizable refrain is a load-bearing payoff of hearing the trilogy read
aloud in one voice.

## Voice-consistency & pronunciation guide

**Honest scope note.** Unlike the Paper Orange spec (a Hunger-Winter Amsterdam
novella genuinely full of Dutch place-names and ration-era terms), *The Night
Kiln* is an **invented cozy-fantasy world (Wenholt)** and its text is **entirely
English** — verified by grep against all three EN masters: the only non-ASCII
characters are the em-dash `—`, the middot `·`, and the `⁂` asterism; there are
**no** accented words and **no** real foreign-language terms to translate. So
there is **nothing to "pronounce correctly" in a native-language sense**. What
this guide does instead is the job a **series** audiobook actually needs:
**fix one consistent pronunciation for every recurring proper name so it never
drifts across three books.** These are **invented names** — there is no
canonical audio source — so the respellings below are a **recommended** house
standard; whatever the narrator settles at audition becomes the trilogy's
canon and must then be held identical Book One → Three.

Respelling key: caps = stressed syllable; vowels as in plain English.

### People (recurring — hold identical across all three books)

| Name | Recommended respelling | Appears | Note |
|------|------------------------|---------|------|
| **Edda Marren** | **ED-uh MARR-un** | 1·2·3 | the witch of Wenholt; the narrative centre |
| **Perrin Loft** | **PERR-in LOFT** | 1·2·3 | her apprentice (17); "elbows and all" |
| **Grams Ilsabet** | **ILL-suh-bet** | 1·2·3 | Edda's late teacher ("Grams"); memory-loss arc |
| **Ansel Rooke** | **AN-sul ROOK** | 1·2·3 | the mason (Book One's stranger); "Rooke" rhymes with "book" |
| "Uncle Anvil" | **ANN-vil** | 1·2·3 | Ansel's nickname (a niece's) — read warm, not literal |
| **Wim** | **WIM** (recommended) | 1·2·3 | the ferryman; Dutch-derived — see house-choice note |
| **Griet** | **GREET** (recommended) | 1·2·3 | the ferrywoman; the cracked race-dish is hers (Book Three) |
| **Hessa** | **HESS-uh** | 1·2·3 | village woman / subplot |
| **Odile** | **oh-DEEL** | 1·2·3 | French-derived name; keep the soft final -l |
| **Nell** | **NEL** | 2·3 | Ansel & Lena's child |
| **Lena** | **LAY-nuh** | 1·2·3 | Ansel's long-estranged, later wife |
| **Widow Sorrel** | **SORR-ul** | 1·2·3 | the one "emptying"; Book One's cautionary tale |
| **Tally Brock** | **TAL-ee BROK** | 1·2·3 | baker's daughter; marries Wilf (Book Two open) |
| **Wilf** | **WILF** | 2 | Tally's husband |
| **Cobb** | **COB** | 1·2·3 | the woodman who carries tellings down from the hills |
| **Mercy Hale** | **MUR-see HAYL** | 2·3 | the Stonebeck schoolmistress (Book Two's letter-writer) |
| **the Askews** | **ASS-kewz** | 1·2·3 | the hill-farm family (harvest) |

House-choice note: **Wim** and **Griet** are Dutch-form names (the author's
heritage surfaces in the ferry family), but the surrounding text is English and
never signals a Dutch reading. **Recommended: anglicize** — WIM / GREET — for an
English narration. If the owner prefers Dutch-authentic pronunciations (Wim =
"VIM", Griet = "KHREET", guttural *g*), that is a deliberate **audition-time
choice**, set once and held across all three books. Flagged, not decided here.

### Places & fixed terms (recurring)

| Name | Recommended respelling | Note |
|------|------------------------|------|
| **Wenholt** | **WEN-holt** | the village; the series' home word — say it the same every time |
| **Harrowgate** | **HARR-oh-gate** | the town up-river (scholars, barges) |
| **Stonebeck** | **STOHN-bek** | the parish whose letter drives Book Two/Three |
| **the Ler** | **the LAIR** (recommended) | the river; short invented name — fix it at audition, hold it |
| **Wintermark** | **WIN-ter-mark** | the midwinter festival / firing (not a person) |

## Word count & runtime

**WPM assumption:** **~150 words per minute**, the standard single-narrator
audiobook delivery rate (industry norm ~150 wpm; literary/cozy fiction with this
series' warm, unhurried register typically sits **140–155 wpm**, so treat every
figure below as the midpoint of a ±~5% band). Estimates are derived from an
**honest per-chapter `wc -w`** of each EN master (`csplit` on the `# Chapter`
rules, then `wc -w` each piece; per book the front block + twelve chapters sum
**exactly** to the whole-file `wc -w`). Runtime = words ÷ 150 wpm. **Finished
hours** (the ACX/producer unit for narrator cost + royalty math) = words ÷ 9,000
(150 wpm × 60); that math itself is owner-gated and not computed here.

Per-book whole-file counts (command reproduced in *Provenance*):

```
15999  ../../en/the-night-kiln.md
15995  ../../en/the-morning-door.md
23334  ../../en/the-harvest-rows.md
55328  trilogy total (read-aloud text)
```

### Book One — *The Night Kiln*

| Section | Words (`wc -w`) | @150 wpm |
|---------|----------------:|---------:|
| Front matter (title, subtitle, blurb, content note) | 104 | 0:42 |
| Chapter One — Moonrise Custom | 1,276 | 8:30 |
| Chapter Two — The Telling Shelf | 1,243 | 8:17 |
| Chapter Three — The Long Fire | 1,300 | 8:40 |
| Chapter Four — The Stranger at Moonrise | 1,477 | 9:51 |
| Chapter Five — Bread and Opinions | 1,242 | 8:17 |
| Chapter Six — The Mason's Hands | 1,167 | 7:47 |
| Chapter Seven — What the Kiln Kept | 1,294 | 8:38 |
| Chapter Eight — The Quarrel Told | 1,711 | 11:24 |
| Chapter Nine — Two on the Rope | 1,150 | 7:40 |
| Chapter Ten — The Keystone | 1,047 | 6:59 |
| Chapter Eleven — The Proving Fire | 1,234 | 8:14 |
| Chapter Twelve — Wintermark, and the Morning Cup | 1,754 | 11:42 |
| **Book One total** | **15,999** | **≈ 1:46:40** |

Finished hours: 15,999 ÷ 9,000 ≈ **1.78**. (Front-matter row includes the
59-word blurb, which the narrator **skips** — narrated front matter ≈ 45 w /
~0:18; blurb-skip keeps the read within the ±5% band.)

### Book Two — *The Morning Door*

| Section | Words (`wc -w`) | @150 wpm |
|---------|----------------:|---------:|
| Front matter (title, subtitle, blurb, content note) | 157 | 1:03 |
| Chapter One — The Wedding Cup | 1,202 | 8:01 |
| Chapter Two — A Nice Jar | 1,466 | 9:46 |
| Chapter Three — The Ledger and the Lime | 1,678 | 11:11 |
| Chapter Four — The Careful Hand | 1,822 | 12:09 |
| Chapter Five — Things in the Room | 1,268 | 8:27 |
| Chapter Six — How a Fire Opens | 1,095 | 7:18 |
| Chapter Seven — The Unclaimed Cup | 1,435 | 9:34 |
| Chapter Eight — What It Costs | 1,192 | 7:57 |
| Chapter Nine — The Apprentice's Bowl | 1,137 | 7:35 |
| Chapter Ten — The Short Night | 1,270 | 8:28 |
| Chapter Eleven — The Morning, Told | 1,152 | 7:41 |
| Chapter Twelve — A House with a Morning in It | 1,121 | 7:28 |
| **Book Two total** | **15,995** | **≈ 1:46:38** |

Finished hours: 15,995 ÷ 9,000 ≈ **1.78**. (Blurb skipped: 96 w.)

### Book Three — *The Harvest Rows*

| Section | Words (`wc -w`) | @150 wpm |
|---------|----------------:|---------:|
| Front matter (title, subtitle, blurb, content note) | 146 | 0:58 |
| Chapter One — Harvest Weather | 2,007 | 13:23 |
| Chapter Two — The Short Entry | 1,980 | 13:12 |
| Chapter Three — What the Frost Took | 1,990 | 13:16 |
| Chapter Four — The Third Temper | 1,946 | 12:58 |
| Chapter Five — Boats and Opinions | 1,804 | 12:02 |
| Chapter Six — The Race Told | 2,003 | 13:21 |
| Chapter Seven — The Colour of the Ler | 2,006 | 13:22 |
| Chapter Eight — Load-Bearing Breaks | 1,870 | 12:28 |
| Chapter Nine — My Stroke and Not Mine | 1,798 | 11:59 |
| Chapter Ten — The Harvest Rows | 1,916 | 12:46 |
| Chapter Eleven — The Level Fire | 1,867 | 12:27 |
| Chapter Twelve — Harvest Home | 2,001 | 13:20 |
| **Book Three total** | **23,334** | **≈ 2:35:34** |

Finished hours: 23,334 ÷ 9,000 ≈ **2.59**. (Blurb skipped: 86 w.)

### Trilogy total

| Book | Words (`wc -w`) | Runtime @150 wpm | Finished hours |
|------|----------------:|-----------------:|---------------:|
| One — *The Night Kiln* | 15,999 | ≈ 1:46:40 | 1.78 |
| Two — *The Morning Door* | 15,995 | ≈ 1:46:38 | 1.78 |
| Three — *The Harvest Rows* | 23,334 | ≈ 2:35:34 | 2.59 |
| **Trilogy total** | **55,328** | **≈ 6:08:51 (~6 h 9 m)** | **≈ 6.15** |

- **Add pacing overhead** (chapter-opener and scene-break silences, breaths, the
  deliberately slower delivery this warm material wants): a realistic finished
  program runs **~6 h 20 m – 6 h 45 m** across the three books. At ~9,000
  words/finished-hour the trilogy is **≈ 6.15 "finished hours"** — the unit
  ACX/producers quote for narrator cost and royalty math (that math is
  owner-gated; not computed here).
- **Recording-time rule of thumb** (not runtime): finished audiobooks take
  ~2–3× the runtime to record + edit + master, so ~6.15 finished hours ≈
  **~13–19 studio hours** of narrator/engineer effort across the trilogy — an
  input to the owner's hire decision, listed for planning only.
- These are the **same measured counts** the `../README.md` index,
  `../omnibus-en/EDITION-SPEC.md`, and `../../LENGTH-BAND-PREP.md` carry
  (15,999 / 15,995 / 23,334) — no re-count drift. The Book-Two ~16k length-band
  question stays the owner's and is **untouched** here.

## Tone / pacing / character-voice notes

- **Register:** warm, literary cozy fantasy — close and unhurried. The prose
  does the emotional work; the narrator **under-plays**. Grief, remembered
  bereavement (offpage/in the past), and the memory-loss thread (Grams Ilsabet;
  the Griet/Stonebeck grief) are delivered gently, never with sentimental swell.
  The comfort register — tea, the kettle "just short of singing," glaze
  chemistry as soft magic — is the whole contract; keep it kind.
- **Pace:** slow and settled — the pace of a workshop at evening. The
  craft-texture passages (spiral wedging, glaze jars, cone packs, the firing
  vigils) are the series' pleasure; let them breathe. Resist speeding the quiet.
- **Edda Marren:** the anchor voice across all three books — dry, kind, economical,
  a little wry ("Put it away," "Say it back to me"). Near sixty; steady. She is
  the narrative register itself; when in doubt the narrator sounds like Edda
  thinking.
- **Perrin Loft:** the apprentice, 17, "mostly elbows"; younger, quicker,
  earnest — differentiate with a lighter touch, **not** a cartoon youth voice.
  His arc across the trilogy (elbows → first carried telling → steady
  wedging-bench hand) is audible if his voice *matures a half-step* Book One →
  Three; keep it subtle.
- **The recurring cast must sound identical across three books** — Wim & Griet
  (the ferry), Ansel Rooke (the mason; low, careful, wastes-nothing), Tally
  Brock, Cobb the woodman (a hat-wringing, word-for-word carrier), Mercy Hale
  (the schoolmistress; letters read in a level teaching voice). Whatever the
  narrator sets in Book One is the trilogy's canon (see *Voice-consistency
  guide*).
- **The rule-sentence & the catechism:** the byte-identical opening
  ("The rule in Wenholt was older than anyone who kept it…") and the growing
  three-line catechism are **refrains** — deliver them the same way each time so
  a series listener *recognizes* them. The three-line catechism landing complete
  on Book Three's last page is the trilogy's emotional payoff; read it plainly,
  a fraction more space, no underlining. Let the accretion speak.
- **Sensitive content:** the content notes, the memory-loss thread, and Book
  One's single "emptying" cautionary tale (Widow Sorrel's jar — told, never
  performed on the page) are handled with dignity in the text; the narration
  matches that — gentle, unhurried, no dramatization of grief.

## Optional single omnibus audio program

The same three recordings can also be issued as **one combined audiobook** — the
audio counterpart of the print/ebook omnibus in `../omnibus-en/EDITION-SPEC.md`
(proposed title *The Night Kiln: The Complete Trilogy*, ⚑ owner to ratify). It
is **the same audio**, re-packaged as one higher-AOV listing.

- **Read order:** Book One → Two → Three, unchanged. Each book keeps its own
  content note (read once at that book's open) and its own "THE END"; the
  omnibus adds only a single volume-level opening credit and a short spoken
  "About this edition" note (≤30 s, producer-supplied) up front.
- **Chapter/file layout:** ACX/Findaway want per-chapter files; the omnibus is
  **37 audio sections** — one combined opening credit + 36 chapters (12 per
  book) with each book's front-matter/credits as that book's first file.
- **Runtime:** the trilogy total above — **≈ 6:08:51 body, ~6.4–6.8 h finished**,
  **≈ 6.15 finished hours**. This is a **single, substantial listen** (a
  standard full-length audiobook length) — the omnibus audio's commercial case
  vs three ~1.8–2.6 h singles is the same "one click, whole arc" AOV lift the
  print omnibus makes.
- **Not a re-record:** recording once to one brief (the point of the trilogy
  program) is what makes the omnibus audio free to assemble. Which SKUs to
  actually publish — three singles, one omnibus, or both — is an **owner
  decision** (see *NOT included*).

## Production reference (when owner green-lights)

*Listed for planning only — none executed or authorized here.*

1. Narrator audition against a sample scene (suggested: Book One Ch. 1
   wedging/queue open, plus the Book Three Ch. 6 "The Race Told") — tests the
   warm cozy register AND the recurring-cast voices in one pass, and **sets the
   invented-name pronunciations** (Wim/Griet/Ler) for the whole trilogy.
2. Record all three from the EN masters unchanged, **to one voicing brief**;
   hold the *Narration script order* per book (skip the blurb; content note read
   in full; the rule-sentence and catechism delivered identically where they
   recur).
3. Master to the distributor's technical spec (ACX and Findaway both publish
   RMS/peak/noise-floor targets and a per-file chapter layout; verify the live
   spec at production — not reproduced here).
4. Decide packaging: three singles, the single omnibus audio, or both (owner).
5. Cover: reuse the standard/omnibus cover art (when it exists) at the
   audiobook's square ratio; any art spend is an owner decision.
6. Run the relevant `docs/publishing/CHECKLIST.md` steps for the format.

## NOT included / owner-gated

This file is a **production-ready spec only**. Every one of the following is an
**owner decision** and is explicitly **out of scope** for this slice — nothing
here authorizes any of them:

- **The component manuscripts** — untouched. No new prose, no edits, no
  re-count; the three EN masters are byte-for-byte the canonical texts.
- **Recording** — no audio has been produced; no narration performed.
- **Narrator hire / casting** — any audition, contract, per-finished-hour fee,
  or royalty-share is a spend and stays owner-gated.
- **Distribution** — ACX, Findaway Voices, Spotify/Audible, or any retailer
  account, upload, listing, price, category, or the single-vs-omnibus SKU
  choice.
- **The NL narration edition** — deferred pending the owner's length-band ratify
  (`../../LENGTH-BAND-PREP.md`); needs a Dutch narrator and its own listings;
  not built here.
- **Any spend / accounts** — no accounts touched, no purchase, no publish.

⚑ **Recording, hire, distribution, and price clicks stay owner-gated**
(vetting packet §7; `docs/publishing/CHECKLIST.md` §7 / CONSTITUTION rail 13) —
nothing in this spec creates a listing, sets a price, hires a narrator, or
spends. Audiobook **production remains a future owner-gated step**; this slice
ships only the preparatory spec.

---

**Provenance footer.** Derived from the three EN masters, unchanged:
`../../en/the-night-kiln.md@aa04700` (blob `e8abb0e`, `wc -w` = **15,999**);
`../../en/the-morning-door.md@aa04700` (blob `f1a5476`, `wc -w` = **15,995**);
`../../en/the-harvest-rows.md@0d9335d` (blob `b691050`, `wc -w` = **23,334**).
Trilogy read-aloud total **55,328** words. Counts measured 2026-07-18 via
`wc -w candidates/adult-novels/the-night-kiln/en/{the-night-kiln,the-morning-door,the-harvest-rows}.md`;
per-chapter counts via `csplit` on each master's `^# Chapter` rules + `wc -w`
(per book: front block + twelve chapters sum **exactly** to the whole-file
count). Text confirmed all-English by grep (no accented / foreign-language
tokens; only `—`, `·`, `⁂` are non-ASCII). Canonical series/title/order facts
from [`../../DECISIONS.md`](../../DECISIONS.md); length-band context from
[`../../LENGTH-BAND-PREP.md`](../../LENGTH-BAND-PREP.md). No manuscript text was
altered.
