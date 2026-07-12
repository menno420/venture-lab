# Session — The Weigh House vetting packet (Tier-1b crime novella, parks at the §7 owner gate)

> **Status:** complete

- **📊 Model:** Claude (Fable family) · weigh-house-vetting
- **session:** advance the book-catalog second revenue line by ONE non-gated
  increment: run the one-pass title-vetting checklist
  (`docs/publishing/CHECKLIST.md`, PR #90) top-to-bottom for **The Weigh
  House** — the publishing plan's Tier-1b "title-fix first" candidate
  (PR #87 §2, re-tier PR #94) — producing
  `docs/publishing/vetting/the-weigh-house.md`, including WORKING the plan
  §7 title-fix action (fresh collision scan + subtitle recommendation).
  Nothing is published; no account, spend, or click is performed.
- **started (date -u):** Sun Jul 12 22:22:54 UTC 2026
- **completed (date -u):** Sun Jul 12 22:31:30 UTC 2026

## Scope

- `docs/publishing/vetting/the-weigh-house.md` — new worked vetting packet
  (third per-title instance of the checklist template; first crime title).
- `docs/publishing/README.md` — index row so the packet is reachable.
- `control/claims/2026-07-12-weigh-house-vetting.md` — claim (born with
  this card's first commit, deleted at close per
  `control/claims/README.md`).
- This card (born-red first commit; flipped `complete` last commit).
- Does NOT touch `control/inbox.md`, `control/status.md`,
  `control/outbox.md`, `docs/current-state.md`, `PUBLISHING-PLAN.md`, or
  any trigger. No publish/spend/account action — all §7 clicks stay a
  queued owner block.

## Work log

- Synced `main` fresh; branch cut from origin/main HEAD `6d80f71` ==
  `git ls-remote origin main` (post-PR #94).
- Rung-1 pre-emption check: `control/inbox.md` at HEAD in BOTH venture-lab
  (ORDERs through 007) and trading-strategy (through 011) — no newer open
  ORDER pre-empts this slice. `control/claims/` at HEAD held only
  README.md; the single open PR (#95) is a `control/**`-only heartbeat —
  no scope collision.
- Grounding reads: exemplar packet `docs/publishing/vetting/the-slow-word.md`
  @ `6d80f71` (structure mirrored), `CHECKLIST.md` (PR #90),
  `PUBLISHING-PLAN.md` §§1/2/7 (the Tier-1b title-fix action for this
  title: "Subtitle *A Novel*; recheck on KDP"), and the manuscript —
  README + DECISIONS + opening chapters (1–2) and closing chapters (16)
  of `en/the-weigh-house.md` read directly so the blurb is written from
  the text, not the pitch.
- **Word count measured, not quoted:** `wc -w
  candidates/adult-novels/the-weigh-house/en/the-weigh-house.md` →
  **36,434** (matches plan §2; ~60 words of that is front-matter/heading
  overhead). Long-novella band.
- **Title-fix worked (the packet's headline):** three fresh web searches
  (2026-07-12) found **no book named "The Weigh House"** — but every
  book-scoped search drifted to *The Weight* (Jeff Boyd 2023; Andrew
  Vachss 2010, itself crime; Melissa Mendes graphic novel), confirming the
  plan's weigh/weight homophone risk LIVE. Evidence-based call: keep the
  title (renaming away from the manuscript's central De Waag image is
  unwarranted — exact phrase open), add subtitle **"An Amsterdam Crime
  Novel"**; final title+subtitle pick flagged ⚑ OWNER in §1/§7 — nothing
  was retitled by the seat.
- Packet written (badge `plan`, slow-word structure): comps (de Jager /
  Baantjer / van de Wetering / Freeling — Amsterdam police crime shelf),
  $4.99 call (70% tier ≈ $3.49/sale; base case $0), **KU yes** (most
  KU-saturated genre — Amazon runs dedicated KU-eligible crime-thriller
  browse nodes), blurb + 2 categories + 7 keywords, §6a cover brief, §7
  queued six-field ⚑ OWNER-ACTION block. Index row added to
  `docs/publishing/README.md`.
- `python3 bootstrap.py check --strict` pre-push: only red was the
  designed born-red hold on this card.
- Landing: claim + born-red card first commit `9ae09e4` (pushed early for
  claim visibility), packet + index `0fd098c`, PR **#97** opened READY
  (never armed/merged by this lane). Pre-flip CI on `0fd098c`:
  membership-kit-tests + stripe-webhook-test-kit-tests + ledger-drift
  green/running clean; substrate-gate red = the designed hold only.

## Status / outcome

**Complete.** The Weigh House — the plan's next genuine cover-only
candidate — is vetted end-to-end and its Tier-1b blocker (the title-fix)
is **worked with evidence** rather than parked: collision verdict None
(inconclusive), the real risk is weigh→weight search drift, and the
subtitle carries the fix. The title now **parks at §7 (owner clicks) by
design**: KDP account, title+subtitle confirmation, cover, $4.99, publish
+ KU are all owner-only. No publish, spend, account, or external action
was performed by the seat.

## 💡 Session idea

💡 **Epub build smoke (prove the "direct epub conversion path" claim).**
Every adult-title packet now asserts a "clean Markdown → direct epub
conversion path" as a fact, but the repo has never once built an epub —
the claim is untested until the owner is mid-upload, which is the worst
possible moment to learn a heading level or em-dash breaks conversion. A
tiny CI job (or `tools/build_epub.sh` run locally per packet) that
converts each vetted title's `en/*.md` through pandoc into an actual
`.epub` and fails loudly on conversion warnings would turn that packet
claim into a verified artifact — and its output IS the file the owner
uploads at §7 step 4, so the smoke test doubles as the deliverable.
(Distinct from the taken ideas: ledger-drift, classification-drift, §7
parsing, keyword allocation, STEP_SUMMARY echo — this one exercises the
MANUSCRIPT build path, none of them touch it.)

## ⟲ Previous-session review

⟲ previous-session review: `.sessions/2026-07-12-painted-stones-vetting.md`
(PR #93) is the strongest card in the vetting run so far — its headline
(manuscript-vs-plan reclassification) was found mechanically, and its
flag-don't-edit discipline (amendment flagged for the coordinator, plan
untouched) paid off within hours when PR #94 landed the re-tier as its own
reviewed change; that division of labor is worth copying. One honest nit:
its §2 collision re-check describes a "web + storefront-style" scan but
logs only verdicts, not the query strings — this session found the query
text itself is the load-bearing evidence (the weigh→weight drift only
shows up when you can see WHAT was searched), so packets should quote
their searches verbatim, as the-slow-word did and this session's packet
does.

## Deliverable summary

`docs/publishing/vetting/the-weigh-house.md` (+ index row in
`docs/publishing/README.md`): third worked instance of the title-vetting
checklist, first on a crime title, and the first to WORK a Tier-1b
title-fix action. Headline: **no title collision exists** (3 searches
logged), but the plan's weigh→weight drift risk was observed live —
fix is keep-title + subtitle "An Amsterdam Crime Novel", with the final
pick ⚑ OWNER. 36,434 words measured (`wc -w`); $4.99 (≈$3.49/sale, base
case $0); KU yes; blurb written from the read manuscript; cover brief
drafted; six-field ⚑ OWNER-ACTION publish block queued. Landing: READY
PR #97, born-red card first commit `9ae09e4`, packet `0fd098c`, claim
released at close.
