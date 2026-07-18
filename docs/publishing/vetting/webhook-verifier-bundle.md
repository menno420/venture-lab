# Title Vetting — Webhook Verifier Bundle (Stripe + GitHub + Slack + Shopify)

> **Status:** `plan` — **HARD-GATED: blocked until the GitHub (D5), Slack
> (D14), and Shopify (D13) component publish clicks are executed. NO ungated
> bundle click is queued.**
>
> Bundle packet mirroring the [Ship-It Bundle](bundle-starter.md) precedent —
> the second-of-its-kind HARD-GATED bundle, gated on a missing *referent*
> (unpublished component products), not a missing artifact. A storefront bundle
> is assembled from **existing live products**; of the four webhook kits only
> the Stripe kit is LIVE (the other three are queued owner clicks), so the
> bundle cannot be created yet by anyone, owner included. The first §7 rows are
> therefore blocking owner steps. Every step marked **⚑ OWNER-GATE** is an owner
> click, never automated.

**Title:** Webhook Verifier Bundle — Stripe + GitHub + Slack + Shopify Test Kits ·
**Category:** digital product / bundle · **Date vetted:** 2026-07-18

Product: [`candidates/webhook-verifier-bundle/`](../../../candidates/webhook-verifier-bundle/README.md)
(bundle of [`stripe-webhook-test-kit`](../../../candidates/stripe-webhook-test-kit/README.md) $29 **LIVE**
+ [`github-webhook-test-kit`](../../../candidates/github-webhook-test-kit/README.md) $29
+ [`slack-webhook-test-kit`](../../../candidates/slack-webhook-test-kit/README.md) $29
+ [`shopify-webhook-test-kit`](../../../candidates/shopify-webhook-test-kit/README.md) $29;
launch assets in [`docs/launch/webhook-verifier-bundle/`](../../launch/webhook-verifier-bundle/owner-actions.md)).

## 1. Built — bundle assembly zip (reproducible), no new product code

Unlike the Ship-It Bundle (which shipped no artifact of its own), this bundle
ships a real assembly zip: `package.sh` produces
`candidates/webhook-verifier-bundle/dist/webhook-verifier-bundle-v0.1.zip`
containing the four component buyer zips **verbatim** plus the bundle README /
QUICKSTART / MANIFEST / PROVENANCE — no component is modified. The build is
byte-reproducible (allow-list copy + fixed mtimes + sorted entries + `zip -X`,
the same convention as the four component `package.sh` scripts); two clean
rebuilds this session produced an identical sha256:

```
$ ./package.sh >/dev/null && sha256sum dist/webhook-verifier-bundle-v0.1.zip   # build 1
28f61d8a33309310640375581ff7a6d2f1320bc03bdecbbc1c08c83d5aaf26c8  dist/webhook-verifier-bundle-v0.1.zip
$ ./package.sh >/dev/null && sha256sum dist/webhook-verifier-bundle-v0.1.zip   # build 2
28f61d8a33309310640375581ff7a6d2f1320bc03bdecbbc1c08c83d5aaf26c8  dist/webhook-verifier-bundle-v0.1.zip
```

Bundle artifact: **`webhook-verifier-bundle-v0.1.zip` sha256
`28f61d8a…f26c8` (121,689 B, 10 entries).** The four component artifact pins
(the real source of truth, re-verified against the committed dists this session,
base `main@ae36afb`):

```
$ sha256sum candidates/*-webhook-test-kit/dist/*.zip
d3ac5f88620976c4dee15f70801eba5986faa47f4898a1a3bda4907336eeb0d8  stripe-webhook-test-kit-v0.1.zip
e17b08bac25b047942281c00eb0047ae592d6bda790284aade7b6cf58dcbf6a9  github-webhook-test-kit-v0.1.zip
9ea865735de0402a534f872f816c8cc1eea68fcecfb114b3a1499114abd755e8  slack-webhook-test-kit-v0.1.zip
8ff06e534187170e3d9622e72f43b7587b7e4f5e63feee4ad3917fd211ee0423  shopify-webhook-test-kit-v0.1.zip
```

- [x] All four component pins match `MANIFEST.json`, both on disk and inside the
      built bundle zip — asserted by the assembly test (`test_bundle.py`, 8
      tests green; wired as the `webhook-verifier-bundle-tests` CI job).
- [x] Component build/test evidence is NOT re-claimed here — it lives in each
      component packet and is inherited by reference. Re-run this session as a
      sanity check: **67 component tests green** (Stripe 14 + GitHub 18 + Slack
      18 + Shopify 17, `python3 -m unittest test_http_realpath` in each dir).

## 2. Collision scan

- [x] "Webhook Verifier Bundle" is descriptive-generic; storefront namespace is
      per-account, so no title-availability gate applies. No trademark-style
      collision (not exhaustively searched — low-risk category, same call as the
      component packets). Distinct from the Ship-It Bundle (different components,
      different price).

## 3. Market / price

- [x] **$79 one-time fixed** vs **$116 bought separately** (4 × $29). All four
      kits are priced at exactly $29 — Stripe is LIVE at $29; GitHub / Slack /
      Shopify were each set at $29 on the Stripe-kit precedent (their §3 rows).
      Pricing math (from
      [`PROVENANCE.md`](../../../candidates/webhook-verifier-bundle/PROVENANCE.md)):
      ~30% target off $116 = ≈$81.20; **$79** is the clean price point at/under
      that line → **$37 / 31.9% off**. Real cross-sell discount, not a
      manufactured anchor. **Never price at $116** (zero discount voids the
      bundle rationale — same rule Ship-It records for its $68 total).
