# Title Vetting — Pagination Test Kit

> **Status:** `plan`
>
> New PRODUCT packet in the vetting directory, so the publish click rides the
> derived owner queue (`../OWNER-QUEUE.md` via `scripts/derive_owner_queue.py`).
> Built under **ORDER 016** (live owner overnight-work order, reaffirmed by the
> live owner turn 2026-07-18) as a NEW sellable (roadmap R2) — the same proven
> kit template applied to a FOURTH problem class (pagination / result-set
> integrity, not signature verification, not dedup/safe-retry, and not
> throttling). No freeze applies — a dev-tool kit with no payment-path
> dependency (the ORDER 003 ⚑B/⚑D freeze, lifted 2026-07-11 by PR #22, never
> attached to it). Every step marked **⚑ OWNER-GATE** is an owner click, never
> automated.

**Title:** Pagination Test Kit · **Category:** digital product / dev tool ·
**Date vetted:** 2026-07-18

Product: [`candidates/pagination-test-kit/`](../../../candidates/pagination-test-kit/README.md)
(v0.1; buyer bundle `dist/pagination-test-kit-v0.1.zip`; launch assets in
[`docs/launch/pagination-test-kit/`](../../launch/pagination-test-kit/owner-actions.md);
intake [`INTAKE.md`](../../../candidates/pagination-test-kit/INTAKE.md), priced
$29 on catalog precedent).

## 1. Built (verified this session, 2026-07-18)

- [x] Stdlib-only harness in two languages (`pgtk.py` + `pgtk.js` Node port, same
      commands: `check` / `traversal` / `stable-under-mutation` / `ordering` /
      `page-size` / `terminal` / `cursor-tamper` / `demo` / `list`), a CORRECT
      reference pager (`stub_handler.py`: keyset pagination over a 12-row dataset
      ordered by `(created_at, id)`, an opaque HMAC-signed cursor, an
      `X-Page-Size-Max` clamp, plus `GET /_debug/all` + `POST /_debug/reset` +
      `POST /_debug/insert` + `POST /_debug/delete` for the mutation test), a
      deliberately NAIVE pager (`stub_handler_naive.py`: OFFSET/LIMIT pagination
      that skips under mutation, no over-max clamp, and a forged cursor silently
      coerced to page 1), a one-page `GOTCHAS.md` (failure modes, each mapped to a
      kit command), plus `QUICKSTART.md` and a placeholders-only `.env.example`.
- [x] **Genuinely NEW problem class, not another webhook / idempotency / rate-limit
      kit:** the webhook kits verify an INBOUND provider signature; the idempotency
      kit verifies a STATEFUL safe-retry / exactly-once contract; the rate-limit
      kit verifies a THROTTLING contract; this kit verifies a buyer's OWN paginated
      endpoint's RESULT-SET INTEGRITY — cursor traversal with no overlap/gap,
      stability under mid-traversal mutation, a consistent total order, a clamped
      page size, a terminal signal, and a rejected forged cursor. Zero shared
      fixtures or crypto/dedup/throttle scheme with the siblings.
- [x] **Six properties checked, each PASS/FAIL/SKIP against a buyer endpoint:**
      (1) **traversal** — following `next_cursor` reproduces the full ordered set
      exactly once (no overlap, no gap); (2) **stable-under-mutation** — deleting an
      already-returned row and inserting a tail row BETWEEN page fetches does not
      skip or duplicate items present throughout (the headline — catches the OFFSET
      skip); (3) **ordering** — a consistent total order by `(sort_key, id)` with a
      unique tiebreaker, no duplicate ids; (4) **page-size** — `limit` honored on
      full pages and an over-max `limit` clamped to the documented max
      (`X-Page-Size-Max`); (5) **terminal** — the last page signals the end
      (null/absent `next_cursor`), no infinite loop; (6) **cursor-tamper** — a
      malformed or forged/opaque cursor is rejected (4xx), not coerced to page 1.
