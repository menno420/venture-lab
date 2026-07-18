# Title Vetting — Shopify Webhook Test Kit

> **Status:** `plan`
>
> New PRODUCT packet in the vetting directory, so the publish click rides the
> derived owner queue (`../OWNER-QUEUE.md` via
> `scripts/derive_owner_queue.py`). Built under **ORDER 016** (live owner
> overnight-work order, 2026-07-17) as the N+1 of the LIVE Stripe Webhook Test
> Kit and the built GitHub + Slack Webhook Test Kits — same proven template,
> fresh Shopify-specific checks. No freeze applies — a dev-tool kit with no
> payment-path dependency (the ORDER 003 ⚑B/⚑D freeze, lifted 2026-07-11 by
> PR #22, never attached to it). Every step marked **⚑ OWNER-GATE** is an owner
> click, never automated.

**Title:** Shopify Webhook Test Kit · **Category:** digital product / dev tool ·
**Date vetted:** 2026-07-17

Product: [`candidates/shopify-webhook-test-kit/`](../../../candidates/shopify-webhook-test-kit/README.md)
(v0.1; buyer bundle `dist/shopify-webhook-test-kit-v0.1.zip`; launch assets in
[`docs/launch/shopify-webhook-test-kit/`](../../launch/shopify-webhook-test-kit/owner-actions.md);
intake [`INTAKE.md`](../../../candidates/shopify-webhook-test-kit/INTAKE.md),
priced $29 on catalog precedent).

## 1. Built (verified this session, 2026-07-17)

- [x] Stdlib-only harness in two languages (`shwtk.py` + `shwtk.js` Node port,
      same three commands), correct example handler (`stub_handler.py`: raw-body
      capture BEFORE parsing, base64 HMAC-SHA256 verify with constant-time
      compare, fail-closed on a missing `X-Shopify-Hmac-Sha256` header,
      DEFENSIVE base64 decode (a malformed header is a clean 401, never a 500),
      topic routing over `X-Shopify-Topic`, `X-Shopify-Webhook-Id` returned for
      dedupe), one-page `GOTCHAS.md` (5 failure modes, each mapped to a kit
      command), plus `QUICKSTART.md` and a placeholders-only `.env.example`.
- [x] **Fixtures reconstructed from Shopify's docs, honestly labeled:** three
      real-shape webhook bodies — `orders/create`, `products/update`, and
      `app/uninstalled` (all `application/json`, topic in the `X-Shopify-Topic`
      header); per-file sha256 pinned in
      [`fixtures/PROVENANCE.md`](../../../candidates/shopify-webhook-test-kit/fixtures/PROVENANCE.md),
      which states up front they are reconstructed from Shopify's published
      example shapes (NOT wire-captured — no store, app, or webhook subscription
      was created) and cites the signing algorithm and each payload type to the
      Shopify docs page it came from.
- [x] **Signing scheme correct + honestly distinct from the sibling kits:** the
      header is `X-Shopify-Hmac-Sha256` = **base64** (not hex, unlike
      Slack/GitHub) of **HMAC-SHA256 over the raw body directly** (NO timestamp
      basestring, unlike Slack's `v0:{ts}:{body}`), keyed with the app's client
      secret, constant-time compared. Because there is no signed timestamp,
      there is deliberately **no `--stale`/replay mode and no challenge command**
      — the kit is honest that Shopify's scheme has neither (dedupe on
      `X-Shopify-Webhook-Id` instead), rather than inventing a check.
- [x] **HMAC proven against a pinned known-answer:** the `vector` command (both
      ports) recomputes a kit-internal known-answer (fixed secret + body →
      `uhRiDuW3…`) and confirms Python and Node agree byte-for-byte — executed
      PASS in both this session. **Honest caveat recorded in PROVENANCE + the
      listing:** Shopify publishes the verification METHOD but NOT a fixed
      known-answer constant, so this vector is the kit's own self-consistency +
      cross-language proof, NOT a reproduction of a vendor value (the one place
      this kit differs from the Slack kit, which reproduced Slack's OWN
      published constant).
- [x] **Tests (real-path, executed 2026-07-17):** 17-test HTTP-layer suite —
      every request signed with the real base64 HMAC scheme and POSTed over
      actual HTTP to a handler on an ephemeral port. Green from source (`Ran 17
      tests / OK`) AND from the extracted zip in a clean dir (`Ran 17 tests /
      OK`). Covers: the pinned known-answer; base64-not-hex guard (44-char,
      `=`-terminated, 32 decoded bytes); independent-HMAC cross-check; all 3
      fixture shapes + topic mapping; valid webhooks accepted for ALL fixtures;
      `orders/create` + `app/uninstalled` routed by the topic header; forged /
      unsigned / tampered-body rejected (401); malformed-base64 rejected cleanly
      (401, not 500); the kit flagging an insecure handler (accepts forged) AND
      a crashing handler (drops the connection on malformed input → status 0 →
      FAIL). All fire modes additionally exercised live against the stub (fire /
      forge / unsigned / tamper / malformed, both ports — all PASS, captured in
      the session card).
- [x] Suite wired into CI: `shopify-webhook-test-kit-tests` job added to
      `.github/workflows/kit-tests.yml`, same convention as the SWTK/GWTK/Slack
      jobs.
- [x] Buyer bundle built via allow-list `package.sh` (webhook-kit pattern: fixed
      mtimes, sorted entries, `zip -X`; excludes INTAKE.md, package.sh, dist/),
      **byte-reproducible** — unconditional double rebuild 2026-07-17 produced
      the identical sha256, committed dist IS that build.
- [x] **sha256 `8ff06e534187170e3d9622e72f43b7587b7e4f5e63feee4ad3917fd211ee0423`**
      (29,142 bytes, 13 content files) — also pinned in the click-script's
      ARTIFACT line.
- [x] Checkout/format verified from the artifact itself: clean-dir unzip —
      README + QUICKSTART + GOTCHAS + .env.example + harness ×2 + stub + test
      suite at top level, fixtures/ 3 payloads + MANIFEST.json + PROVENANCE.md;
      real-secret-shape scan (shpat_/shpca_/sk_live_/whsec_/xoxb-/AKIA/
      private-key) **0 hits** — the only secret-LIKE strings are `.env.example`,
      `GOTCHAS.md`, and `QUICKSTART.md` lines naming token prefixes NOT to use;
      no junk entries in the archive.

## 2. Collision scan

- [x] No in-catalog title collision. Closest shipped products, boundaries
      disclosed: **SWTK $29** (LIVE), **GWTK $29** (queued), **Slack kit $29**
      (queued) — same product shape, DIFFERENT ecosystem (Stripe payments /
      GitHub webhooks / Slack request-signing / Shopify webhooks; zero shared
      fixtures or code, fresh PROVENANCE; the listings cross-reference rather
      than claim each other's scope). The Shopify signing scheme is genuinely
      distinct: a **base64** digest (unlike the hex of GitHub/Slack) over the
      **raw body with no timestamp** (unlike Slack's signed timestamp and
      Stripe's `t=,v1=`), so the kit adds a **malformed-base64 safety check** and
      drops the `--stale`/challenge modes that don't apply here.
- [x] Same/adjacent buyer audience as the dev-tool catalog (intake's
      concentrated-channel risk, disclosed); narrower still because Shopify's
      official libraries (`@shopify/shopify-api`, the `shopify_api` gem) verify
      the HMAC for you, so the audience is specifically hand-rolled / non-library
      integrators and custom stacks.

## 3. Market / price

- [x] Price **$29 one-time** — set on catalog precedent and recorded
      identically in `INTAKE.md`, the listing copy, the click-script, and here.
      Precedent: SWTK sells LIVE at exactly $29 for the same product shape
      (harness + real-shape fixtures + hostile modes) and GWTK + the Slack kit
      are queued at $29 in the sibling ecosystems. Chain: $15 (kill-rule kit,
      false-green) < $19 (merge-wall, template-packs PWYW) < **$29 this kit** =
      SWTK $29 (live) = GWTK $29 (queued) = Slack $29 (queued) < field-manual $39
      < membership-kit $49. Conservative expectation stays 0–5 sales / $0–$145
      first-90-day, $0 absent distribution (the intake's own line; validation
      signal ≥1 sale OR ≥50 article reads in 30 days, else ledgered negative;
      T+7 funnel checkpoint / T+30 kill deadline armed as a KILL-CHECK here once
      the click is DONE-flipped).

## 4–5. Packaging

- [x] Buyer bundle is the allow-listed `package.sh` output (README +
      QUICKSTART + GOTCHAS + .env.example + `shwtk.py` + `shwtk.js` +
      `stub_handler.py` + `test_http_realpath.py` + `fixtures/`; deliberately
      excludes the lane-internal INTAKE.md, package.sh, dist/). No cover image
      ships — owner adds one or uses the storefront default.

## 6. Listing copy (drafted in-repo — nothing published)

- [x] [`listing-copy.md`](../../launch/shopify-webhook-test-kit/listing-copy.md)
      at catalog parity (Title / Short ≤200 chars (185 measured) / Long /
      Bullets / FAQ) and checked claim-by-claim against the extracted bundle:
      "17 tests" = the suite that ran green twice this session; "three
      real-shape fixtures" = 3 fixtures in the zip; the vector claim = executed
      PASS both ports; the FAQ + "what it does NOT do" section states the honest
      boundaries (fixtures reconstructed from docs, not live captures; no live
      Shopify anything; not a CLI-`app dev`/library substitute; no replay/
      challenge because Shopify's scheme has none; the vector is the kit's own,
      not a vendor constant); a PROVENANCE-FOOTER pins `file@sha` sources;
      refund/license lines present, marked owner-to-set.

## 7. ⚑ OWNER-GATE — publish clicks (queued, never automated)

Seat output = this queued OWNER-ACTION block; the seat performed **none** of
it. It is the queue-parseable form of the click-script in
[`owner-actions.md`](../../launch/shopify-webhook-test-kit/owner-actions.md) —
the HOW detail lives there; no freeze applies (no payment-path gate).

**OWNER-ACTION — Publish "Shopify Webhook Test Kit" at $29 one-time**
1. **Storefront account:** owner signs into the storefront (the SWTK Gumroad
   account already exists and has payout configured).
2. **⚑ Storefront pick:** **Gumroad** (default — same account as the live SWTK
   listing; the click-script's HOW is written against it) or Lemon Squeezy —
   owner's call; either works with the same zip + copy.
3. **Product:** New product → Digital product; Name = "Shopify Webhook Test
   Kit"; upload
   `candidates/shopify-webhook-test-kit/dist/shopify-webhook-test-kit-v0.1.zip`
   and verify the upload matches sha256 `8ff06e53…d211ee0423` (full hash in §1
   and the click-script ARTIFACT line — never upload a stale local copy).
4. **Copy:** paste Title / Short + Long description / Bullets / FAQ from
   [`listing-copy.md`](../../launch/shopify-webhook-test-kit/listing-copy.md);
   set the refund/license lines the copy marks owner-to-set.
5. **Price:** set **$29 one-time** (fixed — catalog precedent; SWTK live at the
   identical price for the identical product shape, GWTK + Slack queued at $29).
6. **Publish + record:** publish, copy the public product URL, storefront
   preview/test purchase to confirm the zip delivers. Optional same-visit
   cross-sell: one line on the live SWTK listing (and the GWTK/Slack listings)
   pointing here (first-ten path channel 2).

- [ ] ⚑ **Owner:** storefront pick (**Gumroad** (default)) — or Lemon Squeezy.
- [ ] ⚑ **Owner:** zip uploaded + sha256 spot-check against §1.
- [ ] ⚑ **Owner:** listing copy pasted + refund/license lines set.
- [ ] ⚑ **Owner:** price set (**$29 one-time** (default per catalog precedent + the live SWTK price)).
- [ ] ⚑ **Owner:** the publish click + preview/test purchase + public URL copied.
- [ ] Seat (post-click, no money moved): record the launch durably on `main` —
      verified listing URL, price, timestamp — in the style of
      [`docs/launch/stripe-webhook-test-kit/LAUNCH-LOG.md`](../../launch/stripe-webhook-test-kit/LAUNCH-LOG.md),
      flip these rows to the `— DONE <date>` disposition, arm the intake's kill
      clock as a `KILL-CHECK:` line here (T+7 funnel checkpoint · T+30
      kill-rule deadline: ≥1 sale OR ≥50 article reads, else ledger NEGATIVE +
      pause/delist), and regenerate the owner queue.

---

**Verdict: publish-ready up to the owner gate.** Built + priced + listing
drafted + checkout/format verified + sha recorded (all evidenced above); the
product parks at §7 (owner clicks) by design. Honest caveats: the fixtures are
reconstructed from Shopify's published example shapes, NOT captures from a live
store — no live Shopify store/app was created (this repo's no-accounts rule) and
the kit says so in the listing and PROVENANCE; three topic shapes ship in v0.1
(a buyer wanting other topics adds their own — the MANIFEST.json mechanism
supports it but the listing doesn't promise them); Shopify publishes no fixed
known-answer HMAC constant, so the `vector` is the kit's own (self-consistency +
Python/Node parity), honestly labelled rather than dressed as a vendor value;
the free-substitute risk is real (Shopify documents the verification; the paid
delta is the harness + hostile modes — especially the malformed-base64 crash
check and the base64-not-hex trap — + the topic-routing model + provenance
discipline); Shopify's official libraries verify signatures for you, narrowing
the audience to hand-rolled integrators; same concentrated dev-tool channel
where SWTK has 0 organic sales — expect ~$0 absent distribution; and a live
purchase remains unverified until the owner's own test purchase.
