# Session — Ultramarine (adult historical novella, Delft 1654)

> **Status:** `complete`

- **📊 Model:** opus-4.8 · high · revenue-lane creative
- **session:** write one original adult-audience historical/literary novella (~25–40k words, English) — book wave 2, fresh premise — and land it under candidates/adult-novels/
- **applied:** candidates/adult-novels/ultramarine/{README.md, INTAKE.md, DECISIONS.md, outline.md, bible/, manuscript/}
- **verify:** `python3 bootstrap.py check --strict`
- **started:** 2026-07-12T15:05Z

## ⟲ Previous-session review

Fresh wave-2 creative slice (owner delegation 2026-07-12). No direct predecessor; this is the first ADULT-audience novel candidate, sitting beside the children's-books and dream-series fiction candidates. It follows the established candidate layout (README + DECISIONS + manuscript files) and the born-red card mechanic: this card is committed FIRST with Status `in-progress`, and flipped to `complete` only as the deliberate last step once the manuscript and `bootstrap.py check --strict` are green.

## 💡 Session idea

An original literary novella centred on the Delft Thunderclap of 12 October 1654 — the gunpowder-magazine explosion that destroyed a quarter of the city and killed the painter Carel Fabritius. Protagonist: Clara Wijnants, a widowed pigment-grinder (verfmaalster) who supplies colour to the painters of Delft. The book braids the cost of beauty (ultramarine ground from lapis lazuli), a woman's precarious economic autonomy in the Dutch Republic, catastrophe and grief, and the "new seeing" of Delft painting that emerged from the wounded city. Target ~28–32k words, English, complete with real resolution.

## Work log

- Branch `claude/wave2-adult-historical`; born-red card committed first (Status `in-progress`).
- Researched the Delft Thunderclap (12 Oct 1654), Fabritius, the Guild of St Luke, and period pigment economics; sources cited in `candidates/adult-novels/ultramarine/bible/world.md`.
- Scaffolded the candidate: README (logline, pitch, cast, content note, publishing owner-gated note, expansion note), INTAKE, DECISIONS (D-0001..D-0006), and world/character/style bible.
- Wrote the complete novella — 12 chapters, three parts, ~27,900 words — in a single locked literary voice: Part One (ch1–4, 8,809w), Part Two (ch5–8, the Thunderclap, 9,164w), Part Three (ch9–12, the Blue Hour, ~9,885w). Assembled a clean single-file reading copy at `manuscript/ultramarine.md`.
- Verified with `python3 bootstrap.py check --strict`; card flipped to `complete` as the deliberate last step before push.
- COST NOTE (honest): the session's worker token cost substantially exceeded the ~150k soft budget — research and drafting workers ran token-heavy (a full 27.9k-word literary manuscript plus sourced research). Flagged for the ledger; future book slices should cap draft-worker fan-out or target the lower word band earlier.
