# 2026-07-13 — The Paper Orange: Dutch (NL) edition

> **Status:** `complete`

One-line summary: complete literary Dutch translation of *The Paper Orange*
— *De papieren sinaasappel*, all 12 chapters, honest `wc -w` 16,203 (EN
source 15,811) — plus mandatory NOTES.md (title decision, glossary with
gloss-reversion list, market note, ⚑ owner gates), landed as one READY PR.

Started: Mon Jul 13 02:41:58 UTC 2026 (born-red first commit `0b47c35`).
Closed: Mon Jul 13 03:04:44 UTC 2026.

## Intent

Run under ORDER 008 (owner night run 2026-07-13, BOOKS clause: "multiple new
book ideas AND multiple versions of each (different angles, audiences,
lengths) — versions are cheap once the research exists"). This slice adds a
different-**language** audience version for the most Dutch-market-natural
title of the catalog: the book is set entirely in Amsterdam and the
Hongerwinter is living family memory in the Dutch market. The EN
DECISIONS.md already flagged this as the natural follow-up (its
"NL-translation potential" bullet, incl. the natural NL title *De papieren
sinaasappel*). Landed at
`candidates/adult-novels/the-paper-orange/versions/nl/`.

## Scope

One work increment: the NL manuscript
(`versions/nl/de-papieren-sinaasappel.md`, all 12 chapters, every line
finished prose, committed in 3-chapter chunks) + its `NOTES.md` (source
pinning, title decision with alternatives, terminology glossary incl. the
gloss-reversion list, honest `wc -w`, market note with unmeasured items
marked, ⚑ owner gates). Premise verified at HEAD (`ca4c8a1`) before
building: EN manuscript present on `main` (PR #122), no existing nl edition
or `versions/` dir under the-paper-orange, no live claim covering it.
Historical facts held exactly to the EN text and the DECISIONS.md
verified-vs-invented ledger — no fact drift in translation. Walls held: no
edits to `en/` master, `control/status.md`, `control/outbox.md`,
`control/inbox.md`, `docs/publishing/**`, workflows, or triggers; no
publish, spend, or external action.

## Outcome

- `versions/nl/de-papieren-sinaasappel.md` — title *De papieren
  sinaasappel* (subtitle *Een roman over de Hongerwinter*), exactly as the
  EN DECISIONS.md pre-named it; alternatives (*Oranje*, *Achter het
  behang*) recorded and rejected in NOTES. Netherlands register, names
  unchanged, idioms adapted not calqued, printing-trade vocabulary held to
  period Dutch terms (trapdegel, zethaak, smoutwerk, nummerateur,
  gedistribueerd).
- **Gloss reversions** — where the EN glossed Dutch realities for
  Anglophone readers, the NL speaks plainly again (noodkacheltje,
  Koninginnedag, hongertocht, Landwacht, onderduikers, the pencil word
  *Beter.*); the full list is in NOTES.
- Honest `wc -w`: **16,203** NL vs **15,811** EN source (~+2.5%, matching
  the ratio measured on the catalog's other NL edition; measured, not
  targeted).
- `versions/nl/NOTES.md` — mirrors the novella-cut-nl NOTES convention;
  NL-market specifics explicitly **not measured** (no comps, no NL
  storefront keyword work tonight).
- ⚑ follow-ups (owner-gated / future slice): publishing owner-gated per
  the vetting packet §7; NL listing needs its own vetting/keyword rows
  under `docs/publishing/` (untouched tonight); native-speaker proofread
  before any listing — weighted extra for this title because the NL
  audience includes readers with direct family memory of the events.

## 💡 Session idea
💡 **The gloss-reversion list is a reusable translation asset for
period-Dutch books.** This EN manuscript systematically glosses Dutch
period terms (noodkacheltje, hongertocht, Landwacht, persoonsbewijs...),
and the NL edition systematically un-glosses them — a mechanical,
enumerable transform. The catalog already has two Amsterdam-period books
(the-paper-orange, the-weigh-house) and a versions strategy that makes NL
editions cheap. Extract the reversion pattern into a shared
`docs/corpus/nl-gloss-reversion-checklist.md` (term, EN gloss shape, NL
plain form, false-friend warnings) so the next NL edition starts from a
checklist instead of re-deriving which glosses to dissolve — and so an EN
editor writing book N+1 knows that glossing consistently is what makes the
future NL edition mechanical.

## Previous-session review
previous-session review: `.sessions/2026-07-13-slow-word-novella-nl.md`
(PR #126) — genuine strength: it set the full convention this slice reused
wholesale (versions/<x>-nl layout, NOTES shape with title-decision +
glossary + honest-wc + not-measured market note, born-red→flip card
rhythm), which cut this session's overhead to near zero; honest nit: its
own 💡 (promote per-version glossaries to a shelf-level
TRANSLATION-GLOSSARY.md) is still unlanded, and tonight proved the point —
this session re-derived address-register and ledger-idiom policy from
scratch that a shared glossary convention would have handed it.

## Model
- **📊 Model:** fable-5 · worker · books/translation lane

Run under ORDER 008.
