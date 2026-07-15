# Session — EAP extension capability tests + current-state refresh (ORDER 015)

> **Status:** `complete`

- **📊 Model:** Fable-class (Claude 5) · medium · docs-only (ORDER 015 capability tests + current-state refresh)
- **started (date -u):** Wed Jul 15 04:04:52 UTC 2026
- **closed (date -u):** Wed Jul 15 04:20 UTC 2026
- **branch:** `claude/ext-tests-docs-2026-07-15` (PR #203)
- **session:** Run under ORDER 015 (`control/inbox.md` @ `9ed6a35`: EAP
  extended through 2026-07-21; dormancy 2026-07-14 superseded; "New features
  to test during the extension: overview panel, add_repo, Artifact tool
  (coming), coordinator-comms improvements (coming)"). This slice ran the
  seat-side capability tests that are testable NOW (add_repo, overview-panel
  visibility, coordinator-comms tool inventory — one attempt each, verbatim
  evidence), appended the findings to `docs/CAPABILITIES.md`, and refreshed
  the knowingly-stale `docs/current-state.md` (kit v1.15.0/PR #83 era) to the
  verified live facts (kit v1.17.0 per PR #199 and `.substrate/state.json`,
  2026-07-15 reboot on the v3.6 prompt).
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
  held this card born-red by design until this flip.

## Results (as landed)

- **add_repo (EAP extension feature) — WORKS** (commit `01eb61d`):
  `list_repos` enumerated 20 owner repos; `add_repo menno420/fleet-manager`
  returned `"status":"appended"`, `"workspace":"/workspace/fleet-manager"`;
  verified by a cross-repo READ via github MCP `get_file_contents` on
  fleet-manager `docs/owner-queue.md` ("successfully downloaded text file
  (SHA: 258179f18427d850739095f587046c54b7dcf982)" at repo HEAD `c356f66`).
  fleet-manager held READ-ONLY throughout — no writes performed.
- **Overview panel — seat-side unverifiable; owner-side feature**: no
  tool/surface resembling an overview/panel/dashboard exposed to this seat
  (ToolSearch "overview panel dashboard" → "No matching deferred tools
  found"; one attempt per the discovery rule).
- **Coordinator-comms inventory (names only, none invoked)**: NO
  `mcp__webagent__*` tools in this seat; claude-code-remote cross-session
  tools PRESENT: send_message, list_events, send_later, create_trigger,
  update_trigger, delete_trigger, fire_trigger, list_triggers,
  list_environments, list_repos, add_repo, register_repo_root,
  subscribe_pr_activity, unsubscribe_pr_activity; harness-level SendMessage
  and Monitor also present.
- **current-state refresh** (commit `05c964c`): kit line corrected v1.15.0
  (PR #83) → **v1.17.0 (PR #199)**, both re-verified from the repo
  (`.substrate/state.json` `kit_version: 1.17.0`; merge `ae24321`); new
  dated reboot snapshot — rebooted 2026-07-15 on the v3.6 prompt, EAP
  extended through 2026-07-21, dormancy 2026-07-14 superseded (ORDER 015),
  routines re-armed (trigger ids in `control/status.md` §4), publish-queue
  pointer `docs/publishing/OWNER-QUEUE.md` unchanged. Structure and voice
  preserved; Status badge remains in the first 12 lines.
- Claim `control/claims/2026-07-15-ext-tests-docs.md` removed in this flip
  commit per convention.

## ⟲ Previous-session review

previous-session review: `.sessions/2026-07-14-kit-upgrade-v1.16.0.md`
(PR #198, the most recent prior card) — its "Lane-owed" ledger paid off
directly this session: it named the exact staleness this slice repaired
(current-state's kit line was still v1.15.0-era two upgrades later), so the
refresh here was lookup work, not archaeology. Honest nit back: its owed
item "heartbeat `kit:` bump in control/status.md (chronic class)" was
overtaken by events — status.md became the dormancy record hours later —
and nothing marks an owed item as void when its target file changes role,
so the debt list reads as live when part of it is moot.

## 💡 Session idea

💡 **Give "coming" features a dated pending-probe row in CAPABILITIES.md.**
ORDER 015 names two features that are announced but not yet probeable
(Artifact tool "coming", coordinator-comms improvements "coming"). Today
the only record of that pending work is the order text itself — a later
session has to re-read the full inbox to know a probe is owed. Cheap
convention: when an order announces a not-yet-testable capability, append a
`pending-probe` row (feature · announced-date · source order · "probe once
when it appears") to the append log, and let the probing session resolve it
in place with the dated finding. Deduped against `.sessions/2026-07-14-*.md`
💡 lines: existing ideas cover drift checkers, fence probes, and ledger
anchors for VERIFIED findings — none tracks announced-but-unprobeable
capabilities as first-class ledger rows.

## Verification

- `python3 bootstrap.py check --strict` run at flip (see PR #203 checks; the
  only designed finding pre-flip was this card's own born-red HOLD).
- Capability tests: ONE attempt each, evidence recorded verbatim in
  `docs/CAPABILITIES.md` append log (2026-07-15 rows).
- Claim removed in this flip commit per convention.
