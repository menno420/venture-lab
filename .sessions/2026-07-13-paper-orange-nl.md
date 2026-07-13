# 2026-07-13 — The Paper Orange: Dutch (NL) edition

> **Status:** `in-progress`

One-line summary: complete literary Dutch translation of *The Paper Orange*
(Hunger Winter Amsterdam 1944–45 novella, 15,811-word EN source merged via
PR #122) — *De papieren sinaasappel* — plus mandatory NOTES.md, landed as
one READY PR.

Started: Mon Jul 13 02:41:58 UTC 2026 (born-red first commit).

## Intent

Run under ORDER 008 (owner night run 2026-07-13, BOOKS clause: "multiple new
book ideas AND multiple versions of each (different angles, audiences,
lengths) — versions are cheap once the research exists"). This slice adds a
different-**language** audience version for the most Dutch-market-natural
title of the catalog: the book is set entirely in Amsterdam and the
Hongerwinter is living family memory in the Dutch market. The EN
DECISIONS.md already flagged this as the natural follow-up (its
"NL-translation potential" bullet, incl. the natural NL title *De papieren
sinaasappel*). Landing at
`candidates/adult-novels/the-paper-orange/versions/nl/`.

## Scope

One work increment: the NL manuscript
(`versions/nl/de-papieren-sinaasappel.md`, all 12 chapters, every line
finished prose, committed every 2–3 chapters) + its `NOTES.md` (source
pinning, title decision with alternatives, terminology glossary incl. the
gloss-reversion list, honest `wc -w`, market note with unmeasured items
marked, ⚑ owner gates). Premise verified at HEAD (`ca4c8a1`) before
building: EN manuscript present on `main`, no existing nl edition or
`versions/` dir under the-paper-orange, no live claim covering it. Historical
facts held exactly to the EN text and the DECISIONS.md verified-vs-invented
ledger — translation must not drift facts. Walls held: no edits to `en/`
master, `control/status.md`, `control/outbox.md`, `control/inbox.md`,
`docs/publishing/**`, workflows, or triggers; no publish, spend, or external
action.

## Model
- **📊 Model:** fable-5 · worker · books/translation lane

Run under ORDER 008.
