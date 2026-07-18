# Title Vetting — Idempotency Key Test Kit

> **Status:** `plan`
>
> New PRODUCT packet in the vetting directory, so the publish click rides the
> derived owner queue (`../OWNER-QUEUE.md` via
> `scripts/derive_owner_queue.py`). Built under **ORDER 016** (live owner
> overnight-work order, reaffirmed by the live owner turn 2026-07-18) as a NEW,
> non-webhook sellable — the same proven kit template applied to a DIFFERENT
> problem class (idempotency / safe-retry dedup, not signature verification). No
> freeze applies — a dev-tool kit with no payment-path dependency (the ORDER 003
> ⚑B/⚑D freeze, lifted 2026-07-11 by PR #22, never attached to it). Every step
> marked **⚑ OWNER-GATE** is an owner click, never automated.

**Title:** Idempotency Key Test Kit · **Category:** digital product / dev tool ·
**Date vetted:** 2026-07-18

Product: [`candidates/idempotency-key-test-kit/`](../../../candidates/idempotency-key-test-kit/README.md)
(v0.1; buyer bundle `dist/idempotency-key-test-kit-v0.1.zip`; launch assets in
[`docs/launch/idempotency-key-test-kit/`](../../launch/idempotency-key-test-kit/owner-actions.md);
intake [`INTAKE.md`](../../../candidates/idempotency-key-test-kit/INTAKE.md),
priced $29 on catalog precedent).

## 1. Built (verified this session, 2026-07-18)

- [x] Stdlib-only harness in two languages (`ikt.py` + `ikt.js` Node port, same
      commands: `check` / `replay` / `mismatch` / `distinct-keys` / `concurrent`
      / `missing-key` / `demo` / `list`), a CORRECT reference endpoint
      (`stub_handler.py`: in-memory store keyed on `(method, path,
      Idempotency-Key)` holding a sha256 request fingerprint + the stored
      response, a per-key in-flight lock, 422 on a fingerprint mismatch, a
      configurable missing-key policy, and a `GET /_debug/side_effects`
      counter), a deliberately NAIVE no-dedup endpoint
      (`stub_handler_naive.py`), a one-page `GOTCHAS.md` (5 failure modes, each
      mapped to a kit command), plus `QUICKSTART.md` and a placeholders-only
      `.env.example`.
- [x] **Genuinely NEW problem class, not another webhook kit:** the webhook kits
      verify an INBOUND provider signature (one request → accept/reject on an
      HMAC); this kit verifies a buyer's OWN endpoint's STATEFUL behaviour across
      multiple requests — that a retried `POST /charges` triggers the side effect
      EXACTLY ONCE. Dedup / safe-retry, not signature verification; zero shared
      fixtures or crypto scheme with the webhook kits.
- [x] **Five properties checked, each PASS/FAIL against a buyer endpoint:**
      (1) **replay** — same key + same body replays the STORED response (same
      resource id); the side effect runs once; (2) **mismatch** — same key +
      different body is rejected (409/422); (3) **distinct-keys** — two different
      keys + same body produce two independent resources (per-key scoping);
      (4) **concurrent** — two in-flight same-key requests produce ONE side
      effect (in-flight lock); (5) **missing-key** — no key follows a documented
      configurable policy (`required` → 4xx, `passthrough` → 2xx), never guessed
      silently.
- [x] **Value proof built in (correct vs naive):** `ikt demo` runs all five
      against BOTH bundled stubs with a loud zero-accounts banner — the CORRECT
      stub passes all five (side-effect counter = 5, proving exactly-once) and
      the NAIVE stub is FLAGGED on replay / mismatch / concurrent / missing-key
      (counter = 9, proving over-execution). The kit demonstrably distinguishes
      correct idempotency from a broken implementation.
- [x] **Honest source discipline:** `fixtures/PROVENANCE.md` states up front that
      the fixtures are docs-derived (NOT wire-captured — no account, key, charge,
      or order was created), pins a sha256 per fixture, and is explicit that the
      kit tests the STRIPE-STYLE model: the IETF draft "The Idempotency-Key HTTP
      Header Field" standardises the HEADER, not one mandated status code, so the
      exact codes (409/422 conflict, 400 missing-key-under-`required`) follow
      Stripe's widely-used documented behaviour (the conflict check accepts 409
      OR 422; the missing-key mode is configurable). Expiry (Stripe's 24h TTL) is
      documented in `GOTCHAS.md` but NOT asserted against a live endpoint (it
      would require waiting out the TTL) — stated honestly rather than faked.
- [x] **Tests (real-path, executed 2026-07-18):** 20-test HTTP-layer suite —
      every request POSTed over actual HTTP to a reference stub on an ephemeral
      port. Green from source (`Ran 20 tests / OK`) AND from the extracted zip in
      a clean dir (`Ran 20 tests / OK`). Covers: manifest/fixture shape; the
      primary/variant share-endpoint-differ-in-body invariant; replay passes +
      side-effect counter proves exactly-once; replay returns a byte-identical
      stored response; mismatch passes + does not execute a second time;
      distinct-keys; concurrency (n=4) passes + runs once; missing-key in both
      modes; key scoping across two endpoints; the full suite green on the
      correct stub; AND the kit FLAGGING the naive stub on replay (double
      execution, counter proof), mismatch, concurrency, and missing-key — with
      distinct-keys honestly NOT distinguishing (both stubs pass it), documented.
- [x] Suite wired into CI: `idempotency-key-test-kit-tests` job added to
      `.github/workflows/kit-tests.yml`, same convention as the
      Stripe/GitHub/Slack/Shopify kit jobs.
- [x] Buyer bundle built via allow-list `package.sh` (webhook-kit pattern: fixed
      mtimes, sorted entries, `zip -X`; excludes `INTAKE.md`, `package.sh`,
      `dist/`), **byte-reproducible** — unconditional double rebuild 2026-07-18
      produced the identical sha256, committed dist IS that build.
- [x] **sha256 `8607803d5fd7286e9f86f1515981ea1ca6052ae06d7a8d417526dd85a796f6e1`**
      (32,925 bytes, 14 content files) — also pinned in the click-script's
      ARTIFACT line.
- [x] Checkout/format verified from the artifact itself: clean-dir unzip —
      README + QUICKSTART + GOTCHAS + `.env.example` + harness ×2 + both stubs +
      test suite at top level, `fixtures/` 3 payloads + MANIFEST.json +
      PROVENANCE.md; real-secret-shape scan (`sk_live_`/`whsec_`/`AKIA`/private
      key/etc.) **0 hits**; no junk entries in the archive.

## 2. Collision scan

- [x] No in-catalog title collision. Closest shipped products, boundaries
      disclosed: the four webhook kits (**Stripe $29** LIVE, **GitHub/Slack/
      Shopify $29** queued) share the kit SHAPE but a DIFFERENT problem class —
      they verify an inbound HMAC signature; this kit verifies outbound
      safe-retry / idempotency. Zero shared fixtures or code, fresh PROVENANCE.
      Honest positioning: this is the OUTBOUND companion to the inbound webhook
      line (a developer wiring Stripe Checkout webhooks is the same buyer who
      needs safe retries on their own writes), so the listings cross-reference
      rather than claim each other's scope.
- [x] Same/adjacent buyer audience as the dev-tool catalog (intake's
      concentrated-channel risk, disclosed); narrower still because mature
      frameworks/libraries increasingly ship idempotency middleware, so the
      audience is specifically hand-rolled endpoints and custom stacks.

## 3. Market / price

- [x] Price **$29 one-time** — set on catalog precedent and recorded identically
      in `INTAKE.md`, the listing copy, the click-script, and here. Precedent:
      the Stripe Webhook Test Kit sells LIVE at exactly $29 for the same product
      shape (stdlib harness + docs-derived fixtures + edge-case checks +
      byte-reproducible bundle) and the GitHub/Slack/Shopify kits are queued at
      $29. Chain: $15 (kill-rule kit, false-green) < $19 (merge-wall,
      template-packs PWYW) < **$29 this kit** = Stripe $29 (live) = GitHub/Slack/
      Shopify $29 (queued) < field-manual $39 < membership-kit $49. Conservative
      expectation 0–5 sales / $0–$145 first-90-day, $0 absent distribution (the
      intake's own line; validation signal ≥1 sale OR ≥50 article reads in 30
      days, else ledgered negative; T+7 funnel checkpoint / T+30 kill deadline
      armed as a KILL-CHECK here once the click is DONE-flipped).

## 4–5. Packaging

- [x] Buyer bundle is the allow-listed `package.sh` output (README + QUICKSTART +
      GOTCHAS + `.env.example` + `ikt.py` + `ikt.js` + `stub_handler.py` +
      `stub_handler_naive.py` + `test_http_realpath.py` + `fixtures/`;
      deliberately excludes the lane-internal `INTAKE.md`, `package.sh`,
      `dist/`). No cover image ships — owner adds one or uses the storefront
      default.

## 6. Listing copy (drafted in-repo — nothing published)

- [x] [`listing-copy.md`](../../launch/idempotency-key-test-kit/listing-copy.md)
      at catalog parity (Title / Short ≤200 chars (190 measured) / Long /
      Bullets / FAQ) and checked claim-by-claim against the extracted bundle:
      "20 tests" = the suite that ran green twice this session; "three
      docs-derived fixtures" = 3 fixtures in the zip; the correct/naive demo
      claim = executed (correct all-pass, naive flagged on 4) both ports; the FAQ
      + "what it does NOT do" section states the honest boundaries (not a webhook
      kit; Stripe-style model not the one true RFC; expiry documented not
      asserted; fixtures docs-derived not live captures; no live API anything); a
      PROVENANCE-FOOTER pins `file@sha` sources; refund/license lines present,
      marked owner-to-set.

## 7. ⚑ OWNER-GATE — publish clicks (queued, never automated)

Seat output = this queued OWNER-ACTION block; the seat performed **none** of it.
It is the queue-parseable form of the click-script in `owner-actions.md` (same
directory as this packet's launch assets) — the HOW detail lives there; no
freeze applies (no payment-path gate).

**OWNER-ACTION — Publish "Idempotency Key Test Kit" at $29 one-time**
1. **Storefront account:** owner signs into the storefront (the Stripe kit
   Gumroad account already exists and has payout configured).
2. **⚑ Storefront pick:** **Gumroad** (default — same account as the live Stripe
   kit listing; the click-script's HOW is written against it) or Lemon Squeezy —
   owner's call; either works with the same zip + copy.
3. **Product:** New product → Digital product; Name = "Idempotency Key Test
   Kit"; upload
   `candidates/idempotency-key-test-kit/dist/idempotency-key-test-kit-v0.1.zip`
   and verify the upload matches sha256 `8607803d…a796f6e1` (full hash in §1 and
   the click-script ARTIFACT line — never upload a stale local copy).
4. **Copy:** paste Title / Short + Long description / Bullets / FAQ from the
   `listing-copy.md` in this product's launch dir; set the refund/license lines
   the copy marks owner-to-set.
5. **Price:** set **$29 one-time** (fixed — catalog precedent; the Stripe kit is
   live at the identical price for the identical product shape, GitHub/Slack/
   Shopify queued at $29).
6. **Publish + record:** publish, copy the public product URL, storefront
   preview/test purchase to confirm the zip delivers. Optional same-visit
   cross-sell: one line on the live Stripe kit listing (and the other dev-tool
   listings) pointing here (first-ten path channel 2).

- [ ] ⚑ **Owner:** storefront pick (**Gumroad** (default)) — or Lemon Squeezy.
- [ ] ⚑ **Owner:** zip uploaded + sha256 spot-check against §1.
- [ ] ⚑ **Owner:** listing copy pasted + refund/license lines set.
- [ ] ⚑ **Owner:** price set (**$29 one-time** (default per catalog precedent + the live Stripe kit price)).
- [ ] ⚑ **Owner:** the publish click + preview/test purchase + public URL copied.
- [ ] Seat (post-click, no money moved): record the launch durably on `main` —
      verified listing URL, price, timestamp — in the style of the Stripe kit
      `LAUNCH-LOG.md`, flip these rows to the `— DONE <date>` disposition, arm
      the intake's kill clock as a `KILL-CHECK:` line here (T+7 funnel checkpoint
      · T+30 kill-rule deadline: ≥1 sale OR ≥50 article reads, else ledger
      NEGATIVE + pause/delist), and regenerate the owner queue.

---

**Verdict: publish-ready up to the owner gate.** Built + priced + listing drafted
+ checkout/format verified + sha recorded (all evidenced above); the product
parks at §7 (owner clicks) by design. Honest caveats: this tests the Stripe-style
idempotency model (the IETF draft standardises the header, not one mandated
status code — stated in PROVENANCE + the listing); the fixtures are docs-derived,
NOT captures from a live API (no account/key/charge created — this repo's
no-accounts rule); expiry is documented but not live-asserted (TTL wait
infeasible); the distinct-keys property honestly does NOT distinguish correct
from naive (both pass it), documented; the free-substitute risk is real (Stripe
documents idempotency; the paid delta is the harness testing the buyer's OWN
endpoint — including the unit-test-invisible concurrency case — + the correct/
naive reference pair + provenance discipline); frameworks increasingly ship
idempotency middleware, narrowing the audience to hand-rolled endpoints; same
concentrated dev-tool channel where the Stripe kit has 0 organic sales — expect
~$0 absent distribution; and a live purchase remains unverified until the owner's
own test purchase.
