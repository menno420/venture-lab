# Title Vetting — Kill-Rule Intake Kit

> **Status:** `plan`
>
> Seventh PRODUCT packet in the vetting directory, so the publish click
> rides the derived owner queue (`../OWNER-QUEUE.md` via
> `scripts/derive_owner_queue.py`). Queued under ORDER 008 (2026-07-13
> night run, PRODUCT #7 candidate sweep). No freeze applies — zero-runtime
> Markdown kit, no payment-path dependency (the ORDER 003 ⚑B/⚑D freeze,
> lifted 2026-07-11 by PR #22, never attached to it). Every step marked
> **⚑ OWNER-GATE** is an owner click, never automated.

**Title:** Kill-Rule Intake Kit · **Category:** digital product / decision-template kit ·
**Date vetted:** 2026-07-13

Product: [`candidates/kill-rule-intake-kit/`](../../../candidates/kill-rule-intake-kit/README.md)
(v0.1; buyer bundle `dist/kill-rule-intake-kit-v0.1.zip`; launch assets in
[`docs/launch/kill-rule-intake-kit/`](../../launch/kill-rule-intake-kit/owner-actions.md);
intake [`INTAKE.md`](../../../candidates/kill-rule-intake-kit/INTAKE.md), scored 3.38).

## 1. Built (verified this session, 2026-07-13)

- [x] Buyer bundle built via new allow-list `package.sh` (template-packs
      pattern: fixed mtimes, sorted entries, `zip -X`), **byte-reproducible**
      — double rebuild, identical sha256, committed dist IS that build.
- [x] **sha256 `53a840fd6b4f0860accecff8d2bbc16abeab06e1d2bb38e03251ca8993a770e5`**
      (15,875 bytes, 9 content files) — also pinned in the click-script's
      ARTIFACT line.
- [x] Honest null: the kit ships **no test suite** (plain Markdown, zero
      runtime, by design — the listing's honesty FAQ says so). Executed
      verification instead, from the extracted bundle in a clean dir: all 9
      files non-empty valid UTF-8, H1-headed, balanced code fences; the two
      worked examples' weighted-total arithmetic recomputed in Python and
      matches the shipped totals (3.55 and 3.10); rubric weights sum to
      1.00; 61 `[[fill]]` slots present in the fillable surfaces.
- [x] Checkout/format verified from the artifact itself: bundle unzipped to
      a clean dir — README + QUICKSTART + INCLUDED at top level; `pack/`
      carries the intake template, scoring rubric, kill rules,
      negative-ledger template, and 2 worked examples (matches INCLUDED.md
      manifest 9/9). Secret-pattern scan: zero hits; no `.DS_Store`, no
      `__pycache__`, no junk entries in the archive listing.

## 2. Collision scan

- [x] Product name is descriptive-generic ("kill-rule intake kit") — no
      trademark-style collision found in-catalog or in the obvious template
      category names; storefront namespace is per-account, so no KDP-style
      title-availability gate applies. In-catalog overlap disclosed: Field
      Manual chapter 8 TEACHES this discipline (prose); this kit is the
      fillable working version — cross-sell, not cannibalization, and the
      listing copy does not claim otherwise.

## 3. Market / price

- [x] Price **$15 one-time** — set at intake
      ([`INTAKE.md`](../../../candidates/kill-rule-intake-kit/INTAKE.md))
      and recorded identically in the listing copy, the click-script, and
      here. Precedent chain (bottom rung, below the closest comparable):
      template-packs $19 PWYW (PR #108) < SWTK $29 live (PR #86) <
      field-manual $39 (PR #110) < membership-kit $49 (PR #106).
      Conservative expectation stays 0–3 sales / $0–$45 first-90-day, $0
      absent distribution (Q-0259.4 framing; the intake's own WTP axis is
      2/5 and validation signal is ≥1 sale OR ≥50 reads in 30 days).

## 4–5. Packaging

- [x] Buyer bundle is the allow-listed `package.sh` output (README +
      QUICKSTART + INCLUDED + `pack/`; deliberately excludes LISTING.md,
      the lane-internal INTAKE.md, dist/, package.sh, .git). No cover image
      ships — owner adds one or uses the storefront default.

## 6. Listing copy (drafted in-repo — nothing published)

- [x] [`listing-copy.md`](../../launch/kill-rule-intake-kit/listing-copy.md)
      at membership-kit/template-packs parity (Title / short ≤200 chars
      (196) / long / bullets / FAQ) and checked claim-by-claim against the
      extracted bundle: "nine Markdown files" = 9 (counted); "61 [[fill]]
      slots" claim kept OUT of copy (volatile) — copy says "[[fill]] slots
      throughout" instead; "3.55 / 3.10 worked examples" = shipped values
      (recomputed); honesty FAQ states the zero-runtime null in buyer terms
      ("what was NOT machine-verified") and the "conventions, not
      enforcement" scope.

## 7. ⚑ OWNER-GATE — publish clicks (queued, never automated)

Seat output = this queued OWNER-ACTION block; the seat performed **none** of
it. It is the queue-parseable form of the click-script in
[`owner-actions.md`](../../launch/kill-rule-intake-kit/owner-actions.md) —
the HOW detail lives there; no freeze applies (zero-runtime product, no
payment-path gate).

**OWNER-ACTION — Publish "Kill-Rule Intake Kit" at $15 one-time**
1. **Storefront account:** owner signs into (or creates) the storefront;
   complete its payout setup first or revenue holds.
2. **⚑ Storefront pick:** **Gumroad** (default — the click-script's HOW is
   written against it; same account as SWTK live listing) or Lemon Squeezy —
   owner's call; either works with the same zip + copy.
3. **Product:** New product → Digital product; Name = "Kill-Rule Intake
   Kit"; upload `candidates/kill-rule-intake-kit/dist/kill-rule-intake-kit-v0.1.zip`
   and verify the upload matches sha256 `53a840fd…a770e5` (full hash in §1
   and the click-script ARTIFACT line — never upload a stale local copy).
4. **Copy:** paste Title / Short + Long description / Bullets / FAQ from
   [`listing-copy.md`](../../launch/kill-rule-intake-kit/listing-copy.md).
5. **Price:** set **$15 one-time** (fixed, not PWYW — the kit is the
   catalog's bottom rung and undercuts the $19 PWYW pack deliberately).
6. **Publish + record:** publish, copy the public product URL, storefront
   preview/test purchase to confirm the zip delivers.

- [ ] ⚑ **Owner:** storefront account + payout setup.
- [ ] ⚑ **Owner:** storefront pick (**Gumroad** (default)) — or Lemon Squeezy.
- [ ] ⚑ **Owner:** zip uploaded + sha256 spot-check against §1.
- [ ] ⚑ **Owner:** listing copy pasted.
- [ ] ⚑ **Owner:** price set (**$15 one-time** (default per intake + precedent chain)).
- [ ] ⚑ **Owner:** the publish click + preview/test purchase + public URL copied.
- [ ] Seat (post-click, no money moved): record the launch durably on `main` —
      verified listing URL, price, timestamp — in the style of
      [`docs/launch/stripe-webhook-test-kit/LAUNCH-LOG.md`](../../launch/stripe-webhook-test-kit/LAUNCH-LOG.md),
      and add the kit to the Field Manual cross-sell surfaces (its chapter 8
      is the natural referrer).

---

**Verdict: publish-ready up to the owner gate.** Built + priced + listing
drafted + checkout/format verified + sha recorded (all evidenced above); the
product parks at §7 (owner clicks) by design. Honest caveats: no test suite
exists (none applicable — zero-runtime product; verification was executed
format/arithmetic/secret checks from the extracted bundle), the category is
crowded and free-heavy (intake WTP 2/5 — expect ~$0 absent distribution),
and a live purchase remains unverified until the owner's own test purchase.
