# Session — YA dystopian novella (THE UNDERTOW)

> **Status:** `complete`

- **📊 Model:** opus-4.8 · high · revenue-lane creative build
- **session:** ships candidates/ya-novels/the-undertow/ — a complete ~26k-word original YA dystopian sci-fi novella (English), establishing the candidates/ya-novels/ category (mirrors the childrens-books convention).
- **started (date -u):** Sun Jul 12 15:08:08 UTC 2026 (born-red first commit)

## ⟲ Previous-session review

Previous-session review: prior lane work shipped the children's-book concept portfolio and the Star Pirates Book-1 manuscript (candidates/childrens-books/, PRs #45/#47 and the star-pirates manuscript). Book wave 2 opens a new original-fiction category — young-adult novels — with the first complete novella under a new candidates/ya-novels/ convention. Owner delegation 2026-07-12; every creative call is decide-and-flag in DECISIONS.md, owner-vetoable.

## 💡 Session idea

Owner delegation (2026-07-12, book wave 2): write ONE original YA dystopian sci-fi novella (~20–30k words, English) the owner can read and judge — a full story with a satisfying ending, not a fragment or outline. Fresh original premise, no derivative material. Deliver title, one-paragraph pitch, age band (~13–17), chapter structure, content note (YA-appropriate; tension yes, gratuitous content no), and a one-page "if expanded to a full novel" note. NL/DE translation is out of scope (follow-up on approval).

## Scope

- candidates/ya-novels/README.md — new category index.
- candidates/ya-novels/the-undertow/README.md + DECISIONS.md — story index + creative-decision log.
- candidates/ya-novels/the-undertow/en/ — English novella: README (pitch, age band, chapter list, content note) + epigraph + 15 chapters + epilogue (~26k words) + EXPANSION.md (one-page full-novel note).

## Work log

- Born-red session card opened (first commit).
- Recon: hard-synced main (HEAD d7896f0 == remote), read control/inbox.md (tops at ORDER 007, none newer), captured the childrens-books convention + born-red card format.
- Story bible locked (premise, canon, cast, 15-chapter + epigraph/epilogue beat sheet); decisions recorded in candidates/ya-novels/the-undertow/DECISIONS.md.
- Drafted the full novella across five parallel act-writers from the shared bible: epigraph + 15 chapters + epilogue (~27,781 words).
- Continuity/polish pass reconciled canon, tier system, timeline, the scrip-count scale (fixed an inverted Shallow-2/Undertow contradiction), Tess's name, and normalized American spelling across all 17 files.
- Packaged: new candidates/ya-novels/ category (README + INTAKE-lite) and the-undertow/ (README + DECISIONS + en/ README + EXPANSION.md).
- `python3 bootstrap.py check --strict --session-log .sessions/2026-07-12-ya-dystopian-novella.md` GREEN before push; card flipped complete as the last step.

## Status / outcome

Complete. `bootstrap.py check --strict --session-log <this card>` PASS; card flipped complete as the last step. READY (non-draft) PR opened from `claude/wave2-ya-dystopian` into main; nothing merge-related touched (self-lands via the enabler). control/ untouched.
Deliverable: candidates/ya-novels/the-undertow/ — a complete ~27,781-word original YA dystopian sci-fi novella (English) the owner can read and judge, plus DECISIONS.md and a one-page EXPANSION note. NL/DE localization is an owner-approval follow-up (out of scope).
Honest budget: ~0.45M tokens metered (recon + five parallel act-writers + a full-manuscript continuity pass + packaging + CI). This exceeds the ~150k advisory cap because a complete ~28k-word novella with a thorough continuity pass is inherently large (comparable to the three-language Star Pirates build) — reported honestly, not padded.
Still a creative manuscript, not a shippable product: cover art and every publish/print/listing path remain owner-gated OWNER-ACTIONs; no images generated; no revenue claimed.
