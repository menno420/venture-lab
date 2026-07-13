# Session — The Halfway Ferry (middle-grade, EN)

> **Status:** `complete`

- **📊 Model:** fable-5 · BOOKS-lane write-slice worker · day run 2026-07-13
- **session:** day-run BOOKS clause — first complete manuscript for a round-2 vetted concept; first MIDDLE-GRADE title in the catalog
- **applied:** candidates/middle-grade/{README.md,the-halfway-ferry/{en/the-halfway-ferry.md,DECISIONS.md,CANON.md}}, docs/publishing/vetting/the-halfway-ferry.md §3 (length re-plan line)
- **verify:** `python3 bootstrap.py check --strict`
- **started:** 2026-07-13T11:57Z
- **closed:** 2026-07-13T12:19Z

## ⟲ Previous-session review
Direct review of `.sessions/2026-07-13-seed-catalogue-manuscript.md`: its
genuine strength is the PROMISE-MANIFEST discipline — extracting the packet's
prose promises (required-verbatim strings, banned inflections, spelling
regime) into a 5-line manifest at slice start and grepping BOTH directions at
flip; that card's own catch ("says it exactly once, knowingly" is still not
"never once says it") proves the method finds what close reading misses. This
session adopted it wholesale: manifest extracted from the packet pitch + §6
before drafting, greps run at flip, method + results recorded in this title's
DECISIONS.md. Honest nit: the seed-catalogue card's `## 💡 Session idea`
section actually contains the session's SCOPE (the write-slice assignment
restated), while the real deduped idea lives in a second heading (`## 💡 Idea
(deduped...)`) — two 💡 headings for one card makes the idea harder to
harvest mechanically and drifts from the single-💡 card grammar of the
night-kiln line; this card keeps scope in the metadata bullets and spends its
one 💡 heading on the idea.

## 💡 Session idea
**Age-band voice telemetry: the first title in every age band should set a
measurable house band, recorded in DECISIONS.md.** This slice opened the
repo's first middle-grade directory, and the MG contract ("warm, funny,
concrete, ages 8–12") is currently enforced by nothing mechanical at all —
the register fences grep vocabulary DOMAINS (space stems, bedtime stems) and
the promise manifest greps PACKET STRINGS, but neither would notice a
manuscript drifting into adult-length sentences or abstract diction while
staying inside every fence. Cheap fix: at flip, compute three age-band
proxies — median sentence length, long-word rate (≥9 letters), dialogue-line
share — and record them in DECISIONS.md next to the honest `wc -w`. This
manuscript measures median 10 words/sentence, 3.1% long-word rate, 151
dialogue-carrying lines — numbers a future MG title (or an expansion pass on
THIS one) can be diffed against, exactly as the adult titles diff against
15k-parity. Deduped against the taken list: distinct from register-stem grep
lists and the keyword-register linter (both test WHICH words appear, not how
sentences are built), from the promise-manifest grep (packet-promised
strings), from the packet-§3 single-source length rule (word COUNT, not
sentence shape), and from chronology ledgers / canon sheets / works indexes
(fact continuity, not voice); logged to the shared ideas-taken ledger before
flip and checked against the sibling's entries.

## Outcome
- Complete manuscript delivered:
  `candidates/middle-grade/the-halfway-ferry/en/the-halfway-ferry.md` —
  *The Halfway Ferry, Book 1: The Fogline Crossing*, 14 chapters, one complete
  crossing, full standalone arc, THE END. Honest count: `wc -w` = **15,173**
  (includes front matter and chapter headings), inside the 15,000–16,000
  brief band. Packet §3 plans ~30k–40k; the run's book-parity default won —
  §3 amended in this same PR (paper-orange precedent), delta flagged here, in
  DECISIONS.md, and in the PR body.
- Packet promises on the page (promise-manifest greps, both directions, at
  flip): the three rules verbatim ("Fares are never money" ×6 /
  "the fog decides the route" ×3 / "count the passengers twice" ×3,
  case-insensitive), the asks-for-a-job beat (blurb + ch. 2), the captain
  paying the harbor cat in stories (ch. 2 and ch. 14, as a frame), Wren
  Tolliver (11), Little Slake, the condemned last jetty, no name/no
  timetable. Banned stems all zero: mystery/detective/clue/friendship, space
  stems, bedtime/lullaby, seaside/sea/ocean (river town throughout), all
  Netherlands stems, plus UK-spelling strays (harbour/grey/colour). Method +
  verbatim results in DECISIONS.md.
- First MG title: `candidates/middle-grade/` created mirroring adult-novels
  (slug dir + minimal README index) — decide-and-flag, recorded in
  DECISIONS.md and the PR.
- Series canon sheet: `CANON.md` per the night-kiln book-2 💡 (laws
  byte-exact, geography, cast, open hooks with planting chapters — the
  Tolliver open-dated fare, the ferry's paid-away name, the *Tollgate*, the
  stepping-stone serial, the crossing-song); update in the same PR as each
  future book.
- Continuity pass fixed real issues (twins' joint fare vs seven-fares
  arithmetic; Old Nol's ridden-before contradiction; a gangplank reference
  for a passenger who never used one); expansion added where thinnest
  (halfway title-lore, fog-pressure stakes, crossing-song), never padding.
  Captain Marl carries no pronoun on the page — held as a series constraint
  in CANON.md.
- ⚑ Publishing untouched: all clicks stay queued in the packet §7 OWNER-GATE
  block (verified: `scripts/lint_owner_gates.py` OK post-merge); keyword rows
  remain name-level; no Netherlands stems (C3 untouched).
- Claim `control/claims/2026-07-13-halfway-ferry-manuscript.md` deleted in
  this flip commit per the claims README.

## Work log
- 2026-07-13T11:57Z — Branch `claude/halfway-ferry-manuscript` from
  origin/main (557b744); premise check clean (no `candidates/middle-grade/`
  at HEAD; live claims cover disjoint surfaces; sibling runs The Twelfth Cake
  in parallel, zero shared paths by construction). Born-red card + claim
  committed (first commit, 96847c6), pushed; READY PR #155 opened.
- 2026-07-13T12:10Z — Full 14-chapter draft in section commits (96aabfb
  ch. 1–4, dfebf11 ch. 5–8, 71afade ch. 9–11, ac32f07 ch. 12–14; 14,282
  words at draft). Expansion + continuity pass committed (568bd70) — honest
  15,173.
- 2026-07-13T12:15Z — DECISIONS.md + CANON.md + category README + packet §3
  amendment committed (051f35d). origin/main re-fetched (0f0b6d2, owner-gate
  lint backport #156); merged in (2bafe3f), zero path overlap; new
  `lint_owner_gates.py` run clean over the amended packet.
- 2026-07-13T12:19Z — Promise-manifest greps green both directions; card
  flipped complete, claim deleted same commit; `python3 bootstrap.py check
  --strict` green; pushed. PR #155 left to the enabler on green — no
  auto-merge armed by this session.
