# Title Vetting — Owner-Click Queue Kit

> **Status:** `plan`
>
> Eleventh PRODUCT packet in the vetting directory, so the publish click
> rides the derived owner queue (`../OWNER-QUEUE.md` via
> `scripts/derive_owner_queue.py`) — which is itself the production
> system this product generalizes: the packet's own §7 block is parsed
> by the pattern the kit sells. BUILD #2 (3.60) of the 2026-07-13
> ideation batch (`docs/products/ideas-2026-07-13.md` §2, PR #142),
> built under ORDER 008's products clause. No freeze applies — a
> dev-tool kit with no payment-path dependency (the ORDER 003 ⚑B/⚑D
> freeze, lifted 2026-07-11 by PR #22, never attached to it). Every
> step marked **⚑ OWNER-GATE** is an owner click, never automated.

**Title:** Owner-Click Queue Kit · **Category:** digital product / dev
tool + conventions · **Date vetted:** 2026-07-13

Product: [`candidates/owner-click-queue-kit/`](../../../candidates/owner-click-queue-kit/README.md)
(v0.1; buyer bundle `dist/owner-click-queue-kit-v0.1.zip`; launch assets
in [`docs/launch/owner-click-queue-kit/`](../../launch/owner-click-queue-kit/owner-actions.md);
intake [`INTAKE.md`](../../../candidates/owner-click-queue-kit/INTAKE.md),
scored 3.60 at ideation).

## 1. Built (verified this session, 2026-07-13)

- [x] Stdlib-only tool `ocq.py` (Python 3.9+, no deps, no network):
      `derive` — tolerant/advisory compiler (exits 0 on every path)
      from OWNER-GATE blocks to one deterministic owner queue
      (decisions with bolded defaults first, click-runs with
      HARD-GATED ordering, manual-review section, read-only
      Live/completed with ⏲ kill-clock checkpoints) — and `lint` —
      strict grammar validation (exit 1 with per-file errors: missing
      H1, defaultless decisions, half-flipped DONE rows,
      calendar-invalid dates, malformed KILL-CHECK tokens).
- [x] `GRAMMAR.md` — the complete gate grammar (decisions / ⚑ Owner
      click rows / DONE flip with both-marks fail-safe / KILL-CHECK)
      plus the six-field WHAT/WHERE/HOW/WHY/UNBLOCKS/VERIFIED-WHEN
      detail convention. `GOTCHAS.md` — 10 lessons from THIS repo's
      production use of the pattern, none hypothetical.
- [x] **Generalized, not copied:** the kit is a distillation of
      `scripts/derive_owner_queue.py` (the live in-repo system) with
      the repo couplings removed (keyword-map conflict scan, "Title
      Vetting —" H1 prefix, fixed vetting dir) and buyer-needed
      surface added (strict lint mode, real-calendar-date validation,
      output-file self-skip, EXPECTED-file hygiene, repeatable
      `--gates` targeting).
- [x] **Verified-by-production truth-claim (TEMPLATE.md stage-3 third
      evidence class):** the generalized pattern runs live in this
      repo — `scripts/derive_owner_queue.py` @ `main` generates
      `docs/publishing/OWNER-QUEUE.md` from 11 product packets + the
      keyword map (origin: PR #91's session-card 💡). Real production
      events: PR #147 (GWTK build, merged 2026-07-13, squash
      `44d2a5e`) queued its publish clicks through it, and PR #150
      (merged 2026-07-13, squash `6ecc460`) is the union re-derive
      after a same-day parallel-merge race — the exact gotcha shipped
      as `GOTCHAS.md` #2. This packet's own §7 is parsed by the same
      script (recursion as evidence).
- [x] **Tests (executed 2026-07-13):** 38-test suite
      (`test_ocq.py`, plain unittest — pytest collects it too:
      `38 passed` this session) covering parse (titles, heading
      variants, defaults + fallbacks, continuation folding,
      owner-row filtering), derive (byte-identical determinism,
      committed-EXPECTED equality for BOTH worked examples, no
      timestamps, input immutability, output self-skip, unreadable
      input → manual review), lint (all strict failures incl.
      half-flipped DONE rows and impossible dates), and hostile
      inputs (binary junk, pathological markdown, injection-shaped
      gate text rendered as data with zero side effects). Green from
      source (`Ran 38 tests in 0.028s / OK`, 10:17:14Z) AND from the
      extracted zip in a clean dir (`Ran 38 tests in 0.023s / OK`,
      10:18:50Z).
- [x] Suite wired into CI: `owner-click-queue-kit-tests` job added to
      `.github/workflows/kit-tests.yml`, same convention as the
      GWTK/SWTK jobs.
- [x] Buyer bundle built via explicit per-file allow-list `package.sh`
      (fixed mtimes, sorted entries, `zip -X`; excludes INTAKE.md,
      package.sh, dist/, `__pycache__`), **byte-reproducible** —
      unconditional double rebuild 2026-07-13T10:18:35Z, identical
      sha256, committed dist IS that build.
- [x] **sha256 `f81f1b4eb39194ef96551b24bb20ffbd6f15aac07543fba2f894c670734564e7`**
      (28,712 bytes, 12 content files) — also pinned in the
      click-script's ARTIFACT line.
- [x] Checkout/format verified from the artifact itself: clean-dir
      unzip — README + GRAMMAR + GOTCHAS + ocq.py + test suite at top
      level, examples/ (agent-fleet 3 gates + EXPECTED, solo-repo
      gate + EXPECTED, examples README) (12/12 vs the listing's
      "What's inside"); the shipped example derived from the extracted
      copy **byte-identical** to its committed EXPECTED output and
      `lint` OK (buyer-side self-proof, the kit's own quickstart step
      4); real-secret-shape scan **0 hits**; no junk entries in the
      archive.

## 2. Collision scan

- [x] No in-catalog title collision. Closest shipped products,
      boundaries disclosed: **Agent Fleet Field Manual $39** — its
      ch.4 teaches the owner-gate pattern in PROSE; this kit is the
      runnable tool + grammar + tests (the disclosed cross-sell
      precedent: kill-rule-kit vs field-manual ch.8, named at
      ideation). **Kill-Rule Intake Kit $15** — kill-rule scoring at
      intake time; this kit's KILL-CHECK line is the post-launch clock
      the intake's checkpoints arm into. **Template-packs $19 PWYW** —
      single-repo session discipline; no owner-queue surface. The
      ideation batch's own Multi-Agent Control-Plane Pack (BUILD #3)
      borders this kit at the inbox/heartbeat layer — the boundary is
      stated there: OCQK is the owner-action queue; the control-plane
      pack is agent-to-agent coordination. If #3 is built, its listing
      must disclose the boundary both ways.
- [x] Same buyer audience as the dev-tool catalog (intake's
      concentrated-channel risk, disclosed): distribution scored 3/5
      at ideation.

## 3. Market / price

- [x] Price **$19 one-time** — set at ideation
      (`docs/products/ideas-2026-07-13.md` §2) and recorded identically
      in `INTAKE.md`, the listing copy, the click-script, and here.
      Precedent: the Merge-Wall Cookbook sells at exactly $19 for the
      same shape (conventions + runnable artifacts distilled from this
      repo's production infrastructure); the ideation WTP note caps it
      below the $29 harness rung (DIY-able by a strong buyer — the
      moat is the production evidence, not the code). Chain: $15
      (kill-rule kit, false-green) < **$19 this kit** = merge-wall $19
      = template-packs $19 PWYW < SWTK/GWTK $29 < field-manual $39 <
      membership-kit $49. Conservative expectation: 0–5 sales / $0–$95
      first-90-day, $0 absent distribution (the intake's own line;
      validation signal ≥1 sale OR ≥50 article reads in 30 days, else
      ledgered negative; T+7 funnel checkpoint / T+30 kill deadline
      armed as a KILL-CHECK here once the click is DONE-flipped).

## 4–5. Packaging

- [x] Buyer bundle is the explicit per-file allow-listed `package.sh`
      output (README + GRAMMAR + GOTCHAS + `ocq.py` + `test_ocq.py` +
      `examples/` with both EXPECTED outputs; deliberately excludes
      the lane-internal INTAKE.md, package.sh, dist/, `__pycache__`).
      No cover image ships — owner adds one or uses the storefront
      default.

## 6. Listing copy (drafted in-repo — nothing published)

- [x] [`listing-copy.md`](../../launch/owner-click-queue-kit/listing-copy.md)
      at catalog parity (Title / Short ≤200 chars (189 measured) /
      Long / Bullets / FAQ) and checked claim-by-claim against the
      extracted bundle: "38 tests" = the suite that ran green twice
      this session; "two worked examples with committed expected
      outputs" = the files in the zip, diff-verified byte-identical;
      "deterministic/byte-identical re-runs" = pinned by the suite;
      the "what it does NOT do" section states the honest boundaries
      (executes nothing, integrates nothing out of the box, sandboxes
      nothing — conventions + compiler + lint, and says the production
      evidence is the seller's own repo); refund/license lines
      present, marked owner-to-set.

## 7. ⚑ OWNER-GATE — publish clicks (queued, never automated)

Seat output = this queued OWNER-ACTION block; the seat performed
**none** of it. It is the queue-parseable form of the click-script in
[`owner-actions.md`](../../launch/owner-click-queue-kit/owner-actions.md) —
the HOW detail lives there; no freeze applies (no payment-path gate).

**OWNER-ACTION — Publish "Owner-Click Queue Kit" at $19 one-time**
1. **Storefront account:** owner signs into the storefront (the SWTK
   Gumroad account already exists and has payout configured).
2. **⚑ Storefront pick:** **Gumroad** (default — same account as the
   live SWTK listing; the click-script's HOW is written against it) or
   Lemon Squeezy — owner's call; either works with the same zip + copy.
3. **Product:** New product → Digital product; Name = "Owner-Click
   Queue Kit"; upload
   `candidates/owner-click-queue-kit/dist/owner-click-queue-kit-v0.1.zip`
   and verify the upload matches sha256 `f81f1b4e…734564e7` (full hash
   in §1 and the click-script ARTIFACT line — never upload a stale
   local copy).
4. **Copy:** paste Title / Short + Long description / Bullets / FAQ
   from
   [`listing-copy.md`](../../launch/owner-click-queue-kit/listing-copy.md);
   set the refund/license lines the copy marks owner-to-set.
5. **Price:** set **$19 one-time** (fixed — set at ideation; merge-wall
   cookbook precedent at the identical price for the identical
   conventions-distillation shape).
6. **Publish + record:** publish, copy the public product URL,
   storefront preview/test purchase to confirm the zip delivers.
   Optional same-visit cross-sell: one line each on the field-manual
   and kill-rule-kit listings pointing here (first-ten path channel 2).

- [ ] ⚑ **Owner:** storefront pick (**Gumroad** (default)) — or Lemon Squeezy.
- [ ] ⚑ **Owner:** zip uploaded + sha256 spot-check against §1.
- [ ] ⚑ **Owner:** listing copy pasted + refund/license lines set.
- [ ] ⚑ **Owner:** price set (**$19 one-time** (default per ideation + the merge-wall precedent)).
- [ ] ⚑ **Owner:** the publish click + preview/test purchase + public URL copied.
- [ ] Seat (post-click, no money moved): record the launch durably on
      `main` — verified listing URL, price, timestamp — in the style of
      [`docs/launch/stripe-webhook-test-kit/LAUNCH-LOG.md`](../../launch/stripe-webhook-test-kit/LAUNCH-LOG.md),
      flip these rows to the `— DONE <date>` disposition, arm the
      intake's kill clock as a `KILL-CHECK:` line here (T+7 funnel
      checkpoint · T+30 kill-rule deadline: ≥1 sale OR ≥50 article
      reads, else ledger NEGATIVE + pause/delist), and regenerate the
      owner queue.

---

**Verdict: publish-ready up to the owner gate.** Built + priced +
listing drafted + checkout/format verified + sha recorded (all
evidenced above); the product parks at §7 (owner clicks) by design.
Honest caveats: it's conventions-plus-one-script — a strong buyer can
DIY the deriver in an afternoon, and the listing says the moat is the
production-worn grammar + gotchas, not the code; the buyer population
(operators of agents autonomous enough to need a spend firewall) is
real but small today; the production evidence is this repo's own use —
no external fleet has run the generalized kit; the six-field detail
layer is convention, not parsed structure, and the kit says so; same
concentrated dev-tool channel where SWTK has 0 organic sales as of
2026-07-13 — expect ~$0 absent distribution; and a live purchase
remains unverified until the owner's own test purchase.
