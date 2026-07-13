# Session — The Marmalade Post (adult cozy mystery, book 1, EN)

> **Status:** `complete`

- **📊 Model:** fable-5 · BOOKS-lane landing worker · day run 2026-07-13
- **session:** day-run BOOKS clause — first complete manuscript for a round-2 vetted concept
- **applied:** candidates/adult-novels/the-marmalade-post/{en/the-marmalade-post.md,DECISIONS.md}
- **verify:** `python3 bootstrap.py check --strict`
- **started:** 2026-07-13T09:55Z
- **closed:** 2026-07-13T10:19Z

## ⟲ Previous-session review
Concept lane state inherited clean: the marmalade-post vetting packet
(`docs/publishing/vetting/the-marmalade-post.md`, PR #143) parks at "no
manuscript" — this session is that write-slice. Siblings today worked
`claude/night-kiln-book-2` and `claude/glass-rectory-manuscript` (disjoint
paths, verified at HEAD 847b636 and re-verified after both merged mid-run:
no overlap with this slice's paths); no claim collision in `control/claims/`.
Direct review of `.sessions/2026-07-13-marginalia-society-manuscript.md`:
its 💡 ("when a draft is short, audit the plant→payoff table first — length
repairs go where the clue audit is thinnest") was the rare directly-executable
kind and was executed here verbatim — the first count came in at 14,380, and
the ~660-word repair went precisely where the clue audit was thinnest
(the impostor phone call and committee letter were never attributed in the
confession; the spare-stamp counter-courtesy was asserted in ch. 9 but never
planted; the four-mouths-one-grammar observation had no trace) — raising
fair-play quality instead of diluting it. Honest nit on the same card: it
recommends writing the rule into "the YA manuscript conventions", but this
session needed it on the ADULT lane — the rule is lane-agnostic and its
proposed home was too narrow. The weigh-house → night-kiln → paper-orange
formatting conventions (front-matter shape, `# Chapter N — Name` headings,
⁂ scene breaks, DECISIONS.md) were matched throughout.

## 💡 Session idea
Run under the day-run BOOKS lane (owner day run 2026-07-13). Write the FIRST
COMPLETE MANUSCRIPT for **The Marmalade Post** — the adult cozy-mystery
series concept vetted in `docs/publishing/vetting/the-marmalade-post.md`
(landed via PR #143), which parks at "no manuscript"; this session is the
write-slice that unparks it. Target 15,000–16,000 words (book-parity default;
the packet §3 plans ~45k–55k — the departure is flagged honestly here and in
DECISIONS.md, per the paper-orange-graduation card's length-budget rule).
Cozy MYSTERY contract: a fair-play puzzle with planted clues, red herrings,
and a full reveal; no gore, low-stakes-high-heart; series shape one
misdelivered parcel per book with a book-2 hook that does not cliffhang the
main case. One READY PR, left OPEN on green.

## 💡 Idea (deduped vs all 2026-07-13 cards)
**The adult-novels catalog index is silently stale — index the works list
mechanically.** `candidates/adult-novels/README.md` § Works still lists ONE
title (the-weigh-house) while the directory now holds seven (night-kiln,
paper-orange, slow-word, ultramarine, glass-rectory, marmalade-post landed
without adding their one-line entry), because no write-slice's claim scope
covers the shared README — the same zero-shared-surface construction that
makes manuscript slices conflict-free by design guarantees the index rots.
Cheap fix in two parts: (1) a ~15-line advisory check (same tolerant contract
as `check_claims`) that diffs `candidates/adult-novels/*/` slug dirs against
README § Works bullets and warns on unlisted works; (2) a convention line in
that README: the NEXT slice to touch the shared file (graduation or docs
lane, not manuscript lanes) backfills all missing bullets in one commit.
Distinct from the graduation checker (packet↔manuscript existence), the
CANON.md idea (cross-book fact continuity), and the length-budget rule
(plan forking) — this is catalog *discoverability* drift, and it is already
six titles deep.

## Outcome
- Complete manuscript delivered:
  `candidates/adult-novels/the-marmalade-post/en/the-marmalade-post.md` —
  12 chapters, full fair-play arc, THE END. Honest count: `wc -w` =
  **15,040** (includes front matter and chapter headings), inside the
  15,000–16,000 brief band. Packet §3 plans ~45k–55k; the run's book-parity
  default won — flagged here, in DECISIONS.md, and in the PR body, not
  papered over.
- Mystery contract kept: solution (the show treasurer collected the 2016
  cash box at 9:40 p.m. and let a dead man and an innocent woman carry ten
  years of blame) is deducible from planted clues — the decade-old house
  name, the hoarded 2015 stamps + spare-stamp counter courtesy, the Hedges
  counter hitch, the Truro postmark + Porthgullow prize sticker, the exact
  £3,147 slip against the village's "count was never finished", the keyed
  re-locked nothing-taken break-in aimed at the pre-refit pending drawer,
  the 2016 "no police" minutes, and the letter's "never you mind the back
  pages". Two red herrings resolved honestly (Prue: recipe plagiarism;
  Martin: the mistaken bee-money donations). Bloodless throughout.
- Series shape per packet: one parcel per book; book-2 hook planted in the
  closing page (the seawater-stained box for *Miss Patience Crumb, The
  Quiet Woman* — a pub gone since 1963) with the main case fully resolved.
- ⚑ Publishing untouched: all clicks stay queued in the packet §7
  OWNER-GATE block; keyword-map rows remain name-level reservations.
- Claim `control/claims/marmalade-post-manuscript.md` deleted in this flip
  commit per the claims README.

## Work log
- 2026-07-13T09:55Z — Branch `claude/marmalade-post-manuscript` from
  origin/main (847b636); premise check clean (no
  `candidates/adult-novels/the-marmalade-post/` at HEAD, no covering claim in
  `control/claims/`). Born-red card + claim file committed (first commit,
  f646c6f) and pushed; READY PR #149 opened.
- 2026-07-13T10:11Z — All 12 chapters drafted in 3-chapter chunks (commits
  00ef7de, 3ff4fe4, defd24f, 0c1a3c5): complete fair-play cozy arc, decoy
  night-watch catch, show-day public accounting, churchyard denouement,
  book-2 hook planted. First count 14,380 → clue-audit expansion (phone-call
  and committee-letter attribution, spare-stamp plant, seeded-sentence
  trace) → honest 15,040.
- 2026-07-13T10:15Z — DECISIONS.md written (1637fde). origin/main re-fetched
  (ca7f120: siblings' #145/#148 + #150 merged); no overlap with this slice's
  paths. `python3 bootstrap.py check --strict`: only the by-design born-red
  hold remained pre-flip. Card flipped complete, claim file deleted same
  commit, branch pushed; PR #149 left OPEN on green — no auto-merge armed.