- [x] **Value proof built in (correct vs naive):** `pgtk demo` runs all six against
      BOTH bundled pagers with a loud zero-accounts banner — the CORRECT keyset
      pager passes all six and the NAIVE OFFSET pager is FLAGGED on
      `stable-under-mutation` / `page-size` / `cursor-tamper`. The kit demonstrably
      distinguishes correct keyset pagination from a broken offset one, and is
      HONEST that three properties (`traversal`, `ordering`, `terminal`) do NOT
      distinguish the two in a static dataset (documented in `stub_handler_naive.py`
      and `GOTCHAS.md`).
- [x] **Honest source discipline:** `fixtures/PROVENANCE.md` states up front that
      the fixtures are docs-derived request/response templates (NOT wire-captured —
      no account/key/service call), pins a sha256 per fixture, and is explicit that
      there is NO single RFC for cursor pagination — it is a widely-deployed
      PATTERN. The kit tests the keyset/cursor model and grounds each property in
      the keyset-vs-offset literature (the offset skip/dupe under mutation) and the
      named vendor cursor-pagination docs (Stripe `starting_after`/`has_more`, Slack
      `response_metadata.next_cursor`, GitHub Link-header cursors). The
      implementation choice (HMAC-signed opaque cursor) is stated as ONE honest way
      to satisfy the externally-visible contract, not the only one.
- [x] **Tests (real-path, executed 2026-07-18):** 31-test HTTP-layer suite — every
      request fired over actual HTTP to a reference pager on an ephemeral port; no
      timed waits, so the suite is fast. Green from source (`Ran 31 tests / OK`) AND
      from the extracted zip in a clean dir (`Ran 31 tests / OK`). Covers:
      manifest/fixture shape; the correct pager passing each property (traversal
      reproducing ground truth exactly once; no skip after deleting a seen row;
      over-max clamped; the `X-Page-Size-Max` header; a forged cursor and a tampered
      valid cursor both returning 400); the full suite green on the correct pager;
      the kit FLAGGING the naive pager on the offset skip under mutation, the
      unbounded over-max page, and the forged cursor served as page 1 — with
      `traversal` + `ordering` + `terminal` honestly NOT distinguishing (both pagers
      pass them); the SKIP path proving `stable-under-mutation` SKIPs (not falsely
      fails) when no test-mutation hook exists; plus unit coverage of the opaque
      cursor's sign/verify (roundtrip, bad base64, missing dot, signature mismatch,
      wrong-secret rejection).
- [x] Suite wired into CI: `pagination-test-kit-tests` job added to
      `.github/workflows/kit-tests.yml`, same convention as the Stripe / GitHub /
      Slack / Shopify / idempotency / rate-limit kit jobs.
- [x] Buyer bundle built via allow-list `package.sh` (kit pattern: fixed mtimes,
      sorted entries, `zip -X`; excludes `INTAKE.md`, `package.sh`, `dist/`),
      **byte-reproducible** — unconditional double rebuild 2026-07-18 produced the
      identical sha256, committed dist IS that build.
- [x] **sha256 `ae189fe9465dc7a27204c84b5e187e475fb25158c0f6c31033701fc2e970a118`**
      (42,827 bytes, 13 content files) — also pinned in the click-script's ARTIFACT
      line.
- [x] Checkout/format verified from the artifact itself: clean-dir unzip —
      `README.md` + `QUICKSTART.md` + `GOTCHAS.md` + `.env.example` + harness ×2 +
      both pagers + test suite at top level, `fixtures/` 2 templates +
      `MANIFEST.json` + `PROVENANCE.md`; real-secret-shape scan
      (`sk_live_`/`whsec_`/`AKIA`/private key/etc.) **0 hits**; no junk entries in
      the archive.

## 2. Collision scan

