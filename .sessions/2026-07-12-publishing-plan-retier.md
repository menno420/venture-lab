# Session — PUBLISHING-PLAN re-tier (Painted Stones + Lantern Door → kids track)

> **Status:** `in-progress`

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
- **completed (date -u):** [[fill:completed]]

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
- `python3 bootstrap.py check --strict` pre-flip: [[fill:gate-result]]
- Opened PR [[fill:pr-number]] READY (non-draft), base `main`; the enabler
  lands it on green — this lane never arms or merges.

## Status / outcome

[[fill:outcome]]

## 💡 Session idea

[[fill:idea]]

## ⟲ Previous-session review

[[fill:previous-session-review]]

## Deliverable summary

[[fill:deliverable-summary]]
