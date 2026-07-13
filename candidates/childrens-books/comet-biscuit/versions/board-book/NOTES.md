# comet-biscuit book 1 — board-book cut notes

Version created 2026-07-13 (night run, ORDER 008 "multiple versions of each"). Source: the 15-spread, ages 3–6 read-aloud picture-book manuscripts of **book 1** in the series' language subdirs (`../../en/book-1-the-great-jam-wobble.md`, `../../nl/boek-1-de-grote-jamwiebel.md`, `../../de/buch-1-der-grosse-marmeladen-wackler.md`, body ~520–612 words each). Note: comet-biscuit stores its three books in `{en,nl,de}/` subdirs (unlike the flat-file titles), so this version dir names the book in its filenames: `comet-biscuit-1.board.<lang>.md`. Books 2 and 3 have no board cut yet.

## Honest word counts

Counted with `wc -w`. "Story words" = manuscript body only, excluding headings, metadata bullets, blockquote, illustration notes (italic lines), and `[Spread N]` markers (count command: `grep -v -e '^#' -e '^-' -e '^>' -e '^\*' -e '^\[Spread' -e '^$' -e '^---' <file> | wc -w`).

| Language | File | Story words (`wc -w`) | Full file (`wc -w`) |
| --- | --- | --- | --- |
| EN | `comet-biscuit-1.board.en.md` | 187 | 560 |
| NL | `comet-biscuit-1.board.nl.md` | 178 | 535 |
| DE | `comet-biscuit-1.board.de.md` | 176 | 528 |

All three inside the 150–250 board-book target. 12 spreads each (cut from the picture book's 15 — spreads 2–4's mission-briefing comedy and the spread-14 delivery beat are compressed so the toddler arc runs intro → floats → jam out → jam back → hug). NL and DE are native parallel versions written to the same spread grid, not literal translations of the EN cut — each keeps its own edition's established sound-set from `../../DECISIONS.md` (EN Ker-CHUNK / POP / WHOOOSH / bloop / glug; NL KE-TSJONK / PLOP / WHOESJ / bloep / glok; DE KA-TSCHUNK / PLOPP / WUSCH / blubb / gluck) and localized names (Captain Nutmeg / Kapitein Nootmuskaat / Kapitän Muskat; Bloop / Bloep / Blubb; Moon of Muffins / Muffinmaan / Muffinmond; the Comet Biscuit / de Komeetkoek / der Kometenkeks), matching the picture books so the sound is consistent across a family's shelf. DE keeps Blubb feminine ("die kleine leuchtende Blubb"), as in the DE picture book.

## Kept vs dropped (vs the picture book)

**Kept:** the whole crew by name and shtick — Nutmeg on her cushion-stack, Sprocket taping, Barnaby's slow "...perfect." button-press; the Ker-CHUNK sound bracket opening AND closing the book; the zero-g float beat (helmet, crackers); the POP crate lid; the jam escape and return; the ONE core emotional beat — the littlest, shyest crew member saves the day just by glowing (Bloop drifts into the biggest blob, becomes the light the jam follows home); the sticky group hug with Bloop still in the jam. A toddler refrain engine built from the picture book's own sounds: "Wobble, wobble, glug, glug, GLUG!" chanted on the jam-out spread and again (reversed to homecoming) on the jam-back spread, plus Bloop's name-as-sound as a call-and-response through the book.

**Dropped:** all interior narration and joke-scaffolding (the ship going ker-CHUNK "just to show it meant it"; the MISSION-of-COURAGE/GLORY/JAM briefing routine; "The plan was bad. The heart was huge."; "a little sticky, a little glowing, entirely on time"); Barnaby's last-Tuesday running gag (his button-press stays, the time-joke goes — it's a 4–6 joke); the plan-logic spread's explanatory chain (compressed to "Follow the light!"); Bloop's homesickness framing (0–3 gets a shy hello, not a mood); the "NOTHING can stop us" catchphrase-and-payoff structure; spread 14's Tuesday-mornings smell line; the "just a little bit delicious" aside. A new goodnight landing ("Goodnight, stars" / "Welterusten, sterren" / "Gute Nacht, Sterne") replaces the series-hook ending so the cut lands on sleep like a board book should.

This is a standalone read-aloud — a toddler who never sees the picture book gets a complete jam-gets-loose-and-comes-home story with a hug at the end; a family that owns both gets the same crew and the same glowing helper at two ages.

## Format & fulfillment — ⚑ OWNER

- **Board book (0–3), 12 spreads** is the editorial format of this text. Price point and physical format decision stay **⚑ OWNER** — not decided here.
- **⚑ OWNER research — board-book printing:** KDP does **not** print board books (known KDP limitation), so this version cannot ship through the lane's default KDP path. Fulfillment would need IngramSpark or another board-book printer/POD alternative — that comparison and choice is owner research, deliberately NOT decided in this repo.
- **Illustration remains parked** per the track convention: italic art-direction notes only, the seat generates no art.
