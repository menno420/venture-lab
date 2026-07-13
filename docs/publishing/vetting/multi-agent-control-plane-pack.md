# Title Vetting — Multi-Agent Control-Plane Pack

> **Status:** `plan`
>
> Twelfth PRODUCT packet in the vetting directory; the publish click
> rides the derived owner queue (`../OWNER-QUEUE.md` via
> `scripts/derive_owner_queue.py`). BUILD #3 (3.525, tight budget) of
> the 2026-07-13 ideation batch (`docs/products/ideas-2026-07-13.md`
> §3, PR #142), built under ORDER 008's products clause with the
> ideation doc's Kill Rule 0 gate honored: full INTAKE.md written and
> answered PROCEED before any pack content. PARK #4 (Parallel-Agent
> Claims Kit) folded in as guide chapter 4 per its ideation verdict.
> No freeze applies — a zero-runtime document pack with no payment-path
> dependency (the ORDER 003 ⚑B/⚑D freeze, lifted 2026-07-11 by PR #22,
> never attached to it). Every step marked **⚑ OWNER-GATE** is an owner
> click, never automated.

**Title:** Multi-Agent Control-Plane Pack · **Category:** digital
product / conventions + templates guide · **Date vetted:** 2026-07-13

Product: [`candidates/multi-agent-control-plane-pack/`](../../../candidates/multi-agent-control-plane-pack/README.md)
(v0.1; buyer bundle `dist/multi-agent-control-plane-pack-v0.1.zip`;
launch assets in
[`docs/launch/multi-agent-control-plane-pack/`](../../launch/multi-agent-control-plane-pack/owner-actions.md);
intake [`INTAKE.md`](../../../candidates/multi-agent-control-plane-pack/INTAKE.md),
scored 3.525 at ideation, Kill Rule 0 gate PROCEED).

## 1. Built (verified this session, 2026-07-13)

- [x] **Intake FIRST (Kill Rule 0):** `INTAKE.md` written before any
      pack content — kill-rule fields bound (signal ≥1 sale OR ≥50
      article reads in 30 days; T+7/T+30 clocks to arm post-click;
      budget ≤50k tokens HARD), gate answered PROCEED with the
      borderline-band caveat recorded.
