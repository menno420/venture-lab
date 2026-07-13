# The False-Green Test Trap — owner publish click-script

> **Status:** `reference`

QUEUED (2026-07-13, ORDER 008 night run, PRODUCT #8). No freeze applies:
this is a guide + offline stdlib tool with no Stripe/payment-path dependency
of its own, so the ORDER 003 gate (which froze ⚑B/⚑D and was lifted
2026-07-11 by PR #22) never attached to it. Honest caveat: a live purchase
of ANY catalog product besides SWTK remains unverified — QUEUED means the
owner may click, not that this product's delivery is live-proven. This is a
click-script for the owner, not a request to any agent; no agent performs
publish/spend/account actions.

### ⚑ — Publish "The False-Green Test Trap" at $15 (one-time)
- **WHAT:** Create a $15 one-time digital product on your own no-code
  storefront, selling
  `candidates/false-green-test-trap/dist/false-green-test-trap-v0.1.zip`,
  using `docs/launch/false-green-test-trap/listing-copy.md`.
- **WHERE:** gumroad.com → *New product* → *Digital product* (price $15), or
  lemonsqueezy.com equivalent, in your own account.
- **HOW:** 1) Sign in. 2) New product → Digital product. 3) Name = "The
  False-Green Test Trap". 4) Price = $15 one-time. 5) Upload the dist zip.
  6) Paste the listing copy (Title / Short / Long / Bullets / FAQ).
  7) Publish. 8) Copy the public product URL.
- **WHY:** Broad high-intent dev pain ("tests pass, production broke") with
  the catalog's most auditable credibility mechanic — every chapter cites
  committed file@sha in the public repo — plus a soft funnel to the live
  $29 SWTK (the guide's README cross-links it; the intake scored the
  candidate 3.73 weighted, its distribution axis capped by free-content
  competition). Conservative expectation: 0–4 sales in 90 days, $0–$60;
  zero distribution = $0 (the intake's own line — its WTP axis scored 2/5
  and the listing FAQ tells strong practitioners to buy nothing).
- **UNBLOCKS:** First methodology-guide sale; the SWTK cross-sell surface
  (guide→kit); a natural pairing with the Kill-Rule Intake Kit at the same
  $15 rung for a future methodology-tier bundle.
- **VERIFIED-WHEN:** The public URL loads a purchasable $15 page and a
  preview/test purchase delivers the zip whose sha256 matches the ARTIFACT
  line below.
- **ARTIFACT (verified 2026-07-13):** upload exactly
  `candidates/false-green-test-trap/dist/false-green-test-trap-v0.1.zip` @
  sha256 `1d83702b7259191a88e16ae6238758c7fb46cf0c9c4884dfb6514c01487017b4`
  (25,825 bytes; byte-reproducible via `package.sh` — double rebuild
  produced the identical sha; the committed dist IS that build). Executed
  verification from the extracted bundle in a clean dir: the tool's test
  suite `Ran 8 tests … OK`; `vendor_fixture.py` run end-to-end on the
  included sample payload (exit 0, 7 null fields enumerated incl.
  `data.object.customer_email` — the war-story field); all 14 files valid
  UTF-8, every markdown file H1-headed with balanced fences; secret-pattern
  scan 0 hits; no `.DS_Store`, no `__pycache__`, no junk entries in the
  archive listing.

## Price precedent chain

$15 sits on the catalog's existing rungs, tied with the Kill-Rule Intake
Kit at the bottom: Kill-Rule Intake Kit $15 (click-queued, PRODUCT #7,
same night) = **$15 this guide** < Agent-Workflow Template Pack $19 PWYW
(PR #108) < SWTK $29 (live, PR #86) < Agent Fleet Field Manual $39
(PR #110) < Membership Kit $49 (PR #106). $15 was set at intake
(`candidates/false-green-test-trap/INTAKE.md`: "Conservative revenue
estimate: $15 one-time") and is recorded identically in the listing copy,
the §7 packet, and this script. A compact methodology guide + small tool
prices at the bottom rung honestly — it competes with free blog content and
says so in its own intake.
