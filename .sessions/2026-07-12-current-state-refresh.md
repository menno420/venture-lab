# Session — current-state ledger refresh + publishing checklist

> **Status:** `in-progress`

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

Previous-session review: pending — written at close-out.

## Scope

- `docs/current-state.md` — refresh Stability baseline / In flight / Recently
  shipped from merged PRs and session cards only; keep the badge format.
- `docs/publishing/CHECKLIST.md` — new template doc, linked from the
  publishing index and the current-state ledger so it is reachable from the
  docs root.
- `control/claims/2026-07-12-current-state-refresh.md` — claim file (deleted
  at close).
- This card (born-red first commit; flipped `complete` as the last commit).
- Does NOT touch `control/inbox.md`, `control/status.md`, or
  `control/outbox.md`. No publish, spend, or account action.

## Work log

- Hard-synced `main`: `git fetch origin && git reset --hard origin/main`;
  HEAD `f40aa5b` (PR #89).
