# 2026-07-13 — The Slow Word: Dutch (NL) edition of the novella cut

> **Status:** `complete`

One-line summary: complete literary Dutch translation of the Slow Word
novella cut — *Het trage woord*, all 12 chapters, honest `wc -w` 19,467
(EN source 18,986) — plus mandatory NOTES.md (title decision, glossary,
market note, ⚑ owner gates), landed as one READY PR.

Started: Mon Jul 13 01:04 UTC 2026 (born-red first commit `cfb7298`).
Closed: Mon Jul 13 02:38:34 UTC 2026.

## Intent

Run under ORDER 008 (owner night run 2026-07-13, BOOKS clause: "multiple new
book ideas AND multiple versions of each (different angles, audiences,
lengths) — versions are cheap once the research exists"). This slice adds a
different-**language** audience version: a complete literary Dutch
(Netherlands register) translation of the Slow Word novella cut (18,986-word
EN source at
`candidates/adult-novels/the-slow-word/versions/novella-cut/the-slow-word-novella.md`,
merged via PR #111), landing at
`candidates/adult-novels/the-slow-word/versions/novella-cut-nl/`.

## Scope

One work increment: the NL manuscript
(`versions/novella-cut-nl/het-trage-woord.md`, all 12 chapters, every line
finished prose, committed every 2–3 chapters) + its `NOTES.md` (source
pinning, title decision with alternatives, terminology glossary, honest
`wc -w`, market note with unmeasured items marked, ⚑ owner gates). Premise
verified at HEAD before building: novella cut present on `main`, no existing
nl/Dutch edition under the-slow-word, no live claim covering the-slow-word.
Walls held: no edits to `en/` master, `novella-cut/`, `control/status.md`,
`control/outbox.md`, `control/inbox.md`, `docs/publishing/**`, workflows, or
triggers; no publish, spend, or external action.

## Outcome

- `versions/novella-cut-nl/het-trage-woord.md` — title chosen *Het trage
  woord* over "De trage taal" (the book's central image is the *word*; the
  title sets up Ch 12's "Het woord hield stand"); Netherlands register,
  Samoan terms kept untranslated exactly as the EN keeps them, names
  unchanged, idioms adapted not calqued, invented terminology held
  consistent via a running glossary (de Tragen, neergelegde stenen,
  standvastig/bestendig, de oren, beurtzang).
- Honest `wc -w`: **19,467** NL vs **18,986** EN source (~+2.5%, normal for
  EN→NL; measured, not targeted).
- `versions/novella-cut-nl/NOTES.md` — per versions/README convention;
  NL-market price band $3.99–$5.99 equivalent marked **not measured** for NL
  specifics.
- ⚑ follow-ups (owner-gated / future slice): NL listing needs its own
  vetting/keyword rows under `docs/publishing/` (untouched tonight);
  native-speaker proofread before any listing draft; `versions/README.md`
  index row for this edition (left out to stay inside the claimed path).

## 💡 Session idea
💡 **Translation glossary as a shelf-level artifact.** The NL edition's
term choices (de Tragen, standvastig/bestendig, neergelegde stenen) live
only in this version's NOTES.md. If a DE or FR edition of the-slow-word (or
an NL edition of the FULL novel) is ever cut, each translator re-derives the
same decisions from scratch — and worse, an NL full-novel edition could
silently diverge from this novella's vocabulary. Promote the glossary to
`the-slow-word/TRANSLATION-GLOSSARY.md` with one column per target language,
seeded from this NOTES table, so every future language version inherits and
extends one consistent term ledger instead of forking it.

## Previous-session review
previous-session review: `.sessions/2026-07-12-owner-queue-derive.md`
(PR #101) — genuine strength: it closed the owner-attention scatter by
deriving OWNER-QUEUE.md deterministically from packet §7 state
(byte-identical re-runs, 5/5 inputs parsed, unparseables quarantined under
Manual review instead of normalized); honest nit: its own 💡 already
diagnosed the loop it left open — owner ANSWERS still evaporate in chat with
no DECISIONS-LOG for the deriver to consume, so the queue re-asks decided
questions forever until that follow-up lands.

## Model
- **📊 Model:** fable-5 · worker · books/translation lane

Run under ORDER 008.
