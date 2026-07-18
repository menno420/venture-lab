# Title Vetting — API Robustness Bundle (Idempotency + Rate-Limit + Pagination + JWT Auth)

> **Status:** `plan` — **HARD-GATED: blocked until the Idempotency (D7), JWT
> Auth (D9), Pagination (D15), and Rate-Limit (D18) component publish clicks are
> executed. NO ungated bundle click is queued.**
>
> Bundle packet mirroring the [Webhook Verifier Bundle](webhook-verifier-bundle.md)
> precedent — the third HARD-GATED bundle, gated on a missing *referent*
> (unpublished component products), not a missing artifact. A storefront bundle
> is assembled from **existing live products**; none of the four own-endpoint
> kits is LIVE (all four are queued owner clicks), so the bundle cannot be
> created yet by anyone, owner included. The first §7 rows are therefore blocking
> owner steps. Every step marked **⚑ OWNER-GATE** is an owner click, never
> automated.

**Title:** API Robustness Bundle — Idempotency + Rate-Limit + Pagination + JWT
Auth Test Kits · **Category:** digital product / bundle · **Date vetted:** 2026-07-18

Product: [`candidates/api-robustness-bundle/`](../../../candidates/api-robustness-bundle/README.md)
(bundle of [`idempotency-key-test-kit`](../../../candidates/idempotency-key-test-kit/README.md) $29
+ [`rate-limit-test-kit`](../../../candidates/rate-limit-test-kit/README.md) $29
+ [`pagination-test-kit`](../../../candidates/pagination-test-kit/README.md) $29
+ [`jwt-auth-test-kit`](../../../candidates/jwt-auth-test-kit/README.md) $29;
launch assets in [`docs/launch/api-robustness-bundle/`](../../launch/api-robustness-bundle/owner-actions.md)).

## 1. Built — bundle assembly zip (reproducible), no new product code

Like the Webhook Verifier Bundle, this bundle ships a real assembly zip:
`package.sh` produces
`candidates/api-robustness-bundle/dist/api-robustness-bundle-v0.1.zip`
containing the four component buyer zips **verbatim** plus the bundle README /
QUICKSTART / MANIFEST / PROVENANCE — no component is modified. The build is
byte-reproducible (allow-list copy + fixed mtimes + sorted entries + `zip -X`,
the same convention as the four component `package.sh` scripts and the webhook
bundle); two clean rebuilds this session produced an identical sha256:

```
$ ./package.sh >/dev/null && sha256sum dist/api-robustness-bundle-v0.1.zip   # build 1
6be74b6d78a77180a133fd09c31c452baaea77497cd8db63461b9ee43dfb560c  dist/api-robustness-bundle-v0.1.zip
$ ./package.sh >/dev/null && sha256sum dist/api-robustness-bundle-v0.1.zip   # build 2
6be74b6d78a77180a133fd09c31c452baaea77497cd8db63461b9ee43dfb560c  dist/api-robustness-bundle-v0.1.zip
```

Bundle artifact: **`api-robustness-bundle-v0.1.zip` sha256
`6be74b6d…b560c` (160,844 B, 10 entries).** The four component artifact pins
(the real source of truth, re-verified against the committed dists this session,
base `main@2fb86bf`):

```
$ sha256sum candidates/{idempotency-key,rate-limit,pagination,jwt-auth}-test-kit/dist/*.zip
8607803d5fd7286e9f86f1515981ea1ca6052ae06d7a8d417526dd85a796f6e1  idempotency-key-test-kit-v0.1.zip
908dc84be5a3e6a5be6ee72123c80cac137f1b2338018e39c6af51ef767ecd45  rate-limit-test-kit-v0.1.zip
ae189fe9465dc7a27204c84b5e187e475fb25158c0f6c31033701fc2e970a118  pagination-test-kit-v0.1.zip
d772b26e11ac9e7673c3dd4a47fa9c1671384ae3b8805d1068ccc2d55f391a61  jwt-auth-test-kit-v0.1.zip
```

- [x] All four component pins match `MANIFEST.json`, both on disk and inside the
      built bundle zip — asserted by the assembly test (`test_bundle.py`, 8
      tests green; wired as the `api-robustness-bundle-tests` CI job).
