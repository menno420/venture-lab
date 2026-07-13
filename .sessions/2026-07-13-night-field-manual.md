# Session — Night run: Agent Fleet Field Manual to publish-READY (ORDER 008, PRODUCT #3)

> **Status:** `in-progress`

- **📊 Model:** fable-5 · worker slice · ORDER 008 night-run product lane
- **session:** PRODUCT #3 of the 2026-07-13 night run — drive the Agent Fleet Field Manual ($39, `candidates/agent-fleet-field-manual/`, launch assets `docs/launch/agent-fleet-field-manual/`) through the ORDER 008 quality floor: built + priced + listing drafted + checkout/format verified + sha recorded + click queued.
- **started (date -u):** Mon Jul 13 01:25:29 UTC 2026
- **closed (date -u):** _in progress_

## Scope

- Locate the full manuscript (chapters/ — 11 chapters exist in-repo) + build tooling (`build.py`, `package.sh`).
- Rebuild `dist/agent-fleet-field-manual-v0.1.zip` via `package.sh`; unconditional double rebuild + sha compare vs the committed dist.
- Confirm $39 price citation; verify listing copy parity/claims against the actual artifact.
- Unzip rebuilt dist to a clean dir; inspect (chapters present, HTML renders self-contained, no secrets/junk).
- Record final zip sha256 (ARTIFACT line + packet §1).
- Queue the click as new §7 packet `docs/publishing/vetting/agent-fleet-field-manual.md`; regenerate `docs/publishing/OWNER-QUEUE.md` from THIS branch's packet set (PR #106 open in parallel — expected conflict flagged in PR body per the parallel-branch rule).