- [x] Zero-runtime content pack, 17 content files: README + QUICKSTART
      + INCLUDED + 6 guide chapters + 7 blank-slate templates (+
      templates/README copy map). Everything distilled from COMMITTED
      files only — no invented material: `control/README.md@35e5597`
      (one-writer law, standing ritual), `control/inbox.md@84d4bcb`
      (ORDER grammar, 10 production orders), `control/status.md@e252b46`
      (live heartbeat shape), `control/outbox.md@58cdb14` (SIM-REQUEST /
      WEBSITE-IDEA / INFO markers, ordered reports),
      `control/claims/README.md@35e5597` (claim grammar, arbitration,
      expiry), `docs/conventions.md@35e5597` (session discipline #7–#12),
      `.github/workflows/substrate-gate.yml@35e5597` (born-red HOLD).
      Fleet-specific noise stripped: no session ids, no trigger ids, no
      owner asks, no exact model IDs (family-level convention only).
- [x] **PROVENANCE-FOOTER convention (TEMPLATE.md stage 5):** every
      chapter ends in a Sources footer citing its committed `file@sha`
      sources; the listing names "claims verified by citation" as a
      checkable feature.
- [x] **Verified-by-production truth-claim (TEMPLATE.md stage-3 third
      evidence class):** the subject matter IS this repo's live
      control plane, and the chapters cite real production events by
      ID — the full order round trip: outbox SIM-REQUESTs (PR #144,
      squash `58cdb14`) → manager answers appended as inbox ORDER 010
      (PR #161, squash `84d4bcb`) → lane applies + acks status-side
      (PR #163, squash `e252b46`), the inbox row itself never edited
      by the lane; claims expiry executing as designed (prune PR #154,
      squash `557b744`); the born-red gate's designed recovery path
      run for real (mid-turn-death PR #157 resumed as PR #159, squash
      `3b159d9`; terminal-state heartbeat amendment PR #160, squash
      `765e1f8`); CI append-only/grammar rejections quoted verbatim
      from recorded runs 29216242073 / 29216279657. The claims-ledger
      conflict measurement (~98% shared-append vs 0% per-file) is
      cited as EXTERNAL (`menno420/superbot`
      `tools/sim/claim_layout_sim.py`) per the ideation entry's own
      requirement — not re-run in-kit, and the chapter says so.
- [x] **Honest null (TEMPLATE.md stage-3, zero-runtime clause):**
      no test suite exists or is warranted — nothing in the bundle
      executes. Substitute executed instead (2026-07-13T14:22:25Z,
      from the extracted artifact in a clean dir): inventory
      enumerated 17/17 vs the listing's "What's inside"; every file
      UTF-8-decoded; markdown pass OK (H1-first, balanced fences, no
      fill-slot tokens; `templates/claim-file.md` exempt from H1 — a
      one-bullet fragment by design); secret/session-id/trigger-id
      scan **0 hits**; archive listing free of `.DS_Store` /
      `__pycache__` / junk. No CI job added — nothing to run (the
      merge-wall-cookbook precedent).
- [x] Buyer bundle built via explicit per-file allow-list `package.sh`
      (fixed mtimes, sorted entries, `zip -X`; excludes INTAKE.md,
      package.sh, dist/), **byte-reproducible** — unconditional double
      rebuild 2026-07-13T14:22:25Z, identical sha256, committed dist
      IS that build.
- [x] **sha256 `39fc864880c1fa6d21f1a6974543c4df95df6e89cd8b6ae4656f9dd8311b0a9e`**
      (21,989 bytes, 17 content files) — also pinned in the
      click-script's ARTIFACT line.
- [x] **Budget honesty (the ≤50k-token cap, cuts recorded — never
      silent):** shipped lean by design; three things the cap cut:
      (1) no advisory claims-checker script (PARK #4 mentioned one;
      the chapter documents the checker CONTRACT — parse anchors,
      advisory-only, what to nag on — a buyer writes the ~50-line
      script); (2) no worked multi-day example transcript of a
      manager/lane exchange (the chapters quote real single events
      instead); (3) no wake-scheduling/dead-man's-switch chapter (that
      concept was KILLED at ideation as #6 — deliberately out of
      scope, not squeezed in). All three are named in-listing by the
      "ships no software" honesty section or bounded by "What it does
      NOT do".

## 2. Collision scan

- [x] No in-catalog title collision. Closest shipped products,
      boundaries disclosed (all named at ideation): **template-packs
      $19 PWYW** — SINGLE-repo session discipline; this pack is the
      multi-agent control plane above it (the listing says "only earns
      its price once you run 2+ concurrent sessions"). **Agent Fleet
      Field Manual $39** — its ch.6/7 teach this layer in PROSE; this
      pack is the working version (the disclosed working-version
      cross-sell precedent: kill-rule-kit vs ch.8). **Owner-Click
      Queue Kit $19** — the OCQK packet required this boundary stated
      both ways if #3 shipped, and it is: OCQK is the owner-action
      (spend/publish) queue; this pack is agent-to-agent coordination.
      Both listings disclose it. **Merge-Wall Cookbook $19** — CI
      landing mechanics; this pack's ch.6 touches the born-red gate
      only as the session-card discipline, and cites the cookbook's
      territory rather than re-teaching it.
- [x] PARK #4 (Parallel-Agent Claims Kit, 3.275) folded in as chapter
      4 per its ideation verdict ("correct home: a chapter + template
      inside the Control-Plane Pack, not a standalone SKU") — so the
      PARK is discharged, not orphaned; no standalone claims SKU may
      now ship without superseding this packet.
- [x] Smallest audience of the three batch BUILDs (distribution 2.5
      at ideation) — disclosed here and in the intake, not smoothed
      over.

## 3. Market / price

- [x] Price **$29 one-time** — set at ideation
      (`docs/products/ideas-2026-07-13.md` §3) and recorded
      identically in `INTAKE.md`, the listing copy, the click-script,
      and here. Precedent: SWTK live at exactly $29, GWTK queued at
      $29. The $29 rung (vs the $19 conventions rung of merge-wall /
      OCQK / template-packs) is argued in the click-script's
      precedent chain: a complete multi-surface system (5 surfaces + 7
      installable templates + the folded $15-scored claims chapter),
      not one convention plus one script; capped below the $39 manual
      (one layer, not broad fleet ops). Conservative expectation: 0–5
      sales / $0–$145 first-90-day, $0 absent distribution (the
      intake's own line; validation signal ≥1 sale OR ≥50 article
      reads in 30 days, else ledgered negative; T+7 funnel checkpoint
      / T+30 kill deadline armed as a KILL-CHECK here once the click
      is DONE-flipped).

## 4–5. Packaging

- [x] Buyer bundle is the explicit per-file allow-listed `package.sh`
      output (README + QUICKSTART + INCLUDED + guide/ + templates/;
      deliberately excludes the lane-internal INTAKE.md, package.sh,
      dist/). No cover image ships — owner adds one or uses the
      storefront default.

## 6. Listing copy (drafted in-repo — nothing published)

- [x] [`listing-copy.md`](../../launch/multi-agent-control-plane-pack/listing-copy.md)
      at catalog parity (Title / Short ≤200 chars (196 measured) /
      Long / Bullets / FAQ) and checked claim-by-claim against the
      extracted bundle: "6 chapters / 7 templates / 17 content files"
      = the enumerated inventory; "150+ merged PRs" is conservative
      against the repo's live PR counter (PR #163 merged at build
      time); the "what it does NOT do" section states the honest
      boundaries (ships no software, no CI wiring, seller's-own-repo
      evidence, external-cited measurement, format-checks-only
      verification) and the FAQ names the free substitute out loud
      (reading a public repo that runs the pattern);
      refund/license/support lines present, marked owner-to-set.

## 7. ⚑ OWNER-GATE — publish clicks (queued, never automated)

Seat output = this queued OWNER-ACTION block; the seat performed
**none** of it. It is the queue-parseable form of the click-script in
[`owner-actions.md`](../../launch/multi-agent-control-plane-pack/owner-actions.md) —
the HOW detail lives there; no freeze applies (no payment-path gate).

**OWNER-ACTION — Publish "Multi-Agent Control-Plane Pack" at $29 one-time**
1. **Storefront account:** owner signs into the storefront (the SWTK
   Gumroad account already exists and has payout configured).
2. **⚑ Storefront pick:** **Gumroad** (default — same account as the
   live SWTK listing; the click-script's HOW is written against it) or
   Lemon Squeezy — owner's call; either works with the same zip + copy.
3. **Product:** New product → Digital product; Name = "Multi-Agent
   Control-Plane Pack"; upload
   `candidates/multi-agent-control-plane-pack/dist/multi-agent-control-plane-pack-v0.1.zip`
   and verify the upload matches sha256 `39fc8648…311b0a9e` (full hash
   in §1 and the click-script ARTIFACT line — never upload a stale
   local copy).
4. **Copy:** paste Title / Short + Long description / Bullets / FAQ
   from
   [`listing-copy.md`](../../launch/multi-agent-control-plane-pack/listing-copy.md);
   set the refund/license lines the copy marks owner-to-set.
5. **Price:** set **$29 one-time** (fixed — set at ideation; SWTK/GWTK
   precedent at the identical price for the catalog's system-level
   rung).
6. **Publish + record:** publish, copy the public product URL,
   storefront preview/test purchase to confirm the zip delivers.
   Optional same-visit cross-sell: one line each on the template-packs
   and field-manual listings pointing here (first-ten path channel 1).

- [ ] ⚑ **Owner:** storefront pick (**Gumroad** (default)) — or Lemon Squeezy.
- [ ] ⚑ **Owner:** zip uploaded + sha256 spot-check against §1.
- [ ] ⚑ **Owner:** listing copy pasted + refund/license lines set.
- [ ] ⚑ **Owner:** price set (**$29 one-time** (default per ideation + the SWTK/GWTK rung)).
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
Honest caveats: the smallest audience of the batch's three BUILDs
(distribution 2.5 — the population size is the cap, not willingness);
the free substitute is reading any public repo that runs the pattern,
and the listing says so out loud; pure convention — no runtime, so
nothing beyond format checks was machine-verifiable (honest null
executed, not asserted); the production evidence is this repo's own
use — no external fleet has run these exact files; the conflict-rate
measurement is external-cited, not re-run; the ≤50k budget cut a
claims-checker script, a worked transcript, and any wake-scheduling
chapter (recorded in §1, not silent); same concentrated agent-ops
channel where SWTK has 0 organic sales as of 2026-07-13 — expect ~$0
absent distribution; and a live purchase remains unverified until the
owner's own test purchase.