- [x] Component build/test evidence is NOT re-claimed here — it lives in each
      component packet and is inherited by reference. Re-run this session as a
      sanity check: **125 component tests green** (Idempotency 20 + Rate-Limit 27
      + Pagination 31 + JWT 47, `python3 -m unittest test_http_realpath` in each
      dir).

## 2. Collision scan

- [x] "API Robustness Bundle" is descriptive-generic; storefront namespace is
      per-account, so no title-availability gate applies. No trademark-style
      collision (not exhaustively searched — low-risk category, same call as the
      component packets). Distinct from the Ship-It Bundle (product+process) and
      the Webhook Verifier Bundle (inbound-edge webhook kits) — different
      components, different problem class (own-endpoint robustness).

## 3. Market / price

- [x] **$79 one-time fixed** vs **$116 bought separately** (4 × $29). All four
      kits are priced at exactly $29 (set on the live Stripe-kit precedent —
      their §3 rows / OWNER-QUEUE price rows). Pricing math (from
      [`PROVENANCE.md`](../../../candidates/api-robustness-bundle/PROVENANCE.md)):
      ~30% target off $116 = ≈$81.20; **$79** is the clean price point at/under
      that line → **$37 / 31.9% off**. Priced identically to the Webhook Verifier
      Bundle (also four $29 kits) so the two four-kit SKUs read as one coherent
      catalog. Real cross-sell discount, not a manufactured anchor. **Never price
      at $116** (zero discount voids the bundle rationale — same rule the webhook
      and Ship-It bundles record). The R7 idea card floated ~$89; $79 is the
      deliberate reconciliation to catalog parity (deeper buyer discount, one
      four-kit price).
- [x] Conservative expectation: 0–2 sales/month absent distribution — the
      bundle adds a **price point**, not a new audience or channel. Honest null:
      no bundle-vs-separate conversion evidence for this catalog (none of the
      four components is live; zero sales history). v2 scope (a future
      `candidates/_api-hardening-core/` extraction, or a mega "API Reliability
      Suite" spanning this bundle and the webhook bundle) is deferred until the
      v1 bundle shows any signal.

## 4–5. Packaging

- [x] Buyer receives `api-robustness-bundle-v0.1.zip` (the four component zips
      verbatim + docs) OR, on a native Gumroad bundle, the four component
      products' own uploads. Either way the delivered artifacts are exactly the
      four pinned component zips (§1). Checkout/format verification is inherited
      from the component packets and re-checked at the §7 verify row (test
      purchase must deliver all four zips, spot-checked against the §1 pins).

## 6. Listing copy (drafted in-repo — nothing published)

- [x] [`docs/launch/api-robustness-bundle/listing-copy.md`](../../launch/api-robustness-bundle/listing-copy.md)
      at catalog parity (Title / Short ≤200 chars / Long / Bullets / FAQ — the
      kit / webhook-bundle listing shape). Claim-check against the component
      packets: the per-kit property lines (Idempotency replay/mismatch/
      distinct-keys/concurrent/missing-key; Rate-Limit 429-at-limit/Retry-After/
      RateLimit-*/reset; Pagination traversal/stable-under-mutation/ordering/
      limit/last-page/forged-cursor; JWT valid-accepted/alg-none/signature/
      alg-confusion/expired/nbf/aud/iss/malformed) match each kit's README; the
      honest "own-endpoint test kits, not frameworks" v0.x caveat is carried;
      the JWT "RS256/ES256 signature-math out of scope" honesty is preserved; a
      "what exactly do I download" FAQ states the zip-of-zips reality. Owner
      click-script: [`owner-actions.md`](../../launch/api-robustness-bundle/owner-actions.md).

## 7. ⚑ OWNER-GATE — component clicks first, then the bundle (queued, never automated)

Seat output = this queued OWNER-ACTION block; the seat performed **none** of it.
Like [webhook-verifier-bundle](webhook-verifier-bundle.md), the first rows are
**blocking** — a bundle of unpublished products cannot exist, so every row below
them is frozen by construction. NO bundle click is queued ungated. There are no
open decisions in this packet: the storefront is forced to Gumroad by the
components (a bundle lives in the account that owns its components), and the price
is the listing's cited $79. So the numbered steps below carry no flag marker —
the flag tokens live on the checkbox rows, and the queue derives zero D-items
from this packet by construction. HOW detail:
[`owner-actions.md`](../../launch/api-robustness-bundle/owner-actions.md).

**OWNER-ACTION — Create "API Robustness Bundle" at $79 from the four live kits**
1. **Component clicks first (blocking):** execute the Idempotency (D7), JWT Auth
   (D9), Pagination (D15), and Rate-Limit (D18) test-kit publish clicks (their
   own §7 packets) — all four kits must be LIVE before any bundle step exists.
2. **Bundle creation:** same Gumroad account → New product → **Bundle** →
   name = "API Robustness Bundle — Idempotency + Rate-Limit + Pagination + JWT
   Auth Test Kits" → select the four live kits as contents (or upload the
   reproducible `api-robustness-bundle-v0.1.zip`).
