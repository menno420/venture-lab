# Title Vetting — Agent Fleet Field Manual

> **Status:** `plan`
>
> Third PRODUCT (non-book-catalog) packet in the vetting directory, so the
> field-manual publish click rides the same derived owner queue as the book
> catalog (`../OWNER-QUEUE.md` via `scripts/derive_owner_queue.py`). Queued
> under ORDER 008 (2026-07-13 night run). The click itself was flipped
> QUEUED 2026-07-11 in
> [`publish-owner-action.md`](../../launch/agent-fleet-field-manual/publish-owner-action.md)
> after non-author review (card
> `.sessions/2026-07-11-queue-f-field-manual-publish.md`); this packet is its
> queue-parseable form. The lane's D1/Stripe real-path gate does NOT apply —
> Gumroad hosts checkout and delivery; this product ships no payment code.
> Every step marked **⚑ OWNER-GATE** is an owner click, never automated.

**Title:** Agent Fleet Field Manual · **Category:** digital product / eBook (field manual) ·
**Date vetted:** 2026-07-13

Product: [`candidates/agent-fleet-field-manual/`](../../../candidates/agent-fleet-field-manual/README.md)
(v0.1; buyer bundle `dist/agent-fleet-field-manual-v0.1.zip`; launch assets in
[`docs/launch/agent-fleet-field-manual/`](../../launch/agent-fleet-field-manual/publish-owner-action.md)).

## 1. Built (verified this session, 2026-07-13)

- [x] Full manuscript in-repo: 11 chapters (`chapters/00-preface.md` …
      `10-appendix-templates.md`), 3 runnable templates, single self-contained
      HTML book built by stdlib-only `build.py`. The 2 free chapters (01, 02)
      are separately published as launch assets.
- [x] Dist zip rebuilt via `package.sh`, **byte-reproducible** (unconditional
      double rebuild, identical sha256 both times). This slice REFRESHED the
      bundle: the prior zip (`7eff9235…a29176`) excluded `build.py`/`package.sh`
      while its own README instructed buyers to run them — the refreshed bundle
      ships both, making the "rebuild it yourself" instructions and the
      listing's "rebuild with stdlib Python" bullet true from the artifact.
- [x] **sha256 `63e71b30d1a194b42f92d8c9197148ec89244cba82688e6c097d5727e6ccee23`**
      (65,283 bytes; 19 files) — also pinned in the click-script's ARTIFACT line.
- [x] **Self-reproducing bundle proven buyer-side:** extract the zip, run
      `python3 build.py && sh package.sh` from the extracted copy → regenerates
      the byte-identical zip (same sha256, executed 2026-07-13 ~01:28Z).
- [x] Honest null: zero-runtime product (prose + stdlib build tooling) — **no
      test suite exists or is warranted**; the listing says what the buyer
      gets. Executed verification substitute, from the extracted bundle:
      19/19 files non-empty valid UTF-8; HTML has 0 external src/href refs and
      0 `<script>` tags (fully self-contained); all 12 in-page anchors resolve;
      FREE badges present on chapters 01/02; secret-pattern scan zero hits; no
      `.DS_Store`/`__pycache__`/junk entries in the archive listing.

## 2. Collision scan

- [x] Title is descriptive ("Agent Fleet Field Manual") — no trademark-style
      collision identified; storefront namespace is per-account, so no
      KDP-style title-availability gate applies.

## 3. Market / price

