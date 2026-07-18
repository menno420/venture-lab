# Title Vetting — CORS Preflight Test Kit

> **Status:** `plan`
>
> New PRODUCT packet in the vetting directory, so the publish click rides the
> derived owner queue (`../OWNER-QUEUE.md` via `scripts/derive_owner_queue.py`).
> Built under **ORDER 016** (live owner overnight-work order, reaffirmed by the
> live owner turn 2026-07-18) as a NEW sellable — the same proven kit template
> applied to a NEW problem class (browser cross-origin / CORS correctness, not
> signature verification, dedup/safe-retry, throttling, result-set integrity, or
> token security). No freeze applies — a dev-tool kit with no payment-path
> dependency (the ORDER 003 ⚑B/⚑D freeze, lifted 2026-07-11 by PR #22, never
> attached to it). Every step marked **⚑ OWNER-GATE** is an owner click, never
> automated.

**Title:** CORS Preflight Test Kit · **Category:** digital product / dev tool ·
**Date vetted:** 2026-07-18

Product: [`candidates/cors-preflight-test-kit/`](../../../candidates/cors-preflight-test-kit/README.md)
(v0.1; buyer bundle `dist/cors-preflight-test-kit-v0.1.zip`; launch assets in
[`docs/launch/cors-preflight-test-kit/`](../../launch/cors-preflight-test-kit/owner-actions.md);
intake [`INTAKE.md`](../../../candidates/cors-preflight-test-kit/INTAKE.md), priced
$29 on catalog precedent).

## 1. Built (verified this session, 2026-07-18)

- [x] Stdlib-only harness in two languages (`cptk.py` + `cptk.js` Node port, same
      commands: `check` / `preflight-status` / `allow-origin` / `allow-methods` /
      `allow-headers` / `credentials` / `reflect-guard` / `demo` / `list`), a
      CORRECT reference endpoint (`stub_handler.py`: an allowlist-based CORS
      handler that answers the preflight with `204` + echoed
      `Access-Control-Allow-Origin` + `Vary: Origin` + `-Allow-Methods` +
      `-Allow-Headers` + `-Allow-Credentials`, and returns NO CORS headers for an
      origin off its allowlist), a deliberately NAIVE endpoint
      (`stub_handler_naive.py`: reflects any origin, no `Vary`, no
      `Allow-Methods`/`Allow-Headers` on the preflight), a one-page `GOTCHAS.md`
      (seven failure modes, each mapped to a kit command), plus `QUICKSTART.md` and
      a placeholders-only `.env.example`.
- [x] **Genuinely NEW problem class, not another webhook/idempotency/rate-limit/
      pagination/JWT kit:** the webhook kits verify an INBOUND provider signature;
      the idempotency kit a STATEFUL safe-retry contract; the rate-limit kit a
      THROTTLING contract; the pagination kit RESULT-SET INTEGRITY; the JWT kit
      VERIFIER SECURITY; this kit verifies a buyer's OWN endpoint's BROWSER CORS
      contract — preflight ok status, `Access-Control-Allow-Origin` echo + `Vary`,
      `-Allow-Methods`, `-Allow-Headers`, credentials-vs-`*`, and open-reflection
      guard. Zero shared fixtures or scheme with the siblings.
- [x] **Six properties checked, each PASS/FAIL against a buyer endpoint:**
      (1) **preflight-status** — the cross-origin `OPTIONS` preflight returns an ok
      status (200/204); (2) **allow-origin** — preflight AND actual response carry
      an `Access-Control-Allow-Origin` matching the request `Origin` (or `*`), with
      `Vary: Origin` when the specific origin is echoed; (3) **allow-methods** — the
      preflight's `Access-Control-Allow-Methods` covers the requested method;
      (4) **allow-headers** — the preflight's `Access-Control-Allow-Headers` covers
      every requested header, and flags the Fetch-spec gotcha that a literal `*`
      does NOT cover `Authorization`; (5) **credentials** —
      `Access-Control-Allow-Credentials: true` is never paired with an
      `Access-Control-Allow-Origin: *` (nor `*` methods/headers); (6) **reflect-guard**
      — a disallowed probe origin is NOT reflected into `Access-Control-Allow-Origin`
      (open-CORS security hole), and `*`+credentials is flagged.
- [x] **Value proof built in (correct vs naive):** `cptk demo` runs all six against
      BOTH bundled endpoints with a loud zero-accounts banner — the CORRECT config
      passes all six and the NAIVE config is FLAGGED on `allow-origin` (no `Vary`) /
      `allow-methods` / `allow-headers` / `reflect-guard`. The kit demonstrably
      distinguishes a correct CORS config from a broken one, and is HONEST that two
      properties (`preflight-status`, `credentials`) do NOT distinguish the two
      (documented in `stub_handler_naive.py` and `GOTCHAS.md`).
- [x] **Honest source discipline:** `fixtures/PROVENANCE.md` states up front that
      the fixtures are docs-derived request templates (NOT wire-captured — no
      account/key/service call), pins a sha256 per fixture, and cites every property
      to the WHATWG Fetch Standard "CORS protocol" + MDN CORS. It is explicit about
      scope: this tests server-emitted CORS headers at the HTTP layer (what a
      browser preflight/request checks), does NOT drive a real browser, and does NOT
      cover Private Network Access (`Access-Control-Allow-Private-Network`).
