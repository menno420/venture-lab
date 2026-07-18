# Idempotency Key Test Kit — owner publish click-script

> **Status:** `reference`

QUEUED (2026-07-18, products lane — new sellable built under ORDER 016's
continued autonomous-build authorization, reaffirmed by the live owner turn
2026-07-18). This is a NEW, non-webhook dev-tool kit (idempotency / safe-retry,
a different problem class from the webhook signature kits), built on the same
proven kit template. No freeze applies: the kit has no Stripe/payment-path
dependency of its own (the ORDER 003 gate, lifted 2026-07-11 by PR #22, never
attached to it). Honest caveat: a live purchase of ANY catalog product besides
the Stripe kit remains unverified — QUEUED means the owner may click, not that
this product's delivery is live-proven. This is a click-script for the owner, not
a request to any agent; no agent performs publish/spend/account actions.

### ⚑ — Publish "Idempotency Key Test Kit" at $29 (one-time)
- **WHAT:** Create a $29 one-time digital product on your own no-code
  storefront, selling
  `candidates/idempotency-key-test-kit/dist/idempotency-key-test-kit-v0.1.zip`,
  using `docs/launch/idempotency-key-test-kit/listing-copy.md`.
- **WHERE:** gumroad.com → *New product* → *Digital product* (price $29) —
  same account as the live Stripe Webhook Test Kit listing
  (<https://mennomagic01.gumroad.com/l/stripe-webhook-test-kit>) — or
  lemonsqueezy.com equivalent, in your own account.
- **HOW:** 1) Sign in. 2) New product → Digital product. 3) Name = "Idempotency
  Key Test Kit". 4) Price = $29 one-time. 5) Upload the dist zip. 6) Paste the
  listing copy (Title / Short / Long / Bullets / FAQ; set the refund/license
  lines the copy marks owner-to-set). 7) Publish. 8) Copy the public product URL.
  Optional same-visit cross-sell: add one line to the live Stripe kit listing (and
  the other dev-tool listings) pointing at this kit — a developer wiring Stripe
  Checkout webhooks (inbound) is the same buyer who needs safe retries on their
  own writes (outbound), first-ten path channel 2.
- **WHY:** The catalog's first idempotency/safe-retry kit — the outbound
  companion to the inbound webhook-verifier line, on the same proven template.
  "Your retry double-charged the customer" is a real, expensive, and unit-test-
  invisible bug, and the kit ships the checks that catch it (replay/exactly-once,
  same-key-different-body rejection, concurrency in-flight lock, missing-key
  policy) plus a correct/naive reference pair that proves the checks work.
  Conservative expectation: 0–5 sales in 90 days, $0–$145; zero distribution =
  $0 (the intake's own line — the Stripe kit has 0 organic sales as of the last
  check).
- **UNBLOCKS:** The first-ten-customers funnel (dev.to "double-charge on retry"
  gotcha article ⚑ → dev-tool cross-link ⚑ → Gumroad Discover ⚑) and a new
  dev-tool rung at $29.
- **VERIFIED-WHEN:** The public URL loads a purchasable $29 page AND a
  preview/test purchase delivers the zip whose sha256 matches the ARTIFACT line
  below AND the real-path suite is green in CI on the built head SHA (the
  `idempotency-key-test-kit-tests` job in `.github/workflows/kit-tests.yml`).
- **ARTIFACT (verified 2026-07-18):** upload exactly
  `candidates/idempotency-key-test-kit/dist/idempotency-key-test-kit-v0.1.zip`
  @ sha256
  `8607803d5fd7286e9f86f1515981ea1ca6052ae06d7a8d417526dd85a796f6e1`
  (32,925 bytes, 14 content files; byte-reproducible via `package.sh` —
  unconditional double rebuild produced the identical sha; the committed dist IS
  that build). Executed verification from the extracted bundle in a clean dir:
  the 20-test real-path HTTP suite green from the extracted copy (`Ran 20 tests
  / OK`); `node ikt.js demo` correct-stub all-pass AND naive-stub flagged on 4
  properties; real-secret-shape scan **0 hits** (no secret-shaped strings ship).
  If the source ever changes: rebuild, re-pin this line, and treat any uploaded
  copy as STALE until re-uploaded.

## Price precedent chain

$29 one-time — set by catalog precedent, not a fresh ideation ruling. The
Stripe Webhook Test Kit sells LIVE at exactly $29 for the same product SHAPE
(stdlib-only harness + real-shape/docs-derived fixtures + hostile/edge cases +
byte-reproducible bundle); the GitHub, Slack, and Shopify Webhook Test Kits are
queued at $29. This kit is the same shape applied to a different problem class
(idempotency/safe-retry rather than signature verification), same effort tier,
adjacent buyer. Chain: Kill-Rule Intake Kit $15 = False-Green Test Trap $15 <
Merge-Wall Cookbook $19 = template-packs $19 PWYW < **$29 this kit** = Stripe kit
$29 (live) = GitHub/Slack/Shopify kits $29 (queued) < Field Manual $39 <
Membership Kit $49.
