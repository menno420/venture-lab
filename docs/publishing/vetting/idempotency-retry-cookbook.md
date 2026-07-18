# Title Vetting — The Idempotency & Retry Cookbook

> **Status:** `plan`
>
> PRODUCT packet in the vetting directory, so the publish click rides the derived
> owner queue (`../OWNER-QUEUE.md` via `scripts/derive_owner_queue.py`). Queued
> under ORDER 016 (2026-07-18 continuation run). No freeze applies — a guide +
> stdlib-recipe cookbook with no payment-path dependency (the ORDER 003 ⚑B/⚑D
> freeze, lifted 2026-07-11 by PR #22, never attached to it). Every step marked
> **⚑ OWNER-GATE** is an owner click, never automated.

**Title:** The Idempotency & Retry Cookbook · **Category:** digital product /
developer guide cookbook · **Date vetted:** 2026-07-18

Product: [`candidates/idempotency-retry-cookbook/`](../../../candidates/idempotency-retry-cookbook/README.md)
(v0.1; buyer bundle `dist/idempotency-retry-cookbook-v0.1.zip`; launch assets in
[`docs/launch/idempotency-retry-cookbook/`](../../launch/idempotency-retry-cookbook/owner-actions.md);
intake [`INTAKE.md`](../../../candidates/idempotency-retry-cookbook/INTAKE.md),
scored 3.75).

## 1. Built (verified this session, 2026-07-18)

- [x] Guide assembled from public specs + committed companion-kit material, every
      chapter with a Sources footer: ch.1 naive-retry threat model ← RFC 9110
      §9.2.2/§15.5-6 + Google SRE (Overload / Cascading Failures); ch.2
      idempotency keys ← IETF `draft-ietf-httpapi-idempotency-key-header` + Stripe
      idempotency docs + RFC 9110 §9.2.2/§15.5.10/§15.5.21; ch.3 retryable
      classification ← RFC 9110 §9.2.2/§15.5-6 + RFC 6585 §4 + RFC 8470; ch.4
      backoff & jitter ← AWS *Exponential Backoff And Jitter* (Brooker) + Google
      SRE; ch.5 budgets & breakers ← Google SRE + gRPC A6 retry throttling +
      Nygard *Release It!* Circuit Breaker; ch.6 honoring Retry-After ← RFC 9110
      §10.2.3 + RFC 6585 §4 + IETF `draft-ietf-httpapi-ratelimit-headers`; ch.7
      at-least-once/dedup ← RFC 9110 §9.2.2 + Google SRE + public webhook-event-id
      model; ch.8 recipes + honesty ledger + further reading.
- **Evidence class: hybrid (runnable-and-self-tested recipes + verified-by-citation
      prose).** The four `recipes/` files ship a 26-test stdlib `unittest`
      self-test executed this session — **`Ran 26 tests ... OK`** — from source AND
      from the extracted bundle; the prose chapters are verified by citation to
      public specs (the honest-null substitute for the zero-runtime chapters). No
      fabricated quotes; sources cited by stable identifier. `idempotency_store.py`
      is a labeled in-memory sketch (not a distributed store); both header specs
      are disclosed as IETF drafts.
- [x] **Honest size verdict:** ~5,000 words (~12 pages) of guide across 8 chapters
      + 4 stdlib Python files (~700 lines incl. the 26-test self-test) + ~1,500
      words README/QUICKSTART/PROVENANCE. The material fully supports every
      chapter; the limits (reference-not-library, snippets-not-your-system, draft
      headers) are stated in the README honesty box, PROVENANCE, the listing FAQ,
      and guide ch.8 — not asserted away.
- [x] Recipe self-test **executed via `python3 -m unittest test_recipes`** — 26/26
      pass from the source tree and again from the extracted zip in a clean dir
      (offline, deterministic: seeded RNG, injected clock, recording fake sleeper —
      no wall-clock waits). Wired as the `idempotency-retry-cookbook-tests` job in
      `.github/workflows/kit-tests.yml`, mirroring the kit siblings.
- [x] Buyer bundle built via allow-list `package.sh` (auto-merge-enabler /
      merge-wall cookbook pattern: fixed mtimes, sorted entries, `zip -X`),
      **byte-reproducible** — double rebuild, identical sha256, committed dist IS
      that build.
- [x] **sha256 `9579f98ae0ffbb5e670e03aa48673ad45d070632ac657aef98dde4bbfc8a8981`**
      (43,177 bytes, 16 content files) — also pinned in the click-script's ARTIFACT
      line.
- [x] Inventory + honest-null check (executed substitute for an HTTP test row,
      since the prose chapters are zero-runtime content): inventory 16/16 vs
      `INCLUDED.md`; all 12 markdown files valid UTF-8 non-empty, H1-headed with
      balanced fences; the recipe self-test run from the extracted bundle (26/26).
      Honest remainder: the prose is verified by citation, not a runtime test, and
      the 26-test suite proves the shipped snippets behave — NOT that a buyer's
      real distributed store / backoff-under-load / breaker thresholds are correct
      (load-test those; verify the endpoint with the companion kits).
- [x] Checkout/format verified from the artifact itself: clean-dir unzip — README
      + QUICKSTART + INCLUDED + PROVENANCE at top level, `guide/` 8 chapters,
      `recipes/` 4 Python files (matches `INCLUDED.md` manifest 16/16). **Secret
      scan:** real-secret-shape scan (ghp_/ gho_/ github_pat_/ sk_live_/ whsec_/
      AKIA/ xox/ AIza) **0 hits**. No `.DS_Store`, no `__pycache__`, no `.pyc`, no
      junk entries in the archive.

## 2. Collision scan

- [x] No in-catalog title collision. **Disclosed adjacency to the Idempotency Key
      Test Kit ($29) and the Rate-Limit Test Kit ($29):** shared subject area, but
      the honest boundary, stated in both this listing and the intake, is
      teach-vs-test — the kits fire real HTTP at an endpoint you own and report
      PASS/FAIL on the exactly-once / throttling contracts; THIS cookbook teaches
      the safe-retry patterns (idempotency keys, backoff+jitter, budgets, breakers,
      Retry-After, consumer dedup) and ships tested reference recipes. Same
      teach-vs-test relationship the `merge-wall-cookbook.md` / `auto-merge-enabler-cookbook.md`
      cookbooks have to their kits — natural cross-sell, non-overlapping scope.
      Same concentrated community/content channel as the rest of the catalog (the
      intake's own channel-risk note, disclosed).

## 3. Market / price

- [x] Price **$19 one-time** — set at intake
      ([`INTAKE.md`](../../../candidates/idempotency-retry-cookbook/INTAKE.md):
      "Conservative revenue estimate: $19 one-time") and recorded identically in
      the listing copy, the click-script, and here. Precedent: the **Merge-Wall
      Cookbook $19** ([`merge-wall-cookbook.md`](merge-wall-cookbook.md)) and the
      **Auto-Merge Enabler Cookbook $19**
      ([`auto-merge-enabler-cookbook.md`](auto-merge-enabler-cookbook.md)) — the
      catalog's cited-throughout, runnable-recipe-shipping cookbook rung and this
      product's nearest siblings in shape (a teaching cookbook that pairs with its
      test kits). Chain: $15 (kill-rule-intake-kit, false-green-test-trap) <
      **$19** = merge-wall-cookbook $19 = auto-merge-enabler-cookbook $19 =
      template-packs $19 PWYW < the API-robustness test kits $29 each < SWTK $29
      live < field-manual $39 < membership-kit $49. Conservative expectation 0–4
      sales / $0–$76 first-90-day, $0 absent distribution (the intake's own line;
      validation signal ≥1 sale OR ≥30 reads in 30 days, else ledgered negative).
      Fixed $19 (not PWYW — the ⚑ template-packs listing is the catalog's
      designated PWYW instrument).

## 4–5. Packaging

- [x] Buyer bundle is the allow-listed `package.sh` output (README + QUICKSTART +
      INCLUDED + PROVENANCE + `guide/` + `recipes/`; deliberately excludes
      `LISTING.md`, the lane-internal `INTAKE.md`, `dist/`, `package.sh`, and any
      `__pycache__`/`.pyc`). No cover image ships — owner adds one or uses the
      storefront default.

## 6. Listing copy (drafted in-repo — nothing published)

- [x] [`listing-copy.md`](../../launch/idempotency-retry-cookbook/listing-copy.md)
      at catalog parity (Title / short ≤200 chars / long / bullets / FAQ + the
      "what it does NOT do" honesty section + PROVENANCE-FOOTER) and checked
      claim-by-claim against the extracted bundle: "~12 pages" = measured from the
      extracted `guide/`; "four stdlib recipes with a 26-test self-test" = executed
      (`Ran 26 tests ... OK`); the per-chapter Sources footers match the shipped
      chapters; the FAQ states what was NOT machine-verified (prose by citation;
      recipes proven as snippets not as your system; draft headers) and tells
      already-disciplined buyers to buy nothing.

## 7. ⚑ OWNER-GATE — publish clicks (queued, never automated)

Seat output = this queued OWNER-ACTION block; the seat performed **none** of it.
It is the queue-parseable form of the click-script in
[`owner-actions.md`](../../launch/idempotency-retry-cookbook/owner-actions.md) —
the HOW detail lives there; no freeze applies (no payment-path gate).

**OWNER-ACTION — Publish "The Idempotency & Retry Cookbook" at $19 one-time**
1. **Storefront account:** owner signs into (or creates) the storefront; complete
   its payout setup first or revenue holds.
2. **⚑ Storefront pick:** **Gumroad** (default — the click-script's HOW is written
   against it; same account as the live SWTK listing) or Lemon Squeezy — owner's
   call; either works with the same zip + copy.
3. **Product:** New product → Digital product; Name = "The Idempotency & Retry
   Cookbook"; upload `candidates/idempotency-retry-cookbook/dist/idempotency-retry-cookbook-v0.1.zip`
   and verify the upload matches sha256 `9579f98a…c8a8981` (full hash in §1 and the
   click-script ARTIFACT line — never upload a stale local copy).
4. **Copy:** paste Title / Short + Long description / Bullets / FAQ + the "what it
   does NOT do" honesty section from
   [`listing-copy.md`](../../launch/idempotency-retry-cookbook/listing-copy.md).
5. **Price:** set **$19 one-time** (fixed — set at intake; merge-wall /
   auto-merge-enabler $19 precedent rung).
6. **Publish + record:** publish, copy the public product URL, storefront
   preview/test purchase to confirm the zip delivers.

- [ ] ⚑ **Owner:** storefront account + payout setup.
- [ ] ⚑ **Owner:** storefront pick (**Gumroad** (default)) — or Lemon Squeezy.
- [ ] ⚑ **Owner:** zip uploaded + sha256 spot-check against §1.
- [ ] ⚑ **Owner:** listing copy pasted.
- [ ] ⚑ **Owner:** price set (**$19 one-time** (default per intake + precedent
      chain)).
- [ ] ⚑ **Owner:** the publish click + preview/test purchase + public URL copied.
- [ ] Seat (post-click, no money moved): record the launch durably on `main` —
      verified listing URL, price, timestamp — in the style of
      [`docs/launch/stripe-webhook-test-kit/LAUNCH-LOG.md`](../../launch/stripe-webhook-test-kit/LAUNCH-LOG.md),
      arm the intake's 30-day kill clock as a `KILL-CHECK:` line here, and
      cross-link the cookbook from the Idempotency Key Test Kit / Rate-Limit Test
      Kit surfaces (same developer audience, teach-vs-test cross-sell).

---

**Verdict: publish-ready up to the owner gate.** Built + priced + listing drafted
+ checkout/format verified + sha recorded + recipe self-test green (all evidenced
above); the product parks at §7 (owner clicks) by design. Honest caveats: the
guide is ~12 pages of prose + recipes, sized to what the cited material supports;
the prose is verified by citation, the recipes by a shipped 26-test suite (which
proves the snippets, not your production system); `idempotency_store.py` is a
labeled in-memory sketch; both header specs are IETF drafts (re-verify); the
material is assembled from free public sources, so the moat is curation + tested
recipes + auditable citations, not secret knowledge; the buyer TAM is broad but on
the catalog's one concentrated channel (intake distribution 3/5) — expect ~$0
absent distribution; and a live purchase remains unverified until the owner's own
test purchase.
