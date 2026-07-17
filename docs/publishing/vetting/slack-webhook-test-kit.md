# Title Vetting — Slack Webhook Test Kit

> **Status:** `plan`
>
> New PRODUCT packet in the vetting directory, so the publish click rides the
> derived owner queue (`../OWNER-QUEUE.md` via
> `scripts/derive_owner_queue.py`). Built under **ORDER 016** (live owner
> overnight-work order, 2026-07-17T22:39Z) as the N+1 of the LIVE Stripe
> Webhook Test Kit and the built GitHub Webhook Test Kit — same proven
> template, fresh Slack-specific checks. No freeze applies — a dev-tool kit
> with no payment-path dependency (the ORDER 003 ⚑B/⚑D freeze, lifted
> 2026-07-11 by PR #22, never attached to it). Every step marked
> **⚑ OWNER-GATE** is an owner click, never automated.

**Title:** Slack Webhook Test Kit · **Category:** digital product / dev tool ·
**Date vetted:** 2026-07-17

Product: [`candidates/slack-webhook-test-kit/`](../../../candidates/slack-webhook-test-kit/README.md)
(v0.1; buyer bundle `dist/slack-webhook-test-kit-v0.1.zip`; launch assets in
[`docs/launch/slack-webhook-test-kit/`](../../launch/slack-webhook-test-kit/owner-actions.md);
intake [`INTAKE.md`](../../../candidates/slack-webhook-test-kit/INTAKE.md),
priced $29 on catalog precedent).

## 1. Built (verified this session, 2026-07-17)

- [x] Stdlib-only harness in two languages (`swtk.py` + `swtk.js` Node port,
      same four commands), correct example handler (`stub_handler.py`:
      timestamp-window check FIRST, constant-time `v0=` HMAC-SHA256 verify,
      fail-closed on missing signature/timestamp, raw-body form support,
      `url_verification` challenge echo, `event_id` returned for dedupe),
      one-page `GOTCHAS.md` (6 failure modes, each mapped to a kit command),
      plus `QUICKSTART.md` and a placeholders-only `.env.example`.
- [x] **Fixtures reconstructed from Slack's docs, honestly labeled:** four
      real-shape request bodies — `url_verification` (JSON challenge),
      `event_callback` / `app_mention` (JSON), a slash command (flat
      form-urlencoded), and a `block_actions` interactivity payload
      (`payload=<json>` form-urlencoded); per-file sha256 pinned in
      [`fixtures/PROVENANCE.md`](../../../candidates/slack-webhook-test-kit/fixtures/PROVENANCE.md),
      which states up front they are reconstructed from Slack's published
      example shapes (NOT wire-captured — no Slack app or workspace was
      created) and cites the signing algorithm, the 300s replay window, and
      each payload type to the Slack docs page it came from.
- [x] **HMAC proven against Slack's OWN published worked example:** the
      `vector` command (both ports) recomputes Slack's documented known-answer
      example (signing secret `8f742231…`, timestamp `1531420618`, the
      documented slash-command body) and matches Slack's published
      `v0=a2114d57…` constant — executed PASS in Python and Node this session.
      The vendored `slash_command.txt` fixture IS that worked-example body.
- [x] **Tests (real-path, executed 2026-07-17):** 18-test HTTP-layer suite —
      every request signed with the real `v0` scheme and POSTed over actual
      HTTP to a handler on an ephemeral port. Green from source (`Ran 18 tests
      / OK`) AND from the extracted zip in a clean dir (`Ran 18 tests / OK`).
      Covers: the official vector; all 4 fixture shapes; valid requests
      accepted for ALL fixtures; the `url_verification` challenge echoed
      verbatim; slash-command + interactivity parsed; forged / unsigned /
      stale-timestamp / tampered-body rejected (4xx); the kit flagging an
      insecure handler (accepts forged AND accepts a stale replay). All fire
      modes additionally exercised live against the stub (fire / forge /
      unsigned / stale / tamper / check-challenge, both ports — all PASS,
      captured in the session card).
- [x] Suite wired into CI: `slack-webhook-test-kit-tests` job added to
      `.github/workflows/kit-tests.yml`, same convention as the SWTK/GWTK jobs.
- [x] Buyer bundle built via allow-list `package.sh` (SWTK pattern: fixed
      mtimes, sorted entries, `zip -X`; excludes INTAKE.md, package.sh,
      dist/), **byte-reproducible** — unconditional double rebuild 2026-07-17
      produced the identical sha256, committed dist IS that build.
- [x] **sha256 `9ea865735de0402a534f872f816c8cc1eea68fcecfb114b3a1499114abd755e8`**
      (29,290 bytes, 14 content files) — also pinned in the click-script's
      ARTIFACT line.
- [x] Checkout/format verified from the artifact itself: clean-dir unzip —
      README + QUICKSTART + GOTCHAS + .env.example + harness ×2 + stub + test
      suite at top level, fixtures/ 4 payloads + MANIFEST.json + PROVENANCE.md;
      real-secret-shape scan (xoxb-/xoxp-/xapp-/sk_live_/whsec_/AKIA/
      private-key) **0 hits** — the only secret-LIKE strings are Slack's public
      documentation worked-example values, clearly-fake test secrets labeled as
      such, and a `.env.example` line naming token prefixes NOT to use; no junk
      entries in the archive.

## 2. Collision scan

- [x] No in-catalog title collision. Closest shipped products, boundaries
      disclosed: **SWTK $29** (LIVE) and **GWTK $29** (queued) — same product
      shape, DIFFERENT ecosystem (Stripe payments / GitHub webhooks / Slack
      request-signing; zero shared fixtures or code, fresh PROVENANCE; the
      listings cross-reference rather than claim each other's scope). The
      Slack signing scheme is genuinely distinct: a timestamp that is BOTH
      signed AND independently range-checked (unlike GitHub's timestamp-free
      scheme, and signed differently from Stripe's `t=,v1=`).
- [x] Same buyer audience as the dev-tool catalog (intake's concentrated-
      channel risk, disclosed); narrower still because Slack's official Bolt
      SDK verifies signatures for you, so the audience is specifically
      non-Bolt / custom-stack integrators.

## 3. Market / price

- [x] Price **$29 one-time** — set on catalog precedent and recorded
      identically in `INTAKE.md`, the listing copy, the click-script, and here.
      Precedent: SWTK sells LIVE at exactly $29 for the same product shape
      (harness + real-shape fixtures + hostile modes) and GWTK is queued at
      $29 in the sibling ecosystem. Chain: $15 (kill-rule kit, false-green) <
      $19 (merge-wall, template-packs PWYW) < **$29 this kit** = SWTK $29
      (live) = GWTK $29 (queued) < field-manual $39 < membership-kit $49.
      Conservative expectation stays 0–5 sales / $0–$145 first-90-day, $0
      absent distribution (the intake's own line; validation signal ≥1 sale OR
      ≥50 article reads in 30 days, else ledgered negative; T+7 funnel
      checkpoint / T+30 kill deadline armed as a KILL-CHECK here once the click
      is DONE-flipped).

## 4–5. Packaging

- [x] Buyer bundle is the allow-listed `package.sh` output (README +
      QUICKSTART + GOTCHAS + .env.example + `swtk.py` + `swtk.js` +
      `stub_handler.py` + `test_http_realpath.py` + `fixtures/`; deliberately
      excludes the lane-internal INTAKE.md, package.sh, dist/). No cover image
      ships — owner adds one or uses the storefront default.

## 6. Listing copy (drafted in-repo — nothing published)

- [x] [`listing-copy.md`](../../launch/slack-webhook-test-kit/listing-copy.md)
      at catalog parity (Title / Short ≤200 chars (188 measured) / Long /
      Bullets / FAQ) and checked claim-by-claim against the extracted bundle:
      "18 tests" = the suite that ran green twice this session; "four
      real-shape fixtures" = 4 fixtures in the zip; the vector claim = executed
      PASS both ports; the FAQ + "what it does NOT do" section states the
      honest boundaries (fixtures reconstructed from docs, not live captures;
      no live Slack anything; not a Bolt/Socket-Mode/request-URL-tester
      substitute); a PROVENANCE-FOOTER pins `file@sha` sources; refund/license
      lines present, marked owner-to-set.

## 7. ⚑ OWNER-GATE — publish clicks (queued, never automated)

Seat output = this queued OWNER-ACTION block; the seat performed **none** of
it. It is the queue-parseable form of the click-script in
[`owner-actions.md`](../../launch/slack-webhook-test-kit/owner-actions.md) —
the HOW detail lives there; no freeze applies (no payment-path gate).

**OWNER-ACTION — Publish "Slack Webhook Test Kit" at $29 one-time**
1. **Storefront account:** owner signs into the storefront (the SWTK Gumroad
   account already exists and has payout configured).
2. **⚑ Storefront pick:** **Gumroad** (default — same account as the live SWTK
   listing; the click-script's HOW is written against it) or Lemon Squeezy —
   owner's call; either works with the same zip + copy.
3. **Product:** New product → Digital product; Name = "Slack Webhook Test
   Kit"; upload
   `candidates/slack-webhook-test-kit/dist/slack-webhook-test-kit-v0.1.zip`
   and verify the upload matches sha256 `9ea86573…abd755e8` (full hash in §1
   and the click-script ARTIFACT line — never upload a stale local copy).
4. **Copy:** paste Title / Short + Long description / Bullets / FAQ from
   [`listing-copy.md`](../../launch/slack-webhook-test-kit/listing-copy.md);
   set the refund/license lines the copy marks owner-to-set.
5. **Price:** set **$29 one-time** (fixed — catalog precedent; SWTK live at
   the identical price for the identical product shape, GWTK queued at $29).
6. **Publish + record:** publish, copy the public product URL, storefront
   preview/test purchase to confirm the zip delivers. Optional same-visit
   cross-sell: one line on the live SWTK listing (and the GWTK listing)
   pointing here (first-ten path channel 2).

- [ ] ⚑ **Owner:** storefront pick (**Gumroad** (default)) — or Lemon Squeezy.
- [ ] ⚑ **Owner:** zip uploaded + sha256 spot-check against §1.
- [ ] ⚑ **Owner:** listing copy pasted + refund/license lines set.
- [ ] ⚑ **Owner:** price set (**$29 one-time** (default per catalog precedent + the live SWTK price)).
- [ ] ⚑ **Owner:** the publish click + preview/test purchase + public URL copied.
- [ ] Seat (post-click, no money moved): record the launch durably on `main` —
      verified listing URL, price, timestamp — in the style of
      [`docs/launch/stripe-webhook-test-kit/LAUNCH-LOG.md`](../../launch/stripe-webhook-test-kit/LAUNCH-LOG.md),
      flip these rows to the `— DONE <date>` disposition, arm the intake's kill
      clock as a `KILL-CHECK:` line here (T+7 funnel checkpoint · T+30
      kill-rule deadline: ≥1 sale OR ≥50 article reads, else ledger NEGATIVE +
      pause/delist), and regenerate the owner queue.

---

**Verdict: publish-ready up to the owner gate.** Built + priced + listing
drafted + checkout/format verified + sha recorded (all evidenced above); the
product parks at §7 (owner clicks) by design. Honest caveats: the fixtures are
reconstructed from Slack's published example shapes, NOT captures from a live
workspace — no live Slack app was created (this repo's no-accounts rule) and
the kit says so in the listing and PROVENANCE; four request shapes ship in
v0.1 (a buyer wanting other event types adds their own — the MANIFEST.json
mechanism supports it but the listing doesn't promise them); the
free-substitute risk is real (Slack documents the verification with a full
worked example; the paid delta is the harness + hostile modes — especially the
stale-timestamp replay check — + the challenge test + provenance discipline);
Slack's official Bolt SDK verifies signatures for you, narrowing the audience
to non-Bolt integrators; same concentrated dev-tool channel where SWTK has 0
organic sales — expect ~$0 absent distribution; and a live purchase remains
unverified until the owner's own test purchase.
