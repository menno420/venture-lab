# star-pirates — board-book version notes

Version created 2026-07-13 (ORDER 008 "multiple versions of each", wave 2 after the comet-biscuit board cuts). Source: the finished **7–9 chapter book** *Star Pirates — Book 1: The Wrong Way Down* (`../../{en,nl,de}/`, chapters 01–10; EN 11,401 / NL 12,080 / DE 11,806 words per the title README).

## Honest format note — this is a distillation, not a cut

**The formats do not match, and no cut could bridge them.** The comet-biscuit board versions compress a ~575-word 15-spread picture book to 12 spreads; that recipe does not apply to an ~11.4k-word plot-driven chapter book — compressing crash, bluff, harbour race, Kroll's raid and the sea chase into 200 toddler words would produce a summary, and the versions convention (`../../../VERSIONS.md`) forbids summaries: a version must read complete on its own. So this board book is a **standalone new goodnight story** built from the chapter book's characters and its gentlest motifs, on the standard 12-spread / 150–250-word board grid. **This is the first chapter-book→board conversion in the track — there is no precedent card for it**; the comet-biscuit cards (`.sessions/2026-07-13-comet-biscuit-board-cut.md` and predecessors) cover only picture-book→board cuts.

**What was distilled (and from where):**

- **The ship that glows** — Mr. Pumble's "GLOWING THINGS (unexplained)" ledger column from chapter 6 (the smokeless lantern, the rope that ties itself, the humming patch of deck) becomes the book's central goodnight image: the glowing things "wake up" as the crew goes to sleep, and the ship itself is the night-light.
- **Squish's kind mistranslations** — the chapter book's running gag (insults rendered as compliments) becomes the refrain engine: Squish "translates" the gulls, the waves and the wind into goodnights, and on the last translation ("sleep... sleep... sleep") is, for once, exactly right.
- **Gorm crying at sunsets** (chapter 6) — one happy tear, *plink*.
- **Each character's established voice, one goodnight each:** Bolt's four arms and near-silence ("Goodnight" as "a whole song"), Fizzwick's laminated rule card (a bedtime Rule Hundred), Ironjaw's gruffness-as-care ("Captains don't tuck... Captains CHECK" — an original beat for this version, patterned on her established softness-behind-gruffness in the chapter book, e.g. her uncharacteristically soft voice in chapter 6; the line itself does not appear in the source), and Pip in the crow's nest calling the stars.
- **Names/epithets per DECISIONS.md §4:** personal names stable across languages (Fizzwick, Bolt, Squish, Gorm, Pip); localized ship and captain epithets used — *Bright Revenge* / *De Felle Wraak* / *Die Helle Rache*; Ironjaw / IJzerkaak / Eisenkiefer.

**What was deliberately left out:** the entire plot (crash, bluff, race, Kroll, chase, choice), all peril and villainy (Kroll does not exist at this age band), Squish's insult-material (the mistranslated sources here are animal/weather sounds, not rude pirates), Gorm's crab terror (fear beat, wrong register for a goodnight book), and all worldbuilding that needs explaining. A toddler who never meets the chapter book gets a complete tuck-the-ship-in story; a family that owns both meets the same crew at two ages.

## Honest word counts

Counted with `wc -w`. "Story words" = manuscript body only, excluding headings, metadata bullets, blockquote, illustration notes (italic lines), and `[Spread N]` markers (count command: `grep -v -e '^#' -e '^-' -e '^>' -e '^\*' -e '^\[Spread' -e '^$' -e '^---' <file> | wc -w`).

| Language | File | Story words (`wc -w`) | Full file (`wc -w`) |
| --- | --- | --- | --- |
| EN | `star-pirates.board.en.md` | 219 | 620 |
| NL | `star-pirates.board.nl.md` | 215 | 607 |
| DE | `star-pirates.board.de.md` | 222 | 619 |

All three inside the 150–250 board-book target. 12 spreads each; NL and DE are native parallel versions written to the same spread grid, not literal translations of the EN text.

## Format & fulfillment — ⚑ OWNER

- **Board book (0–3), 12 spreads** is the editorial format of this text. Price point and physical format decision stay **⚑ OWNER** — not decided here.
- **⚑ OWNER research — board-book printing:** KDP does **not** print board books (known KDP limitation), so this version cannot ship through the lane's default KDP path. Fulfillment would need IngramSpark or another board-book printer/POD alternative — that comparison and choice is owner research, deliberately NOT decided in this repo.
- **Illustration remains parked** per the track convention: italic art-direction notes only, the seat generates no art.