- [x] No in-catalog title collision. Closest shipped products, boundaries
      disclosed: the four webhook kits (**Stripe $29** LIVE, **GitHub/Slack/Shopify
      $29** queued), the **Idempotency Key Test Kit $29** (queued), and the
      **Rate-Limit Test Kit $29** (queued) share the kit SHAPE but a DIFFERENT
      problem class — the webhook kits verify an inbound HMAC signature, the
      idempotency kit verifies safe-retry dedup, the rate-limit kit verifies
      throttling (429 + Retry-After), and this kit verifies pagination / result-set
      integrity (no skip/dupe under mutation + ordering + clamp + terminal + forged
      cursor). Zero shared fixtures or code, fresh PROVENANCE. Honest positioning:
      this is the *result-set-integrity* rung of API robustness — the natural pair
      to the idempotency kit's safe-retry half and the rate-limit kit's throttling
      half — so the listings cross-reference rather than claim each other's scope.
- [x] Same/adjacent buyer audience as the dev-tool catalog (intake's
      concentrated-channel risk, disclosed); narrower still because many ORMs and
      API frameworks ship a cursor pager, so the audience is specifically
      hand-rolled pagers and custom offset-based endpoints.

## 3. Market / price

- [x] Price **$29 one-time** — set on catalog precedent and recorded identically in
      `INTAKE.md`, the listing copy, the click-script, and here. Precedent: the
      Stripe Webhook Test Kit sells LIVE at exactly $29 for the same product shape
      (stdlib harness + docs-derived fixtures + a correct/naive reference pair +
      byte-reproducible bundle), and the GitHub/Slack/Shopify kits + the Idempotency
      kit + the Rate-Limit kit are queued at $29. Chain: $15 (kill-rule kit,
      false-green) < $19 (merge-wall, template-packs PWYW) < **$29 this kit** =
      Stripe $29 (live) = GitHub/Slack/Shopify $29 (queued) = Idempotency $29
      (queued) = Rate-Limit $29 (queued) < field-manual $39 < membership-kit $49.
      Conservative expectation 0–5 sales / $0–$145 first-90-day, $0 absent
      distribution (the intake's own line; validation signal ≥1 sale OR ≥50 article
      reads in 30 days, else ledgered negative; T+7 funnel checkpoint / T+30 kill
      deadline armed as a KILL-CHECK here once the click is DONE-flipped).

## 4–5. Packaging

- [x] Buyer bundle is the allow-listed `package.sh` output (`README.md` +
      `QUICKSTART.md` + `GOTCHAS.md` + `.env.example` + `pgtk.py` + `pgtk.js` +
      `stub_handler.py` + `stub_handler_naive.py` + `test_http_realpath.py` +
      `fixtures/`; deliberately excludes the lane-internal `INTAKE.md`,
      `package.sh`, `dist/`). No cover image ships — owner adds one or uses the
      storefront default.

## 6. Listing copy (drafted in-repo — nothing published)

- [x] [`listing-copy.md`](../../launch/pagination-test-kit/listing-copy.md) at
      catalog parity (Title / Short ≤200 chars (197 measured) / Long / Bullets /
      FAQ) and checked claim-by-claim against the extracted bundle: "31 tests" =
      the suite that ran green twice this session; "two docs-derived templates" = 2
      fixtures in the zip; the correct/naive demo claim = executed (correct
      all-pass, naive flagged on 3) both languages; the FAQ + "what it does NOT do"
      section states the honest boundaries (not a webhook/idempotency/rate-limit
      kit; no single RFC for cursor pagination; the stability property SKIPs on a
      read-only endpoint; single-caller scope; fixtures docs-derived not live
      captures; no live API anything); a PROVENANCE-FOOTER pins `file@sha` sources;
      refund/license lines present, marked owner-to-set.

## 7. ⚑ OWNER-GATE — publish clicks (queued, never automated)

