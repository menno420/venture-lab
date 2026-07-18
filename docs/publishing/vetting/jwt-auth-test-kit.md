# Title Vetting — JWT Auth Test Kit

> **Status:** `plan`
>
> New PRODUCT packet in the vetting directory, so the publish click rides the
> derived owner queue (`../OWNER-QUEUE.md` via `scripts/derive_owner_queue.py`).
> Built under **ORDER 016** (live owner overnight-work order, reaffirmed by the
> live owner turn 2026-07-18) as a NEW sellable (roadmap R3) — the same proven
> kit template applied to the HIGHEST-SEVERITY problem class in the family (JWT
> verifier security / auth bypass, not signature verification of an inbound
> provider, not dedup/safe-retry, not throttling, and not pagination). No freeze
> applies — a dev-tool kit with no payment-path dependency (the ORDER 003 ⚑B/⚑D
> freeze, lifted 2026-07-11 by PR #22, never attached to it). Every step marked
> **⚑ OWNER-GATE** is an owner click, never automated.

**Title:** JWT Auth Test Kit · **Category:** digital product / dev tool ·
**Date vetted:** 2026-07-18

Product: [`candidates/jwt-auth-test-kit/`](../../../candidates/jwt-auth-test-kit/README.md)
(v0.1; buyer bundle `dist/jwt-auth-test-kit-v0.1.zip`; launch assets in
[`docs/launch/jwt-auth-test-kit/`](../../launch/jwt-auth-test-kit/owner-actions.md);
intake [`INTAKE.md`](../../../candidates/jwt-auth-test-kit/INTAKE.md), priced
$29 on catalog precedent).

## 1. Built (verified this session, 2026-07-18)

- [x] Stdlib-only harness in two languages (`jatk.py` + `jatk.js` Node port, same
      commands: `check` / the nine single-property checks / `demo` / `list`), a
      CORRECT reference verifier (`stub_handler.py`: pins an `HS256` algorithm
      allowlist, verifies the signature with `hmac.compare_digest`, and enforces
      `exp`/`nbf`/`aud`/`iss` over `GET /protected`), a deliberately NAIVE verifier
      (`stub_handler_naive.py`: accepts `alg:none`, HMACs a token against a public
      key it holds → algorithm-confusion, and checks no time/audience/issuer
      claims), a one-page `GOTCHAS.md` (bypass classes, each mapped to a kit
      command), plus `QUICKSTART.md` and a placeholders-only `.env.example`.
- [x] **Genuinely NEW and HIGHEST-severity problem class, not another webhook /
      idempotency / rate-limit / pagination kit:** the webhook kits verify an
      INBOUND provider signature; the idempotency kit verifies a STATEFUL safe-retry
      contract; the rate-limit kit verifies a THROTTLING contract; the pagination
      kit verifies RESULT-SET INTEGRITY; this kit verifies a buyer's OWN JWT
      verifier's SECURITY — it accepts a valid token and rejects the auth-bypass
      classes. Where the others catch correctness bugs, a failure here is a security
      incident (auth bypass). Zero shared fixtures or crypto/dedup/throttle/paging
      scheme with the siblings; fresh PROVENANCE.
- [x] **Nine properties checked, each PASS/FAIL/SKIP against a buyer endpoint:**
      (1) **valid-accepted** — a valid HS256 token with correct claims is accepted;
      (2) **alg-none-rejected** — an `{"alg":"none"}` unsigned token is rejected
      (RFC 8725 §3.1); (3) **signature-rejected** — a tampered payload AND a
      wrong-key token are rejected (RFC 7515); (4) **alg-confusion-rejected** — an
      HS256 token signed with the RSA/EC public-key bytes is rejected
      (RFC 8725 §2.1); (5) **expired-rejected** — `exp` in the past is rejected;
      (6) **not-yet-valid-rejected** — `nbf`/`iat` in the future is rejected;
      (7) **audience-enforced** — a wrong/missing `aud` is rejected (SKIP if none
      configured); (8) **issuer-enforced** — a wrong/missing `iss` is rejected (SKIP
      if none configured); (9) **malformed-rejected** — a non-three-segment / bad
      base64url token is rejected.
- [x] **Value proof built in (correct vs naive):** `jatk demo` runs all nine against
      BOTH bundled verifiers with a loud zero-accounts banner — the CORRECT verifier
      passes all nine and the NAIVE verifier is FLAGGED on `alg-none-rejected` /
      `alg-confusion-rejected` / `expired-rejected` / `not-yet-valid-rejected` /
      `audience-enforced` / `issuer-enforced` (6 bypasses). The kit demonstrably
      distinguishes a secure verifier from a bypassable one, and is HONEST that
      three properties (`valid-accepted`, `signature-rejected`, `malformed-rejected`)
      do NOT distinguish the two (documented in `stub_handler_naive.py` and
      `GOTCHAS.md`).
- [x] **Honest source + scope discipline:** `fixtures/PROVENANCE.md` grounds every
      property in RFC 7519 (JWT claims), RFC 7515 (JWS signature), and RFC 8725
      ("JWT BCP" — the `alg:none` and RS256→HS256 confusion attacks), pins a sha256
      per vendored fixture, and states the DEPENDENCY scope plainly: the kit is
      stdlib-only (HS256 via `hmac`/`hashlib`/`base64`/`json`), which fully covers
      valid-accept + every attack class; real RS256/ES256 signature-math
      verification is scoped OUT-OF-BAND (it would need an asymmetric-crypto dep) and
      the listing's "what it does NOT do" says so — no overclaimed RS256 coverage.
      The confusion attack needs no RSA verify (it forges an HS256 token over the
      public-key bytes). The bundled key is a throwaway RSA PUBLIC key (its private
      half discarded at generation); the demo secret is a clearly-labelled
      non-secret.
- [x] **Tests (real-path, executed 2026-07-18):** 47-test HTTP-layer suite — every
      request fired over actual HTTP to a reference verifier on an ephemeral port;
      time claims are fixed ±1h offsets, so no test waits on a real clock. Green from
      source (`Ran 47 tests / OK`) AND from the extracted zip in a clean dir
      (`Ran 47 tests / OK`). Covers: manifest/fixture shape; the PEM being a PUBLIC
      key; token-minting units; the correct verifier accepting the valid token and
      returning 401 for each of the 14 attack tokens over HTTP; the full suite green
      on the correct verifier; the kit FLAGGING the naive verifier on the six
      bypasses — with `valid-accepted` + `signature-rejected` + `malformed-rejected`
      honestly NOT distinguishing (both verifiers handle them the same); the SKIP
      paths proving `audience-enforced`/`issuer-enforced` SKIP (not falsely fail)
      when no expected value is configured, and `alg-confusion-rejected` SKIP without
      a pubkey; plus direct `verify_jwt` reason-code coverage (alg_none,
      bad_signature for the confusion token under a pinned verifier, expired,
      not_yet_valid, bad_audience, bad_issuer, malformed) and confirmation that the
      naive verifier ACCEPTS the confusion + alg:none tokens.
- [x] Suite wired into CI: `jwt-auth-test-kit-tests` job added to
      `.github/workflows/kit-tests.yml`, same convention as the Stripe / GitHub /
      Slack / Shopify / idempotency / rate-limit / pagination kit jobs.
- [x] Buyer bundle built via allow-list `package.sh` (kit pattern: fixed mtimes,
      sorted entries, `zip -X`; excludes `INTAKE.md`, `package.sh`, `dist/`),
      **byte-reproducible** — unconditional double rebuild 2026-07-18 produced the
      identical sha256, committed dist IS that build.
- [x] **sha256 `d772b26e11ac9e7673c3dd4a47fa9c1671384ae3b8805d1068ccc2d55f391a61`**
      (40,703 bytes, 13 content files) — also pinned in the click-script's ARTIFACT
      line.
- [x] Checkout/format verified from the artifact itself: clean-dir unzip —
      `README.md` + `QUICKSTART.md` + `GOTCHAS.md` + `.env.example` + harness ×2 +
      both verifiers + test suite at top level, `fixtures/` with `MANIFEST.json` +
      `PROVENANCE.md` + `test_public_key.pem` + `sample_tokens.json`;
      real-secret-shape scan (`sk_live_`/`whsec_`/`AKIA`/private key/etc.) **0 hits**
      (the bundled PEM is a PUBLIC key; the demo secret is a labelled non-secret); no
      junk entries in the archive.

## 2. Collision scan

- [x] No in-catalog title collision. Closest shipped products, boundaries
      disclosed: the four webhook kits (**Stripe $29** LIVE, **GitHub/Slack/Shopify
      $29** queued), the **Idempotency Key Test Kit $29** (queued), the **Rate-Limit
      Test Kit $29** (queued), and the **Pagination Test Kit $29** (queued) share the
      kit SHAPE but a DIFFERENT problem class — the webhook kits verify an inbound
      HMAC signature, the idempotency kit verifies safe-retry dedup, the rate-limit
      kit verifies throttling, the pagination kit verifies result-set integrity, and
      this kit verifies JWT verifier security / auth bypass (reject alg:none +
      algorithm-confusion + expired/not-yet-valid + wrong-aud/iss + malformed; accept
      a valid token). Zero shared fixtures or code, fresh PROVENANCE. Honest
      positioning: this is the *auth-bypass* rung of API robustness — the
      highest-severity tier, a security incident when it fails — so the listings
      cross-reference rather than claim each other's scope.
- [x] Same/adjacent buyer audience as the dev-tool catalog (intake's
      concentrated-channel risk, disclosed); narrower still because every major
      language ships a vetted JWT library, so the audience is specifically
      hand-rolled verifiers and mis-configured library calls (defaults that trust the
      token `alg`, the wrong key passed to verify, claims left unchecked).

## 3. Market / price

- [x] Price **$29 one-time** — set on catalog precedent and recorded identically in
      `INTAKE.md`, the listing copy, the click-script, and here. Precedent: the
      Stripe Webhook Test Kit sells LIVE at exactly $29 for the same product shape
      (stdlib harness + docs-derived fixtures + a correct/naive reference pair +
      byte-reproducible bundle), and the GitHub/Slack/Shopify kits + the Idempotency
      kit + the Rate-Limit kit + the Pagination kit are queued at $29. Chain: $15
      (kill-rule kit, false-green) < $19 (merge-wall, template-packs PWYW) < **$29
      this kit** = Stripe $29 (live) = GitHub/Slack/Shopify $29 (queued) =
      Idempotency $29 (queued) = Rate-Limit $29 (queued) = Pagination $29 (queued) <
      field-manual $39 < membership-kit $49. Conservative expectation 0–5 sales /
      $0–$145 first-90-day, $0 absent distribution (the intake's own line; validation
      signal ≥1 sale OR ≥50 article reads in 30 days, else ledgered negative; T+7
      funnel checkpoint / T+30 kill deadline armed as a KILL-CHECK here once the click
      is DONE-flipped). One honest plus over the correctness-bug siblings: the failure
      mode here is a security incident (auth bypass), which lifts willingness-to-pay.

## 4–5. Packaging

- [x] Buyer bundle is the allow-listed `package.sh` output (`README.md` +
      `QUICKSTART.md` + `GOTCHAS.md` + `.env.example` + `jatk.py` + `jatk.js` +
      `stub_handler.py` + `stub_handler_naive.py` + `test_http_realpath.py` +
      `fixtures/`; deliberately excludes the lane-internal `INTAKE.md`, `package.sh`,
      `dist/`). No cover image ships — owner adds one or uses the storefront default.

## 6. Listing copy (drafted in-repo — nothing published)

- [x] [`listing-copy.md`](../../launch/jwt-auth-test-kit/listing-copy.md) at catalog
      parity (Title / Short ≤200 chars (187 measured) / Long / Bullets / FAQ) and
      checked claim-by-claim against the extracted bundle: "47 tests" = the suite
      that ran green twice this session; "correct/naive demo" = executed (correct
      all-pass, naive flagged on 6) both languages; the FAQ + "what it does NOT do"
      section states the honest boundaries (not a webhook/idempotency/rate-limit/
      pagination kit; RS256/ES256 signature-math out of the stdlib scope; the aud/iss
      properties SKIP on an unconfigured endpoint; verifier-contract scope only, not
      issuance/rotation/refresh/revocation/transport); a PROVENANCE-FOOTER pins
      `file@sha` sources; refund/license lines present, marked owner-to-set.

## 7. ⚑ OWNER-GATE — publish clicks (queued, never automated)

Seat output = this queued OWNER-ACTION block; the seat performed **none** of it. It
is the queue-parseable form of the click-script in `owner-actions.md` (same directory
as this packet's launch assets) — the HOW detail lives there; no freeze applies (no
payment-path gate).

**OWNER-ACTION — Publish "JWT Auth Test Kit" at $29 one-time**
1. **Storefront account:** owner signs into the storefront (the Stripe kit Gumroad
   account already exists and has payout configured).
2. **⚑ Storefront pick:** **Gumroad** (default — same account as the live Stripe
   kit listing; the click-script's HOW is written against it) or Lemon Squeezy —
   owner's call; either works with the same zip + copy.
3. **Product:** New product → Digital product; Name = "JWT Auth Test Kit";
   upload `candidates/jwt-auth-test-kit/dist/jwt-auth-test-kit-v0.1.zip` and verify
   the upload matches sha256 `d772b26e…f391a61` (full hash in §1 and the click-script
   ARTIFACT line — never upload a stale local copy).
4. **Copy:** paste Title / Short + Long description / Bullets / FAQ from the
   `listing-copy.md` in this product's launch dir; set the refund/license lines the
   copy marks owner-to-set.
5. **Price:** set **$29 one-time** (fixed — catalog precedent; the Stripe kit is
   live at the identical price for the identical product shape, GitHub/Slack/Shopify
   + Idempotency + Rate-Limit + Pagination queued at $29).
6. **Publish + record:** publish, copy the public product URL, storefront preview/
   test purchase to confirm the zip delivers. Optional same-visit cross-sell: one
   line on the Idempotency kit, Rate-Limit kit, Pagination kit, and webhook kit
   listings pointing here (first-ten path channel 2).

- [ ] ⚑ **Owner:** storefront pick (**Gumroad** (default)) — or Lemon Squeezy.
- [ ] ⚑ **Owner:** zip uploaded + sha256 spot-check against §1.
- [ ] ⚑ **Owner:** listing copy pasted + refund/license lines set.
- [ ] ⚑ **Owner:** price set (**$29 one-time** (default per catalog precedent + the live Stripe kit price)).
- [ ] ⚑ **Owner:** the publish click + preview/test purchase + public URL copied.
- [ ] Seat (post-click, no money moved): record the launch durably on `main` —
      verified listing URL, price, timestamp — in the style of the Stripe kit
      `LAUNCH-LOG.md`, flip these rows to the `— DONE <date>` disposition, arm the
      intake's kill clock as a `KILL-CHECK:` line here (T+7 funnel checkpoint · T+30
      kill-rule deadline: ≥1 sale OR ≥50 article reads, else ledger NEGATIVE +
      pause/delist), and regenerate the owner queue.

---

**Verdict: publish-ready up to the owner gate.** Built + priced + listing drafted +
checkout/format verified + sha recorded (all evidenced above); the product parks at
§7 (owner clicks) by design. Honest caveats: the kit is stdlib-only and does NOT
perform real RS256/ES256 signature-math verification — that is scoped out-of-band and
stated plainly in the listing, so no coverage is overclaimed (the highest-value
bugs — alg:none, algorithm-confusion, exp/nbf, aud/iss, malformed — need no RSA
verify and are fully covered); the `audience-enforced`/`issuer-enforced` properties
SKIP (not fail) on an endpoint that configures no expected value; the kit tests the
externally-visible verifier contract (which tokens are accepted vs. rejected), not
token issuance, key rotation, refresh, revocation, or transport (use HTTPS);
`valid-accepted`, `signature-rejected`, and `malformed-rejected` honestly do NOT
distinguish a secure verifier from the naive one (all three pass on both),
documented; the free-substitute risk is real (RFC 8725 is public and every language
ships a JWT library; the paid delta is the harness testing the buyer's OWN endpoint —
including the alg:none and algorithm-confusion tokens a from-memory test skips — + the
correct/naive reference pair + provenance discipline); the audience is narrowed to
hand-rolled/mis-configured verifiers; same concentrated dev-tool channel where the
Stripe kit has 0 organic sales — expect ~$0 absent distribution; and a live purchase
remains unverified until the owner's own test purchase.
