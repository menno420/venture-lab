# 4. The publish gate: the vetting packet

*(This chapter was planned as its own standalone product — a "Fiction
Vetting-Packet Kit" — and scored as a strict subset of this kit's
audience and content at ideation. Its honest verdict was "a chapter
and a template inside this kit, not a standalone SKU," so that is what
it is. You are not missing a fuller version.)*

## "Written" and "publishable" are different states

The most expensive confusion in a self-publishing pipeline is treating
a finished draft as a finished product. The production lane keeps the
two states separate with a per-title **vetting packet**: one markdown
file, seven numbered sections, worked top to bottom, that a title must
pass before its publish steps can even be *queued*. 31 packets were
worked this way in the source repo — including concept-stage packets
written BEFORE their manuscripts existed, which then "park at no
manuscript" honestly rather than pretending readiness.

## The seven sections

`templates/vetting-packet.md` is the skeleton; the grammar:

1. **Title.** Working title + subtitle decision. A subtitle is often
   load-bearing (see the collision scan) — decide it here, don't
   default it.
2. **Collision scan.** Search your exact title as a buyer would.
   Record findings in a table: what surfaced, a severity verdict
   (None / Low / Moderate / Strong), and the ACTION. The verdict
   vocabulary matters: a Moderate for "search space crowded by a
   common noun" is a different failure mode than "a competing novel
   exists," and the packet records which one it is. Real production
   outcomes: a title kept with a MANDATORY fiction-signalling
   subtitle; another title's rename recommended outright after a
   Strong collision (two novels and a game franchise on the name).
3. **Market verification.** Length class (planned vs MEASURED —
   flagged when they differ), comparable titles with links, series/KU
   context, seasonality stated plainly, and the revenue framing rule:
   **unknown-author base case ≈ $0; unit economics only, no
   projections.**
4. **Price band.** Verified band for the category, a recommended
   point in it, and the royalty-tier arithmetic that justifies it.
5. **Packaging.** The production gate: cover-only vs illustrated
   (illustration = a money decision, flagged as such), format spec,
   TRUE length confirmed against the actual manuscript.
6. **Listing copy.** Blurb drafted from the finished text (not the
   pitch), two categories, seven keywords — checked against your own
   catalog's keyword allocation so titles tile the search space
   instead of cannibalizing it (chapter 6).
7. **The publish-click checklist.** Every step that touches an
   account, money, or a publish button, as an explicit checkbox list
   for the human who clicks — with sane defaults pre-picked. The
   packet's output is a QUEUED plan, not an executed launch.

## Why a packet and not a mental checklist

Because the packet catches what enthusiasm skips: the collision scan
that would have shipped a title into a franchise's search shadow; the
"true length unconfirmed — manuscript does not exist" flag that keeps
a concept from being priced as a book; the seasonal window that says
publish by mid-November or wait a year. And because a packet is
*auditable* — every claim carries its evidence inline, so a
second reader (or you, six months later) can re-verify instead of
re-trusting.

## Honesty block

The packet gates *quality of preparation*, not market outcome — a
title can pass all seven sections and still sell zero (the revenue
framing rule exists precisely because of this). And the grammar was
built for one catalog's workflow; treat section 7's click-queue shape
as a pattern, not a law, if you are your own owner.

---

**Sources:** `docs/publishing/vetting/the-twelfth-cake.md@3b159d9`
(worked packet: Moderate common-noun collision + mandatory-subtitle
mitigation, concept-stage "parks at no manuscript," §3 length
amendment, seasonal window, §7 owner-click queue) ·
`docs/publishing/CHECKLIST.md@873d5d9` (the one-pass checklist the
packets instantiate) ·
`docs/publishing/vetting/ultramarine.md@e252b46` (the Strong-collision
rename case) · packet count (31) per `docs/current-state.md@79a1987`.
