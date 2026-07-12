# Session — current-state ledger refresh + publishing checklist

> **Status:** `complete`

- **📊 Model:** fable-5 · current-state-refresh
- **session:** one contained docs increment: (a) refresh the stale
  `docs/current-state.md` living ledger (it still showed only membership-kit
  v0.1; missing the 2026-07-12 SWTK Gumroad launch, the 14-title book-catalog
  waves, and the publishing plan), and (b) add
  `docs/publishing/CHECKLIST.md` — the one-pass title-vetting checklist
  template proposed by the publishing-plan card's 💡 idea (title → collision
  scan → market verification → price band → packaging → listing copy →
  owner-click gate), with every real-money / external-account / publish click
  marked as an OWNER-GATE step, never automated.
- **started (date -u):** Sun Jul 12 2026 (born-red first commit)

## ⟲ Previous-session review

Previous-session review: the money-seat ender
(`.sessions/2026-07-12-money-seat-ender.md`, PR #88) cleanly re-stamped
`control/status.md` at then-HEAD 85f23e0 with a neutral close-out and the
⚑ needs-owner queue — but it also shows the split this session closes: the
fast-moving `control/status.md` heartbeat stayed current while the durable
`docs/current-state.md` ledger silently fell a full launch behind. This slice
brings the durable ledger back in line with merged reality (cards + PRs only,
nothing invented).

## Scope

- `docs/current-state.md` — refreshed Stability baseline / In flight /
  Recently shipped from merged PRs and session cards only; badge format kept.
- `docs/publishing/CHECKLIST.md` — new template doc, linked from the
  publishing index and the current-state ledger so it is reachable from the
  docs root.
- `control/claims/2026-07-12-current-state-refresh.md` — claim file (created
  born-red, deleted at close per `control/claims/README.md`).
- This card (born-red first commit; flipped `complete` as the last commit).
- Does NOT touch `control/inbox.md`, `control/status.md`, or
  `control/outbox.md`. No publish, spend, or account action.

## Work log

- Hard-synced `main`: `git fetch origin && git reset --hard origin/main`;
  HEAD `f40aa5b` (PR #89).
- Grounding reads: `.sessions/README.md`, the four 2026-07-12 cards
  (publishing-plan, swtk-launch-log, money-seat-ender, test-purchase-log),
  `docs/current-state.md`, `docs/publishing/README.md` + `PUBLISHING-PLAN.md`,
  `docs/launch/README.md`,
  `docs/launch/stripe-webhook-test-kit/LAUNCH-LOG.md`,
  `control/claims/README.md`, and `git log` PR numbers #67–#89.
- Born-red card + claim committed first; PR #90 opened READY (non-draft),
  base `main`.
- Refreshed `docs/current-state.md`: stability baseline (canonical landing
  path, SWTK verified product, kit v1.15.0); In flight = SWTK measurement
  mode (T+7 2026-07-19 / T+14 kill-rule 2026-07-26, coordinator-owned) + the
  owner-gated book-catalog lane; Recently shipped rebuilt newest-first from
  merged PRs only, each line citing its PR # or path.
- Added `docs/publishing/CHECKLIST.md` (badge `reference` — the checker
  rejected `template` as a badge token) and linked it from
  `docs/publishing/README.md` and `docs/current-state.md`.
- `python3 bootstrap.py check --strict`: only remaining red before the flip
  was the designed born-red hold on this card; fully clean at flip.

## Status / outcome

**Complete.** The living ledger reflects merged reality again (SWTK launch
legs #74/#84/#85/#86, book waves #67–#82, publishing plan #87, kit v1.15.0
#83), and future titles get a one-pass vetting path with hard OWNER-GATE
markers instead of re-deriving the pipeline. Landing: READY `claude/`-headed
PR #90 self-lands on green via the enabler; the lane never arms or merges its
own PR.

## 💡 Session idea

The ledger went stale silently: `control/status.md` has a heartbeat rhythm
that keeps it current, but nothing nags when `docs/current-state.md` drifts.
A cheap advisory checker — compare the highest PR number cited in the
ledger's "Recently shipped" against the newest merged PR on `main` and warn
past a gap threshold (the same advisory pattern as `claims-stale`) — would
surface ledger drift automatically instead of waiting for a session to
notice a launch is missing.
