# Session — The Night Kiln (trilogy) audiobook/narration EDITION-SPEC (gate-free format reach)

> **Status:** `in-progress`

- **📊 Model:** [[fill:model]]
- **started (date -u):** Sat Jul 18 00:16:29 UTC 2026
- **branch:** `claude/night-kiln-audio-spec-2026-07-18`
- **base:** `main@12e221d`
- **purpose:** add a new **gate-free format edition** to the completed EN
  *Night Kiln* trilogy — an **audiobook / narration-ready EDITION-SPEC** a
  narrator/producer could follow, landed as ONE PR. New file
  `candidates/adult-novels/the-night-kiln/versions/audio/EDITION-SPEC.md`,
  covering the three EN books as **one trilogy audio program** (per-book
  audiobooks + an optional single omnibus audio program), mirroring the
  just-merged Paper Orange audio spec (PR #225) and the sibling
  `versions/large-print/` + `versions/omnibus-en/` + `versions/README.md`
  convention. The spec ships **per-book narration script order** (front-matter
  read order, 12-chapter sequence, back matter, what to SKIP), a
  **pronunciation / voice-consistency guide** for the invented proper names
  that recur across three books (grep-verified — the text is entirely English
  invented cozy-fantasy, so there are **no** real Dutch/foreign-language terms
  to translate, stated honestly), **honest per-book AND per-chapter `wc -w`**
  (numbers shown, reconciling exactly to 15,999 / 15,995 / 23,334) with
  runtime @ ~150 wpm + ACX finished-hours per book and a **trilogy total**,
  tone/pacing/character-voice notes, and an explicit owner-gated NOT-included
  section. **Spec only — no recording, no narrator hire, no distribution, no
  spend.** Actual narration/production stays owner-gated.
- **distinct-from:** the `versions/large-print/` + `large-print-book-2/` specs
  are *per-book print* format extensions (6×9, 16pt, KDP royalty math); the
  `nl/` `nl-book-2/` `nl-book-3/` dirs are *translations*; the
  `versions/omnibus-en/` spec is a *single-volume recombination* (higher-AOV
  print/ebook box-set). THIS is the *audio* format extension (script order,
  pronunciation/voice consistency, runtime) off the SAME three EN masters — no
  overlap; near-zero-marginal-cost catalog reach off research that already
  exists ("versions are cheap once the research exists").
- **NL note:** this spec is **EN-only**. An NL narration edition (*De Nachtoven*
  / *De Morgendeur* / *De Oogstslag*, all three NL editions complete under
  `../nl/`, `../nl-book-2/`, `../nl-book-3/`) is a natural mirror but is
  **deferred**: it rides the owner's still-open one-word length-band ratify in
  `LENGTH-BAND-PREP.md` (needs a Dutch narrator + native pronunciation +
  separate ACX/Findaway listing). The EN audio program does **not** depend on
  that ratify and does not touch it.
- **queue note:** editions do **not** get their own §7 vetting packet or
  OWNER-QUEUE row — the large-print sibling created neither, and
  `scripts/derive_owner_queue.py` derives the queue only from vetting packets'
  §7 blocks (confirmed on the slice-3 audio spec #225 and the slice-4 omnibus
  spec #226). This slice adds **no queue row** and regenerates nothing.
  Audiobook **production** (recording, narrator hire, ACX/Findaway
  distribution, any spend) stays owner-gated under the title's existing packet
  gate; this slice invents no publish surface.
- **session:** Born-red card holds substrate-gate red (in-progress badge +
  unresolved fill slots) until the deliberate completion flip; mirrors the
  Paper Orange audio-spec scaffold exactly (identity → per-book script order →
  pronunciation/voice guide → per-book+per-chapter `wc -w` runtime → tone →
  owner-gate → per-`file@sha` provenance footer).

## 💡 Session idea

[[fill:idea]]

## previous-session review

[[fill:prev-review]]
