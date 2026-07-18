# Provenance & pricing rationale — API Robustness Bundle v0.1

This bundle ships **no new product code**. It is an assembly of four already-built,
already-tested own-endpoint robustness test kits plus the README / QUICKSTART /
MANIFEST in this directory. Every artifact the buyer receives is a component
kit's own published buyer zip, pinned below by sha256.

## Component artifact pins

Verified against the committed component dists on branch
`claude/api-robustness-bundle-2026-07-18` (base `main@2fb86bf`):

| Kit | Price | Status | Artifact | sha256 |
|-----|-------|--------|----------|--------|
| Idempotency Key Test Kit | $29 | queued — OWNER-QUEUE **D7** | `idempotency-key-test-kit-v0.1.zip` | `8607803d5fd7286e9f86f1515981ea1ca6052ae06d7a8d417526dd85a796f6e1` |
| Rate-Limit Test Kit | $29 | queued — OWNER-QUEUE **D18** | `rate-limit-test-kit-v0.1.zip` | `908dc84be5a3e6a5be6ee72123c80cac137f1b2338018e39c6af51ef767ecd45` |
| Pagination Test Kit | $29 | queued — OWNER-QUEUE **D15** | `pagination-test-kit-v0.1.zip` | `ae189fe9465dc7a27204c84b5e187e475fb25158c0f6c31033701fc2e970a118` |
| JWT Auth Test Kit | $29 | queued — OWNER-QUEUE **D9** | `jwt-auth-test-kit-v0.1.zip` | `d772b26e11ac9e7673c3dd4a47fa9c1671384ae3b8805d1068ccc2d55f391a61` |

These four sha256 values are the machine-checked source of truth — they are
duplicated in [`MANIFEST.json`](MANIFEST.json) and asserted by
[`test_bundle.py`](test_bundle.py) both against the component dists on disk and
against the copies packed inside `dist/api-robustness-bundle-v0.1.zip`.

## Pricing rationale

```
component prices:  Idempotency $29 + Rate-Limit $29 + Pagination $29 + JWT $29
sum bought separately:                                     $116
bundle discount (~30% target):     $116 × 0.30 = $34.80 off  →  ≈ $81.20
bundle price (clean point at/under the ~30% line):          $79
actual savings:                    $116 − $79 = $37 off
actual discount:                   $37 / $116 = 31.9%
```

**$79 one-time, fixed.** The four kits are each priced at exactly $29 (set on
the live Stripe-kit precedent — see each kit's vetting packet §3 / OWNER-QUEUE
price rows). A ~30% target off the $116 sum lands at ≈$81.20; **$79** is the
clean price point at (just under) that line, giving an honest **$37 / 31.9%**
discount. This deliberately mirrors the **Webhook Verifier Bundle** (also four
$29 kits → $79): the two four-kit SKUs price identically so the storefront reads
as one coherent catalog, not two ad-hoc anchors. This is a real cross-sell
discount, not a manufactured "half off" anchor: the bundle removes three
checkout decisions for a buyer hardening more than one property, and the $116
comparison is the genuine separate-purchase total. **Never price at $116** — at
$116 the buyer discount is $0 and the bundle rationale voids (same rule the
Ship-It and Webhook Verifier bundles record).

> **Note on the JWT-kit card's `~$89` figure.** The R7 idea that spawned this
> bundle (session card `.sessions/2026-07-18-jwt-auth-test-kit.md`) floated a
> `~$89` anchor. This bundle instead uses **$79** to match the Webhook Verifier
> Bundle exactly — two four-kit SKUs at one price is more honest and more
> legible than two different four-kit anchors, and $79 is the deeper (better)
> buyer discount. The reconciliation is deliberate, not an oversight.

Conservative expectation, mirroring the Webhook Verifier Bundle's honest null:
the bundle adds a **price point**, not a new audience or channel. Absent
distribution, 0–2 sales/month is the same expectation as the components; there
is no bundle-vs-separate conversion evidence for this catalog yet (the four
components have zero sales history — none is live). The bundle is worth cutting
because it is zero-marginal-cost catalog reach off kits that already exist and
already cross-reference each other as a cross-sell channel in their intakes.

## Reproducibility

`package.sh` builds `dist/api-robustness-bundle-v0.1.zip` deterministically
(allow-list copy, fixed mtimes, sorted entries, `zip -X`) — the same convention
the four component `package.sh` scripts and the Webhook Verifier Bundle use.
Because the component zips are themselves byte-reproducible and are copied in
verbatim, two clean rebuilds of the bundle produce an identical sha256. The
double-rebuild sha256 is recorded in the vetting packet §1 and the session card
work log.
