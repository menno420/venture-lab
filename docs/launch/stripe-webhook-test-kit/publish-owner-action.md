**STATUS: NOT-QUEUED — do not action.**

> **Status:** `owner-guidance`

This publish click is **earned**, not queued. It becomes actionable ONLY after
BOTH of the following hold:

1. The v0.1 real-path HTTP test suite is **green in CI** against the vendored
   real-shape fixtures, on the built head SHA.
2. The **coordinator reviews the evidence** (test output + built zip) and confirms.

Until then this document is a specification of the future click, not an
instruction to perform it. Do not publish, do not create a listing, do not arm
auto-merge.

## Owner-action row (six-field grammar)

- **WHAT:** publish Stripe Webhook Test Kit v0.1 at $29 on a digital marketplace.
- **WHERE:** Gumroad or Lemon Squeezy (Discover).
- **HOW:** upload `candidates/stripe-webhook-test-kit/dist/stripe-webhook-test-kit-v0.1.zip`;
  paste the listing copy from `docs/launch/stripe-webhook-test-kit/LISTING.md`;
  set price $29.
- **WHY:** revenue-lane candidate #1 (eval-001, 2026-07-11); packages the lane's
  paid-for real-Stripe-path lessons into a sellable dev tool.
- **UNBLOCKS:** the first-ten-customers funnel (free gotcha article → free gist →
  StackOverflow answer → this listing → r/stripe).
- **VERIFIED-WHEN:** the live listing URL returns HTTP 200 AND the real-path HTTP
  test is green in CI on the built head SHA.

No secret values are involved in this action — the webhook signing secret is read
from an environment variable at test time and never stored in the repo or the
bundle. The owner performs the click.
