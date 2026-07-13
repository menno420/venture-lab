# Session — The Night Kiln (adult cozy-fantasy novella, EN)

> **Status:** `complete`

- **📊 Model:** fable-5 · BOOKS-lane landing worker · night run 2026-07-13
- **session:** ORDER 008 BOOKS clause — first complete manuscript for a vetted concept
- **applied:** candidates/adult-novels/the-night-kiln/{en/the-night-kiln.md,DECISIONS.md}
- **verify:** `python3 bootstrap.py check --strict`
- **started:** 2026-07-13T01:31Z

## ⟲ Previous-session review
Concept lane state inherited clean: the night-kiln vetting packet
(`docs/publishing/vetting/the-night-kiln.md`, PR #105) parks at "no
manuscript" — this session is that write-slice. Siblings tonight are working
`versions/` under the-slow-word and the-weigh-house (disjoint paths, verified
at HEAD 1eb4fe4); no claim collision in `control/claims/`. The weigh-house
manuscript session (2026-07-12) set the adult-novels formatting conventions
(front-matter shape, `# Chapter N — Name` headings, ⁂ scene breaks,
DECISIONS.md) — matched here.

## 💡 Session idea
Run under ORDER 008 (owner night run 2026-07-13: "BOOKS: multiple new book
ideas AND multiple versions of each"). Write the FIRST COMPLETE MANUSCRIPT for
**The Night Kiln** — the adult cozy-fantasy novella concept vetted in
`docs/publishing/vetting/the-night-kiln.md` (landed via PR #105), which parks
at "no manuscript"; this session is the write-slice that unparks it. Target
12,000–16,000 words, full three-act arc, cozy genre contract honored
(low-stakes-but-true conflict, community cast, researched-real pottery craft,
no grimdark). One READY PR, left OPEN on green per tonight's rule 2.

## Work log
- 2026-07-13T01:31Z — Branch `claude/night-kiln-manuscript` from origin/main
  (1eb4fe4); premise check clean (no `candidates/adult-novels/the-night-kiln/`
  at HEAD, no covering claim in `control/claims/`). Born-red card + claim file
  committed (first commit). Manuscript drafting begins.
- 2026-07-13T01:40Z — All 12 chapters drafted in 3-chapter chunks (commits
  2152dee, 067a65c, 281cdc9, 8bf6fd8): complete three-act cozy arc, keystone
  resolution, Wintermark denouement, book-2 hook planted.
- 2026-07-13T01:46Z — DECISIONS.md written; honest `wc -w` = 15,999 (inside
  the 12k–16k slice target after a light trim from 16,011).
  `python3 bootstrap.py check --strict`: only the by-design born-red hold
  remained pre-flip. Card flipped complete, claim file deleted same commit,
  branch pushed for READY PR (left OPEN on green per tonight's rule 2 — no
  auto-merge armed).