Seat output = this queued OWNER-ACTION block; the seat performed **none** of it.
It is the queue-parseable form of the click-script in `owner-actions.md` (same
directory as this packet's launch assets) — the HOW detail lives there; no freeze
applies (no payment-path gate).

**OWNER-ACTION — Publish "Pagination Test Kit" at $29 one-time**
1. **Storefront account:** owner signs into the storefront (the Stripe kit Gumroad
   account already exists and has payout configured).
2. **⚑ Storefront pick:** **Gumroad** (default — same account as the live Stripe
   kit listing; the click-script's HOW is written against it) or Lemon Squeezy —
   owner's call; either works with the same zip + copy.
3. **Product:** New product → Digital product; Name = "Pagination Test Kit";
   upload `candidates/pagination-test-kit/dist/pagination-test-kit-v0.1.zip` and
   verify the upload matches sha256 `ae189fe9…970a118` (full hash in §1 and the
   click-script ARTIFACT line — never upload a stale local copy).
4. **Copy:** paste Title / Short + Long description / Bullets / FAQ from the
   `listing-copy.md` in this product's launch dir; set the refund/license lines the
   copy marks owner-to-set.
5. **Price:** set **$29 one-time** (fixed — catalog precedent; the Stripe kit is
   live at the identical price for the identical product shape, GitHub/Slack/Shopify
   + Idempotency + Rate-Limit queued at $29).
6. **Publish + record:** publish, copy the public product URL, storefront preview/
   test purchase to confirm the zip delivers. Optional same-visit cross-sell: one
   line on the Idempotency kit, Rate-Limit kit, and webhook kit listings pointing
   here (first-ten path channel 2).

- [ ] ⚑ **Owner:** storefront pick (**Gumroad** (default)) — or Lemon Squeezy.
- [ ] ⚑ **Owner:** zip uploaded + sha256 spot-check against §1.
- [ ] ⚑ **Owner:** listing copy pasted + refund/license lines set.
- [ ] ⚑ **Owner:** price set (**$29 one-time** (default per catalog precedent + the live Stripe kit price)).
- [ ] ⚑ **Owner:** the publish click + preview/test purchase + public URL copied.
- [ ] Seat (post-click, no money moved): record the launch durably on `main` —
      verified listing URL, price, timestamp — in the style of the Stripe kit
      `LAUNCH-LOG.md`, flip these rows to the `— DONE <date>` disposition, arm the
      intake's kill clock as a `KILL-CHECK:` line here (T+7 funnel checkpoint · T+30
      kill-rule deadline: ≥1 sale OR ≥50 article reads, else ledger NEGATIVE +
      pause/delist), and regenerate the owner queue.

---

**Verdict: publish-ready up to the owner gate.** Built + priced + listing drafted +
checkout/format verified + sha recorded (all evidenced above); the product parks at
§7 (owner clicks) by design. Honest caveats: there is NO single RFC for cursor
pagination — the model is the widely-deployed keyset/cursor pattern, sourced to the
keyset-vs-offset literature + named vendor docs (Stripe/Slack/GitHub), stated
honestly rather than cited to one authority; the `stable-under-mutation` property
needs a test-mutation hook and SKIPs (not fails) on a read-only endpoint — its full
proof runs against the bundled stubs or a seeded mutable test dataset; the kit tests
a single caller's ordered set, not per-user visibility or cross-shard cursor
consistency; `traversal`, `ordering`, and `terminal` honestly do NOT distinguish a
correct pager from the naive one in a static dataset (all three pass on both),
documented; the free-substitute risk is real (keyset pagination is well-documented;
the paid delta is the harness testing the buyer's OWN endpoint — including the
mid-traversal mutation and forged-cursor rejection a from-memory test skips — + the
correct/naive reference pair + provenance discipline); many frameworks ship a cursor
pager, narrowing the audience to hand-rolled/offset ones; same concentrated dev-tool
channel where the Stripe kit has 0 organic sales — expect ~$0 absent distribution;
and a live purchase remains unverified until the owner's own test purchase.
