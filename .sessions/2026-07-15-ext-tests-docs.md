# Session — EAP extension capability tests + current-state refresh (ORDER 015)

> **Status:** `in-progress`

- **📊 Model:** Fable-class (Claude 5) · worker slice · ORDER 015 capability tests + docs refresh
- **started (date -u):** Wed Jul 15 04:04:52 UTC 2026
- **branch:** `claude/ext-tests-docs-2026-07-15` (PR TBD at birth)
- **session:** Run under ORDER 015 (`control/inbox.md` @ `9ed6a35`: EAP
  extended through 2026-07-21; dormancy 2026-07-14 superseded; "New features
  to test during the extension: overview panel, add_repo, Artifact tool
  (coming), coordinator-comms improvements (coming)"). This slice runs the
  seat-side capability tests that are testable NOW (add_repo, overview-panel
  visibility, coordinator-comms tool inventory — one attempt each, verbatim
  evidence), appends the findings to `docs/CAPABILITIES.md`, and refreshes
  the knowingly-stale `docs/current-state.md` (kit v1.15.0/PR #83 era) to the
  verified live facts (kit v1.17.0, 2026-07-15 reboot on the v3.6 prompt).
- **plan:** (1) born-red card + claim, PR open READY per fleet convention;
  (2) capability tests, ONE attempt each, denials recorded verbatim as
  findings; (3) dated CAPABILITIES.md append citing ORDER 015 as the test
  mandate; (4) current-state refresh — facts only, structure and voice
  preserved, Status badge kept in the first 12 lines; (5) flip this card
  `complete` as the last commit.
- **walls:** no publish, spend, account, or external action; READ-ONLY on
  menno420/fleet-manager (standing fleet-read authorization — never write
  there); no edits to `control/status.md`, `control/inbox.md`,
  `control/outbox.md`, manuscripts, workflows, or triggers; no merge or
  auto-merge action of any kind; no secrets, no exact model IDs
  (family-level names only).
- **verify:** `python3 bootstrap.py check --strict` at flip; substrate-gate
  holds this card born-red by design until the final flip.

## Results (as landed)

- (in progress — filled at flip)

## ⟲ Previous-session review

previous-session review: (written at flip)

## 💡 Session idea

💡 (written at flip, deduped against prior cards)