- [x] Price **$39 one-time** — recorded in
      [`publish-owner-action.md`](../../launch/agent-fleet-field-manual/publish-owner-action.md)
      (WHAT/HOW fields), the candidate README ("**$39 one-time.**"), and
      [`docs/launch/agent-fleet-field-manual/LISTING.md`](../../launch/agent-fleet-field-manual/LISTING.md)
      ("Launch price: **$39** (one-time)"). Conservative expectation stays
      0–4 sales / 90 days ($0–$156); $0 without distribution (Q-0259.4 framing;
      eval-001 candidate #4, score 3.55).

## 4–5. Packaging

- [x] Buyer bundle is the allow-listed `package.sh` output: README, LISTING,
      11 chapters, 3 templates, the built HTML, and the stdlib build tooling;
      deliberately excludes the internal INTAKE.md and any nested zip. No
      cover image ships — owner adds one or uses the storefront default.

## 6. Listing copy (drafted in-repo — nothing published)

- [x] [`docs/launch/agent-fleet-field-manual/LISTING.md`](../../launch/agent-fleet-field-manual/LISTING.md)
      verified claim-by-claim against the extracted bundle 2026-07-13:
      "eleven chapters" = 11 chapter files; "three copy-paste templates" = 3
      template files; "single self-contained HTML (no CDN, no fonts, no
      tracking)" = 0 external refs / 0 scripts, confirmed by scan; "two
      chapters are free" = FREE badges on 01/02 + standalone free-chapter
      exports in the launch dir; "rebuild with stdlib Python, zero
      dependencies" = TRUE as of this slice's bundle fix (was unfulfillable
      from the old artifact — the tooling was excluded). Honest-scope caveats
      (soft willingness-to-pay, one lane's lessons, some claims
      owner-statement-only) retained in the copy and the in-zip README.

## 7. ⚑ OWNER-GATE — publish clicks (queued, never automated)

Seat output = this queued OWNER-ACTION block; the seat performed **none** of
it. It is the queue-parseable form of the QUEUED (2026-07-11) click-script in
[`publish-owner-action.md`](../../launch/agent-fleet-field-manual/publish-owner-action.md)
— the six-field HOW detail lives there. No freeze applies (no payment code in
this product; the D1 gate covers products shipping their own payment path).

**OWNER-ACTION — Publish "Agent Fleet Field Manual" at $39 one-time**
1. **Storefront account:** owner signs into (or creates) the storefront;
   complete its payout setup first or revenue holds.
2. **⚑ Storefront pick:** **Gumroad** (default — the click-script's HOW is
   written against it) or Lemon Squeezy — owner's call; either works with the
   same zip + copy.
3. **Product:** New product → Digital product; Name = "Agent Fleet Field
   Manual"; upload
   `candidates/agent-fleet-field-manual/dist/agent-fleet-field-manual-v0.1.zip`
   and verify the upload matches sha256 `63e71b30…ee23` (full hash in §1 and
   the click-script ARTIFACT line — never upload a stale local copy).
4. **Copy:** paste Title / Tagline / Description / Bullets / Who-it's-for /
   FAQ from
   [`docs/launch/agent-fleet-field-manual/LISTING.md`](../../launch/agent-fleet-field-manual/LISTING.md).
5. **Price:** **$39**, one-time.
6. **Publish + record:** publish, copy the public product URL, storefront
   preview/test purchase to confirm the zip delivers; posting the ≥2 free
   chapters starts the 14-day validation clock (per the click-script's
   UNBLOCKS/VERIFIED-WHEN).

- [ ] ⚑ **Owner:** storefront account + payout setup.
- [ ] ⚑ **Owner:** storefront pick (**Gumroad** (default)) — or Lemon Squeezy.
- [ ] ⚑ **Owner:** zip uploaded + sha256 spot-check against §1.
- [ ] ⚑ **Owner:** listing copy pasted.
- [ ] ⚑ **Owner:** price set (**$39 one-time** (default)).
- [ ] ⚑ **Owner:** the publish click + preview/test purchase + public URL copied.
- [ ] Seat (post-click, no money moved): record the launch durably on `main` —
      verified listing URL, price, timestamp — in the style of
      [`docs/launch/stripe-webhook-test-kit/LAUNCH-LOG.md`](../../launch/stripe-webhook-test-kit/LAUNCH-LOG.md),
      and refresh the $59 bundle listing
      ([`candidates/BUNDLE-LISTING.md`](../../../candidates/BUNDLE-LISTING.md))
      if the bundle scope includes the manual.

---

**Verdict: publish-ready up to the owner gate.** Built + priced + listing
drafted + checkout/format verified + sha recorded (all evidenced above); the
product parks at §7 (owner clicks) by design. Honest caveats: zero-runtime
product — verification was artifact-side execution (self-rebuild + format/
anchor/secret scans), not a test suite (none applicable); a live purchase
remains unverified until the owner's own test purchase; guide/eBook content
sits in the softest willingness-to-pay category on the board.
