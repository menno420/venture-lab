# JWT Auth Test Kit — owner publish click-script

> **Status:** `reference`

QUEUED (2026-07-18, products lane — new sellable built under ORDER 016's continued
autonomous-build authorization, reaffirmed by the live owner turn 2026-07-18). This
is a NEW dev-tool kit in the API-robustness family (JWT verifier security / auth
bypass — the highest-severity problem class in it, a different class from the
webhook signature kits, the idempotency kit, the rate-limit kit, and the pagination
kit), built on the same proven kit template. No freeze applies: the kit has no
Stripe/payment-path dependency of its own (the ORDER 003 gate, lifted 2026-07-11 by
PR #22, never attached to it). Honest caveat: a live purchase of ANY catalog product
besides the Stripe kit remains unverified — QUEUED means the owner may click, not
that this product's delivery is live-proven. This is a click-script for the owner,
not a request to any agent; no agent performs publish/spend/account actions.

### ⚑ — Publish "JWT Auth Test Kit" at $29 (one-time)
- **WHAT:** Create a $29 one-time digital product on your own no-code storefront,
  selling `candidates/jwt-auth-test-kit/dist/jwt-auth-test-kit-v0.1.zip`, using
  `docs/launch/jwt-auth-test-kit/listing-copy.md`.
- **WHERE:** gumroad.com → *New product* → *Digital product* (price $29) — same
  account as the live Stripe Webhook Test Kit listing
  (<https://mennomagic01.gumroad.com/l/stripe-webhook-test-kit>) — or
  lemonsqueezy.com equivalent, in your own account.
- **HOW:** 1) Sign in. 2) New product → Digital product. 3) Name = "JWT Auth Test
  Kit". 4) Price = $29 one-time. 5) Upload the dist zip. 6) Paste the listing copy
  (Title / Short / Long / Bullets / FAQ; set the refund/license lines the copy marks
  owner-to-set). 7) Publish. 8) Copy the public product URL. Optional same-visit
  cross-sell: add one line to the Idempotency kit, Rate-Limit kit, Pagination kit,
  and webhook kit listings pointing at this kit — a developer hardening an API needs
  a secure JWT verifier alongside safe-retry (idempotency), throttling (rate
  limits), and correct pagination, first-ten path channel 2.
- **WHY:** The catalog's first JWT-auth / auth-bypass kit — the highest-severity
  API-robustness rung, the security-incident tier above the correctness kits, on the
  same proven template. The `alg:none` and RS256→HS256 algorithm-confusion bypasses
  are real, cheap-to-ship auth bypasses that are invisible in a green unit-test
  suite, and the kit ships the checks that catch them (reject alg:none, reject
  algorithm-confusion, verify the signature, enforce exp/nbf/aud/iss, fail closed on
  malformed) plus a correct/naive reference pair that proves the checks work.
  Conservative expectation: 0–5 sales in 90 days, $0–$145; zero distribution = $0
  (the intake's own line — the Stripe kit has 0 organic sales as of the last check).
- **UNBLOCKS:** The first-ten-customers funnel (dev.to "your JWT verifier probably
  accepts alg:none / is vulnerable to algorithm confusion" gotcha article ⚑ →
  dev-tool cross-link ⚑ → Gumroad Discover ⚑) and a fifth API-robustness dev-tool
  rung at $29 — the auth-bypass tier.
- **VERIFIED-WHEN:** The public URL loads a purchasable $29 page AND a preview/test
  purchase delivers the zip whose sha256 matches the ARTIFACT line below AND the
  real-path suite is green in CI on the built head SHA (the `jwt-auth-test-kit-tests`
  job in `.github/workflows/kit-tests.yml`).
- **ARTIFACT (verified 2026-07-18):** upload exactly
  `candidates/jwt-auth-test-kit/dist/jwt-auth-test-kit-v0.1.zip` @ sha256
  `d772b26e11ac9e7673c3dd4a47fa9c1671384ae3b8805d1068ccc2d55f391a61`
  (40,703 bytes, 13 content files; byte-reproducible via `package.sh` —
  unconditional double rebuild produced the identical sha; the committed dist IS
  that build). Executed verification from the extracted bundle in a clean dir: the
  47-test real-path HTTP suite green from the extracted copy (`Ran 47 tests / OK`);
  `node jatk.js demo` correct-verifier all-pass AND naive-verifier flagged on 6
  properties; real-secret-shape scan **0 hits** (only .env.example placeholders + a
  labelled TEST public key + a non-secret demo secret). If the source ever changes:
  rebuild, re-pin this line, and treat any uploaded copy as STALE until re-uploaded.

## Price precedent chain

$29 one-time — set by catalog precedent, not a fresh ideation ruling. The Stripe
Webhook Test Kit sells LIVE at exactly $29 for the same product SHAPE (stdlib-only
harness + docs-derived fixtures + a correct/naive reference pair + byte-reproducible
bundle); the GitHub, Slack, and Shopify Webhook Test Kits, the Idempotency Key Test
Kit, the Rate-Limit Test Kit, and the Pagination Test Kit are queued at $29. This kit
is the same shape applied to the highest-severity problem class (JWT verifier
security / auth bypass rather than signature verification, dedup, throttling, or
pagination), same effort tier, adjacent buyer. Chain: Kill-Rule Intake Kit $15 =
False-Green Test Trap $15 < Merge-Wall Cookbook $19 = template-packs $19 PWYW <
**$29 this kit** = Stripe kit $29 (live) = GitHub/Slack/Shopify kits $29 (queued) =
Idempotency kit $29 (queued) = Rate-Limit kit $29 (queued) = Pagination kit $29
(queued) < Field Manual $39 < Membership Kit $49.
