# Session — Night run: Agent Fleet Field Manual to publish-READY (ORDER 008, PRODUCT #3)

> **Status:** `complete`

- **📊 Model:** fable-5 · worker slice · ORDER 008 night-run product lane
- **session:** PRODUCT #3 of the 2026-07-13 night run — drove the Agent Fleet Field Manual ($39, `candidates/agent-fleet-field-manual/`, click QUEUED 2026-07-11 in `publish-owner-action.md` but absent from the derived owner queue) through the ORDER 008 quality floor: built + priced + listing drafted + checkout/format verified + sha recorded + click queued.
- **started (date -u):** Mon Jul 13 01:25:29 UTC 2026
- **closed (date -u):** Mon Jul 13 01:31 UTC 2026

## ⟲ Previous-session review

Previous session (`.sessions/2026-07-13-night-template-packs.md`, PR #108, merged `d0ab1dd`): the cheapest floor pass yet — its double-rebuild check proved dist freshness in under a minute, validating the membership-kit card's 💡 in the cheap direction, and its honest-null pattern (artifact-side execution substitute for zero-runtime products) was reused here nearly verbatim for a prose product. Its predicted parallel-branch OWNER-QUEUE conflict materialized exactly as written: PR #106 went `dirty` the moment #108 landed, and the resolution was precisely the mechanical one it prescribed (merge main in, re-run `derive_owner_queue.py` on the union set — executed on #106 this same night slice, 13/13 clean). One gap this session exposed: template-packs verified the artifact matched the listing, but did not re-check the *in-artifact README's instructions against the artifact's own file set* — that check is what caught the field manual's broken "rebuild it yourself" instruction (tooling excluded from the very zip whose README invokes it). Worth adding to the TEMPLATE.md checkout step: "execute the README's own instructions from inside the extracted bundle."

## 💡 Session idea

Self-reproducing bundles as a verification primitive: because `package.sh` pins mtimes and sorts entries, shipping the build tooling *inside* the zip lets the strongest possible checkout verification run buyer-side — extract, `python3 build.py && sh package.sh`, and the bundle regenerates its own byte-identical zip (executed this session: sha `63e71b30…ee23` reproduced from inside the extracted copy). That one command proves build determinism, tooling completeness, and README honesty simultaneously, at zero marginal cost for any stdlib-built product. Candidate TEMPLATE.md stage-6 upgrade: "if the product is stdlib-buildable, ship the tooling and require the buyer-side self-rebuild as the checkout check."

## Scope

- Located the full manuscript in-repo (11 chapters + 3 templates + build.py/package.sh — NOT free-chapters-only; no blocked-on-content).
- Rebuilt the dist via `package.sh`; unconditional double rebuild + sha compare.
- Verified $39 price citations; listing checked claim-by-claim against the extracted artifact.
- Queued the click as §7 packet `docs/publishing/vetting/agent-fleet-field-manual.md`; regenerated OWNER-QUEUE from this branch's packet set (PR #106 open in parallel — expected conflict flagged in the PR body).

## Work log — quality floor, each item executed

1. **Built:** full manuscript present. First double rebuild reproduced the committed zip exactly (`7eff9235…a29176`, 60,300 B, 3× identical) — dist WAS fresh, but checkout verification caught a parity defect: the in-zip README's "Rebuild it yourself" section invokes `build.py`/`package.sh`, which `package.sh` excluded from the bundle, and the listing sells "rebuild with stdlib Python". Fixed: bundle now ships both tooling files; refreshed zip `63e71b30d1a194b42f92d8c9197148ec89244cba82688e6c097d5727e6ccee23` (65,283 B, 19 files), double rebuild identical, and — proven buyer-side — extracting the zip and running `python3 build.py && sh package.sh` from the extracted copy regenerates the byte-identical zip.
2. **Priced:** $39 one-time — `publish-owner-action.md` WHAT/HOW; candidate README "$39 one-time."; launch LISTING "Launch price: **$39** (one-time)".
3. **Listing copy:** verified claim-by-claim vs the extracted bundle: 11 chapters ✓, 3 templates ✓, self-contained HTML (0 external refs, 0 scripts) ✓, 2 free chapters (FREE badges in HTML + standalone exports) ✓, stdlib-rebuild claim now TRUE via the bundle fix. Stale "NOT-QUEUED" cross-refs in both LISTINGs corrected to QUEUED (2026-07-11).
4. **Checkout/format verified:** zip unzipped to a clean dir — 19/19 files non-empty valid UTF-8; all 12 HTML anchors resolve; secret-pattern scan zero hits; no junk entries; buyer-side self-rebuild executed (above).
5. **sha256 recorded:** new ARTIFACT line in `publish-owner-action.md` (supersedes `7eff9235…` with the refresh rationale) + packet §1.
6. **Click queued:** §7 packet parser-clean — `derive_owner_queue.py`: 13/13 inputs clean, D1 [agent-fleet-field-manual.md] default Gumroad, manual-review none; OWNER-QUEUE.md regenerated from this branch's 12-packet set; publishing README row added. No freeze applies (no payment code — Gumroad-hosted; D1/Stripe gate n/a per the 2026-07-11 queue review).

## Guard recipe

Before any future field-manual click-queue touch: double-rebuild `package.sh` and sha-compare with the committed dist; if the zip changes, re-pin the ARTIFACT sha in `publish-owner-action.md` AND packet §1 in the same commit; and run the buyer-side self-rebuild from the extracted copy — the bundle must always regenerate itself byte-identically.
