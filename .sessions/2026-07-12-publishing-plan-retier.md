# Session — PUBLISHING-PLAN re-tier (Painted Stones + Lantern Door → kids track)

> **Status:** `complete`

- **📊 Model:** fable-5 · publishing-plan-retier
- **session:** execute the plan amendment PR #93's vetting packet flagged for
  the coordinator: amend `docs/publishing/PUBLISHING-PLAN.md` §2/§4 to
  correct plan-vs-manuscript drift — re-tier **The Painted Stones** and
  **The Lantern Door** from the Tier-1 adult cover-only track to the Tier-2
  children's (illustration-gated) track on manuscript evidence, withdraw the
  §4 "$4.99 reflowable ebook" Painted Stones block (superseded by the
  packet's §7 kids-path queue), and name the next verified cover-only
  candidates (The Weigh House, Ultramarine). Factual re-tier only — no
  price or strategy changes beyond it; no new vetting packets; no publish,
  spend, account, or click.
- **started (date -u):** Sun Jul 12 22:07:47 UTC 2026
- **completed (date -u):** Sun Jul 12 22:10:34 UTC 2026

## Scope

- `docs/publishing/PUBLISHING-PLAN.md` — §2 tier lists + §4 owner-action
  block amended, evidence-cited per changed line. Badge stays `plan`.
- `control/claims/2026-07-12-publishing-plan-retier.md` — claim (born-red
  first commit, deleted at close per `control/claims/README.md`).
- This card (born-red first commit; flipped `complete` last commit).
- Does NOT touch `control/inbox.md`, `control/status.md`,
  `control/outbox.md`, any trigger, any vetting packet, or any manuscript.

## Work log

- Synced `main` fresh; HEAD `7fc4054` == `git ls-remote origin main`.
- Preemption check: venture `control/inbox.md` max ORDER 007, trading
  `control/inbox.md` (HEAD `135f937`) max ORDER 011 — all within the acked
  range; no newer open ORDER.
- Claims scan: `control/claims/` at HEAD held only README. Live GitHub:
  PR #92 MERGED 21:57:27Z, PR #93 MERGED 21:57:46Z (both by
  github-actions[bot]); zero open PRs — no scope collision.
- Evidence re-measured this session (never assumed):
  - `candidates/childrens-books/painted-stones/painted-stones.en.md` —
    13 `[Spread N]` markers; EN body **565 words** by `wc -w` after
    stripping frontmatter/spread-markers/illustration-notes (file
    self-reports 556; raw file 957) — matches the packet
    (`docs/publishing/vetting/the-painted-stones.md` @ `7fc4054`, §3).
  - `candidates/childrens-books/the-lantern-door/the-lantern-door.en.md` —
    real manuscript EXISTS; 14 spread markers; EN body **624 words** by the
    same `wc -w` method (file self-reports 621; raw 1073); frontmatter:
    read-aloud picture book, ages 4–8, series *The Small Doors*.
  - `candidates/adult-novels/` holds only README + the-slow-word +
    the-weigh-house + ultramarine — no adult manuscript of either
    re-tiered title.
  - `candidates/adult-novels/the-weigh-house/en/the-weigh-house.md` —
    **36,434 words** (`wc -w`); README: Amsterdam crime novella, adult
    content note; prose sampled and confirmed adult crime fiction.
  - `candidates/adult-novels/ultramarine/manuscript/ultramarine.md` —
    **27,865 words** (`wc -w`); adult literary/historical novella (Delft
    1654), content note in file; prose sampled and confirmed.
- Amended `docs/publishing/PUBLISHING-PLAN.md`: §2 Tier-1 list rebuilt
  without the two kids titles + RE-TIER block with the evidence above;
  both titles added to §2 Tier 2; §4 Painted Stones block WITHDRAWN with a
  pointer to the packet's §7 queue; next cover-only candidates named
  (stay Tier 1b until their title fixes — strategy unchanged).
- `python3 bootstrap.py check --strict` pre-flip: exit 1 with the ONLY
  output being the designed born-red hold on this card (+ its unresolved
  auto-draft slots) — no real gate failures; clean at flip.
- Opened PR #94 READY (non-draft), base `main`; the enabler lands it on
  green — this lane never arms or merges.

## Status / outcome

**Complete.** The publishing plan no longer contradicts the manuscript
tree: The Painted Stones and The Lantern Door sit in the Tier-2
illustration-gated kids track where their manuscripts put them, the §4
"$4.99 reflowable ebook" Painted Stones block is withdrawn in favor of the
packet's §7 kids-path queue, and the next cover-only candidates (The Weigh
House, Ultramarine) are named on measured evidence while keeping their
Tier-1b title-fix gates unchanged. Factual re-tier only; no publish,
spend, account, or external action by the seat.

## 💡 Session idea

💡 **Catalog-level keyword & category allocation map.** Vetting packets
each draft "2 categories + 7 keywords" per title in isolation — with 14
titles heading for the same storefront, several will inevitably converge
on the same high-value phrases (e.g. `read aloud mystery for kids`,
literary-fiction generics) and cannibalize each other's placement instead
of covering adjacent shelves. One small living table
(`docs/publishing/keyword-map.md`: keyword/category → title that owns it)
consulted at packet-writing time would make each new packet CLAIM its
phrases the way `control/claims/` claims work — cheap to maintain (one row
per vetted title), and it turns 14 independent listings into a portfolio
that deliberately tiles the search space. (Distinct from the taken ideas:
not a drift checker at all — it's a shared allocation ledger for listing
metadata.)

## ⟲ Previous-session review

⟲ previous-session review: `.sessions/2026-07-12-painted-stones-vetting.md`
(PR #93) is the reason this slice existed and it did the hard part right —
it read the manuscript instead of trusting the plan, measured word counts
mechanically, and (good discipline) flagged the plan amendment for the
coordinator rather than scope-creeping into `PUBLISHING-PLAN.md` from a
vetting slice. One honest gap: having discovered that Tier-1 title #2 was
misclassified BECAUSE its manuscript lives under
`candidates/childrens-books/`, it stopped one directory short — the very
next Tier-1 title (#3, The Lantern Door) sits in the SAME directory with
the same picture-book frontmatter, and a single `ls` would have flagged
both misclassifications in one packet instead of leaving #3 for this
session to re-derive. Its own 💡 (plan-vs-manuscript drift checker) is
precisely the generalization of that miss, so the lesson was learned in
the same breath it was taught.

## Deliverable summary

`docs/publishing/PUBLISHING-PLAN.md` amended (PR #94): §2 Tier-1 list
rebuilt without the two kids titles + RE-TIER evidence block (Painted
Stones 13 spreads / EN 565 words measured, packet @ `7fc4054`; Lantern
Door 14 spreads / EN 624 words measured); both titles added to §2 Tier 2;
§4 Painted Stones owner-action withdrawn → packet §7 supersedes; next
cover-only candidates named as verified (The Weigh House 36,434 words;
Ultramarine 27,865 words — both remain Tier 1b pending title fixes).
Landing: READY `claude/`-headed PR #94, born-red card first commit
(a17c0c7), plan edit 2dbfb99, claim released at flip.
