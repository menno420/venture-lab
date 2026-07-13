# Title Vetting — AI Novella Production Kit

> **Status:** `plan`
>
> Thirteenth PRODUCT packet in the vetting directory; the publish click
> rides the derived owner queue (`../OWNER-QUEUE.md` via
> `scripts/derive_owner_queue.py`). Sole BUILD (#1, 3.525, tight
> budget) of the 2026-07-13 NIGHT ideation batch
> (`docs/products/ideas-2026-07-13-night.md` §1), built under ORDER 011
> item 1 with the batch's Kill Rule 0 gate honored: full INTAKE.md
> written and answered PROCEED before any pack content. PARK #2
> (Fiction Vetting-Packet Kit) folded in as guide chapter 4 per its
> ideation verdict. HARD content rule honored throughout: the 16
> fiction manuscripts are themselves separate paid products — this kit
> ships METHOD, templates, and worked-example structure, never
> manuscript text (illustrative quotes of a sentence or two max, with
> file@sha provenance). No freeze applies — a zero-runtime document
> kit with no payment-path dependency (the ORDER 003 ⚑B/⚑D freeze,
> lifted 2026-07-11 by PR #22, never attached to it). Every step
> marked **⚑ OWNER-GATE** is an owner click, never automated.

**Title:** AI Novella Production Kit · **Category:** digital product /
method + templates guide · **Date vetted:** 2026-07-13

Product: [`candidates/ai-novella-production-kit/`](../../../candidates/ai-novella-production-kit/README.md)
(v0.1; buyer bundle `dist/ai-novella-production-kit-v0.1.zip`; launch
assets in
[`docs/launch/ai-novella-production-kit/`](../../launch/ai-novella-production-kit/owner-actions.md);
intake [`INTAKE.md`](../../../candidates/ai-novella-production-kit/INTAKE.md),
scored 3.525 at ideation, Kill Rule 0 gate PROCEED).

## 1. Built (verified this session, 2026-07-13)

- [x] **Intake FIRST (Kill Rule 0):** `INTAKE.md` written and
      committed (`759f727`) before any pack content — kill-rule fields
      bound (signal ≥1 sale OR ≥50 article reads in 30 days of
      listing; T+7 2026-07-20 / T+30 2026-08-12 clocks, arming at the
      publish click; budget ≤60k tokens HARD), gate answered PROCEED
      with the band-edge caveat recorded honestly (3.525 at the
      borderline band's upper edge; WTP 2.5 the weak axis).
- [x] Zero-runtime content kit, 16 content files: README + QUICKSTART
      + INCLUDED + 7 guide chapters + 5 blank-slate templates (+
      templates/README copy map). Everything distilled from COMMITTED
      files only — no invented material:
      `candidates/adult-novels/the-twelfth-cake/DECISIONS.md@3b159d9`
      (promise manifest, aimed pass, single-source-of-length,
      dead-session production record),
      `candidates/middle-grade/the-halfway-ferry/CANON.md@abf1f23`
      (series-bible anatomy),
      `candidates/adult-novels/ultramarine/versions/*@873d5d9`
      (edition-variant conventions, serial/large-print specs),
      `candidates/adult-novels/the-slow-word/en/README.md@873d5d9`
      (chapter-file structure),
      `docs/publishing/{CHECKLIST,PUBLISHING-PLAN,keyword-map}.md`
      (gate grammar, price bands, keyword tiling),
      `candidates/kill-rule-intake-kit/pack/*@f974455` (kill rules).
      Fleet-specific noise stripped: no session ids, no trigger ids,
      no exact model IDs. **Manuscript-text rule verified:** quotes
      from fiction-lane artifacts are ≤2 sentences, series-bible or
      decisions-record lines only (never manuscript prose), each
      covered by a file@sha Sources footer.
- [x] **Honest null (TEMPLATE.md stage-3, zero-runtime clause):** no
      test suite exists or is warranted — nothing in the bundle
      executes. Substitute executed instead (2026-07-13T23:00Z, from
      the extracted artifact in a clean scratch dir), output pasted
      verbatim: `content files: 16` / `flags: 0` — i.e. inventory
      enumerated 16/16 vs INCLUDED.md and the listing's "What's
      inside"; every file UTF-8-decoded; markdown pass OK (H1-first,
      balanced fences, no fill-slot/TODO tokens);
      secret/session-id/trigger-id scan **0 hits** (patterns:
      `trig_*`, `session_01*`, key shapes, dated model IDs); archive
      listing free of `.DS_Store` / `__pycache__` / junk. No CI job
      added — nothing to run (the merge-wall-cookbook / MACP
      precedent).
- [x] Buyer bundle built via explicit per-file allow-list `package.sh`
      (fixed mtimes, sorted entries, `zip -X`; excludes INTAKE.md,
      package.sh, dist/), **byte-reproducible** — unconditional double
      rebuild 2026-07-13T23:00:02Z, both sha256 lines verbatim:
      `f85f709bc7477e626ec2fe2c70c048266298b139041cc1831c54bc5df070bf78  dist/ai-novella-production-kit-v0.1.zip`
      `f85f709bc7477e626ec2fe2c70c048266298b139041cc1831c54bc5df070bf78  dist/ai-novella-production-kit-v0.1.zip`
      — identical; the committed dist IS that build.
- [x] **sha256 `f85f709bc7477e626ec2fe2c70c048266298b139041cc1831c54bc5df070bf78`**
      (28,525 bytes, 16 content files) — also pinned in the
      click-script's ARTIFACT line.
- [x] **Budget honesty (the ≤60k-token cap, cuts recorded — never
      silent):** build actuals not precisely metered this slice (no
      per-session token meter is exposed to the seat; recorded as
      unmeasured in INTAKE.md rather than invented — cap enforced by
      scope discipline). Three things the cap cut: (1) no fully worked
      sample book (a filled-in PLAN/CANON/packet for a demonstration
      title) — the templates carry inline guidance instead and the
      chapters cite the real committed artifacts; (2) no
      translation-workflow chapter — the catalog's trilingual/NL
      practice appears only as an edition-matrix row and citations;
      (3) no genre-specific band/price tables beyond the catalog's own
      novella numbers — chapter 6 ships the procedure, not a data
      product. All three are bounded by the listing's "What it does
      NOT do" / FAQ honesty sections.

## 2. Collision scan

- [x] No in-catalog title collision. Closest shipped/queued products,
      boundaries disclosed: **Agent-Workflow Template Pack $19 PWYW**
      and **Multi-Agent Control-Plane Pack $29** — agent-ops session
      and fleet discipline for developers; this kit serves writers and
      contains zero control-plane material (the listing FAQ states the
      boundary). **Agent Fleet Field Manual $39** — fleet operations
      in prose; the recovery chapter (5) translates ONE fleet-side
      convention for writers and says so in-chapter (the disclosed
      cross-sell precedent). **Kill-Rule Intake Kit $15** — the
      generic intake/kill system; chapter 7 applies it to fiction and
      cites the kit's committed rules rather than re-shipping them.
      **The book catalog itself** — the nearest neighbor of all: the
      16 manuscripts are separate paid products; this kit ships no
      manuscript text (≤2-sentence cited structural quotes only), so
      the kit CROSS-SELLS the books rather than cannibalizing them,
      and the README says "it is not the books" out loud.
- [x] PARK #2 (Fiction Vetting-Packet Kit, 3.275) folded in as
      chapter 4 + `templates/vetting-packet.md` per its ideation
      verdict ("correct home: a chapter + template inside the AI
      Novella Production Kit, not a standalone SKU") — the PARK is
      discharged, not orphaned; no standalone fiction-vetting SKU may
      now ship without superseding this packet.
- [x] First writing-audience SKU in the catalog — a NEW channel with
      zero lane evidence, disclosed here, at ideation, and in the
      intake, not smoothed over.

## 3. Market / price

- [x] Price **$29 one-time** — set at ideation
      (`docs/products/ideas-2026-07-13-night.md` §1) and recorded
      identically in `INTAKE.md`, the listing copy, the click-script,
      and here. Precedent: SWTK live at exactly $29; GWTK and MACP
      queued at $29. The $29 rung (vs the $19 conventions rung) is
      argued in the click-script's precedent chain: a complete
      multi-surface production system (method + bible + bands/editions
      + gate + recovery + pricing + kill rules, 5 installable
      templates, the folded $19-scored vetting chapter), capped below
      the $39 manual. Conservative expectation: **0–3 sales / $0–$87
      first 90 days**, $0 absent distribution (the intake's own line;
      validation signal ≥1 sale OR ≥50 article reads in 30 days, else
      ledgered negative; clocks below arm at the publish click).
- [x] Buyers demonstrably pay for AI-writing prompt packs and courses
      (the ideation entry's WTP evidence) — but WTP scored 2.5, the
      batch's honest weak axis: free substitutes are endless; the moat
      is the cited receipts (16 finished manuscripts, PR-cited word
      counts), which only repo-literate buyers can audit.

## 4–5. Packaging

- [x] Buyer bundle is the explicit per-file allow-listed `package.sh`
      output (README + QUICKSTART + INCLUDED + guide/ + templates/;
      deliberately excludes the lane-internal INTAKE.md, package.sh,
      dist/). No cover image ships — owner adds one or uses the
      storefront default. Storefront category note in the
      click-script: Gumroad WRITING category, not software.

## 6. Listing copy (drafted in-repo — nothing published)

- [x] [`listing-copy.md`](../../launch/ai-novella-production-kit/listing-copy.md)
      at catalog parity (Title / Short ≤200 chars (**199 measured**) /
      Description / What's inside / Requirements / What it does NOT do
      / FAQ) and checked claim-by-claim against the extracted bundle:
      "7 chapters / 5 templates / 16 content files" = the enumerated
      inventory; "16 complete manuscripts" and "15,995-word resumed
      manuscript" are cited to the ledger at `79a1987` and PR #159
      (squash `3b159d9`); the "What it does NOT do" section states the
      honest boundaries (contains no fiction, ships no software,
      no automated enforcement for solo writers, seller's-own-repo
      evidence, zero verified book sales behind the pricing chapter,
      format-checks-only verification) and the FAQ names the free
      substitute out loud; refund/license/support lines present,
      marked owner-to-set.

## 7. ⚑ OWNER-GATE — publish clicks (queued, never automated)

Seat output = this queued OWNER-ACTION block; the seat performed
**none** of it. It is the queue-parseable form of the click-script in
[`owner-actions.md`](../../launch/ai-novella-production-kit/owner-actions.md) —
the HOW detail lives there; no freeze applies (no payment-path gate).

**OWNER-ACTION — Publish "AI Novella Production Kit" at $29 one-time**
1. **Storefront account:** owner signs into the storefront (the SWTK
   Gumroad account already exists and has payout configured).
2. **⚑ Storefront pick:** **Gumroad** (default — same account as the
   live SWTK listing; the click-script's HOW is written against it,
   including the writing-category note) or Lemon Squeezy — owner's
   call; either works with the same zip + copy.
3. **Product:** New product → Digital product; Name = "AI Novella
   Production Kit"; upload
   `candidates/ai-novella-production-kit/dist/ai-novella-production-kit-v0.1.zip`
   and verify the upload matches sha256 `f85f709b…70bf78` (full hash
   in §1 and the click-script ARTIFACT line — never upload a stale
   local copy).
4. **Copy:** paste Title / Short + Description / What's inside / FAQ
   from
   [`listing-copy.md`](../../launch/ai-novella-production-kit/listing-copy.md);
   set the refund/license lines the copy marks owner-to-set.
5. **Price:** set **$29 one-time** (fixed — set at ideation; the
   SWTK/GWTK/MACP precedent rung).
6. **Publish + record:** publish, copy the public product URL,
   storefront preview/test purchase to confirm the zip delivers.
   Optional same-visit cross-sell: one line each on the
   template-packs and field-manual listings pointing here (first-ten
   path channel 2, weak-fit disclosed).

- [ ] ⚑ **Owner:** storefront pick (**Gumroad** (default)) — or Lemon Squeezy.
- [ ] ⚑ **Owner:** zip uploaded + sha256 spot-check against §1.
- [ ] ⚑ **Owner:** listing copy pasted + refund/license lines set.
- [ ] ⚑ **Owner:** price set (**$29 one-time** (default per ideation + the SWTK/GWTK/MACP rung)).
- [ ] ⚑ **Owner:** the publish click + preview/test purchase + public URL copied.
- [ ] Seat (post-click, no money moved): record the launch durably on
      `main` — verified listing URL, price, timestamp — in the style of
      [`docs/launch/stripe-webhook-test-kit/LAUNCH-LOG.md`](../../launch/stripe-webhook-test-kit/LAUNCH-LOG.md),
      flip these rows to the `— DONE <date>` disposition, confirm the
      KILL-CHECK line below against the actual click date (re-dating
      it T+7/T+30 from the click if the click lands later than
      2026-07-13), and regenerate the owner queue.

KILL-CHECK: ⏲ 2026-07-20 T+7 first-signal check · ⏲ 2026-08-12 T+30 validation-signal deadline

(Clock note: dates derived from `date -u` at listing-queue time,
2026-07-13; per `docs/products/TEMPLATE.md` stage 8 they ARM at the
owner's publish click — the post-click seat row above re-dates them
from the actual click date if it differs.)

---

**Verdict: publish-ready up to the owner gate.** Built + priced +
listing drafted + format verified + sha recorded (all evidenced
above); the product parks at §7 (owner clicks) by design. Honest
caveats: the score (3.525) sits at the borderline band's edge and WTP
2.5 is the structural weak axis — free writing advice is endless and
the method is transcribable; the channel is brand-new (the lane has
never posted, listed, or sold anything to writers — distribution 3 was
scored on the surface existing, not on us reaching it); the
method-without-the-agent gap is real (production enforcement came from
a coding-agent fleet + CI gate; solo buyers get structure, not
enforcement — disclosed in chapter 1 and the listing); the production
evidence is this repo's own use, and the fiction-side kill rules are
gates-applied, not kills-survived (no book has launched yet); the ≤60k
budget cut a worked sample book, a translation-workflow chapter, and
genre band tables (recorded in §1, not silent); build token actuals
were not precisely metered (recorded as unmeasured, never invented);
conservative expectation 0–3 sales / $0–$87 first 90 days, $0 absent
distribution; and a live purchase remains unverified until the owner's
own test purchase.
