# Session — Night run: template-packs to publish-READY (ORDER 008, PRODUCT #2)

> **Status:** `complete`

- **📊 Model:** fable-5 · worker slice · ORDER 008 night-run product lane
- **session:** PRODUCT #2 of the 2026-07-13 night run — drove the Agent-Workflow Template Pack ($19 PWYW, ⚑D, UNFROZEN by PR #22) through the ORDER 008 quality floor: built + priced + listing drafted + checkout/format verified + sha recorded + click queued.
- **started (date -u):** Mon Jul 13 01:13:59 UTC 2026
- **closed (date -u):** Mon Jul 13 01:22 UTC 2026

## ⟲ Previous-session review

Previous session (`.sessions/2026-07-13-night-membership-ready.md`, on the still-open PR #106 branch at review time): strong slice — its rebuild caught a genuinely stale committed dist carrying a missing security fix ("presence is not freshness"), and its §7 packet + TEMPLATE.md extraction made this session measurably cheaper: the packet grammar, ARTIFACT-line convention, and §-by-§ structure were reused here nearly verbatim, exactly the N+1 cost drop ORDER 008 asked for. Two notes: (1) its card's 💡 (CI step that rebuilds each `package.sh` dist and fails on sha mismatch) is validated by this session — the same double-rebuild check ran here in under a minute and this time proved freshness rather than staleness, so the check is cheap in both outcomes; still unbuilt, worth picking up. (2) Landing membership-kit.md and OWNER-QUEUE.md on a branch that stayed OPEN (per the night rule) means every subsequent packet session regenerates OWNER-QUEUE from a different packet set — this session's queue (11 packets) lacks membership-kit by construction, guaranteeing a merge conflict one side must regenerate away. Follow-up noted for the coordinator: after both PRs land, one `derive_owner_queue.py` re-run on main reconciles it deterministically.

## 💡 Session idea

The honest-null pattern for zero-runtime products: "run any tests it has" degenerates gracefully when there are none — the floor-equivalent is executing what the buyer will execute (the 3 shipped hooks ran under their declared bash shebang, advisory output, exit 0) plus format lint (JSON parse, `sh -n`, UTF-8/non-empty) from the *extracted artifact*, not the source tree. Worth a TEMPLATE.md stage-6 clause: when a product has no test suite, say so in the packet as an explicit `[x] Honest null` line and substitute artifact-side execution evidence — never leave the "tests" row silently absent. (TEMPLATE.md is not at HEAD — PR #106 open — so this is queued as a refinement in the run report, not appended.)

## Scope

- Rebuild `candidates/template-packs/dist/template-packs-v0.1.zip` via `package.sh`; verify byte-reproducibility; refresh if stale vs source.
- Confirm $19 PWYW price citation; check `docs/launch/template-packs/listing-copy.md` at membership-kit/SWTK parity.
- Unzip rebuilt dist to a clean dir; inspect contents (docs present, no secrets/junk, formats render/lint).
- Record final zip sha256 (ARTIFACT line in owner-actions ⚑D + packet §1).
- Re-verify UNFROZEN at HEAD, then queue the ⚑D click as new §7 packet `docs/publishing/vetting/template-packs.md`; regenerate `docs/publishing/OWNER-QUEUE.md` from packets on this branch (PR #106 unmerged at branch time — base stays origin/main, packet pattern replicated read-only).

## Work log — quality floor, each item executed

1. **Built:** `package.sh` double rebuild → identical sha256 `d65d4c9ef4b23f3ef7fed7277ef6d73f659891d83773eac9d27e86e35463a2b3` (12,989 B) both times, matching the committed zip bit-for-bit — dist FRESH, no refresh needed. Honest null: no test suite exists (zero-runtime Markdown+shell product); executed instead from the extracted bundle: 3 hook scripts `sh -n` clean + run clean under `#!/usr/bin/env bash` (advisory print, exit 0), `settings.template.json` valid JSON, 11/11 files non-empty valid UTF-8.
2. **Priced:** $19 pay-what-you-want suggested — `docs/launch/template-packs/owner-actions.md` ⚑D; `candidates/template-packs/LISTING.md:61`; listing-copy FAQ.
3. **Listing copy:** `docs/launch/template-packs/listing-copy.md` verified at parity (Title / short 187≤200 chars / long / bullets / FAQ) and claim-checked against the extracted bundle — already honest and accurate, no refresh needed.
4. **Checkout/format verified:** zip unzipped to a clean scratch dir — 11 files, QUICKSTART/README/INCLUDED + full `pack/` tree; secret-pattern scan zero hits; no `.DS_Store`/`__pycache__`/junk entries.
5. **sha256 recorded:** new ARTIFACT line in the ⚑D click-script + packet §1.
6. **Click queued (UNFROZEN re-verified at HEAD 81c47ec):** `docs/publishing/vetting/template-packs.md` §7 parser-clean — `derive_owner_queue.py`: 12/12 inputs clean, D1 storefront default Gumroad, manual-review none; OWNER-QUEUE.md regenerated; launch README stale "FROZEN ❄️" template-packs link corrected to the PR #22 unfreeze; publishing README row added.

## Guard recipe

Before any future template-packs click-queue touch: double-rebuild `package.sh` and sha-compare with the committed dist (byte-reproducible, so this is a one-line check); if refreshing the zip, re-pin the ARTIFACT sha in `owner-actions.md` AND packet §1 in the same commit — the two hashes must never diverge.