- [x] **Tests (real-path, executed 2026-07-18):** 37-test HTTP-layer suite — every
      request fired over actual HTTP to a reference endpoint on an ephemeral port,
      no timed waits. Green from source (`Ran 37 tests / OK`) AND from the extracted
      zip in a clean dir (`Ran 37 tests / OK`). Covers: manifest/fixture shape; the
      correct config passing each property (204 preflight; echoed origin + `Vary`;
      `Allow-Methods` covers the method; `Allow-Headers` covers `Authorization`
      explicitly; credentials with a specific origin; a disallowed origin gets no
      `Allow-Origin`); the full suite green on the correct config and on a second
      allowlisted origin; the kit FLAGGING the naive config on missing-`Vary` /
      missing-`Allow-Methods` / missing-`Allow-Headers` / arbitrary-origin-reflection
      — with `preflight-status` + `credentials` honestly NOT distinguishing (both
      configs pass them), documented; plus inline edge-case stubs proving the two
      Fetch footguns over real HTTP (`Allow-Headers: *` does NOT cover
      `Authorization`; `Allow-Origin: *` + credentials is flagged; a public `*`
      without credentials passes reflect-guard) and helper unit coverage.
- [x] Suite wired into CI: `cors-preflight-test-kit-tests` job added to
      `.github/workflows/kit-tests.yml`, same convention as the Stripe/GitHub/Slack/
      Shopify/idempotency/rate-limit/pagination/JWT kit jobs.
- [x] Buyer bundle built via allow-list `package.sh` (kit pattern: fixed mtimes,
      sorted entries, `zip -X`; excludes `INTAKE.md`, `package.sh`, `dist/`),
      **byte-reproducible** — unconditional double rebuild 2026-07-18 produced the
      identical sha256, committed dist IS that build.
- [x] **sha256 `5c754e4432385d8c3b3f892a5ff572ddcf0e13cb0e07ee0dad522705be0b6c29`**
      (35,779 bytes, 13 content files) — also pinned in the click-script's ARTIFACT
      line.
- [x] Checkout/format verified from the artifact itself: clean-dir unzip —
      README + QUICKSTART + GOTCHAS + `.env.example` + harness ×2 + both endpoints +
      test suite at top level, `fixtures/` 2 templates + MANIFEST.json +
      PROVENANCE.md; real-secret-shape scan (`sk_live_`/`whsec_`/`AKIA`/private
      key/etc.) **0 hits**; no junk entries in the archive.

## 2. Collision scan

- [x] No in-catalog title collision. Closest shipped products, boundaries
      disclosed: the four webhook kits (**Stripe $29** LIVE, **GitHub/Slack/
      Shopify $29** queued), the **Idempotency Key Test Kit $29**, the **Rate-Limit
      Test Kit $29**, the **Pagination Test Kit $29**, and the **JWT Auth Test Kit
      $29** (all queued) share the kit SHAPE but a DIFFERENT problem class — none
      touches the browser cross-origin contract. Zero shared fixtures or code, fresh
      PROVENANCE. Honest positioning: this is the *browser-facing edge* of API
      robustness — the natural pair to the server-internal kits — so the listings
      cross-reference rather than claim each other's scope.
- [x] Same/adjacent buyer audience as the dev-tool catalog (intake's
      concentrated-channel risk, disclosed), but WIDER than the siblings on one
      honest point: CORS is felt by both front-end and back-end developers, so the
      audience is larger than the server-only kits — though most web frameworks ship
      a CORS middleware, so the sharpest audience is hand-rolled CORS and custom
      middleware.

## 3. Market / price

- [x] Price **$29 one-time** — set on catalog precedent and recorded identically
      in `INTAKE.md`, the listing copy, the click-script, and here. Precedent: the
      Stripe Webhook Test Kit sells LIVE at exactly $29 for the same product shape
      (stdlib harness + docs-derived fixtures + a correct/naive reference pair +
      byte-reproducible bundle), and the GitHub/Slack/Shopify + Idempotency +
      Rate-Limit + Pagination + JWT kits are queued at $29. Chain: $15 (kill-rule
      kit, false-green) < $19 (merge-wall, template-packs PWYW) < **$29 this kit** =
      Stripe $29 (live) = GitHub/Slack/Shopify/Idempotency/Rate-Limit/Pagination/JWT
      $29 (queued) < field-manual $39 < membership-kit $49. Conservative expectation
      0–5 sales / $0–$145 first-90-day, $0 absent distribution (the intake's own
      line; validation signal ≥1 sale OR ≥50 article reads in 30 days, else ledgered
      negative; T+7 funnel checkpoint / T+30 kill deadline armed as a KILL-CHECK here
      once the click is DONE-flipped).

## 4–5. Packaging

