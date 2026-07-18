# Session — Resync stale bundle D-refs + fix lint_owner_gates DONE marker

> **Status:** `in-progress`

- **📊 Model:** [[fill:model-family-line]]
- **started (date -u):** Sat Jul 18 22:11 UTC 2026
- **branch:** `claude/bundle-dref-resync`
- **base:** `main@1809c7e`
- **purpose:** PR #244 folded the CORS SKU into `docs/publishing/OWNER-QUEUE.md`
  as new **D4**, shifting every alphabetically-later decision ID +1. Two
  sellable-bundle doc families still carry STALE decision-ID (D-ref)
  cross-references from an older numbering (last touched by PRs #231/#239), so
  after the #244 renumber they now MISPOINT to the wrong SKUs' owner-queue rows.
  `bootstrap --strict` does not catch this (it is a semantic cross-ref, not a
  syntax error), but an owner who follows a bundle's owner-actions would land on
  the wrong queue row. This slice resyncs every mispointed bundle D-ref to the
  LIVE OWNER-QUEUE numbering and fixes a half-flipped `— DONE` marker on an
  UNCHECKED ⚑ Owner box that makes `scripts/lint_owner_gates.py` FAIL.
- **source of truth:** `docs/publishing/OWNER-QUEUE.md` (D1–D28, generated) —
  the live map was derived from its `### D<n> — <Title>` headings:
  D6=GitHub Webhook, D7=Idempotency Key, D9=JWT Auth, D15=Pagination,
  D18=Rate-Limit, D19=Shopify Webhook, D20=Slack Webhook.
- **scope (files):** api-robustness-bundle family (owner-actions.md,
  listing-copy.md, vetting packet, MANIFEST.json — and the sibling candidates
  README.md/PROVENANCE.md that carry the same live `queued (OWNER-QUEUE D<n>)`
  pointer) + webhook-verifier-bundle family (same set). Plus the lint DONE-marker
  fix in `docs/publishing/vetting/webhook-verifier-bundle.md`. OWNER-QUEUE.md is
  NOT touched (it is the authority; confirmed byte-identical). No point-in-time
  snapshots (`.sessions/*`, `control/inbox.md`/`outbox.md`, `docs/NEXT-*.md`,
  `docs/current-state.md`) touched. The binary `dist/*.zip` build snapshots are
  left alone (no test compares them to live docs). Plus claim + this born-red
  card + a `control/status.md` heartbeat. Born-red card holds substrate-gate red
  until the completion flip.

## 💡 Session idea

[[fill:idea]]

## previous-session review

[[fill:previous-session-review]]

## Work log

- 2026-07-18T22:11Z — Branch `claude/bundle-dref-resync` from origin/main
  (`1809c7e`); collision check clean. Derived the live D-ref → SKU map from
  OWNER-QUEUE and confirmed the expected corrections. Claim + born-red card
  committed (first commit), pushed. Build begins.
- [[fill:build-log]]
- [[fill:verification-log]]
- [[fill:heartbeat-log]]
- [[fill:flip-log]]
