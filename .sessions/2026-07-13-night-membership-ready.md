# Session — Night run: membership-kit to publish-READY + product template extraction (ORDER 008)

> **Status:** in-progress

- **📊 Model:** fable-5 · worker slice · ORDER 008 night-run product lane
- **session:** PRODUCT #1 of the 2026-07-13 night run — drive membership-kit through the ORDER 008 quality floor (built + priced + listing drafted + checkout/format verified + sha recorded + click queued), then extract the repeatable idea→publish-READY path into `docs/products/TEMPLATE.md` so product N+1 gets cheaper.
- **started (date -u):** Mon Jul 13 01:00:36 UTC 2026
- **closed (date -u):** [in progress]

## Scope

- Verify/rebuild `candidates/membership-kit/dist/membership-kit-v0.2.zip` via `package.sh`; run all three kit test suites; unzip-and-inspect the shipped artifact (checkout/format verification).
- Confirm price ($49) and listing copy (`docs/launch/membership-kit/listing-copy.md`) at parity with the SWTK launch assets.
- Record the final zip sha256 where the repo convention puts it.
- Freeze check, then (verified UNFROZEN — PR #22, owner-actions.md@HEAD) queue the ⚑B click as a §7 OWNER-GATE block parsed by `scripts/derive_owner_queue.py`; regenerate `docs/publishing/OWNER-QUEUE.md`.
- `docs/products/TEMPLATE.md` — the distilled SWTK + membership-kit playbook (docs-gate badge + reachability).