- [x] Conservative expectation: 0–2 sales/month absent distribution — the
      bundle adds a **price point**, not a new audience or channel. Honest null:
      no bundle-vs-separate conversion evidence for this catalog (SWTK is live
      in measurement mode with 0 organic sales to date; the other three have no
      sales history). v2 scope (a future `_webhook-kit-core/` extraction, or
      adding kit N+5 to the bundle) is deferred until the v1 bundle shows any
      signal.

## 4–5. Packaging

- [x] Buyer receives `webhook-verifier-bundle-v0.1.zip` (the four component zips
      verbatim + docs) OR, on a native Gumroad bundle, the four component
      products' own uploads. Either way the delivered artifacts are exactly the
      four pinned component zips (§1). Checkout/format verification is inherited
      from the component packets and re-checked at the §7 verify row (test
      purchase must deliver all four zips, spot-checked against the §1 pins).

## 6. Listing copy (drafted in-repo — nothing published)

- [x] [`docs/launch/webhook-verifier-bundle/listing-copy.md`](../../launch/webhook-verifier-bundle/listing-copy.md)
      at catalog parity (Title / Short ≤200 chars / Long / Bullets / FAQ — the
      webhook-kit / SWTK listing shape). Claim-check against the component
      packets: the per-provider scheme lines (Stripe `t=`/`v1=` timestamped;
      GitHub `sha256=` hex no-timestamp; Slack `v0=` hex 5-min window; Shopify
      base64 no-timestamp) match each kit's README/GOTCHAS; the honest "verifier
      test kits, not full frameworks" v0.x caveat is carried; a "what exactly do
      I download" FAQ states the zip-of-zips reality. Owner click-script:
      [`owner-actions.md`](../../launch/webhook-verifier-bundle/owner-actions.md).

## 7. ⚑ OWNER-GATE — component clicks first, then the bundle (queued, never automated)

Seat output = this queued OWNER-ACTION block; the seat performed **none** of it.
Like [bundle-starter](bundle-starter.md), the first rows are **blocking** — a
bundle of unpublished products cannot exist, so every row below them is frozen by
construction. NO bundle click is queued ungated. There are no open decisions in
this packet: the storefront is forced to Gumroad by the components (a bundle
lives in the account that owns its components), and the price is the listing's
cited $79. So the numbered steps below carry no flag marker — the flag tokens
live on the checkbox rows, and the queue derives zero D-items from this packet by
construction. HOW detail:
[`owner-actions.md`](../../launch/webhook-verifier-bundle/owner-actions.md).

**OWNER-ACTION — Create "Webhook Verifier Bundle" at $79 from the four live kits**
1. **Component clicks first (blocking):** execute the GitHub (D5), Slack (D14),
   and Shopify (D13) webhook-kit publish clicks (their own §7 packets) — all
   four kits must be LIVE before any bundle step exists. (Stripe is already
   live, DONE 2026-07-12.)
2. **Bundle creation:** same Gumroad account → New product → **Bundle** →
   name = "Webhook Verifier Bundle — Stripe + GitHub + Slack + Shopify Test
   Kits" → select the four live kits as contents (or upload the reproducible
   `webhook-verifier-bundle-v0.1.zip`).
3. **Copy:** paste Title / Short + Long / Bullets / FAQ from
   [`listing-copy.md`](../../launch/webhook-verifier-bundle/listing-copy.md).
4. **Price:** **$79 one-time, fixed** (§3; never $116).
5. **Publish + verify:** publish, copy the public bundle URL, storefront
   preview/test purchase confirming all four zips deliver (spot-check against
   the §1 sha256 pins).

- [ ] ⚑ **Owner:** execute the GitHub Webhook Test Kit ($29) publish click —
      blocking: the GitHub kit publish click must be executed first (a Gumroad
      bundle references existing live products; queued OWNER-QUEUE D5, packet
      `github-webhook-test-kit.md` §7). Nothing below proceeds.
- [ ] ⚑ **Owner:** execute the Slack Webhook Test Kit ($29) publish click —
      blocking: the Slack kit publish click must be executed first (same
      live-referent rule; queued OWNER-QUEUE D14, packet
      `slack-webhook-test-kit.md` §7). Nothing below proceeds.
- [ ] ⚑ **Owner:** execute the Shopify Webhook Test Kit ($29) publish click —
      blocking: the Shopify kit publish click must be executed first (same
      live-referent rule; queued OWNER-QUEUE D13, packet
      `shopify-webhook-test-kit.md` §7). Nothing below proceeds. (Stripe is
      already live — DONE 2026-07-12 — so it carries no blocking row here.)
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

**Verdict: NOT actionable yet — HARD-GATED on the GitHub (D5) / Slack (D14) /
Shopify (D13) component clicks, by design; publish-ready the moment all four
kits are live.** Everything agent-doable is done and evidenced: a real,
byte-reproducible assembly zip (double-rebuild sha256 `28f61d8a…f26c8`) with an
8-test assembly check wired into CI, listing copy at parity, price cited ($79 vs
$116 with the discount math), the four component pins re-verified, and the §7
sequence puts the blocking component clicks first with no ungated bundle click.
Honest caveats: zero conversion evidence for the bundle (components have
near-zero sales history); only Stripe is live today; live purchase verification
of the components themselves remains with their own packets.
