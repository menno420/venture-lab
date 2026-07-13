# 5 · Assert at the HTTP layer: the real path, not a shortcut

A vendored fixture injected in-process is only half the cure. The other half
is the entry path: your handler must be exercised the way production hits it
— **over actual HTTP, with the fixture's raw bytes, with real auth**. The
lane's rule, from the docstring of the suite that fixed the war story:

> every event is signed with the REAL Stripe-Signature scheme and POSTed
> over actual HTTP to a handler running on an ephemeral port — never a
> payload synthesised from memory, never an in-process shortcut.

## The pattern (Python stdlib; ~15 lines of harness)

Both of the lane's committed suites use the same skeleton — no framework,
no test client shortcut:

1. **Ephemeral real server.** Start your handler in a
   `ThreadingHTTPServer(("127.0.0.1", 0), handler)`; port 0 lets the OS
   pick; register shutdown as cleanup. You now have a real
   `http://127.0.0.1:<port>` that requests traverse byte-for-byte.
2. **Fixtures read as raw bytes.** `read_bytes()`, never
   `json.load` → re-`dumps`. Signatures are computed over exact bytes;
   re-serializing silently changes them and your signature tests test
   nothing.
3. **A fake secret that cannot be real.** e.g.
   `whsec_test_..._not_a_real_secret`, in the test file. Real secrets live
   in env, never in code.

## The assertion set that catches false greens

The committed suites assert four families — each one targets a way a green
suite can lie:

- **Fixture-shape assertions.** Before any HTTP: assert the fixture itself
  carries the trap — `customer_email` **is** None, `customer_details.email`
  is populated; the legacy fixture is the inverse. If someone later
  "cleans up" a fixture from memory, these go red first.
- **Valid path.** Sign the fixture bytes with the real scheme
  (HMAC-SHA256 over `f"{ts}." + body`), POST, expect 200 — and assert the
  handler resolved the buyer email to the `customer_details.email` value,
  proving the read-order fix end to end.
- **Rejection paths.** Forged signature → 400. Stale timestamp (beyond the
  300s tolerance) → 400. A handler that fails these is accepting anyone's
  POSTs.
- **The insecure-handler canary.** The cleverest test in the committed
  suite: run a deliberately signature-blind handler, fire a forged event,
  watch it return 2xx — and assert your verifier *flags that as a failure*.
  It tests that your test harness can actually detect the vulnerability it
  exists to catch: a guard against false greens in the guard itself.

Cover both fixture shapes on the happy path (null-email and legacy), and
finish with format lints where placeholders can be plausible-but-wrong —
the committed suite rejects `{CHECKOUT_EMAIL}` and accepts
`{CHECKOUT_SESSION_ID}` for exactly the chapter-1 reason.

## Why HTTP and not the framework test client

The war-story codebase had thirteen green tests and **zero** at the HTTP
layer. Framework test clients and direct function calls skip raw-body
handling, header parsing, content-length behavior, and byte-exact signature
verification — four places real webhooks break. An ephemeral-port server
costs three lines over the shortcut and executes all of them.

---

*Provenance of this chapter: the quoted discipline docstring, the
ephemeral-port/raw-bytes/fake-secret harness, and all four assertion
families are committed at
`candidates/stripe-webhook-test-kit/test_http_realpath.py` @ `dfe3332`
(14 tests, incl. the insecure-handler canary and both lint cases) and
`candidates/membership-kit/server/test_http_realpath.py` @ `dfe3332` (the
production-shaped variant; 9 tests re-verified green 2026-07-13 per
`.sessions/2026-07-13-order-003-stripe-path.md` @ `d058c4d`); the
zero-HTTP-layer-tests fact — `control/inbox.md` (ORDER 003) @ `c99caa4`.*
