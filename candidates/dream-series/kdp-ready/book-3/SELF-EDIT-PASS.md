# Self-Edit Pass — *The Fourth Hour Comes* (Lull, Book Three)

> **Status:** `draft` · Proofreading + continuity read across all 12 chapters
> (`book3/ch01.md`–`ch12.md`, ~22,760 words), done for the KDP compile
> (`MANUSCRIPT-KDP.md`). Records (a) mechanical fixes **applied** to the
> compiled file, (b) continuity / scope questions **flagged, not auto-fixed**,
> and (c) the caveat that this is not a professional proofread.
>
> **The canonical source chapter files were NOT modified.** Every fix below was
> applied only to the compiled `MANUSCRIPT-KDP.md` (via `sed` after `cat`).

---

## (a) Mechanical fixes APPLIED (to `MANUSCRIPT-KDP.md`)

1. **Stray/corrupt token `t4` — Chapter Three ("The Holiest Site").**
   - **Before:** "…the tired clever librarians, the darners, the **t4 old men** who keep the true record…"
   - **After:** "…the tired clever librarians, the darners, the **old men** who keep the true record…"
   - **Rationale:** `t4` is not a word and reads as a garbled/stray token in the middle of an appositive list; the minimal safe correction is to drop it, leaving a clean parallel list. Applied by targeted `sed` on the full sentence (single occurrence in the whole manuscript).

2. **Removed the per-chapter draft sublines (structural / build normalization) — all 12 chapters.**
   - Each source chapter opened with a status subline `*Lull, Book Three · draft*` on line 3. All 12 were removed from the compile (the subline line plus its trailing blank line), so each chapter now reads `# Chapter N — Title` → blank → body.
   - **Rationale:** the subline carries a **"draft"** status marker that must not ship in a publish-ready file, and the new front matter already supplies the series/book line (`**Lull · Book Three**`). This matches the prep source-pack build note ("drop the `*Lull, Book Three · draft*` sublines for KDP"). Chapter **prose is preserved byte-for-byte** otherwise.

*Chapter headings were already consistent and correctly formatted in the source
(`# Chapter One — …` through `# Chapter Twelve — …`); no heading normalization was
needed. No other mechanical issues were found: automated scans for doubled words,
double spaces, and broken headings came back clean, and the quote/apostrophe style
is uniformly straight-ASCII across all 12 chapters (a consistent house style — left
as-is; typographic quote-curling, if wanted, is a downstream typesetting step, not
a proofreading fix).*

---

## (b) Continuity / scope questions FLAGGED (not auto-fixed)

1. **⚑ Craft leak — a repo filename appears in the narrator's prose (Chapter One).**
   - Text: *"…the year the seal is supposed to set, **world.md** would say, if **world.md** were a book you were allowed to read."*
   - `world.md` is the literal filename of the series bible (`bible/world.md`). Confirmed this leak is in **narrative prose in `ch01` only** — every other `world.md` reference in the series lives in planning files (`outline.md`, `part*-direction.md`), where it belongs. In-story it reads as a build/craft artifact that breaks the fiction.
   - **Not auto-fixed** because the correction is an authorial choice, not a mechanical typo (e.g. replace with an in-world phrase such as *"the old books would say"* / *"the Vigil's own books"*, or delete the clause). **Flag for the author/owner** before publish.

2. **⚑ Genre-scope mismatch in the publishing keyword-map (not in this book's copy).**
   - The manuscript is unambiguously **MG/YA Percy-Jackson-lane portal fantasy** (Sam, the Vigil/Palimpsest factions, Anchoring, Pompeii, the Lull) — confirmed by a full read. The book's own listing and description are correctly scoped to that.
   - However, per the prep pack, `docs/publishing/keyword-map.md` **§3 reserves the "Lull" niche as** *"Quiet/literary novella — stillness, small-town hush."* That is **mis-scoped** for this series, and the drafted keywords (`middle grade fantasy adventure`, `portal fantasy`, `Percy Jackson readalike`, `Pompeii fantasy`) do not match it.
   - **Action for owner (not done here — out of this task's scope):** re-scope the §3 row to MG portal fantasy before promoting the 7 keywords to §1 ownership rows, and check the possible **title collision** — "Lull" as a literary-novella name vs "Lull" as the MG series title (`DECISIONS.md` D-001). Mirrored in `KDP-METADATA.md`.

3. **Trilogy-finale resolution / timeline consistency with Books 1–2 — checked, no contradictions found.**
   - **The clock/date:** the nightmare begins at 4 a.m. on Sam's **sixth** birthday and the finale lands on his **thirteenth** — "counting… for seven years" (chs 1, 12). 6 → 13 = 7 years. Consistent.
   - **Joris under "forty years":** stated consistently across chs 2, 3, 4, 5, 6, 9, 10, 11 — no drift.
   - **Lost-faces cost:** father's face lost in Book 1 ("went first, in the museum," ch02) and mother's face in Book 2's backwash (ch01: "my mum whom I couldn't picture") — the "two smooth places" (chs 1, 7) are internally consistent and restored together in ch10. Consistent with the series-arc escalation (Book 1 = father's face, Book 2 = mother's face).
   - **Vibia** ("thirteen for two thousand years," the first anchor): introduced in the finale only — confirmed she appears in `book3` only, correctly (not seeded by name earlier). Her arc (chs 5–11) is internally consistent.
   - **Names vs canon:** cross-checked against `bible/names.md`, `series-arc.md`, `DECISIONS.md` (D-003/D-004), and the earlier books. **Lena Marchetti** (Book 1 ch12 → Book 2 ch05 → Book 3 ch03) and **Fenna Bakker** (Book 2 ch09 → Book 3 ch07) carry consistent surnames across books; **Serafina** and **Nico** (Venetian cast) are consistent Book 2 → Book 3. The recommended bible name-set (Palimpsest / Vivid / Anchoring / the Lull / the Vigil) is used throughout. No name conflicts found. *(Note: `bible/names.md` documents only the four owner naming-blanks; Serafina/Nico/Vibia are Book-2/3 cast defined in `DECISIONS.md`/`series-arc.md`, so their absence from `names.md` is expected, not a discrepancy.)*
   - **Finale contract:** every open series thread the outline promises to resolve (the date; Pompeii; the Lantern Man = Joris *and* future-Sam; Vibia; the Vigil's 1630 forgery; Lena's allegiance; the restored parent-memories; the confession-frame close) lands on-page. No trilogy-length thread is left dangling.

---

## (c) Caveat — this is NOT a professional proofread

> **This pass was a careful editorial read by the build worker, not a
> professional edit.** It does not replace a **native-speaker proofread and
> copyedit** before publication. It covers obvious mechanical errors and
> internal/continuity consistency only; it does not guarantee catching every
> typo, punctuation nuance, or line-level infelicity, and it makes no
> line-editing or developmental changes. The one craft leak in §b(1) and the
> keyword-map scope issue in §b(2) are **owner/author decisions** left
> deliberately untouched. Treat a professional proofread (and the missing
> vetting packet) as required gates before any publish.

**Net:** 2 mechanical fixes applied (1 stray token in ch03; 12 draft sublines removed for the compile); 2 items flagged for author/owner (a `world.md` prose leak in ch01; the mis-scoped keyword-map §3 "Lull" niche). Timeline, finale resolution, and character names are internally consistent with Books 1–2; no contradictions found.
