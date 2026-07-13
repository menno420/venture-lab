# dormouse — board-book cut notes

Version created 2026-07-13 (night run, ORDER 008 "multiple versions of each", second board-book slice). Source: the 12-spread, ages 3–6 read-aloud picture-book manuscripts one level up (`../../dormouse.{en,nl,de}.md`, body ~607–634 words each) — the DREAMLINE spin-off origin story titled "Pippa and the Tear in the Night" (EN) / "Pippa en het Scheurtje in de Nacht" (NL) / "Pippa und der Riss in der Nacht" (DE).

## Honest word counts

Counted with `wc -w`. "Story words" = manuscript body only, excluding headings, metadata bullets, blockquote, illustration notes (italic lines), and `[Spread N]` markers (count command: `grep -v -e '^#' -e '^-' -e '^>' -e '^\*' -e '^\[Spread' -e '^$' -e '^---' <file> | wc -w`).

| Language | File | Story words (`wc -w`) | Full file (`wc -w`) |
| --- | --- | --- | --- |
| EN | `dormouse.board.en.md` | 219 | 621 |
| NL | `dormouse.board.nl.md` | 220 | 629 |
| DE | `dormouse.board.de.md` | 218 | 623 |

All three inside the 150–250 board-book target. 12 spreads each (same count as the picture book — the origin arc is kept whole; the cut is in register and density, not structure). NL and DE are native parallel versions written to the same spread grid, not literal translations of the EN cut — each keeps its own edition's established refrains and sound-set (tuck-in ritual EN "one, two, curl" / NL "een, twee, krul" / DE "eins, zwei, Ringel"; Heron's anchor EN "Gently now. Small and gentle." / NL "Rustig maar. Klein en zachtjes." / DE "Ganz ruhig. Klein und sanft."; bounce EN bounce / NL wip / DE wipp; plip kept in all three), matching the picture books so the sound is consistent across a family's shelf.

## Kept vs dropped (vs the picture book)

**Kept:** Pippa, Mama Dormouse/Slaapmuis/Siebenschläfer, Heron/Reiger/Reiher, the Lamplighter Beetle (as the one-line night clock); the waking-inside-the-dream wonder (bridge of moonlight, canal of stars); the tear with its shimmer/shiver and the cold thread; the fear beat and the wing-around reassurance; the ONE core emotional beat — small and gentle is exactly what mends best; the in/out stitch as a physical toddler chant; the bedtime landing bracketed by the tuck-in ritual (one, two, curl opens AND closes).

**Dropped:** all interior narration and explanation — Heron's hundred-quiet-years backstory, the grown-ups/sleepy-fog exchange, and the closing Mama dialogue ("Did you dream?" — the sleepy-fog joke is a 3–6 payoff; for 0–3 the book ends directly on sleep); the "smallest dormice have the biggest sleeps" thesis line; the she-sees-her-own-bedroom-through-the-tear detail (conceptually too layered for 0–3); the "the way small creatures know things" aside; the DE series-blurb Siebenschläfer wordplay note (grown-up apparatus). No DREAMLINE canon terms appear in the cut — it inherits the picture book's deliberate tot-register (night-watchman, moonlight stitch) one level below canon.

This is a standalone read-aloud — a toddler who never sees the picture book gets a complete brave-little-mender bedtime story; a family that owns both gets the same dormouse and the same gentle heron at two ages.

## ⚑ Pending title/slug pointer (not decided here)

- ⚑ The folder and filenames use the working slug `dormouse` while the manuscripts inside carry the book title "Pippa and the Tear in the Night" (per `../../DECISIONS.md`, which logs the per-language titles). Whether the folder/slug is ever renamed to match the Pippa title is left pending exactly as found — this version keeps the existing `dormouse` slug in filenames and the existing manuscript titles in text, and decides nothing about the rename.

## Format & fulfillment — ⚑ OWNER

- **Board book (0–3), 12 spreads** is the editorial format of this text. Price point and physical format decision stay **⚑ OWNER** — not decided here.
- **⚑ OWNER research — board-book printing:** KDP does **not** print board books (known KDP limitation), so this version cannot ship through the lane's default KDP path. Fulfillment would need IngramSpark or another board-book printer/POD alternative — that comparison and choice is owner research, deliberately NOT decided in this repo.
- **Illustration remains parked** per the track convention: italic art-direction notes only, the seat generates no art.
