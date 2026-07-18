# Provenance & pricing rationale — Webhook Verifier Bundle v0.1

This bundle ships **no new product code**. It is an assembly of four already-built,
already-tested webhook verifier kits plus the README / QUICKSTART / MANIFEST in
this directory. Every artifact the buyer receives is a component kit's own
published buyer zip, pinned below by sha256.

## Component artifact pins

Verified against the committed component dists on branch
`claude/webhook-verifier-bundle-2026-07-18` (base `main@ae36afb`):

| Kit | Price | Status | Artifact | sha256 |
|-----|-------|--------|----------|--------|
| Stripe Webhook Test Kit | $29 | **LIVE** (Gumroad, PR #86; `docs/launch/stripe-webhook-test-kit/LAUNCH-LOG.md`) | `stripe-webhook-test-kit-v0.1.zip` | `d3ac5f88620976c4dee15f70801eba5986faa47f4898a1a3bda4907336eeb0d8` |
| GitHub Webhook Test Kit | $29 | queued — OWNER-QUEUE **D6** | `github-webhook-test-kit-v0.1.zip` | `e17b08bac25b047942281c00eb0047ae592d6bda790284aade7b6cf58dcbf6a9` |
| Slack Webhook Test Kit | $29 | queued — OWNER-QUEUE **D20** | `slack-webhook-test-kit-v0.1.zip` | `9ea865735de0402a534f872f816c8cc1eea68fcecfb114b3a1499114abd755e8` |
| Shopify Webhook Test Kit | $29 | queued — OWNER-QUEUE **D19** | `shopify-webhook-test-kit-v0.1.zip` | `8ff06e534187170e3d9622e72f43b7587b7e4f5e63feee4ad3917fd211ee0423` |

These four sha256 values are the machine-checked source of truth — they are
duplicated in [`MANIFEST.json`](MANIFEST.json) and asserted by
[`test_bundle.py`](test_bundle.py) both against the component dists on disk and
against the copies packed inside `dist/webhook-verifier-bundle-v0.1.zip`.

## Pricing rationale

```
component prices:  Stripe $29 + GitHub $29 + Slack $29 + Shopify $29
sum bought separately:                                     $116
bundle discount (~30% target):     $116 × 0.30 = $34.80 off  →  ≈ $81.20
bundle price (clean point at/under the ~30% line):          $79
actual savings:                    $116 − $79 = $37 off
actual discount:                   $37 / $116 = 31.9%
```

**$79 one-time, fixed.** The four kits are each priced at exactly $29 (Stripe is
LIVE at $29; GitHub / Slack / Shopify were each set at $29 on the Stripe-kit
precedent — see each kit's vetting packet §3). A ~30% target off the $116 sum
lands at ≈$81.20; **$79** is the clean price point at (just under) that line,
giving an honest **$37 / 31.9%** discount. This is a real cross-sell discount,
not a manufactured "half off" anchor: the bundle removes three checkout
decisions for a buyer wiring up more than one provider, and the $116 comparison
is the genuine separate-purchase total. **Never price at $116** — at $116 the
buyer discount is $0 and the bundle rationale voids (same rule the Ship-It
Bundle records for its $68 separate total).

Conservative expectation, mirroring the Ship-It Bundle's honest null: the bundle
adds a **price point**, not a new audience or channel. Absent distribution,
0–2 sales/month is the same expectation as the components; there is no
bundle-vs-separate conversion evidence for this catalog yet (the components have
near-zero sales history — SWTK is live in measurement mode with 0 organic sales
to date). The bundle is worth cutting because it is zero-marginal-cost catalog
reach off kits that already exist and already cross-reference each other as a
cross-sell channel in their intakes.

## Reproducibility

`package.sh` builds `dist/webhook-verifier-bundle-v0.1.zip` deterministically
(allow-list copy, fixed mtimes, sorted entries, `zip -X`) — the same convention
the four component `package.sh` scripts use. Because the component zips are
themselves byte-reproducible and are copied in verbatim, two clean rebuilds of
the bundle produce an identical sha256. The double-rebuild sha256 is recorded in
the vetting packet §1 and the session card work log.
