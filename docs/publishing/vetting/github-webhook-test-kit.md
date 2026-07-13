# Title Vetting — GitHub Webhook Test Kit

> **Status:** `plan`
>
> Tenth PRODUCT packet in the vetting directory, so the publish click rides
> the derived owner queue (`../OWNER-QUEUE.md` via
> `scripts/derive_owner_queue.py`). BUILD #1 (3.60) of the 2026-07-13
> ideation batch (`docs/products/ideas-2026-07-13.md` §1, PR #142), built
> under ORDER 008's products clause. No freeze applies — a dev-tool kit
> with no payment-path dependency (the ORDER 003 ⚑B/⚑D freeze, lifted
> 2026-07-11 by PR #22, never attached to it). Every step marked
> **⚑ OWNER-GATE** is an owner click, never automated.

**Title:** GitHub Webhook Test Kit · **Category:** digital product / dev
tool · **Date vetted:** 2026-07-13

Product: [`candidates/github-webhook-test-kit/`](../../../candidates/github-webhook-test-kit/README.md)
(v0.1; buyer bundle `dist/github-webhook-test-kit-v0.1.zip`; launch assets
in [`docs/launch/github-webhook-test-kit/`](../../launch/github-webhook-test-kit/owner-actions.md);
intake [`INTAKE.md`](../../../candidates/github-webhook-test-kit/INTAKE.md),
scored 3.60 at ideation).

## 1. Built (verified this session, 2026-07-13)

- [x] Stdlib-only harness in two languages (`gwtk.py` + `gwtk.js` Node
      port, same four commands), correct example handler
      (`stub_handler.py`: constant-time sha256 verify, fail-closed on
      missing/SHA-1-only signatures, raw-form-body support, ping handling,
      delivery-GUID dedupe), one-page `GOTCHAS.md` (6 failure modes, each
      mapped to a kit command).
- [x] **Fixtures vendored, never synthesized:** all 5 payloads (`ping`,
      `push`, `pull_request` opened, `issue_comment` created, `check_run`
      completed) vendored **byte-for-byte** from `octokit/webhooks @ main`
      (GitHub's own machine-readable example set, MIT), fetched
      2026-07-13; per-file sha256 pinned in
      [`fixtures/PROVENANCE.md`](../../../candidates/github-webhook-test-kit/fixtures/PROVENANCE.md),
      which also cites every signature/header/content-type fact to the
      `github/docs @ main` source files behind docs.github.com.
- [x] **HMAC proven against GitHub's OWN published test vector:** the
      `vector` command (both ports) recomputes the documented known-answer
      test (secret `It's a Secret to Everybody`, payload `Hello, World!`)
      and matches GitHub's published `sha256=757107ea…` constant — executed
      PASS in Python and Node this session.
- [x] **Tests (real-path, executed 2026-07-13):** 18-test HTTP-layer suite
      — every delivery signed with the real scheme and POSTed over actual
      HTTP to a handler on an ephemeral port. Green from source (`Ran 18
      tests in 4.552s / OK`, 09:44:21Z) AND from the extracted zip in a
      clean dir (`Ran 18 tests in 4.547s / OK`, 09:48:06Z). Covers: the
      official vector; all 5 fixture shapes (incl. the no-`action` reality
      of push/ping and the cross-event action collision); valid deliveries
      accepted for ALL fixtures; forged/unsigned/SHA-1-only rejected;
      the kit flagging an insecure handler; form-encoded raw-body signing
      accepted AND the sign-the-inner-JSON bug rejected; replay with the
      same GUID flagged duplicate. All fire modes additionally exercised
      live against the stub (fire / forge / unsigned / sha1-only / form /
      replay, both ports — all PASS, captured in the session card).
- [x] Suite wired into CI: `github-webhook-test-kit-tests` job added to
      `.github/workflows/kit-tests.yml`, same convention as the SWTK job.
- [x] Buyer bundle built via allow-list `package.sh` (SWTK pattern: fixed
      mtimes, sorted entries, `zip -X`; excludes INTAKE.md, package.sh,
      dist/), **byte-reproducible** — unconditional double rebuild
      2026-07-13T09:47:54Z, identical sha256, committed dist IS that build.
- [x] **sha256 `e17b08bac25b047942281c00eb0047ae592d6bda790284aade7b6cf58dcbf6a9`**
      (36,214 bytes, 13 content files) — also pinned in the click-script's
      ARTIFACT line.
- [x] Checkout/format verified from the artifact itself: clean-dir unzip —
      README + GOTCHAS + harness ×2 + stub + test suite at top level,
      fixtures/ 5 payloads + EVENTS.json + PROVENANCE.md (13/13 vs the
      listing's "What's inside"); real-secret-shape scan (ghp_/gho_/
      github_pat_/sk_live_/sk_test_/whsec_/AKIA/private-key/xox/AIza)
      **0 hits** — the only secret-LIKE strings are GitHub's public
      documentation test-vector values and clearly-fake test secrets,
      labeled as such in the files; no junk entries in the archive.

## 2. Collision scan

- [x] No in-catalog title collision. Closest shipped products, boundaries
      disclosed: **SWTK $29** (same product shape, DIFFERENT ecosystem —
      Stripe payments vs GitHub webhooks; zero shared fixtures or code,
      fresh PROVENANCE; the listing cross-references rather than claims
      each other's scope) and the **False-Green Test Trap $15** (teaches
      the vendored-fixture discipline as a guide; this kit is a runnable
      tool). The ideation batch's own Webhook Fixture Vault concept was
      KILLED for cannibalizing exactly this boundary — that verdict stands.
- [x] Same buyer audience as the dev-tool catalog (intake's concentrated-
      channel risk, disclosed): distribution scored 3/5 at ideation.

## 3. Market / price

- [x] Price **$29 one-time** — set at ideation
      (`docs/products/ideas-2026-07-13.md` §1) and recorded identically in
      `INTAKE.md`, the listing copy, the click-script, and here.
      Precedent: SWTK sells LIVE at exactly $29 for the same product shape
      (harness + vendored fixtures + hostile modes) in the sibling
      ecosystem. Chain: $15 (kill-rule kit, false-green) < $19
      (merge-wall, template-packs PWYW) < **$29 this kit** = SWTK $29
      (live, PR #86) < field-manual $39 < membership-kit $49.
      Conservative expectation stays 0–5 sales / $0–$145 first-90-day, $0
      absent distribution (the intake's own line; validation signal ≥1
      sale OR ≥50 article reads in 30 days, else ledgered negative;
      T+7 funnel checkpoint / T+30 kill deadline armed as a KILL-CHECK
      here once the click is DONE-flipped).

## 4–5. Packaging

- [x] Buyer bundle is the allow-listed `package.sh` output (README +
      GOTCHAS + `gwtk.py` + `gwtk.js` + `stub_handler.py` +
      `test_http_realpath.py` + `fixtures/`; deliberately excludes the
      lane-internal INTAKE.md, package.sh, dist/). No cover image ships —
      owner adds one or uses the storefront default.

## 6. Listing copy (drafted in-repo — nothing published)

- [x] [`listing-copy.md`](../../launch/github-webhook-test-kit/listing-copy.md)
      at catalog parity (Title / Short ≤200 chars (183 measured) / Long /
      Bullets / FAQ) and checked claim-by-claim against the extracted
      bundle: "18 tests" = the suite that ran green twice this session;
      "five vendored payloads" = 5 fixtures in the zip; the vector claim =
      executed PASS both ports; the FAQ + "what it does NOT do" section
      states the honest boundaries (fixtures are documented examples, not
      live captures; no live GitHub anything; not a `gh webhook forward`
      substitute); refund/license lines present, marked owner-to-set.

## 7. ⚑ OWNER-GATE — publish clicks (queued, never automated)

Seat output = this queued OWNER-ACTION block; the seat performed **none**
of it. It is the queue-parseable form of the click-script in
[`owner-actions.md`](../../launch/github-webhook-test-kit/owner-actions.md) —
the HOW detail lives there; no freeze applies (no payment-path gate).

**OWNER-ACTION — Publish "GitHub Webhook Test Kit" at $29 one-time**
1. **Storefront account:** owner signs into the storefront (the SWTK
   Gumroad account already exists and has payout configured).
2. **⚑ Storefront pick:** **Gumroad** (default — same account as the live
   SWTK listing; the click-script's HOW is written against it) or Lemon
   Squeezy — owner's call; either works with the same zip + copy.
3. **Product:** New product → Digital product; Name = "GitHub Webhook
   Test Kit"; upload
   `candidates/github-webhook-test-kit/dist/github-webhook-test-kit-v0.1.zip`
   and verify the upload matches sha256 `e17b08ba…8dcbf6a9` (full hash in
   §1 and the click-script ARTIFACT line — never upload a stale local
   copy).
4. **Copy:** paste Title / Short + Long description / Bullets / FAQ from
   [`listing-copy.md`](../../launch/github-webhook-test-kit/listing-copy.md);
   set the refund/license lines the copy marks owner-to-set.
5. **Price:** set **$29 one-time** (fixed — set at ideation; SWTK live
   precedent at the identical price for the identical product shape).
6. **Publish + record:** publish, copy the public product URL, storefront
   preview/test purchase to confirm the zip delivers. Optional same-visit
   cross-sell: one line on the live SWTK listing pointing here
   (first-ten path channel 2).

- [ ] ⚑ **Owner:** storefront pick (**Gumroad** (default)) — or Lemon Squeezy.
- [ ] ⚑ **Owner:** zip uploaded + sha256 spot-check against §1.
- [ ] ⚑ **Owner:** listing copy pasted + refund/license lines set.
- [ ] ⚑ **Owner:** price set (**$29 one-time** (default per ideation + the live SWTK precedent)).
- [ ] ⚑ **Owner:** the publish click + preview/test purchase + public URL copied.
- [ ] Seat (post-click, no money moved): record the launch durably on `main` —
      verified listing URL, price, timestamp — in the style of
      [`docs/launch/stripe-webhook-test-kit/LAUNCH-LOG.md`](../../launch/stripe-webhook-test-kit/LAUNCH-LOG.md),
      flip these rows to the `— DONE <date>` disposition, arm the intake's
      kill clock as a `KILL-CHECK:` line here (T+7 funnel checkpoint ·
      T+30 kill-rule deadline: ≥1 sale OR ≥50 article reads, else ledger
      NEGATIVE + pause/delist), and regenerate the owner queue.

---

**Verdict: publish-ready up to the owner gate.** Built + priced + listing
drafted + checkout/format verified + sha recorded (all evidenced above);
the product parks at §7 (owner clicks) by design. Honest caveats: the
fixtures are GitHub's documented example payloads vendored byte-for-byte,
NOT captures from a live delivery — no live webhook was created (this
repo's no-accounts rule) and the kit says so in the listing; five event
types ship in v0.1 (a buyer wanting `workflow_run`/`release`/etc. must add
their own payloads — the EVENTS.json mechanism supports it but the listing
doesn't promise them); the free-substitute risk is real (GitHub documents
the verification snippet in six languages; the paid delta is the harness +
hostile modes + provenance discipline); same concentrated dev-tool channel
where SWTK has 0 organic sales as of 2026-07-13 — expect ~$0 absent
distribution; and a live purchase remains unverified until the owner's own
test purchase.
