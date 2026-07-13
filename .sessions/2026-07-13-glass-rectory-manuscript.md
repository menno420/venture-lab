# Session — The Glass Rectory (adult Victorian gothic ghost novella, EN)

> **Status:** `complete`

- **📊 Model:** fable-5 · BOOKS-lane worker · day run 2026-07-13
- **session:** BOOKS lane — complete manuscript for a round-2 vetted concept
- **applied:** candidates/adult-novels/the-glass-rectory/{en/the-glass-rectory.md,DECISIONS.md}
- **verify:** `python3 bootstrap.py check --strict`
- **started:** 2026-07-13T09:54Z

## ⟲ Previous-session review
Concept lane state inherited clean: the glass-rectory vetting packet
(`docs/publishing/vetting/the-glass-rectory.md`, PR #143, collision Low)
parks at "no manuscript" — this session is that write-slice. Based on fresh
origin/main (847b636, includes PR #143 and #146). Siblings today are on
`claude/night-kiln-book-2` and `claude/marmalade-post-manuscript` (disjoint
paths); `control/claims/` at HEAD holds only round2-idea-packets and the
night-report claim — no collision with this scope, and no
`candidates/adult-novels/the-glass-rectory/` exists at HEAD. Formatting
conventions follow the night-kiln manuscript session (front-matter shape,
`# Chapter N — Name` headings, ⁂ scene breaks, DECISIONS.md).

## 💡 Session idea
Write the FIRST COMPLETE MANUSCRIPT for **The Glass Rectory** — the adult
Victorian gothic ghost novella vetted concept-stage in
`docs/publishing/vetting/the-glass-rectory.md` (landed via PR #143), which
parks at "no manuscript"; this session is the write-slice that unparks it.
Target 15,000–16,000 words (proven adult-novella band; the packet's §3
planned length class is ~20k–30k — the run's parity default wins, flagged
honestly here rather than padded). Classic-register ghost story per the
packet: 1893 moorland parish, Honor Vane keeping house for her curate
brother, the dead rector's glass conservatory wing that never fogs and never
dies, dread by restraint, no gore, emotionally coherent resolution ("about
the things we grow in place of grief"). Standalone, no series claim. One
READY PR, left OPEN on green; the enabler lands it.

## Work log
- 2026-07-13T09:54Z — Branch `claude/glass-rectory-manuscript` from
  origin/main (847b636) in an isolated worktree; premise check clean (no
  `candidates/adult-novels/the-glass-rectory/` at HEAD, no covering claim in
  `control/claims/`). Born-red card + claim file committed (first commit).
  Manuscript drafting begins.
- 2026-07-13T09:58Z — READY PR #148 opened (draft: false) against main;
  claim live on the branch.
- 2026-07-13T10:07Z — All 12 chapters drafted in 3-chapter chunks (commits
  57f21be, 1b588cd, 235d90e, fade38e): complete arc, THE END on the page —
  arrival and the two instructions, the green wing, the Snow history, the
  tapping answered, the garden-book, the keeper's confession, the last
  entry, the after-dark entry and refused temptation, the garden let die,
  discovery and double burial, daylight coda. DECISIONS.md written.
- 2026-07-13T10:12Z — Honest `wc -w` = 15,117 (inside the 15k–16k parity
  target; the packet's §3 ~20k–30k plan deviation flagged in DECISIONS.md
  and this card). `python3 bootstrap.py check --strict` run pre-flip. Card
  flipped complete, claim file deleted same commit, branch pushed — READY
  PR #148 left OPEN on green (no auto-merge armed; the enabler lands it).

## Outcome
Complete manuscript landed-ready in PR #148:
`candidates/adult-novels/the-glass-rectory/en/the-glass-rectory.md` —
**15,117 words** (honest `wc -w`, includes front matter and headings), 12
chapters, full arc, THE END; plus DECISIONS.md. Packet promises honored:
§1 title/subtitle (*The Glass Rectory: A Ghost Story*), §3 premise (1893
moorland parish, Honor Vane, the vanished rector's glass wing) with the
blurb's two instructions delivered verbatim on the page, §6 blurb register
("the things we grow in place of grief" is the resolution). Classic-register
ghost story: dread by architecture/light/glass, no gore; haunting resolves
with meaning (the kept grief is let die; Snow found and buried beside
Eugenie). Standalone, no series hook. Length note: packet §3 planned
~20k–30k; the run's parity default (15k–16k) won — recorded here and in
DECISIONS.md, per the length-budget lesson on today's
paper-orange-graduation card.

## 💡 Idea (deduped vs all 2026-07-13 cards)
**Period manuscripts should land with a chronology ledger in DECISIONS.md.**
This book runs on load-bearing dates (1850 institution, 1859 marriage, 1869
death, 1870 build, 22 Jan 1881 disappearance, 1893 arrival, "twelve years",
"five-and-twenty year" in dialect dialogue), and two internal-consistency
slips were caught only by a hand audit before the final commit. The catalog
now holds several date-driven period titles (paper-orange, weigh-house,
ultramarine, this) whose derived versions multiply every date into N copies.
A required small table for period titles — event · canonical date · chapters
that cite it — filled at manuscript-landing time would make every future
pass (translation, cut, large print) diff dates mechanically. Distinct from
weigh-house-novella-cut's clue-chain audit (plot-clue planting for
abridgments) and weigh-house-nl's FINDINGS.md channel (routing defects found
later back to the master): this one prevents canon date drift at landing,
before derived versions exist to catch or copy it.
