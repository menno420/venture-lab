# Session — Night run: membership-kit to publish-READY + product template extraction (ORDER 008)

> **Status:** `complete`

- **📊 Model:** fable-5 · worker slice · ORDER 008 night-run product lane
- **session:** PRODUCT #1 of the 2026-07-13 night run — drove membership-kit through the ORDER 008 quality floor (built + priced + listing drafted + checkout/format verified + sha recorded + click queued), then extracted the repeatable idea→publish-READY path into `docs/products/TEMPLATE.md` so product N+1 gets cheaper.
- **started (date -u):** Mon Jul 13 01:00:36 UTC 2026
- **closed (date -u):** Mon Jul 13 01:14 UTC 2026

## ⟲ Previous-session review

Previous session (`.sessions/2026-07-13-order-003-stripe-path.md`): correctly turned a re-dispatched ORDER 003 into a verification slice instead of duplicate work — every D-item re-proven live at HEAD `c99caa4`, ORDER 007 confirmed terminal via MCP, and the inbox-append wall documented verbatim with both gate findings. Two notes: (1) its "coordinator relay 2026-07-13: freeze STANDS" line conflicted with repo evidence at HEAD — `docs/launch/membership-kit/owner-actions.md` says UNFROZEN (2026-07-11) and PR #22 (merged 2026-07-11T01:58:35Z) is exactly the unfreeze; this session re-verified all three sources and proceeded on the repo evidence, per ORDER 008's own "queue the click + evidence" clause. (2) Its "test_http_realpath 9 OK" count was source-tree truth, but the COMMITTED dist zip still carried the 8-test copy predating the fail-closed misconfig fix — the card verified suites and zip presence separately and missed the source↔dist skew; this session's rebuild caught it. Lesson folded into TEMPLATE.md stage 6: always rebuild and diff the dist against source, presence is not freshness.

## 💡 Session idea

"Presence is not freshness" for committed build artifacts: a dist zip in git can silently trail its own source (here: shipped 8-test copy vs source's 9, missing a fail-closed security fix). Cheap standing defense worth extracting: a CI step or bootstrap check that rebuilds each `package.sh` dist into a temp dir and fails on sha mismatch with the committed zip — byte-reproducible packaging makes this a one-line comparison.

## Scope

- Verify/rebuild `candidates/membership-kit/dist/membership-kit-v0.2.zip` via `package.sh`; run all three kit test suites; unzip-and-inspect the shipped artifact (checkout/format verification).
- Confirm price ($49) and listing copy (`docs/launch/membership-kit/listing-copy.md`) at parity with the SWTK launch assets.
- Record the final zip sha256 where the repo convention puts it.
- Freeze check, then (verified UNFROZEN — PR #22, owner-actions.md@HEAD) queue the ⚑B click as a §7 OWNER-GATE block parsed by `scripts/derive_owner_queue.py`; regenerate `docs/publishing/OWNER-QUEUE.md`.
- `docs/products/TEMPLATE.md` — the distilled SWTK + membership-kit playbook (docs-gate badge + reachability).

## Work log — quality floor, each item executed

1. **Built:** rebuild via `package.sh` exposed a stale committed dist (39,955 B, sha `d795d260…23ad877`) missing the fail-closed webhook-misconfig fix + its test; refreshed zip committed — sha256 `9f262fc84008ad7b1517116ef999c331672d756f6d68fe5378682e38e1d5d3e1` (40,547 B), byte-reproducible (double rebuild identical). Suites at source: `test_http_realpath` `Ran 9 tests in 4.537s / OK`, `test_membership` `Ran 15 tests in 0.005s / OK`, `test_supabase_store` `Ran 12 tests in 6.050s / OK`.
2. **Priced:** $49 one-time — `docs/launch/membership-kit/owner-actions.md` ⚑B, `candidates/membership-kit/LISTING.md:46`, web CTA.
3. **Listing copy:** `docs/launch/membership-kit/listing-copy.md` refreshed to v0.2 reality (HTTP-layer real-path claims, fail-closed behavior, 36 tests, Supabase option) at SWTK parity; ⚑A no-live-purchase caveat retained; short description 199 chars.
4. **Checkout/format verified:** rebuilt zip unzipped to a clean dir — README, QUICKSTART (loud MOCK-mode warning up top), server + vendored fixtures + PROVENANCE.md, web files, `.env.example` placeholders only, zero members.json/__pycache__/secrets; packaged suites re-run from the extracted copy: `Ran 36 tests in 10.583s / OK`.
5. **sha256 recorded:** in the ⚑B click-script's new ARTIFACT line (SWTK publish-doc convention) + §1 of the vetting packet.
6. **Click queued (freeze verified lifted):** `docs/publishing/vetting/membership-kit.md` — first PRODUCT packet, §7 grammar parser-clean (`derive_owner_queue.py`: 6/6 inputs, D1 storefront default Gumroad, 6-click sequence); `docs/publishing/OWNER-QUEUE.md` regenerated; indexes updated (publishing README row; launch README stale FROZEN line corrected to the PR #22 unfreeze).

Template: `docs/products/TEMPLATE.md` (badge `reference`, reachable via `docs/launch/README.md`) — stages, quality floor, freeze discipline, landing procedure, per-stage evidence bar.

## Guard recipe

Before any future membership-kit click-queue touch: rebuild `package.sh` into a temp copy and sha-compare with the committed dist; if they differ, the committed zip is stale — refresh it and re-pin the ARTIFACT sha in `owner-actions.md` before anything else.
