# Title Vetting — Membership-Site Boilerplate Kit

> **Status:** `plan`
>
> First PRODUCT (non-book) packet in the vetting directory, so the ⚑B
> publish click rides the same derived owner queue as the book catalog
> (`../OWNER-QUEUE.md` via `scripts/derive_owner_queue.py`). Queued under
> ORDER 008 (2026-07-13 night run) after the ⚑B/⚑D freeze was verified
> lifted: PR #22 (merged 2026-07-11T01:58Z) flipped
> [`owner-actions.md`](../../launch/membership-kit/owner-actions.md) to
> UNFROZEN on the ORDER 003 gate (PR #16 squash `912da3e` + kit-tests CI
> run 29135371209 green). Every step marked **⚑ OWNER-GATE** is an owner
> click, never automated.

**Title:** Membership-Site Boilerplate Kit · **Category:** digital product / code kit ·
**Date vetted:** 2026-07-13

Product: [`candidates/membership-kit/`](../../../candidates/membership-kit/README.md)
(v0.2; buyer bundle `dist/membership-kit-v0.2.zip`; launch assets in
[`docs/launch/membership-kit/`](../../launch/membership-kit/owner-actions.md)).

## 1. Built (verified this session, 2026-07-13)

- [x] Dist zip rebuilt via `package.sh`, **byte-reproducible** (double rebuild,
      identical sha256), and refreshed on the branch — the previously committed
      zip predated the fail-closed webhook-misconfiguration fix + its test.
- [x] **sha256 `9f262fc84008ad7b1517116ef999c331672d756f6d68fe5378682e38e1d5d3e1`**
      (40,547 bytes) — also pinned in the click-script's ARTIFACT line.
- [x] Test suites green at source: `test_http_realpath` 9 OK ·
      `test_membership` 15 OK · `test_supabase_store` 12 OK.
- [x] Checkout/format verified from the artifact itself: bundle unzipped to a
      clean dir; README + QUICKSTART (loud MOCK-mode warning up top), server +
      vendored Stripe fixtures + `PROVENANCE.md`, web files, `.env.example`
      placeholders only; no `members.json`, no `__pycache__`, no secret
      values; packaged suites re-run from the extracted copy:
      `Ran 36 tests … OK`.

## 2. Collision scan

- [x] Product name is descriptive-generic ("membership site boilerplate") —
      no trademark-style collision risk identified; storefront namespace is
      per-account, so no KDP-style title-availability gate applies.

## 3. Market / price

- [x] Price **$49 one-time** — precedent recorded in
      [`owner-actions.md`](../../launch/membership-kit/owner-actions.md) ⚑B,
      [`candidates/membership-kit/LISTING.md`](../../../candidates/membership-kit/LISTING.md)
      ("**$49** (one-time, lifetime updates to the v0.x line)"), and the kit's
      own landing page CTA. Conservative expectation stays 0–2 sales/month
      absent distribution (Q-0259.4 framing).

## 4–5. Packaging

- [x] Buyer bundle is the allow-listed `package.sh` output (no repo/build
      tooling, no runtime data). No cover image ships — owner adds one or uses
      the storefront default.

## 6. Listing copy (drafted in-repo — nothing published)

- [x] [`listing-copy.md`](../../launch/membership-kit/listing-copy.md)
      refreshed 2026-07-13 to v0.2 reality at SWTK-listing parity: HTTP-layer
      real-path verification claims, fail-closed misconfig behavior, 36
      bundled tests, honest no-live-purchase (⚑A) caveat retained.

## 7. ⚑ OWNER-GATE — publish clicks (queued, never automated)

Seat output = this queued OWNER-ACTION block; the seat performed **none** of
it. It is the queue-parseable form of the ⚑B click-script in
[`owner-actions.md`](../../launch/membership-kit/owner-actions.md) — the HOW
detail lives there; freeze state UNFROZEN (2026-07-11, PR #22).

**OWNER-ACTION — Publish "Membership-Site Boilerplate Kit" at $49**
1. **Storefront account:** owner signs into (or creates) the storefront;
   complete its payout setup first or revenue holds.
2. **⚑ Storefront pick:** **Gumroad** (default — simplest digital-product
   flow; the click-script's HOW is written against it) or Lemon Squeezy —
   owner's call; either works with the same zip + copy.
3. **Product:** New product → Digital product; Name = "Membership-Site
   Boilerplate Kit"; upload `candidates/membership-kit/dist/membership-kit-v0.2.zip`
   and verify the upload matches sha256 `9f262fc8…5d3e1` (full hash in §1 and
   the click-script ARTIFACT line — never upload a stale local copy).
4. **Copy:** paste Title / Short + Long description / Bullets / FAQ from
   [`listing-copy.md`](../../launch/membership-kit/listing-copy.md); set the
   refund-policy placeholder while pasting the FAQ.
5. **Price:** **$49** one-time.
6. **Publish + record:** publish, copy the public product URL, storefront
   preview/test purchase to confirm the zip delivers.

- [ ] ⚑ **Owner:** storefront account + payout setup.
- [ ] ⚑ **Owner:** storefront pick (**Gumroad** (default)) — or Lemon Squeezy.
- [ ] ⚑ **Owner:** zip uploaded + sha256 spot-check against §1.
- [ ] ⚑ **Owner:** listing copy pasted; refund policy set.
- [ ] ⚑ **Owner:** price set (**$49** (default, one-time)).
- [ ] ⚑ **Owner:** the publish click + preview/test purchase + public URL copied.
- [ ] Seat (post-click, no money moved): record the launch durably on `main` —
      verified listing URL, price, timestamp — in the style of
      [`docs/launch/stripe-webhook-test-kit/LAUNCH-LOG.md`](../../launch/stripe-webhook-test-kit/LAUNCH-LOG.md),
      and fill [`readme-buy-snippet.md`](../../launch/membership-kit/readme-buy-snippet.md)
      with the live URL.

---

**Verdict: publish-ready up to the owner gate.** Built + priced + listing
drafted + checkout/format verified + sha recorded (all evidenced above); the
product parks at §7 (owner clicks) by design. Honest caveat carried from the
click-script: a live purchase remains unverified (⚑A) until the owner's own
test purchase.
