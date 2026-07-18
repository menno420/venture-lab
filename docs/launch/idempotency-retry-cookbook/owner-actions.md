# The Idempotency & Retry Cookbook — owner publish click-script

> **Status:** `reference`

QUEUED (2026-07-18, ORDER 016 continuation). No freeze applies: this is a guide +
stdlib-recipe cookbook with no Stripe/payment-path dependency of its own, so the
ORDER 003 gate (lifted 2026-07-11 by PR #22) never attached to it. Honest caveat:
a live purchase of ANY catalog product besides the live Stripe Webhook Test Kit
remains unverified — QUEUED means the owner may click, not that this product's
delivery is live-proven. This is a click-script for the owner, not a request to
any agent; no agent performs publish/spend/account actions.

### ⚑ — Publish "The Idempotency & Retry Cookbook" at $19 (one-time)
- **WHAT:** Create a $19 one-time digital product on your own no-code storefront,
  selling
  `candidates/idempotency-retry-cookbook/dist/idempotency-retry-cookbook-v0.1.zip`,
  using `docs/launch/idempotency-retry-cookbook/listing-copy.md`.
- **WHERE:** gumroad.com → *New product* → *Digital product* (price $19), or
  lemonsqueezy.com equivalent, in your own account.
- **HOW:** 1) Sign in. 2) New product → Digital product. 3) Name = "The
  Idempotency & Retry Cookbook". 4) Price = $19 one-time. 5) Upload the dist zip.
  6) Paste the listing copy (Title / Short / Long / Bullets / FAQ / the "what it
  does NOT do" honesty section). 7) Publish. 8) Copy the public product URL.
- **WHY:** A broad, high-intent developer audience — anyone integrating a paid or
  stateful API hits the double-charge / retry-storm pain — with a coherent,
  cited, tested pattern set. Natural cross-sell hub for the two companion kits
  (Idempotency Key Test Kit $29, Rate-Limit Test Kit $29): the cookbook teaches
  what those kits verify, and a client that retries on 429 is exactly the one that
  needs idempotent writes. Conservative expectation: 0–4 sales in 90 days, $0–$76;
  zero distribution = $0 (the intake's own line).
- **UNBLOCKS:** A third guide-rung sale on the developer surface; a "safe retries"
  content-marketing seed (the guide doubles as the outline of a launch article);
  cross-sell lift for the Idempotency Key + Rate-Limit test kits.
- **VERIFIED-WHEN:** The public URL loads a purchasable $19 page and a
  preview/test purchase delivers the zip whose sha256 matches the ARTIFACT line
  below. The recipes are self-tested (26 tests green from source, from the
  extracted bundle, and in CI as `idempotency-retry-cookbook-tests`); the prose is
  verified by citation to public specs (Sources footer per chapter); the honest
  limits (in-memory store sketch, snippets-not-your-system, draft headers) are
  disclosed in the listing FAQ, the README honesty box, PROVENANCE.md, and guide
  ch.8 — not asserted away.
- **ARTIFACT (verified 2026-07-18):** upload exactly
  `candidates/idempotency-retry-cookbook/dist/idempotency-retry-cookbook-v0.1.zip`
  @ sha256 `9579f98ae0ffbb5e670e03aa48673ad45d070632ac657aef98dde4bbfc8a8981`
  (43,177 bytes; byte-reproducible via `package.sh` — double rebuild produced the
  identical sha; the committed dist IS that build). Executed verification from the
  extracted bundle in a clean dir: the 26-test recipe self-test passes
  (`Ran 26 tests ... OK`) both from source and from the extracted zip; inventory
  16/16 vs INCLUDED.md; all 12 markdown files valid UTF-8 non-empty, H1-headed
  with balanced fences; real-secret-shape scan **0 hits**; no `.DS_Store`, no
  `__pycache__`, no `.pyc`, no junk entries in the archive listing.

## Price precedent chain

$19 one-time — set at intake
(`candidates/idempotency-retry-cookbook/INTAKE.md`: "Conservative revenue
estimate: $19 one-time") and recorded identically in the listing copy, the §7
packet, and this script. Precedent rung: the **Merge-Wall Cookbook** and the
**Auto-Merge Enabler Cookbook** both sell at $19 (`docs/publishing/vetting/
merge-wall-cookbook.md`, `docs/publishing/vetting/auto-merge-enabler-cookbook.md`)
— cited-throughout, runnable-recipe-shipping cookbooks for a developer audience,
this product's nearest siblings in shape (a teaching cookbook that pairs with its
test kits). Chain: Kill-Rule Intake Kit $15 = False-Green Test Trap $15 <
**$19 this cookbook** = merge-wall-cookbook $19 = auto-merge-enabler-cookbook $19
= template-packs $19 PWYW < the API-robustness test kits $29 each < SWTK $29
(live) < Field Manual $39 < Membership Kit $49. A guide that ships runnable,
cited, self-tested recipes prices at parity with its cookbook siblings and below
the HTTP test kits it teaches the patterns for.
