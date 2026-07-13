# Session — The Twelfth Cake (seasonal novella, EN)

> **Status:** `in-progress`

- **📊 Model:** fable-5 · BOOKS-lane landing worker · day run 2026-07-13
- **session:** day-run BOOKS clause — first complete manuscript for a round-2 vetted concept
- **applied:** candidates/adult-novels/the-twelfth-cake/{en/the-twelfth-cake.md,DECISIONS.md}
- **verify:** `python3 bootstrap.py check --strict`
- **started:** 2026-07-13T12:00Z

## ⟲ Previous-session review
Concept lane state inherited clean: the twelfth-cake vetting packet
(`docs/publishing/vetting/the-twelfth-cake.md`, PR #143) parks at "no
manuscript" (§3/§5 flag true length as unconfirmed) — this session is that
write-slice. Base was fresh origin/main (557b744, includes #151/#152 landed
and their claims pruned by #154); premise check clean: no
`candidates/adult-novels/the-twelfth-cake/` at HEAD and `control/claims/`
held only its README. A sibling runs in parallel on a middle-grade title
(disjoint directory tree — zero shared surface by construction). Direct
review of `.sessions/2026-07-13-salvage-orchard-manuscript.md`: its genuine
strength is that the expansion pass was AIMED — the ~1,500-word repair went
exactly where its blurb/plant→payoff audit was thinnest (the windshield
image made literal, the convent plant paid off) instead of where padding
was easiest, and register-disjointness was verified mechanically, not by
vibes; both disciplines adopted here (promise-manifest greps both
directions, expansion targeted at the thinnest promised beats). Honest nit:
its 💡 (packets encode `register-stems-forbidden:` lines; a checker greps
every `candidates/*/*/en/*.md` against its packet's line) silently covers
only round-2 titles — most shipped works (weigh-house, night-kiln,
slow-word, ultramarine, glass-rectory) predate packets and have no
forbidden-stem source at all, so the checker as specced would pass the
catalog while checking a third of it; the coverage gap belongs in the spec.
Formatting conventions (front-matter shape, `# Chapter N — Name` headings,
⁂ scene breaks, DECISIONS.md) inherited from the weigh-house → night-kiln →
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
*(to be completed at flip)*

## Outcome
*(to be completed at flip)*

## Work log
- 2026-07-13T12:00Z — Branch `claude/twelfth-cake-manuscript` from
  origin/main (557b744); premise check clean (no
  `candidates/adult-novels/the-twelfth-cake/` at HEAD, no covering claim in
  `control/claims/`). Born-red card + claim file committed and pushed;
  READY PR opened.
