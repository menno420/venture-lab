# Session — The Painted Stones vetting packet (Tier-1 title #2 → reclassified kids, parks at illustration gate)

> **Status:** `complete`

- **📊 Model:** fable-5 · painted-stones-vetting
- **session:** advance the book-catalog second revenue line by ONE non-gated
  increment: run the one-pass title-vetting checklist
  (`docs/publishing/CHECKLIST.md`, PR #90) top-to-bottom for **The Painted
  Stones** — the publishing plan's Tier-1 title #2 (PR #87, §2) — producing
  `docs/publishing/vetting/the-painted-stones.md`. Headline finding: the
  plan misclassified this title as an adult cover-only standalone; the
  manuscript is a 13-spread kids picture book, so the packet works the
  checklist's KIDS path and parks at the §5 illustration owner-gate.
  Nothing is published; no account, spend, or click is performed.
- **started (date -u):** Sun Jul 12 21:54:26 UTC 2026
- **completed (date -u):** Sun Jul 12 21:57:30 UTC 2026

## Scope

- `docs/publishing/vetting/the-painted-stones.md` — new worked vetting
  packet (second per-title instance of the checklist template).
- `docs/publishing/README.md` — index row so the packet is reachable.
- `control/claims/2026-07-12-painted-stones-vetting.md` — claim (born-red
  first commit, deleted at close per `control/claims/README.md`).
- This card (born-red first commit; flipped `complete` last commit).
- Does NOT touch `control/inbox.md`, `control/status.md`,
  `control/outbox.md`, `PUBLISHING-PLAN.md`, or any trigger. No
  publish/spend/account action — the illustration money-decision and all
  §7 clicks stay queued owner blocks.

## Work log

- Synced `main` fresh; HEAD `c1214b8` == `git ls-remote origin main`.
- Grounding reads: `docs/publishing/PUBLISHING-PLAN.md` (PR #87),
  `docs/publishing/CHECKLIST.md` (PR #90), exemplar packet
  `docs/publishing/vetting/the-slow-word.md` (PR #91),
  `candidates/childrens-books/painted-stones/` (all 3 language files +
  DECISIONS.md).
- **Reclassification verified mechanically:** `candidates/adult-novels/`
  holds only README + the-slow-word + the-weigh-house + ultramarine — no
  adult "Painted Stones" exists; the actual manuscript is the kids picture
  book (13 spreads, ages 4–8).
- Word counts measured (`wc -w`, frontmatter/spread-markers/illustration
  notes stripped): EN 565 (file self-reports 556), NL 570, DE 552 — all in
  the picture-book fiction band (~500–800), category-correct as kids.
- Fresh web + storefront-style collision re-check (2026-07-12): exact title
  open (agrees with plan §7), but component words sit in a crowded
  rock-painting craft-book cluster → verdict Low; series subtitle
  "A Little Notebook Mystery" recommended as differentiator.
- Wrote `docs/publishing/vetting/the-painted-stones.md` (badge `plan`;
  linked from `docs/publishing/README.md` for reachability): kids-path
  checklist run — $12.99 paperback call (≈$4.19/unit after the flat ~$3.60
  premium-color print cost), blurb/2 categories/7 keywords/KU call drafted,
  §6a cover+interior illustration brief, and the ⚑ OWNER-GATE illustration
  money-decision (Commission ~$1,300–$5,200 / AI+disclosure / Park — seat
  recommends Park, owner decides). §7 stays a queued six-field
  ⚑ OWNER-ACTION block superseding the plan §4 block.
- Collision-checked the lane before building: `control/claims/` at
  origin/main HEAD held only README + this claim; the one open PR (#92,
  ledger-drift checker) explicitly avoids `docs/publishing/**`.
- Opened PR #93 READY (non-draft), base `main`; the enabler lands it on
  green — this lane never arms or merges.
- `python3 bootstrap.py check --strict` pre-flip: only red was the designed
  born-red hold on this card; clean at flip.

## Status / outcome

**Complete.** The Painted Stones — the plan's Tier-1 title #2 — is now
**vetted as what it actually is** (kids picture book, not adult standalone)
and **parks at the §5 illustration owner-gate** by design: §§1–4 and §6 are
done with citations, but publication is blocked on the owner's illustration
money-decision. The plan §2/§4 amendment (move the title to the
illustration-gated kids tier) is flagged for the coordinator; the plan
itself was not edited. No publish, spend, account, or external action was
performed by the seat.

## 💡 Session idea

💡 **Plan-vs-manuscript classification drift check.** This slice burned its
opening on discovering that the plan's §2 tier list and the actual
manuscript disagree about what The Painted Stones IS — and the mismatch was
mechanically checkable the whole time: the title sits under
`candidates/childrens-books/` while the plan calls it an adult cover-only
standalone. A tiny advisory checker (same always-exit-0 contract as
`claims-stale` / PR #92's ledger-drift) could cross-reference each plan §2
title against its `candidates/` directory placement (adult-novels /
ya-novels / childrens-books) and nag on disagreement — one line of drift
output would have caught this before any session spent a slice on it, and
it guards every future tier edit for free. (Distinct from the taken ideas:
ledger-drift watches PR numbers; the §7 owner-queue derivation parses
vetting packets; this one diffs the PLAN against the MANUSCRIPT TREE.)

## ⟲ Previous-session review

⟲ previous-session review: `.sessions/2026-07-12-slow-word-vetting.md`
(PR #91) set a genuinely reusable template — this session was a fill-in
exercise for structure and only had to think about substance, which is
compounding working as intended; its measured-not-guessed word-count move
is the right discipline and was copied here. One honest nit: its work log
shows grounding reads only of its OWN title's candidate folder, so it
walked past the plan's misclassification of the very next title in the
queue — a one-line "does Tier-1 title #2 exist where the plan says it
does?" glance at `candidates/` would have surfaced this session's headline
finding a session earlier. (Also, its `📊 Model:` line says "Claude (Fable
family)" where `.sessions/README.md` asks for the family-level form like
`fable-5` — cosmetic, but the README's byte-form examples exist for
grep-ability.)

## Deliverable summary

`docs/publishing/vetting/the-painted-stones.md` (+ index row in
`docs/publishing/README.md`): second worked instance of the title-vetting
checklist, and the first on the KIDS path. Headline: Tier-1 title #2
reclassified — the manuscript is a 13-spread picture book (EN 565 words
measured / 556 self-report; NL 570 / DE 552), not an adult standalone;
plan §2/§4 amendment flagged for the coordinator. Collision Low (exact
title open; craft-cluster crowding), subtitle "A Little Notebook Mystery"
locked; $12.99 paperback ≈ $4.19/unit (base case $0); listing copy +
illustration brief drafted in-repo; ⚑ OWNER-GATE illustration
money-decision queued (seat recommends Park). Landing: READY `claude/`-headed
PR #93, born-red card first commit (853b3ed), packet cfc0423, claim
released at close.
