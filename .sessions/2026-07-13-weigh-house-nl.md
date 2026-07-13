# 2026-07-13 — The Weigh House: Dutch (NL) edition

> **Status:** `complete`

One-line summary: complete literary Dutch translation of *The Weigh House*
— *De Waag*, all 16 chapters, honest `wc -w` 36,997 (EN source 36,434) —
plus mandatory NOTES.md AND, unlike the first two NL editions, the
NL vetting packet + keyword-map C4 rows in the SAME PR, landed as one
READY PR (#134).

Started: Mon Jul 13 03:25:57 UTC 2026 (born-red first commit `a64d6c4`).
Closed: Mon Jul 13 04:00:20 UTC 2026. PR #134.

## Intent

Run under ORDER 008 (owner night run 2026-07-13, BOOKS clause: "multiple new
book ideas AND multiple versions of each (different angles, audiences,
lengths) — versions are cheap once the research exists"). This slice adds
the different-**language** audience version for the catalog's second
Amsterdam-set title: the book is set entirely in Amsterdam (Nieuwmarkt,
the canals, the duikteam) and its own DECISIONS.md defers "NL/DE
translations … to a follow-on session" — this is that session, for NL. The
backlog check at HEAD (`12986b7`) showed the-weigh-house/versions/ holding
only the novella-cut; the NL edition was OPEN, and control/claims/ carried
no collision (only the coordinator's inbox-scope night-run claim).

## Scope

One work increment: the NL manuscript
(`candidates/adult-novels/the-weigh-house/versions/nl/de-waag.md`, all 16
chapters, every line finished prose, committed in 2-chapter chunks) + its
`NOTES.md` (source pinning, title decision with alternatives, terminology
glossary incl. gloss reversions, honest `wc -w`, market note with
unmeasured items marked, ⚑ owner gates) + — the PR #131 pattern folded
into the same PR — the NL vetting packet
(`docs/publishing/vetting/de-waag.md`, dated 2026-07-13 collision scan),
7 keyword-map rows under the C4 Dutch-namespace / C3 modern-crime-register
rules, and the derived owner queue regenerated. Walls held: no edits to
`en/` master, `control/status.md`, `control/outbox.md`, `control/inbox.md`,
workflows, or triggers; no publish, spend, or external action.

## Outcome

- `versions/nl/de-waag.md` — title ***De Waag*** (subtitle *Een
  Amsterdamse misdaadroman*): the Waag on the Nieuwmarkt is the book's
  own title anchor (Ch 1 recovery, Ch 16 honest-scale meditation).
  Collision scan **None** for fiction (nearest: Kurpershoek's nonfiction
  history of the building); bare-word searchability handicap named and
  mitigated by the subtitle (the catalog's Lull pattern). Alternatives
  (*Het waaggebouw*, *Zwart water*, *De lijn*) recorded and rejected in
  NOTES.
- Netherlands register throughout; police-diving vocabulary held to real
  NL terms (daallijn, seinlijn/seiner, ademautomaat, ponyfles, halve
  steek, tamp, staand part); motif systems carried whole (tellen in
  drieën; zwaar/gewicht; schoon; 'Goed zo, meisje'; de eerlijke
  weegschaal/de evenaar).
- **Gloss reversions** — where the EN glossed Dutch realities (the Waag
  "the weigh house", Kadaster, grachtenpand, *meisje*), the NL speaks
  plainly again; full list in NOTES per the paper-orange convention.
- Honest `wc -w`: **36,997** NL vs **36,434** EN source (+1.5%; below the
  catalog's +2.5% prior ratio — plausibly because this book's Dutch
  institutional vocabulary was already Dutch in the EN; measured, not
  targeted). The catalog's longest NL edition by ~2×.
- EN continuity wobble found during translation (Prinsengracht flat in
  Ch 2 vs the houseboat from Ch 7 on) — carried over unfixed per
  fixes-propagate-EN→NL, flagged in NOTES for an EN-side patch.
- Vetting packet `plan`, publish-ready up to the §7 owner gate, sequenced
  behind the EN edition; honest gaps (NL comps not pulled, €4.99 band
  inherited, native proofread pending) are explicit §7 rows. Keyword map:
  +7 Dutch rows in the C4 namespace, C3 modern-crime register; the
  `weduwe onderzoekt dood echtgenoot` row logs the Dutch mirror of the
  EN C2 watched adjacency. OWNER-QUEUE regenerated (manual-review none).
- `bootstrap.py check --strict`: only the designed born-red HOLD
  pre-flip. PR #134 opened READY, not draft; per tonight's owner rule the
  seat leaves it OPEN if auto-merge does not arm.

## 💡 Session idea
💡 **A translation-findings defect channel back into the EN masters.**
The NL translation pass is the closest re-read any manuscript in this
catalog gets, and it keeps finding EN-source facts nobody else will:
tonight a real continuity wobble (Ch 2 Prinsengracht flat vs Ch 7+
houseboat), earlier slices found systematic gloss shapes. But the
convention only defines fixes propagating EN → NL — there is no standing
place where a translation slice FILES what it found so the EN master
actually gets patched and re-propagated. Add a per-title
`candidates/<title>/FINDINGS.md` (or a section in DECISIONS.md): one row
per defect found in ANY derived-version pass (translation, novella cut,
large print), with chapter anchor and proposed fix, so the cheapest
proofread the catalog owns stops evaporating into NOTES footnotes.
Distinct from the landed shared-click-hoisting idea (#131, owner-queue
mechanics) and from the gloss-reversion checklist / shelf glossary ideas
(translation tooling) — this one is an EN-master quality loop.

## Previous-session review
previous-session review: `.sessions/2026-07-13-nl-editions-vetting.md`
(PR #131) — genuine strength: its C4 standing rule pre-answered every
Dutch keyword/category question this slice had (namespace, node sharing,
register split, "Oorlogswinter" etiquette), so tonight's keyword rows
were assembly under an existing rule instead of convention-inventing, and
its packet format copied verbatim; honest nit: its packets enshrined the
two-PR rhythm ("the manuscript exists and is complete" as the packet
premise) without saying whether the NEXT NL edition should keep splitting
manuscript and vetting across PRs — this slice decided the obvious
improvement (one PR, manuscript + packet together) but had to infer that
the C4 rule permitted it rather than read it anywhere.

## Model
- **📊 Model:** fable-5 · worker slice · ORDER 008 night-run books lane

Run under ORDER 008.
