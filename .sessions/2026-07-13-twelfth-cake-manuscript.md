# Session — The Twelfth Cake (seasonal novella, EN)

> **Status:** `complete`

- **📊 Model:** fable-5 · BOOKS-lane landing worker · day run 2026-07-13
- **session:** day-run BOOKS clause — first complete manuscript for a round-2 vetted concept
- **applied:** candidates/adult-novels/the-twelfth-cake/{en/the-twelfth-cake.md,DECISIONS.md}
- **verify:** `python3 bootstrap.py check --strict`
- **started:** 2026-07-13T12:00Z
- **closed:** 2026-07-13T13:05Z

## ⟲ Previous-session review
Concept lane state inherited clean: the twelfth-cake vetting packet
(`docs/publishing/vetting/the-twelfth-cake.md`, PR #143) parks at "no
manuscript" (§3/§5 flag true length as unconfirmed) — this session is that
write-slice. Base was fresh origin/main (557b744, includes #151/#152 landed
and their claims pruned by #154); premise check clean: no
`candidates/adult-novels/the-twelfth-cake/` at HEAD and `control/claims/`
held only its README. A sibling ran in parallel on a middle-grade title
(disjoint directory tree — zero shared surface by construction; its #155
merged mid-run and was merged in cleanly). Direct review of
`.sessions/2026-07-13-salvage-orchard-manuscript.md`: its genuine strength
is that the repair pass was AIMED — the ~1,500-word expansion went exactly
where its blurb/plant→payoff audit was thinnest (the windshield image made
literal, the convent plant paid off) instead of where padding was easiest,
and register-disjointness was verified mechanically, not by vibes; both
disciplines adopted here (promise-manifest greps both directions; this
slice's pass aimed at the promised beats — and, unusually, cut rather than
added, the draft having run long). Honest nit: its 💡 (packets encode
`register-stems-forbidden:` lines; a checker greps every
`candidates/*/*/en/*.md` against its packet's line) silently covers only
round-2 titles — most shipped works (weigh-house, night-kiln, slow-word,
ultramarine, glass-rectory) predate packets and have no forbidden-stem
source at all, so the checker as specced would pass the catalog while
checking a third of it; the coverage gap belongs in the spec. Formatting
conventions (front-matter shape, `# Chapter N — Name` headings, ⁂ scene
breaks, DECISIONS.md) inherited from the weigh-house → night-kiln →
paper-orange → marmalade-post line.

## 💡 Session idea
Run under the day-run BOOKS lane (owner day run 2026-07-13). Write the
FIRST COMPLETE MANUSCRIPT for **The Twelfth Cake** — the adult
seasonal-holiday historical novella (warm Dickensian, Victorian London)
vetted concept-stage in `docs/publishing/vetting/the-twelfth-cake.md`
(landed via PR #143, collision an honest Moderate for common-noun search
crowding with its mitigation locked: subtitle *"A Twelfth Night Novella"*
is MANDATORY), which parks at "no manuscript"; this session is the
write-slice that unparks it. Honor the packet: London, 5 January 1847,
Pridd's bakery's last night before it is sold, sale papers signed, ovens
going cold, one enormous Twelfth Night cake in the window, twelve
snowbound strangers, the bean-in-the-slice rule ("apprentice or alderman,
no appeals"), and the bean in the most inconvenient slice in London. Warm
hearth register — a book for the week AFTER Christmas (Jan-5, not Dec-25);
no crime plot (Marmalade Post owns the cozy-mystery register), no
folk-dark stems (Hollowtide's reserved pole), no Netherlands stems (C3
untouched). Target 15,000–16,000 words (book-parity default; packet §3
plans ~20k–30k — delta flagged honestly here, in DECISIONS.md, in a §3
amendment in this same PR, and in the PR body). One READY PR, left OPEN
on green.

## 💡 Idea (deduped vs all 2026-07-13 cards)
**Seasonal packets state their sales window in prose; make it a
machine-readable SEASONAL-WINDOW CALENDAR LEDGER.** This slice landed the
catalog's first seasonal title, and its packet carries the whole seasonal
economics in two prose fragments: §3 "sales window ≈ late November – early
January" and a musing that Michaelmas/Midsummer "feast-day novellas" are
possible. Nothing machine-readable says WHICH weeks of the year the
catalog's seasonal shelf covers, so the next seasonal concept will be
pitched from memory — most likely straight into the crowded December shelf
this packet deliberately side-stepped — and the owner's §7 launch-timing
click ("publish by mid-November") gets re-derived by hand each time. Cheap
fix in two parts: (1) seasonal packets carry a `season-window:
Nov-15..Jan-10` line (optionally `launch-by: Nov-15`); (2) a ~15-line
advisory view (same tolerant contract as `check_claims`) renders the
catalog's season windows as a 12-month coverage strip, warning on pile-ups
and showing empty months as pitch targets. Deduped explicitly: not the
promise-manifest grep (packet strings in prose), not register-stem grep
lists (vocabulary domains), not the §3 single-source length rule (numeric
length plans), not the keyword-register linter (keyword phrasing), not the
machine-readable catalog manifest (title inventory, not time), not the
mechanical works index (directory listing), not the chronology ledger
(intra-book dates), not the sibling's age-band voice telemetry (prose
metrics), and not shared-click/fulfillment-gate hoisting (owner-action
mechanics) — this is the CALENDAR as a catalog surface, currently owned by
nobody. One-liner appended to the run's shared ideas-taken scratchpad
before flip, verified distinct against the sibling's entry.

## Outcome
- Complete manuscript delivered:
  `candidates/adult-novels/the-twelfth-cake/en/the-twelfth-cake.md` — *A
  Twelfth Night Novella* (the §2-mandated subtitle on the title page), 12
  chapters, ⁂ scene breaks, full arc, THE END. Honest count: `wc -w` =
  **15,995** (includes front matter and chapter headings), inside the
  15,000–16,000 brief band. Packet §3 plans ~20k–30k; the run's book-parity
  default won — §3 amended in this same PR, flagged here, in DECISIONS.md,
  and in the PR body, not papered over.
- Packet promises on the page, grep-verified both directions at flip:
  "apprentice or alderman, no appeals" ×2 (verbatim in Pridd's rule
  speech); "sale papers signed"; "ovens going cold"; "twelve strangers" ×5;
  "the most inconvenient slice in London" ×2; "the one night a year the
  world agrees to turn upside down" ×2; blurb rewritten from the finished
  text keeping every §6 beat. Banned stems zero: no
  murder/detective/crime-plot register, no dread stems, no Netherlands
  stems, no Santa/Dec-25 iconography (draft hits — "alibis," "dreading,"
  and a "Father Christmas" figure of speech — caught mechanically and
  rephrased). Full grep table in DECISIONS.md.
- Arc: the snow herds twelve strangers into a sold bakery; the cake is cut
  by full custom (bean, pea, the youngest under the table crying slices);
  the bean crowns the incognito purchaser; the feast's misrule extracts his
  1801 window-boy account; the oven proves not cold till Thursday and the
  company bakes Epiphany bread for the street; the king's one law converts
  the inversion into an earned resolution — sale stands, offices upstairs,
  bakehouse leased to Comfort Pell (the succession the pitch promised),
  window covenanted lit every fifth of January, second slice to the
  children at the glass. Standalone; only the packet-permitted gentle
  feast-day possibility in the closing lines.
- Housekeeping landed in the same PR: packet §3 length amendment;
  `candidates/adult-novels/README.md` § Works backfilled to all ten
  adult-novel titles on disk (middle-grade Halfway Ferry deliberately NOT
  listed — different directory); chronology ledger in DECISIONS.md.
- ⚑ Publishing untouched: all clicks stay queued in the packet §7
  OWNER-GATE block; keyword rows remain name-level reservations; C3
  untouched; no spend.
- Honest interruption record: the worker died mid-slice on a transient API
  error with chapter commits local-only; the ender closed born-red PR #157
  as incomplete at 2026-07-13T12:40Z (seam pointer left, branch kept); this
  session resumed on the same branch and this same card, pushed after every
  subsequent commit, and delivered via PR #159 (resume of #157).
- Claim `control/claims/2026-07-13-twelfth-cake-manuscript.md` deleted in
  this flip commit per the claims README.

## Work log
- 2026-07-13T12:00Z — Branch `claude/twelfth-cake-manuscript` from
  origin/main (557b744); premise check clean (no
  `candidates/adult-novels/the-twelfth-cake/` at HEAD, no covering claim in
  `control/claims/`). Born-red card + claim file committed (first commit,
  bc2013c) and pushed; READY PR #157 opened.
- 2026-07-13T12:10Z–12:25Z — Front matter + chapters 1–4 committed
  (08d8d13); chapters 5–12 committed (4fa9e3f, first full count 17,599 —
  over the band). Both commits were LOCAL-ONLY when the worker died on a
  transient API error; at 12:40Z the ender closed PR #157 as incomplete
  (only bc2013c was on the remote), keeping the branch with a seam resume
  pointer.
- 2026-07-13T12:44Z — Resumed in the same worktree; local commits verified
  intact. Tightening + continuity pass in place of an expansion pass
  (055d848, 2fae4a7): ~1,750 words cut from ornamental density, none from
  promised beats; continuity fixes (snow-depth progression ch2→ch3, Kit's
  age in a ch6 aside, Crail's age arithmetic vs the 1801 window, Lady Day
  possession terms unified, the ch-7 story-count made honest — ten accounts
  on the page + hosts ruled exempt before "Eleven paid", strangers-vs-slices
  counts in the ch-11 law); register fix ("Father Christmas" figure of
  speech replaced). Pushed after each commit from here on.
- 2026-07-13T12:59Z — Promise-manifest greps run both directions; two
  banned-stem draft hits ("alibis", "dreading") rephrased. DECISIONS.md +
  packet §3 amendment + adult-novels README works backfill committed
  (3f1899d) and pushed. origin/main re-fetched (abf1f23: sibling's #155 +
  #156); merged in (2d26c58), zero overlap with this slice's paths. READY
  PR #159 opened (resume of #157).
- 2026-07-13T13:05Z — Final `wc -w` 15,995. Card flipped complete, claim
  file deleted same commit; `python3 bootstrap.py check --strict` green;
  branch pushed; PR #159 left to the enabler — no auto-merge armed by this
  session.
