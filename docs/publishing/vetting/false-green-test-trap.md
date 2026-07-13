# Title Vetting — The False-Green Test Trap

> **Status:** `plan`
>
> Eighth PRODUCT packet in the vetting directory, so the publish click
> rides the derived owner queue (`../OWNER-QUEUE.md` via
> `scripts/derive_owner_queue.py`). Queued under ORDER 008 (2026-07-13
> night run, PRODUCT #8). No freeze applies — a guide + offline stdlib
> tool with no payment-path dependency (the ORDER 003 ⚑B/⚑D freeze,
> lifted 2026-07-11 by PR #22, never attached to it). Every step marked
> **⚑ OWNER-GATE** is an owner click, never automated.

**Title:** The False-Green Test Trap · **Category:** digital product /
methodology guide + tool · **Date vetted:** 2026-07-13

Product: [`candidates/false-green-test-trap/`](../../../candidates/false-green-test-trap/README.md)
(v0.1; buyer bundle `dist/false-green-test-trap-v0.1.zip`; launch assets in
[`docs/launch/false-green-test-trap/`](../../launch/false-green-test-trap/owner-actions.md);
intake [`INTAKE.md`](../../../candidates/false-green-test-trap/INTAKE.md),
scored 3.73).

## 1. Built (verified this session, 2026-07-13)

- [x] Guide assembled ONLY from committed repo material, every chapter with
      a provenance footer citing file@sha: ch.1 war story ←
      `control/inbox.md` ORDER 003 @ `c99caa4` +
      `.sessions/2026-07-13-order-003-stripe-path.md` @ `d058c4d` (fix
      PR #16 `912da3e`) + `candidates/membership-kit/server/app.py` @
      `dfe3332`; ch.2 mechanism ← `docs/products/TEMPLATE.md` stage-3 rule
      @ `53f6b65`; ch.3–4 vendoring + PROVENANCE pattern ← both kits'
      `fixtures/PROVENANCE.md` @ `dfe3332`; ch.5 real-path testing ← both
      `test_http_realpath.py` suites @ `dfe3332`; ch.6 checklist distilled
      from the above (+ the lane's verify-before-claiming discipline,
      Q-0120, `.sessions/2026-07-12-heartbeat-2026-07-12b.md` @ `d7896f0`).
- [x] **Honest size verdict:** the committed material supports ~3,600
      words (~8 pages) across 7 chapters — NOT the intake's "~15-page"
      estimate. Scoped down rather than padded; the bundle README's
      honesty box and the listing FAQ state the real size.
- [x] Runnable `vendor_fixture.py` (stdlib-only, offline, fail-closed on
      secrets) authored AND **executed end-to-end** on SWTK's committed
      `checkout_session_completed.json` as the pasted sample: exit 0,
      fixture + PROVENANCE stub written, **7 null fields enumerated
      including `data.object.customer_email`** — the tool surfaces the
      exact war-story field. Output pasted verbatim in guide ch.7.
- [x] Buyer bundle built via allow-list `package.sh` (kill-rule-intake-kit
      pattern: fixed mtimes, sorted entries, `zip -X`), **byte-reproducible**
      — double rebuild, identical sha256, committed dist IS that build.
- [x] **sha256 `1d83702b7259191a88e16ae6238758c7fb46cf0c9c4884dfb6514c01487017b4`**
      (25,825 bytes, 14 content files) — also pinned in the click-script's
      ARTIFACT line.
- [x] Test row (NOT a null — this product ships an executable): from the
      extracted bundle in a clean dir, `python3 -m unittest
      test_vendor_fixture` → `Ran 8 tests … OK`; `vendor_fixture.py` run
      end-to-end on the included sample → exit 0. Content substitute for
      the prose chapters, same clean dir: all 14 files valid UTF-8 and
      non-empty, all 11 markdown files H1-headed with balanced code
      fences, sample JSON parses. Honest remainder: the chapters' claims
      are verified by citation, not execution — the listing FAQ says so.
- [x] Checkout/format verified from the artifact itself: clean-dir unzip —
      README + QUICKSTART + INCLUDED + tool + tests at top level, guide/ 7
      chapters, examples/ 2 files (matches INCLUDED.md manifest 14/14).
      Secret-pattern scan: zero hits; no `.DS_Store`, no `__pycache__`, no
      junk entries in the archive listing.

## 2. Collision scan

- [x] Title is a coined phrase ("false-green test trap") — no in-catalog
      collision; the free-content category is crowded (the intake's own
      risk section) but no product-name collision found in the obvious
      testing-guide names. In-catalog overlap disclosed: SWTK is the
      Stripe-specific done-for-you tool for the same pain — the guide
      cross-links it as a soft funnel (intake: "PRODUCT with a soft funnel
      edge"), and the listing copy does not claim the kit's capabilities.

## 3. Market / price

- [x] Price **$15 one-time** — set at intake
      ([`INTAKE.md`](../../../candidates/false-green-test-trap/INTAKE.md):
      "Conservative revenue estimate: $15 one-time") and recorded
      identically in the listing copy, the click-script, and here.
      Precedent chain (bottom rung, tied with the same night's Kill-Rule
      Intake Kit $15): $15 < template-packs $19 PWYW (PR #108) < SWTK $29
      live (PR #86) < field-manual $39 (PR #110) < membership-kit $49
      (PR #106). Conservative expectation stays 0–4 sales / $0–$60
      first-90-day, $0 absent distribution (the intake's own line; WTP
      axis 2/5; validation signal ≥1 sale OR ≥40 reads with ≥1 SWTK
      click-through in 30 days).

## 4–5. Packaging

- [x] Buyer bundle is the allow-listed `package.sh` output (README +
      QUICKSTART + INCLUDED + `vendor_fixture.py` + `test_vendor_fixture.py`
      + `guide/` + `examples/`; deliberately excludes LISTING.md, the
      lane-internal INTAKE.md, dist/, package.sh, `__pycache__`, .git). No
      cover image ships — owner adds one or uses the storefront default.

## 6. Listing copy (drafted in-repo — nothing published)

- [x] [`listing-copy.md`](../../launch/false-green-test-trap/listing-copy.md)
      at catalog parity (Title / short ≤200 chars (196) / long / bullets /
      FAQ) and checked claim-by-claim against the extracted bundle:
      "seven chapters" = 7 (counted); "~3,600 words — about 8 pages" =
      measured 3,584 from the extracted guide/ (rounded, not inflated);
      "8-test suite" = 8 (executed); "13 green tests" / customer_email
      war-story claims match the committed ORDER 003 text; honesty FAQ
      states what was NOT machine-verified (prose verified by citation,
      not execution) and tells already-disciplined practitioners to buy
      nothing.

## 7. ⚑ OWNER-GATE — publish clicks (queued, never automated)

Seat output = this queued OWNER-ACTION block; the seat performed **none** of
it. It is the queue-parseable form of the click-script in
[`owner-actions.md`](../../launch/false-green-test-trap/owner-actions.md) —
the HOW detail lives there; no freeze applies (no payment-path gate).

**OWNER-ACTION — Publish "The False-Green Test Trap" at $15 one-time**
1. **Storefront account:** owner signs into (or creates) the storefront;
   complete its payout setup first or revenue holds.
2. **⚑ Storefront pick:** **Gumroad** (default — the click-script's HOW is
   written against it; same account as the SWTK live listing) or Lemon
   Squeezy — owner's call; either works with the same zip + copy.
3. **Product:** New product → Digital product; Name = "The False-Green
   Test Trap"; upload
   `candidates/false-green-test-trap/dist/false-green-test-trap-v0.1.zip`
   and verify the upload matches sha256 `1d83702b…7017b4` (full hash in §1
   and the click-script ARTIFACT line — never upload a stale local copy).
4. **Copy:** paste Title / Short + Long description / Bullets / FAQ from
   [`listing-copy.md`](../../launch/false-green-test-trap/listing-copy.md).
5. **Price:** set **$15 one-time** (fixed — bottom rung, tied with the
   Kill-Rule Intake Kit; set at intake).
6. **Publish + record:** publish, copy the public product URL, storefront
   preview/test purchase to confirm the zip delivers.

- [ ] ⚑ **Owner:** storefront account + payout setup.
- [ ] ⚑ **Owner:** storefront pick (**Gumroad** (default)) — or Lemon Squeezy.
- [ ] ⚑ **Owner:** zip uploaded + sha256 spot-check against §1.
- [ ] ⚑ **Owner:** listing copy pasted.
- [ ] ⚑ **Owner:** price set (**$15 one-time** (default per intake + precedent chain)).
- [ ] ⚑ **Owner:** the publish click + preview/test purchase + public URL copied.
- [ ] Seat (post-click, no money moved): record the launch durably on `main` —
      verified listing URL, price, timestamp — in the style of
      [`docs/launch/stripe-webhook-test-kit/LAUNCH-LOG.md`](../../launch/stripe-webhook-test-kit/LAUNCH-LOG.md),
      arm the intake's 30-day kill clock as a `KILL-CHECK:` line here, and
      add the guide to the SWTK cross-sell surfaces (the guide is SWTK's
      natural top-of-funnel neighbor).

---

**Verdict: publish-ready up to the owner gate.** Built + priced + listing
drafted + checkout/format verified + sha recorded (all evidenced above); the
product parks at §7 (owner clicks) by design. Honest caveats: the guide is
~8 pages, not the intake's estimated ~15 (the committed material honestly
supports no more, and padding was declined); the prose chapters are
verified by citation to committed material, not by execution (the tool IS
executed: 8/8 tests + an end-to-end run from the extracted bundle); the
category competes with free content (intake WTP 2/5 — expect ~$0 absent
distribution); and a live purchase remains unverified until the owner's own
test purchase.
