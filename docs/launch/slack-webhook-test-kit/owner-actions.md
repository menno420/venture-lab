# Slack Webhook Test Kit — owner publish click-script

> **Status:** `reference`

QUEUED (2026-07-17, products lane — new sellable built under ORDER 016's
overnight autonomous-build authorization; the N+1 of the LIVE Stripe Webhook
Test Kit and the built GitHub Webhook Test Kit). No freeze applies: the kit
has no Stripe/payment-path dependency of its own, so the ORDER 003 gate
(lifted 2026-07-11 by PR #22) never attached to it. Honest caveat: a live
purchase of ANY catalog product besides SWTK remains unverified — QUEUED means
the owner may click, not that this product's delivery is live-proven. This is
a click-script for the owner, not a request to any agent; no agent performs
publish/spend/account actions.

### ⚑ — Publish "Slack Webhook Test Kit" at $29 (one-time)
- **WHAT:** Create a $29 one-time digital product on your own no-code
  storefront, selling
  `candidates/slack-webhook-test-kit/dist/slack-webhook-test-kit-v0.1.zip`,
  using `docs/launch/slack-webhook-test-kit/listing-copy.md`.
- **WHERE:** gumroad.com → *New product* → *Digital product* (price $29) —
  same account as the live SWTK listing
  (<https://mennomagic01.gumroad.com/l/stripe-webhook-test-kit>) — or
  lemonsqueezy.com equivalent, in your own account.
- **HOW:** 1) Sign in. 2) New product → Digital product. 3) Name = "Slack
  Webhook Test Kit". 4) Price = $29 one-time. 5) Upload the dist zip.
  6) Paste the listing copy (Title / Short / Long / Bullets / FAQ; set the
  refund/license lines the copy marks owner-to-set). 7) Publish. 8) Copy the
  public product URL. Optional same-visit cross-sell: add one line to the live
  SWTK and GWTK listings pointing at this kit (same buyer, sibling products —
  first-ten path channel 2).
- **WHY:** The third rung of the catalog's webhook-kit line, built on the
  proven SWTK template: "verify X-Slack-Signature / the 5-minute timestamp is
  on you" is a real, searched pain, and the kit ships the checks Slack will
  never send you (forged / unsigned / stale-timestamp / tampered /
  form-encoded requests + the url_verification challenge) plus Slack's own
  published HMAC worked example as an offline proof. Conservative expectation:
  0–5 sales in 90 days, $0–$145; zero distribution = $0 (the intake's own
  line — SWTK has 0 organic sales as of the last check).
- **UNBLOCKS:** The first-ten-customers funnel (dev.to gotcha article ⚑ →
  SWTK/GWTK cross-link ⚑ → Gumroad Discover ⚑) and the catalog's third
  dev-tool rung at $29.
- **VERIFIED-WHEN:** The public URL loads a purchasable $29 page AND a
  preview/test purchase delivers the zip whose sha256 matches the ARTIFACT
  line below AND the real-path suite is green in CI on the built head SHA (the
  `slack-webhook-test-kit-tests` job in `.github/workflows/kit-tests.yml`).
- **ARTIFACT (verified 2026-07-17):** upload exactly
  `candidates/slack-webhook-test-kit/dist/slack-webhook-test-kit-v0.1.zip`
  @ sha256
  `9ea865735de0402a534f872f816c8cc1eea68fcecfb114b3a1499114abd755e8`
  (29,290 bytes, 14 content files; byte-reproducible via `package.sh` —
  unconditional double rebuild 2026-07-17 produced the identical sha; the
  committed dist IS that build). Executed verification from the extracted
  bundle in a clean dir (2026-07-17): the 18-test real-path HTTP suite green
  from the extracted copy (`Ran 18 tests / OK`); `node swtk.js vector` PASS
  against Slack's published constant; real-secret-shape scan **0 hits** (the
  only secret-like strings are Slack's own PUBLIC documentation worked-example
  values and clearly-fake test secrets, both labeled as such in the files, and
  a `.env.example` line naming token prefixes NOT to use). If the source ever
  changes: rebuild, re-pin this line, and treat any uploaded copy as STALE
  until re-uploaded.

## Price precedent chain

$29 one-time — set by catalog precedent, not a fresh ideation ruling. The
Stripe Webhook Test Kit sells LIVE at exactly $29 (`price_cents 2900` verified
on the live page) and the GitHub Webhook Test Kit is queued at $29; this kit
is the same product shape for the Slack request-signing surface — same
stdlib-only harness + real-shape-fixture + hostile-mode structure, same buyer.
Chain: Kill-Rule Intake Kit $15 = False-Green Test Trap $15 < Merge-Wall
Cookbook $19 = template-packs $19 PWYW < **$29 this kit** = SWTK $29 (live)
= GWTK $29 (queued) < Field Manual $39 < Membership Kit $49.
