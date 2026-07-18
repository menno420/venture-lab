# CORS Preflight Test Kit — owner publish click-script

> **Status:** `reference`

QUEUED (2026-07-18, products lane — new sellable built under ORDER 016's continued
autonomous-build authorization, reaffirmed by the live owner turn 2026-07-18).
This is a NEW dev-tool kit in the API-robustness family (browser cross-origin /
CORS correctness — a different problem class from the webhook signature kits, the
idempotency kit, the rate-limit kit, the pagination kit, and the JWT kit), built on
the same proven kit template. No freeze applies: the kit has no Stripe/payment-path
dependency of its own (the ORDER 003 gate, lifted 2026-07-11 by PR #22, never
attached to it). Honest caveat: a live purchase of ANY catalog product besides the
Stripe kit remains unverified — QUEUED means the owner may click, not that this
product's delivery is live-proven. This is a click-script for the owner, not a
request to any agent; no agent performs publish/spend/account actions.

### ⚑ — Publish "CORS Preflight Test Kit" at $29 (one-time)
- **WHAT:** Create a $29 one-time digital product on your own no-code storefront,
  selling `candidates/cors-preflight-test-kit/dist/cors-preflight-test-kit-v0.1.zip`,
  using `docs/launch/cors-preflight-test-kit/listing-copy.md`.
- **WHERE:** gumroad.com → *New product* → *Digital product* (price $29) — same
  account as the live Stripe Webhook Test Kit listing
  (<https://mennomagic01.gumroad.com/l/stripe-webhook-test-kit>) — or
  lemonsqueezy.com equivalent, in your own account.
- **HOW:** 1) Sign in. 2) New product → Digital product. 3) Name = "CORS Preflight
  Test Kit". 4) Price = $29 one-time. 5) Upload the dist zip. 6) Paste the listing
  copy (Title / Short / Long / Bullets / FAQ; set the refund/license lines the copy
  marks owner-to-set). 7) Publish. 8) Copy the public product URL. Optional
  same-visit cross-sell: add one line to the JWT / idempotency / rate-limit /
  webhook kit listings pointing at this kit — a developer hardening a browser-facing
  API needs correct CORS AND safe retries AND correct throttling AND a verifier that
  can't be bypassed, first-ten path channel 2.
- **WHY:** The catalog's first CORS kit — the browser-facing edge of API robustness,
  the pair to the server-internal kits, on the same proven template. The two worst
  CORS outcomes — a config that silently blocks every browser request, and one that
  silently reflects any origin (open CORS, so any website can read authenticated
  responses) — are invisible to `curl` and to a same-origin unit test, and the kit
  ships the checks that catch both (preflight ok status, Allow-Origin echo + Vary,
  Allow-Methods, Allow-Headers incl. the `*`-doesn't-cover-Authorization footgun,
  credentials-vs-`*`, and the open-reflection guard) plus a correct/naive reference
  pair that proves the checks work. Conservative expectation: 0–5 sales in 90 days,
  $0–$145; zero distribution = $0 (the intake's own line — the Stripe kit has 0
  organic sales as of the last check).
- **UNBLOCKS:** The first-ten-customers funnel (dev.to "your CORS is either broken
  in the browser or wide open — here's how to tell in 30 seconds" gotcha article ⚑ →
  dev-tool cross-link ⚑ → Gumroad Discover ⚑) and another API-robustness dev-tool
  rung at $29.
- **VERIFIED-WHEN:** The public URL loads a purchasable $29 page AND a preview/test
  purchase delivers the zip whose sha256 matches the ARTIFACT line below AND the
  real-path suite is green in CI on the built head SHA (the
  `cors-preflight-test-kit-tests` job in `.github/workflows/kit-tests.yml`).
- **ARTIFACT (verified 2026-07-18):** upload exactly
  `candidates/cors-preflight-test-kit/dist/cors-preflight-test-kit-v0.1.zip` @ sha256
  `5c754e4432385d8c3b3f892a5ff572ddcf0e13cb0e07ee0dad522705be0b6c29`
  (35,779 bytes, 13 content files; byte-reproducible via `package.sh` —
  unconditional double rebuild produced the identical sha; the committed dist IS
  that build). Executed verification from the extracted bundle in a clean dir: the
  37-test real-path HTTP suite green from the extracted copy (`Ran 37 tests / OK`);
  `node cptk.js demo` correct-config all-pass AND naive-config flagged on 4
  properties; real-secret-shape scan **0 hits** (no secret-shaped strings ship).
  If the source ever changes: rebuild, re-pin this line, and treat any uploaded
  copy as STALE until re-uploaded.

## Price precedent chain

$29 one-time — set by catalog precedent, not a fresh ideation ruling. The Stripe
Webhook Test Kit sells LIVE at exactly $29 for the same product SHAPE (stdlib-only
harness + docs-derived fixtures + a correct/naive reference pair + byte-reproducible
bundle); the GitHub, Slack, and Shopify Webhook Test Kits and the Idempotency,
Rate-Limit, Pagination, and JWT kits are queued at $29. This kit is the same shape
applied to a new problem class (browser cross-origin / CORS correctness rather than
signature verification, dedup, throttling, result-set integrity, or token security),
same effort tier, adjacent (and wider — both front-end and back-end) buyer. Chain:
Kill-Rule Intake Kit $15 = False-Green Test Trap $15 < Merge-Wall Cookbook $19 =
template-packs $19 PWYW < **$29 this kit** = Stripe kit $29 (live) =
GitHub/Slack/Shopify/Idempotency/Rate-Limit/Pagination/JWT kits $29 (queued) <
Field Manual $39 < Membership Kit $49.
