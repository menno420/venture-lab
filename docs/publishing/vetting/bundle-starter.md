# Title Vetting — Ship-It Bundle (Membership Kit + Template Pack)

> **Status:** `plan` — **HARD-GATED: blocked until the ⚑B and ⚑D component
> publish clicks are executed. NO ungated bundle click is queued.**
>
> PRODUCT #6 packet of the 2026-07-13 night run (ORDER 008). Sixth packet in
> this directory, second HARD-GATED one (after
> [photo-packs](photo-packs.md)) — but gated on a *different* kind of wall:
> not a missing artifact, a missing *referent*. A Gumroad bundle is assembled
> from **existing live products**; as of 2026-07-13 both components are
> click-queued (⚑B PR #106, ⚑D PR #108), not live, so the bundle cannot be
> created yet by anyone, owner included. The first §7 rows are therefore
> blocking owner steps. Every step marked **⚑ OWNER-GATE** is an owner click,
> never automated.

**Title:** Ship-It Bundle — Membership-Site Kit + Agent-Workflow Template Pack ·
**Category:** digital product / bundle · **Date vetted:** 2026-07-13

Product: [`candidates/BUNDLE-LISTING.md`](../../../candidates/BUNDLE-LISTING.md)
(bundle of [`candidates/membership-kit/`](../../../candidates/membership-kit/LISTING.md) $49
+ [`candidates/template-packs/`](../../../candidates/template-packs/LISTING.md) $19 PWYW;
launch assets in [`docs/launch/bundle-starter/`](../../launch/bundle-starter/owner-actions.md)).

## 1. Built — **N/A with reason (honest null: a bundle has no artifact of its own)**

Stage 6 of [`docs/products/TEMPLATE.md`](../../products/TEMPLATE.md)
(package + sha) is **N/A for this product, with the rationale stated
explicitly rather than silently skipped**: a Gumroad bundle *references the
existing live component products* — it uploads no new file, so there is no
new zip to package, no `package.sh`, no double-rebuild, and no new sha256.
Faking one (e.g. zipping the two zips) would create a SECOND artifact chain
to keep in sync with the components and would not be what the buyer
receives — Gumroad delivers the components' own uploads. **The component
shas ARE the artifact pins**, and both were re-verified against the
committed dists this session (executed 2026-07-13, branch
`claude/night-bundle-packet`, base `cf4f17e`):

```
$ sha256sum candidates/membership-kit/dist/membership-kit-v0.2.zip candidates/template-packs/dist/template-packs-v0.1.zip
9f262fc84008ad7b1517116ef999c331672d756f6d68fe5378682e38e1d5d3e1  candidates/membership-kit/dist/membership-kit-v0.2.zip
d65d4c9ef4b23f3ef7fed7277ef6d73f659891d83773eac9d27e86e35463a2b3  candidates/template-packs/dist/template-packs-v0.1.zip
```

- [x] membership-kit pin matches its packet
      ([membership-kit.md](membership-kit.md) §1 / the ARTIFACT line in
      [owner-actions.md](../../launch/membership-kit/owner-actions.md)):
      `9f262fc8…d5d3e1` — the 2026-07-13 dist refresh (40,547 B), verified.
- [x] template-packs pin matches its packet ([template-packs.md](template-packs.md)
      §1): `d65d4c9e…3a2b3` (12,989 B), verified.
- [x] Component build/test evidence is NOT re-claimed here — it lives in the
      component packets (kit: 36 packaged tests green from the extracted
      bundle, PR #106; pack: zero-runtime honest null with executed
      substitutes, PR #108) and is inherited by reference, not re-asserted.

## 2. Collision scan

- [x] "Ship-It Bundle" is descriptive-generic; storefront namespace is
      per-account, so no KDP-style title-availability gate applies. No
      trademark-style collision identified (not exhaustively searched —
      low-risk category, same call as the component packets).

## 3. Market / price

- [x] **$59 one-time fixed** vs **$68 bought separately** ($49 kit + $19
      suggested for the PWYW pack) — both numbers cited from
      [`candidates/BUNDLE-LISTING.md`](../../../candidates/BUNDLE-LISTING.md)
      § Pricing, which frames the $9 off as "a modest, honest nudge," not a
      manufactured discount anchor. The bundle price is FIXED even though
      the pack alone is PWYW — inheriting PWYW would let the bundle undercut
      the $49 kit alone, which is incoherent pricing.
- [x] Conservative expectation (Q-0259.4): 0–2 sales/month absent
      distribution, same as the components — the bundle adds a **price
      point**, not a new audience or channel. Honest null: no evidence
      exists on bundle-vs-separate conversion for this catalog (zero sales
      history on the components themselves); v2 scope (adding the $39 field
      manual for a three-product bundle) is deliberately deferred until the
      v1 bundle has any signal at all.

## 4–5. Packaging

- [x] **N/A by construction** (see §1) — the buyer receives exactly
      `membership-kit-v0.2.zip` + `template-packs-v0.1.zip`, delivered by
      the storefront from the component products' own uploads. Checkout/
      format verification is inherited from the component packets and
      re-checked at the bundle's own §7 verify row (test purchase must
      deliver BOTH zips, spot-checked against the §1 pins).

## 6. Listing copy (drafted in-repo — nothing published)

- [x] [`docs/launch/bundle-starter/listing-copy.md`](../../launch/bundle-starter/listing-copy.md)
      refreshed 2026-07-13 from
      [`candidates/BUNDLE-LISTING.md`](../../../candidates/BUNDLE-LISTING.md)
      to catalog parity (Title / short ≤200 chars (190) / long / bullets /
      FAQ — the membership-kit/template-packs/SWTK shape). Claim-check
      against the component packets: "36 tests" matches the kit packet's
      extracted-bundle run; "three advisory fail-open hooks" matches the
      pack packet's executed hook check; the honest v0.x caveats are carried
      verbatim, and a "what exactly do I download" FAQ states the
      two-existing-zips reality. The source doc's stale "nothing published"
      header was fixed the same session (SWTK live PR #86; components
      click-queued PR #106/#108).

## 7. ⚑ OWNER-GATE — component clicks first, then the bundle (queued, never automated)

Seat output = this queued OWNER-ACTION block; the seat performed **none** of
it. Like [photo-packs](photo-packs.md), the first rows are **blocking** — a
bundle of unpublished products cannot exist, so every row below them is
frozen by construction. NO bundle click is queued ungated. There are no open
decisions in this packet: the storefront is forced to Gumroad by the
components (a bundle lives in the account that owns its components — the
component packets' storefront picks decide, and both default Gumroad), and
the price is the listing's cited $59. So the numbered steps below carry no
flag marker — the flag tokens live on the checkbox rows, and the queue
derives zero D-items from this packet by construction. HOW detail:
[`owner-actions.md`](../../launch/bundle-starter/owner-actions.md).

**OWNER-ACTION — Create "Ship-It Bundle" at $59 from the two live components**
1. **Component clicks first (blocking):** execute the B membership-kit
   click ([membership-kit.md](membership-kit.md) §7) and the D
   template-packs click ([template-packs.md](template-packs.md) §7) —
   both products must be LIVE before any bundle step exists.
2. **Bundle creation:** same Gumroad account → New product → **Bundle** →
   name = "Ship-It Bundle — Membership-Site Kit + Agent-Workflow Template
   Pack" → select the two live products as contents.
3. **Copy:** paste Title / Short + Long description / Bullets / FAQ from
   [`listing-copy.md`](../../launch/bundle-starter/listing-copy.md).
4. **Price:** **$59 one-time, fixed** (not PWYW — §3).
5. **Publish + verify:** publish, copy the public bundle URL, storefront
   preview/test purchase confirming BOTH zips deliver (spot-check against
   the §1 sha256 pins).

- [ ] ⚑ **Owner:** execute the ⚑B membership-kit ($49) publish click —
      blocking: ⚑B membership-kit publish click must be executed first (a
      Gumroad bundle references existing live products; click queued PR
      #106, [membership-kit.md](membership-kit.md) §7). Nothing below
      proceeds.
- [ ] ⚑ **Owner:** execute the ⚑D template-packs ($19 PWYW) publish click —
      blocking: ⚑D template-packs publish click must be executed first
      (same live-referent rule; click queued PR #108,
      [template-packs.md](template-packs.md) §7). Nothing below proceeds.
- [ ] ⚑ **Owner:** create the Gumroad bundle of the two live products (New
      product → Bundle, both components selected).
- [ ] ⚑ **Owner:** listing copy pasted from the refreshed bundle
      listing-copy.
- [ ] ⚑ **Owner:** price set ($59 one-time fixed; $68-separate comparison
      cited in the copy).
- [ ] ⚑ **Owner:** the publish click + preview/test purchase delivering
      BOTH zips (sha256 spot-check against the §1 pins) + public bundle URL
      copied.
- [ ] Seat (post-click, no money moved): record the launch durably on
      `main` — verified bundle URL, price, timestamp — in the style of
      [`docs/launch/stripe-webhook-test-kit/LAUNCH-LOG.md`](../../launch/stripe-webhook-test-kit/LAUNCH-LOG.md);
      flip these rows to `- [x] … — DONE <date>` per the DONE disposition
      (never flip a DONE row back); this also closes the "refresh the $59
      bundle listing" post-click seat row queued in
      [template-packs.md](template-packs.md) §7.

---

**Verdict: NOT actionable yet — HARD-GATED on the ⚑B/⚑D component clicks,
by design; publish-ready the moment both components are live.** Everything
agent-doable is done and evidenced: listing copy at parity, price cited
($59 vs $68), stage-6 recorded as an explicit N/A-with-reason (no bundle
artifact exists or should — the re-verified component shas are the pins),
and the §7 sequence puts the blocking component clicks first with no
ungated bundle click. Honest caveats: zero conversion evidence for the
bundle (components have no sales history yet); the field manual joins only
in a v2 bundle after v1 shows any signal; live purchase verification of the
components themselves (⚑A-style) remains with their own packets.
