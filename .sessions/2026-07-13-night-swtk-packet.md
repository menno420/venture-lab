# Session — Night run: Stripe Webhook Test Kit catalog parity (ORDER 008, PRODUCT #4)

> **Status:** `complete`

- **📊 Model:** fable-5 · worker slice · ORDER 008 night-run product lane
- **session:** PRODUCT #4 of the 2026-07-13 night run — assessed whether the Stripe Webhook Test Kit ($29) needed a publish click queued (verdict: NO — it has been LIVE since 2026-07-12, owner test purchase verified) and brought it to catalog parity with the packet-era products: dist freshness proof, ARTIFACT sha line, listing-vs-artifact verification, click-script flipped from stale QUEUED to CLICKED-LIVE. Also repaired PR #110's OWNER-QUEUE merge conflict (second-lander rule) in the same night slice.
- **started (date -u):** Mon Jul 13 01:36:24 UTC 2026
- **closed (date -u):** Mon Jul 13 01:40 UTC 2026

## ⟲ Previous-session review

Previous session (`.sessions/2026-07-13-night-field-manual.md`, PR #110): its checkout-verification upgrade — "execute the in-zip README's own instructions from inside the extracted bundle" — caught a real defect there (tooling excluded from the zip whose README invokes it) and was reused here as a first-class parity check: every SWTK README-invoked file was confirmed present, and `python3 swtk.py list` + `node swtk.js list` were executed buyer-side from the extracted copy. Its predicted OWNER-QUEUE conflict also landed exactly as flagged: #110 went `dirty` when #106 merged, and THIS slice executed the mechanical remedy its own PR body prescribed (merge `origin/main`, re-run `derive_owner_queue.py` on the union tree → 14/14 clean, resolution commit `8718f55`). One gap it left: its packet-first framing assumes every product WANTS a §7 packet — SWTK proved the opposite case exists (already-live product; the grammar has no no-click disposition), which this session documented as an explicit anti-pattern in the launch log instead of forcing a packet.

## 💡 Session idea

The derive grammar needs an already-live/RECORD disposition. Tonight's parity pass had to *withhold* a §7 packet because every parsed `⚑ **Owner:**` checkbox becomes a queued click — there is no way to represent "this product is LIVE, nothing to click, here is its artifact sha" in the owner queue. That means the queue silently under-reports the catalog: the owner sees 12 click-runs but not the one product actually earning. Cheap fix: teach `derive_owner_queue.py` a `- [x] ⚑ **Owner:** … — DONE <date>` checked-box form rendered into a read-only "Live / completed" section (checked boxes are already tolerated by `CHECKBOX_RE` but currently queue as if unclicked — inspect before relying on it). Then SWTK gets a packet, the queue becomes the full catalog view, and the "already-live" case stops being a documented exception.

## Scope

- TASK A: repaired PR #110 (`claude/night-field-manual`) — merged `origin/main` (post-#106/#109), resolved `docs/publishing/OWNER-QUEUE.md` by re-running the derive script on the union packet set (14/14 clean), strict green, pushed `8718f55`. Left OPEN, not armed.
- TASK B verdict: SWTK ALREADY LIVE (LAUNCH-LOG: Gumroad HTTP 200 2026-07-12T16:25:16Z + 16:28:47Z re-verification, owner test purchase 18:09:34Z). NO duplicate click queued.
- Parity work on this branch: double rebuild + sha, suite runs (source + clean-dir extract), bundle inspection + secret scan, listing claim-by-claim check, ARTIFACT line, click-script status flip, launch-log parity entry.

## Work log — parity items, each executed 2026-07-13

1. **Dist freshness (stage-6):** committed `dist/stripe-webhook-test-kit-v0.1.zip` sha256 `d3ac5f88620976c4dee15f70801eba5986faa47f4898a1a3bda4907336eeb0d8` (19,872 B); `package.sh` twice → both rebuilds byte-identical (3× same sha, 01:36:52Z). Matches the 2026-07-11 non-author sha and the 19.4 KB live-download size.
2. **Tests:** `python3 -m unittest test_http_realpath -v` → `Ran 14 tests in 3.028s / OK` from source (01:37:03Z); `Ran 14 tests in 3.033s / OK` from the clean-dir extracted copy (01:37:19Z).
3. **Bundle/checkout:** 10/10 files, zero junk/empty entries; secret scan zero hits; buyer-side `swtk.py list` + `swtk.js list` executed clean (stdlib claim TRUE, no installs).
4. **Listing parity:** four gotcha claims ↔ four named executed tests; $29 identical across `LISTING.md` / `publish-owner-action.md` / live page (`price_cents 2900`).
5. **Records:** ARTIFACT sha line + CLICKED-LIVE flip in `publish-owner-action.md`; catalog-parity entry + no-packet rationale in `LAUNCH-LOG.md`; `derive_owner_queue.py` re-run → OWNER-QUEUE.md byte-identical (no packet change, as intended).

## Guard recipe

Before touching SWTK again: it is LIVE — never re-queue its publish click; any source change requires rebuild + re-pin of the ARTIFACT line in `publish-owner-action.md` AND an owner re-upload flag (live listing goes STALE); parity checks run buyer-side from the extracted zip, never only from the repo tree.
