# Title Vetting — Rate-Limit Test Kit

> **Status:** `plan`
>
> New PRODUCT packet in the vetting directory, so the publish click rides the
> derived owner queue (`../OWNER-QUEUE.md` via `scripts/derive_owner_queue.py`).
> Built under **ORDER 016** (live owner overnight-work order, reaffirmed by the
> live owner turn 2026-07-18) as a NEW sellable — the same proven kit template
> applied to a THIRD problem class (rate-limiting / throttling correctness, not
> signature verification and not dedup/safe-retry). No freeze applies — a
> dev-tool kit with no payment-path dependency (the ORDER 003 ⚑B/⚑D freeze,
> lifted 2026-07-11 by PR #22, never attached to it). Every step marked
> **⚑ OWNER-GATE** is an owner click, never automated.

**Title:** Rate-Limit Test Kit · **Category:** digital product / dev tool ·
**Date vetted:** 2026-07-18

Product: [`candidates/rate-limit-test-kit/`](../../../candidates/rate-limit-test-kit/README.md)
(v0.1; buyer bundle `dist/rate-limit-test-kit-v0.1.zip`; launch assets in
[`docs/launch/rate-limit-test-kit/`](../../launch/rate-limit-test-kit/owner-actions.md);
intake [`INTAKE.md`](../../../candidates/rate-limit-test-kit/INTAKE.md), priced
$29 on catalog precedent).

## 1. Built (verified this session, 2026-07-18)

- [x] Stdlib-only harness in two languages (`rltk.py` + `rltk.js` Node port, same
      commands: `check` / `under-limit` / `over-limit` / `retry-after` /
      `headers` / `window-reset` / `retry-after-honored` / `demo` / `list`), a
      CORRECT reference limiter (`stub_handler.py`: a thread-safe fixed-window
      counter with a short configurable window, emitting `429` + a positive
      `Retry-After` + consistent `RateLimit-*` and legacy `X-RateLimit-*`
      headers, plus `GET /_debug/state` + `POST /_debug/reset`), a deliberately
      NAIVE limiter (`stub_handler_naive.py`: off-by-one, a 429 with no
      `Retry-After`, and stuck/stale `X-RateLimit-*` headers), a one-page
      `GOTCHAS.md` (failure modes, each mapped to a kit command), plus
      `QUICKSTART.md` and a placeholders-only `.env.example`.
- [x] **Genuinely NEW problem class, not another webhook or idempotency kit:** the
      webhook kits verify an INBOUND provider signature; the idempotency kit
      verifies a STATEFUL safe-retry / exactly-once contract; this kit verifies a
      buyer's OWN endpoint's THROTTLING contract — 2xx under the limit, 429 + a
      valid `Retry-After` at it, consistent `RateLimit-*` headers, and a window
      that resets. Zero shared fixtures or crypto/dedup scheme with the siblings.
- [x] **Six properties checked, each PASS/FAIL against a buyer endpoint:**
      (1) **under-limit** — the first `limit` requests in a window return 2xx;
      (2) **over-limit** — request `limit`+1 returns 429 (catches the off-by-one
      quota leak); (3) **retry-after** — the 429 carries a positive, sane
      `Retry-After` (delay-seconds or a future HTTP-date; missing/0/negative/past
      is flagged); (4) **headers** — `RateLimit-*`/`X-RateLimit-*`, when present,
      are consistent (Remaining decrements to 0 at the boundary, Reset in the
      future); (5) **window-reset** — requests succeed again after the advertised
      reset; (6) **retry-after-honored** — the advertised delay matches when the
      service actually resumes (still 429 before, 2xx after, within tolerance).
- [x] **Value proof built in (correct vs naive):** `rltk demo` runs all six
      against BOTH bundled limiters with a loud zero-accounts banner — the CORRECT
      limiter passes all six and the NAIVE limiter is FLAGGED on `over-limit` /
      `retry-after` / `headers` / `retry-after-honored`. The kit demonstrably
      distinguishes a correct limiter from a broken one, and is HONEST that two
      properties (`under-limit`, `window-reset`) do NOT distinguish the two
      (documented in `stub_handler_naive.py` and `GOTCHAS.md`).
- [x] **Honest source discipline:** `fixtures/PROVENANCE.md` states up front that
      the fixtures are docs-derived request templates (NOT wire-captured — no
      account/key/service call), pins a sha256 per fixture, and is explicit about
      which claims rest on STABLE RFCs vs a DRAFT: the 429 + `Retry-After`
      behaviour is RFC 6585 §4 + RFC 9110 §10.2.3 (stable), while the
      `RateLimit-Limit`/`Remaining`/`Reset` header fields follow the IETF draft
      "RateLimit header fields for HTTP" (NOT yet an RFC; newest revisions favour
      a combined structured `RateLimit:` field the kit does NOT assert). The
      `RateLimit-*` headers are treated as OPTIONAL — an endpoint emitting none
      passes the `headers` check with a note — stated honestly rather than faked.
- [x] **Tests (real-path, executed 2026-07-18):** 27-test HTTP-layer suite —
      every request fired over actual HTTP to a reference limiter on an ephemeral
      port, with a short 800 ms window so the timed properties stay fast. Green
      from source (`Ran 27 tests / OK`) AND from the extracted zip in a clean dir
      (`Ran 27 tests / OK`). Covers: manifest/fixture shape; the correct limiter
      passing each property (429 exactly at the boundary; Remaining 4→0;
      Retry-After present and positive; legacy header style read correctly; window
      reset; Retry-After honored); the full suite green on the correct limiter; the
      kit FLAGGING the naive limiter on off-by-one over-limit, missing Retry-After,
      stuck/stale headers, and an un-honourable Retry-After — with `under-limit` +
      `window-reset` honestly NOT distinguishing (both limiters pass them),
      documented; plus unit coverage of the Retry-After parser (delay-seconds +
      future/past HTTP-date + absurd/zero/negative + the Reset epoch heuristic).
- [x] Suite wired into CI: `rate-limit-test-kit-tests` job added to
      `.github/workflows/kit-tests.yml`, same convention as the Stripe/GitHub/
      Slack/Shopify/idempotency kit jobs.
- [x] Buyer bundle built via allow-list `package.sh` (kit pattern: fixed mtimes,
      sorted entries, `zip -X`; excludes `INTAKE.md`, `package.sh`, `dist/`),
      **byte-reproducible** — unconditional double rebuild 2026-07-18 produced the
      identical sha256, committed dist IS that build.
- [x] **sha256 `908dc84be5a3e6a5be6ee72123c80cac137f1b2338018e39c6af51ef767ecd45`**
      (35,991 bytes, 13 content files) — also pinned in the click-script's ARTIFACT
      line.
- [x] Checkout/format verified from the artifact itself: clean-dir unzip —
      README + QUICKSTART + GOTCHAS + `.env.example` + harness ×2 + both limiters +
      test suite at top level, `fixtures/` 2 templates + MANIFEST.json +
      PROVENANCE.md; real-secret-shape scan (`sk_live_`/`whsec_`/`AKIA`/private
      key/etc.) **0 hits**; no junk entries in the archive.

## 2. Collision scan

- [x] No in-catalog title collision. Closest shipped products, boundaries
      disclosed: the four webhook kits (**Stripe $29** LIVE, **GitHub/Slack/
      Shopify $29** queued) and the **Idempotency Key Test Kit $29** (queued)
      share the kit SHAPE but a DIFFERENT problem class — the webhook kits verify
      an inbound HMAC signature, the idempotency kit verifies safe-retry dedup,
      and this kit verifies throttling correctness (429 + Retry-After +
      RateLimit-* + reset). Zero shared fixtures or code, fresh PROVENANCE. Honest
      positioning: this is the *server-emitting-429* half of API robustness — the
      natural pair to the idempotency kit's safe-retry half — so the listings
      cross-reference rather than claim each other's scope.
- [x] Same/adjacent buyer audience as the dev-tool catalog (intake's
      concentrated-channel risk, disclosed); narrower still because most API
      gateways/frameworks ship a limiter, so the audience is specifically
      hand-rolled limiters and custom middleware.

## 3. Market / price

- [x] Price **$29 one-time** — set on catalog precedent and recorded identically
      in `INTAKE.md`, the listing copy, the click-script, and here. Precedent: the
      Stripe Webhook Test Kit sells LIVE at exactly $29 for the same product shape
      (stdlib harness + docs-derived fixtures + a correct/naive reference pair +
      byte-reproducible bundle), and the GitHub/Slack/Shopify kits + the
      Idempotency kit are queued at $29. Chain: $15 (kill-rule kit, false-green) <
      $19 (merge-wall, template-packs PWYW) < **$29 this kit** = Stripe $29 (live)
      = GitHub/Slack/Shopify $29 (queued) = Idempotency $29 (queued) < field-manual
      $39 < membership-kit $49. Conservative expectation 0–5 sales / $0–$145
      first-90-day, $0 absent distribution (the intake's own line; validation
      signal ≥1 sale OR ≥50 article reads in 30 days, else ledgered negative; T+7
      funnel checkpoint / T+30 kill deadline armed as a KILL-CHECK here once the
      click is DONE-flipped).

## 4–5. Packaging

- [x] Buyer bundle is the allow-listed `package.sh` output (README + QUICKSTART +
      GOTCHAS + `.env.example` + `rltk.py` + `rltk.js` + `stub_handler.py` +
      `stub_handler_naive.py` + `test_http_realpath.py` + `fixtures/`;
      deliberately excludes the lane-internal `INTAKE.md`, `package.sh`, `dist/`).
      No cover image ships — owner adds one or uses the storefront default.

## 6. Listing copy (drafted in-repo — nothing published)

- [x] [`listing-copy.md`](../../launch/rate-limit-test-kit/listing-copy.md) at
      catalog parity (Title / Short ≤200 chars (188 measured) / Long / Bullets /
      FAQ) and checked claim-by-claim against the extracted bundle: "27 tests" =
      the suite that ran green twice this session; "two docs-derived templates" =
      2 fixtures in the zip; the correct/naive demo claim = executed (correct
      all-pass, naive flagged on 4) both languages; the FAQ + "what it does NOT
      do" section states the honest boundaries (not a webhook kit, not the
      idempotency kit; the RateLimit-* spec is a draft not an RFC; the headers are
      optional; single-bucket scope; fixtures docs-derived not live captures; no
      live API anything); a PROVENANCE-FOOTER pins `file@sha` sources; refund/
      license lines present, marked owner-to-set.

