# Shopify Webhook Test Kit — owner publish click-script

> **Status:** `reference`

QUEUED (2026-07-17, products lane — new sellable built under ORDER 016's
overnight autonomous-build authorization; the N+1 of the LIVE Stripe Webhook
Test Kit and the built GitHub + Slack Webhook Test Kits). No freeze applies: the
kit has no Stripe/payment-path dependency of its own, so the ORDER 003 gate
(lifted 2026-07-11 by PR #22) never attached to it. Honest caveat: a live
purchase of ANY catalog product besides SWTK remains unverified — QUEUED means
the owner may click, not that this product's delivery is live-proven. This is a
click-script for the owner, not a request to any agent; no agent performs
publish/spend/account actions.

### ⚑ — Publish "Shopify Webhook Test Kit" at $29 (one-time)
- **WHAT:** Create a $29 one-time digital product on your own no-code
  storefront, selling
  `candidates/shopify-webhook-test-kit/dist/shopify-webhook-test-kit-v0.1.zip`,
  using `docs/launch/shopify-webhook-test-kit/listing-copy.md`.
- **WHERE:** gumroad.com → *New product* → *Digital product* (price $29) —
  same account as the live SWTK listing
  (<https://mennomagic01.gumroad.com/l/stripe-webhook-test-kit>) — or
  lemonsqueezy.com equivalent, in your own account.
- **HOW:** 1) Sign in. 2) New product → Digital product. 3) Name = "Shopify
  Webhook Test Kit". 4) Price = $29 one-time. 5) Upload the dist zip.
  6) Paste the listing copy (Title / Short / Long / Bullets / FAQ; set the
  refund/license lines the copy marks owner-to-set). 7) Publish. 8) Copy the
  public product URL. Optional same-visit cross-sell: add one line to the live
  SWTK and the GWTK/Slack listings pointing at this kit (adjacent buyer, sibling
  products — first-ten path channel 2).
- **WHY:** The fourth rung of the catalog's webhook-kit line, built on the
  proven SWTK template: "verify X-Shopify-Hmac-Sha256 / base64 not hex / hash
  the raw body" is a real, searched pain, and the kit ships the checks Shopify
  will never send you (forged / unsigned / tampered / malformed-base64 webhooks
  + topic routing) plus a pinned known-answer HMAC as an offline proof.
  Conservative expectation: 0–5 sales in 90 days, $0–$145; zero distribution =
  $0 (the intake's own line — SWTK has 0 organic sales as of the last check).
- **UNBLOCKS:** The first-ten-customers funnel (dev.to gotcha article ⚑ →
  SWTK/GWTK/Slack cross-link ⚑ → Gumroad Discover ⚑) and the catalog's fourth
  dev-tool rung at $29.
- **VERIFIED-WHEN:** The public URL loads a purchasable $29 page AND a
  preview/test purchase delivers the zip whose sha256 matches the ARTIFACT line
  below AND the real-path suite is green in CI on the built head SHA (the
  `shopify-webhook-test-kit-tests` job in `.github/workflows/kit-tests.yml`).
- **ARTIFACT (verified 2026-07-18):** upload exactly
  `candidates/shopify-webhook-test-kit/dist/shopify-webhook-test-kit-v0.1.zip`
  @ sha256
  `8ff06e534187170e3d9622e72f43b7587b7e4f5e63feee4ad3917fd211ee0423`
  (29,142 bytes, 13 content files; byte-reproducible via `package.sh` —
  unconditional double rebuild produced the identical sha; the committed dist IS
  that build). Executed verification from the extracted bundle in a clean dir:
  the 17-test real-path HTTP suite green from the extracted copy (`Ran 17 tests
  / OK`); `node shwtk.js vector` PASS against the pinned known-answer;
  real-secret-shape scan **0 hits** (the only secret-like strings are
  `.env.example`/GOTCHAS/QUICKSTART lines naming token prefixes NOT to use). If
  the source ever changes: rebuild, re-pin this line, and treat any uploaded
  copy as STALE until re-uploaded.

## Price precedent chain

$29 one-time — set by catalog precedent, not a fresh ideation ruling. The
Stripe Webhook Test Kit sells LIVE at exactly $29 (`price_cents 2900` verified
on the live page); the GitHub and Slack Webhook Test Kits are queued at $29;
this kit is the same product shape for the Shopify webhook-signing surface —
same stdlib-only harness + real-shape-fixture + hostile-mode structure, adjacent
buyer. Chain: Kill-Rule Intake Kit $15 = False-Green Test Trap $15 < Merge-Wall
Cookbook $19 = template-packs $19 PWYW < **$29 this kit** = SWTK $29 (live)
= GWTK $29 (queued) = Slack kit $29 (queued) < Field Manual $39 < Membership Kit
$49.