3. **Copy:** paste Title / Short + Long / Bullets / FAQ from
   [`listing-copy.md`](../../launch/api-robustness-bundle/listing-copy.md).
4. **Price:** **$79 one-time, fixed** (§3; never $116).
5. **Publish + verify:** publish, copy the public bundle URL, storefront
   preview/test purchase confirming all four zips deliver (spot-check against
   the §1 sha256 pins).

- [ ] ⚑ **Owner:** execute the Idempotency Key Test Kit ($29) publish click —
      blocking: the Idempotency kit publish click must be executed first (a
      Gumroad bundle references existing live products; queued OWNER-QUEUE D7,
      packet `idempotency-key-test-kit.md` §7). Nothing below proceeds.
- [ ] ⚑ **Owner:** execute the JWT Auth Test Kit ($29) publish click —
      blocking: the JWT Auth kit publish click must be executed first (same
      live-referent rule; queued OWNER-QUEUE D9, packet `jwt-auth-test-kit.md`
      §7). Nothing below proceeds.
- [ ] ⚑ **Owner:** execute the Pagination Test Kit ($29) publish click —
      blocking: the Pagination kit publish click must be executed first (same
      live-referent rule; queued OWNER-QUEUE D15, packet `pagination-test-kit.md`
      §7). Nothing below proceeds.
- [ ] ⚑ **Owner:** execute the Rate-Limit Test Kit ($29) publish click —
      blocking: the Rate-Limit kit publish click must be executed first (same
      live-referent rule; queued OWNER-QUEUE D18, packet `rate-limit-test-kit.md`
      §7). Nothing below proceeds.
- [ ] ⚑ **Owner:** create the Gumroad bundle of the four live kits (New product
      → Bundle, all four components selected, or the single reproducible zip).
- [ ] ⚑ **Owner:** listing copy pasted from the bundle listing-copy.
- [ ] ⚑ **Owner:** price set ($79 one-time fixed — §3; $116-separate comparison
      cited in the copy, never the sale price).
- [ ] ⚑ **Owner:** the publish click + preview/test purchase delivering all four
      zips (sha256 spot-check against the §1 pins) + public bundle URL copied.
- [ ] Seat (post-click, no money moved): record the launch durably on `main` —
      verified bundle URL, price, timestamp — in the style of
      [`docs/launch/stripe-webhook-test-kit/LAUNCH-LOG.md`](../../launch/stripe-webhook-test-kit/LAUNCH-LOG.md);
      flip these rows to `- [x] … — DONE <date>` per the DONE disposition (never
      flip a DONE row back).

---

**Verdict: NOT actionable yet — HARD-GATED on the Idempotency (D7) / JWT (D9) /
Pagination (D15) / Rate-Limit (D18) component clicks, by design; publish-ready
the moment all four kits are live.** Everything agent-doable is done and
evidenced: a real, byte-reproducible assembly zip (double-rebuild sha256
`6be74b6d…b560c`) with an 8-test assembly check wired into CI, listing copy at
parity, price cited ($79 vs $116 with the discount math), the four component
pins re-verified, and the §7 sequence puts the four blocking component clicks
first with no ungated bundle click. Honest caveats: zero conversion evidence for
the bundle (no component is live yet); live purchase verification of the
components themselves remains with their own packets.