- [x] Buyer bundle is the allow-listed `package.sh` output (README + QUICKSTART +
      GOTCHAS + `.env.example` + `cptk.py` + `cptk.js` + `stub_handler.py` +
      `stub_handler_naive.py` + `test_http_realpath.py` + `fixtures/`; deliberately
      excludes the lane-internal `INTAKE.md`, `package.sh`, `dist/`). No cover image
      ships — owner adds one or uses the storefront default.

## 6. Listing copy (drafted in-repo — nothing published)

- [x] [`listing-copy.md`](../../launch/cors-preflight-test-kit/listing-copy.md) at
      catalog parity (Title / Short ≤200 chars / Long / Bullets / FAQ) and checked
      claim-by-claim against the extracted bundle: "37 tests" = the suite that ran
      green twice this session; "two docs-derived templates" = 2 fixtures in the
      zip; the correct/naive demo claim = executed (correct all-pass, naive flagged
      on 4) both languages; the FAQ + "what it does NOT do" section states the
      honest boundaries (not a webhook/idempotency/rate-limit/pagination/JWT kit; no
      real browser; no Private Network Access; single origin + one probe per run;
      fixtures docs-derived not live captures; no live API anything); a
      PROVENANCE-FOOTER pins `file@sha` sources; refund/license lines present,
      marked owner-to-set.

## 7. ⚑ OWNER-GATE — publish clicks (queued, never automated)

Seat output = this queued OWNER-ACTION block; the seat performed **none** of it.
It is the queue-parseable form of the click-script in `owner-actions.md` (same
directory as this packet's launch assets) — the HOW detail lives there; no freeze
applies (no payment-path gate).

**OWNER-ACTION — Publish "CORS Preflight Test Kit" at $29 one-time**
1. **Storefront account:** owner signs into the storefront (the Stripe kit Gumroad
   account already exists and has payout configured).
2. **⚑ Storefront pick:** **Gumroad** (default — same account as the live Stripe
   kit listing; the click-script's HOW is written against it) or Lemon Squeezy —
   owner's call; either works with the same zip + copy.
3. **Product:** New product → Digital product; Name = "CORS Preflight Test Kit";
   upload `candidates/cors-preflight-test-kit/dist/cors-preflight-test-kit-v0.1.zip`
   and verify the upload matches sha256 `5c754e44…be0b6c29` (full hash in §1 and the
   click-script ARTIFACT line — never upload a stale local copy).
4. **Copy:** paste Title / Short + Long description / Bullets / FAQ from the
   `listing-copy.md` in this product's launch dir; set the refund/license lines the
   copy marks owner-to-set.
5. **Price:** set **$29 one-time** (fixed — catalog precedent; the Stripe kit is
   live at the identical price for the identical product shape, the other kits
   queued at $29).
6. **Publish + record:** publish, copy the public product URL, storefront preview/
   test purchase to confirm the zip delivers. Optional same-visit cross-sell: one
   line on the JWT / idempotency / rate-limit / webhook kit listings pointing here.

- [ ] ⚑ **Owner:** storefront pick (**Gumroad** (default)) — or Lemon Squeezy.
- [ ] ⚑ **Owner:** zip uploaded + sha256 spot-check against §1.
- [ ] ⚑ **Owner:** listing copy pasted + refund/license lines set.
- [ ] ⚑ **Owner:** price set (**$29 one-time** (default per catalog precedent + the live Stripe kit price)).
- [ ] ⚑ **Owner:** the publish click + preview/test purchase + public URL copied.
- [ ] Seat (post-click, no money moved): record the launch durably on `main` —
      verified listing URL, price, timestamp — in the style of the Stripe kit
      `LAUNCH-LOG.md`, flip these rows to the `— DONE <date>` disposition, arm the
      intake's kill clock as a `KILL-CHECK:` line here (T+7 funnel checkpoint ·
      T+30 kill-rule deadline: ≥1 sale OR ≥50 article reads, else ledger NEGATIVE +
      pause/delist), and regenerate the owner queue.

---

**Verdict: publish-ready up to the owner gate.** Built + priced + listing drafted +
checkout/format verified + sha recorded (all evidenced above); the product parks at
§7 (owner clicks) by design. Honest caveats: this tests server-emitted CORS response
headers at the HTTP layer (what a browser preflight/request checks) — it does NOT
drive a real browser and does NOT cover Private Network Access
(`Access-Control-Allow-Private-Network`); it tests CORS for the origin you name plus
one disallowed probe, not the whole allowlist or per-route matrix; the `credentials`
property only asserts something when the endpoint enables credentialed CORS;
`preflight-status` and `credentials` honestly do NOT distinguish a correct config
from the naive one (both pass them), documented; the fixtures are docs-derived
request templates, NOT captures from a live API (no account/key/service call — this
repo's no-accounts rule); the free-substitute risk is real (the Fetch standard and
MDN are free; the paid delta is the harness testing the buyer's OWN endpoint +
the correct/naive reference pair + provenance discipline); most web frameworks ship
a CORS middleware, narrowing the sharpest audience to hand-rolled configs; same
concentrated dev-tool channel where the Stripe kit has 0 organic sales — expect ~$0
absent distribution; and a live purchase remains unverified until the owner's own
test purchase.