## 7. ⚑ OWNER-GATE — publish clicks (queued, never automated)

Seat output = this queued OWNER-ACTION block; the seat performed **none** of it.
It is the queue-parseable form of the click-script in `owner-actions.md` (same
directory as this packet's launch assets) — the HOW detail lives there; no freeze
applies (no payment-path gate).

**OWNER-ACTION — Publish "Rate-Limit Test Kit" at $29 one-time**
1. **Storefront account:** owner signs into the storefront (the Stripe kit Gumroad
   account already exists and has payout configured).
2. **⚑ Storefront pick:** **Gumroad** (default — same account as the live Stripe
   kit listing; the click-script's HOW is written against it) or Lemon Squeezy —
   owner's call; either works with the same zip + copy.
3. **Product:** New product → Digital product; Name = "Rate-Limit Test Kit";
   upload `candidates/rate-limit-test-kit/dist/rate-limit-test-kit-v0.1.zip` and
   verify the upload matches sha256 `908dc84b…767ecd45` (full hash in §1 and the
   click-script ARTIFACT line — never upload a stale local copy).
4. **Copy:** paste Title / Short + Long description / Bullets / FAQ from the
   `listing-copy.md` in this product's launch dir; set the refund/license lines
   the copy marks owner-to-set.
5. **Price:** set **$29 one-time** (fixed — catalog precedent; the Stripe kit is
   live at the identical price for the identical product shape, GitHub/Slack/
   Shopify + Idempotency queued at $29).
6. **Publish + record:** publish, copy the public product URL, storefront preview/
   test purchase to confirm the zip delivers. Optional same-visit cross-sell: one
   line on the Idempotency kit and webhook kit listings pointing here (first-ten
   path channel 2).

- [ ] ⚑ **Owner:** storefront pick (**Gumroad** (default)) — or Lemon Squeezy.
- [ ] ⚑ **Owner:** zip uploaded + sha256 spot-check against §1.
- [ ] ⚑ **Owner:** listing copy pasted + refund/license lines set.
- [ ] ⚑ **Owner:** price set (**$29 one-time** (default per catalog precedent + the live Stripe kit price)).
- [ ] ⚑ **Owner:** the publish click + preview/test purchase + public URL copied.
- [ ] Seat (post-click, no money moved): record the launch durably on `main` —
      verified listing URL, price, timestamp — in the style of the Stripe kit
      `LAUNCH-LOG.md`, flip these rows to the `— DONE <date>` disposition, arm the
      intake's kill clock as a `KILL-CHECK:` line here (T+7 funnel checkpoint ·
      T+30 kill-rule deadline: ≥1 sale OR ≥50 article reads, else ledger NEGATIVE +
      pause/delist), and regenerate the owner queue.

---

**Verdict: publish-ready up to the owner gate.** Built + priced + listing drafted +
checkout/format verified + sha recorded (all evidenced above); the product parks at
§7 (owner clicks) by design. Honest caveats: the `RateLimit-*` header fields the
`headers` property checks come from an IETF DRAFT (not an RFC) and its newest
revisions favour a combined structured field this kit does not assert — the stable
half it asserts is the 429 + Retry-After (RFC 6585 / RFC 9110); the RateLimit-*
headers are optional (an endpoint emitting none passes with a note); the fixtures
are docs-derived request templates, NOT captures from a live API (no account/key/
service call — this repo's no-accounts rule); the kit tests a single caller-bucket,
not per-user/per-IP fairness or distributed-limiter consistency; `under-limit` and
`window-reset` honestly do NOT distinguish a correct limiter from the naive one
(both pass them), documented; the free-substitute risk is real (the RFCs are free;
the paid delta is the harness testing the buyer's OWN endpoint — including the
boundary and reset a from-memory test skips — + the correct/naive reference pair +
provenance discipline); most gateways/frameworks ship a limiter, narrowing the
audience to hand-rolled ones; same concentrated dev-tool channel where the Stripe
kit has 0 organic sales — expect ~$0 absent distribution; and a live purchase
remains unverified until the owner's own test purchase.
