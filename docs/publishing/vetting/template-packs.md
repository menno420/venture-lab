# Title Vetting — Agent-Workflow Template Pack

> **Status:** `plan`
>
> Second PRODUCT (non-book) packet in the vetting directory, so the ⚑D
> publish click rides the same derived owner queue as the book catalog
> (`../OWNER-QUEUE.md` via `scripts/derive_owner_queue.py`). Queued under
> ORDER 008 (2026-07-13 night run) after the ⚑B/⚑D freeze was re-verified
> lifted at HEAD: PR #22 (merged 2026-07-11T01:58Z) flipped
> [`owner-actions.md`](../../launch/template-packs/owner-actions.md) to
> UNFROZEN on the coupled ORDER 003 gate (PR #16 squash `912da3e` +
> kit-tests CI run 29135371209 green). Every step marked **⚑ OWNER-GATE**
> is an owner click, never automated.

**Title:** Agent-Workflow Template Pack · **Category:** digital product / template pack ·
**Date vetted:** 2026-07-13

Product: [`candidates/template-packs/`](../../../candidates/template-packs/README.md)
(v0.1; buyer bundle `dist/template-packs-v0.1.zip`; launch assets in
[`docs/launch/template-packs/`](../../launch/template-packs/owner-actions.md)).

## 1. Built (verified this session, 2026-07-13)

- [x] Dist zip rebuilt via `package.sh`, **byte-reproducible** (double rebuild,
      identical sha256), and — unlike the membership-kit case — the rebuild
      reproduced the **committed** zip bit-for-bit: the committed dist is
      FRESH vs source, no refresh needed.
- [x] **sha256 `d65d4c9ef4b23f3ef7fed7277ef6d73f659891d83773eac9d27e86e35463a2b3`**
      (12,989 bytes) — also pinned in the click-script's ARTIFACT line.
- [x] Honest null: the pack ships **no test suite** (it is plain Markdown +
      shell templates with zero runtime, by design — the listing says so).
      Executed verification instead, from the extracted bundle: 3 hook
      scripts pass `sh -n` and run clean under their declared
      `#!/usr/bin/env bash` shebang (advisory output, exit 0);
      `settings.template.json` is valid JSON; all 11 files non-empty valid
      UTF-8.
- [x] Checkout/format verified from the artifact itself: bundle unzipped to a
      clean dir — QUICKSTART + README + INCLUDED at top level; `pack/` carries
      the constitution template, session-card template, discipline playbook,
      hooks README, settings template, 3 hook scripts. Secret-pattern scan:
      zero hits; no `.DS_Store`, no `__pycache__`, no junk entries in the
      archive listing.

## 2. Collision scan

- [x] Product name is descriptive-generic ("agent-workflow template pack") —
      no trademark-style collision risk identified; storefront namespace is
      per-account, so no KDP-style title-availability gate applies.

## 3. Market / price

- [x] Price **$19 pay-what-you-want (suggested)** — precedent recorded in
      [`owner-actions.md`](../../launch/template-packs/owner-actions.md) ⚑D
      and [`candidates/template-packs/LISTING.md`](../../../candidates/template-packs/LISTING.md)
      ("**Pay-what-you-want, $19 suggested** (one-time, free updates to the
      v0.x line)"). Conservative expectation stays 0–3 downloads/month,
      $0–$20/month absent distribution (Q-0259.4 framing).

## 4–5. Packaging

- [x] Buyer bundle is the allow-listed `package.sh` output (QUICKSTART +
      README + INCLUDED + `pack/`; deliberately excludes LISTING.md, dist/,
      package.sh, .git). No cover image ships — owner adds one or uses the
      storefront default.

## 6. Listing copy (drafted in-repo — nothing published)

- [x] [`listing-copy.md`](../../launch/template-packs/listing-copy.md)
      verified 2026-07-13 at membership-kit/SWTK parity (Title / short ≤200
      chars (187) / long / bullets / FAQ) and checked claim-by-claim against
      the extracted bundle: "three advisory fail-open hooks" = the 3 scripts
      (print + exit 0, confirmed by execution); "no deps, no runtime" = true
      (Markdown + shell only); honest "conventions, not a policy engine"
      framing retained. No refresh needed — copy already matches product
      reality.

## 7. ⚑ OWNER-GATE — publish clicks (queued, never automated)

Seat output = this queued OWNER-ACTION block; the seat performed **none** of
it. It is the queue-parseable form of the ⚑D click-script in
[`owner-actions.md`](../../launch/template-packs/owner-actions.md) — the HOW
detail lives there; freeze state UNFROZEN (2026-07-11, PR #22).

**OWNER-ACTION — Publish "Agent-Workflow Template Pack" at $19 pay-what-you-want**
1. **Storefront account:** owner signs into (or creates) the storefront;
   complete its payout setup first or revenue holds.
2. **⚑ Storefront pick:** **Gumroad** (default — simplest PWYW digital-product
   flow; the click-script's HOW is written against it) or Lemon Squeezy —
   owner's call; either works with the same zip + copy.
3. **Product:** New product → Digital product; Name = "Agent-Workflow
   Template Pack"; upload `candidates/template-packs/dist/template-packs-v0.1.zip`
   and verify the upload matches sha256 `d65d4c9e…3a2b3` (full hash in §1 and
   the click-script ARTIFACT line — never upload a stale local copy).
4. **Copy:** paste Title / Short + Long description / Bullets / FAQ from
   [`listing-copy.md`](../../launch/template-packs/listing-copy.md).
5. **Price:** enable **pay-what-you-want**, suggested **$19**, minimum the
   owner's choice.
6. **Publish + record:** publish, copy the public product URL, storefront
   preview/test purchase to confirm the zip delivers.

- [ ] ⚑ **Owner:** storefront account + payout setup.
- [ ] ⚑ **Owner:** storefront pick (**Gumroad** (default)) — or Lemon Squeezy.
- [ ] ⚑ **Owner:** zip uploaded + sha256 spot-check against §1.
- [ ] ⚑ **Owner:** listing copy pasted.
- [ ] ⚑ **Owner:** price set (**$19 pay-what-you-want suggested** (default); minimum owner's choice).
- [ ] ⚑ **Owner:** the publish click + preview/test purchase + public URL copied.
- [ ] Seat (post-click, no money moved): record the launch durably on `main` —
      verified listing URL, price, timestamp — in the style of
      [`docs/launch/stripe-webhook-test-kit/LAUNCH-LOG.md`](../../launch/stripe-webhook-test-kit/LAUNCH-LOG.md),
      fill [`readme-buy-snippet.md`](../../launch/template-packs/readme-buy-snippet.md)
      with the live URL, and refresh the $59 bundle listing
      ([`candidates/BUNDLE-LISTING.md`](../../../candidates/BUNDLE-LISTING.md)).

---

**Verdict: publish-ready up to the owner gate.** Built + priced + listing
drafted + checkout/format verified + sha recorded (all evidenced above); the
product parks at §7 (owner clicks) by design. Honest caveats: no test suite
exists (none applicable — zero-runtime product; verification was execution of
the shipped scripts + format lint), and a live purchase remains unverified
(⚑A) until the owner's own test purchase.
