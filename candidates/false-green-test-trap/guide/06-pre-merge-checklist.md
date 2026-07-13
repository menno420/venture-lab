# 6 · The pre-merge checklist

Copy this into your PR template or CONTRIBUTING.md. It is one page on
purpose: the trap survives on "we'll harden the tests later." Every line
below traces to a defect class the war-story incident actually contained or
to the committed discipline that fixed it.

## Before an integration/webhook PR merges

**Fixtures**

- [ ] Every payload the tests use is **vendored** — copied from provider
      tooling, a dashboard event log, documented samples, or verified
      against SDK/OpenAPI source. Zero payloads typed from memory.
- [ ] Fixtures keep the **complete envelope** (wrapper, `data.object`,
      `api_version`, `request`) — nothing hand-trimmed.
- [ ] The **nulls are present and asserted**: at least one fixture carries
      the field-is-null shape live traffic sends (for Stripe Checkout:
      `customer_email: null` + populated `customer_details.email`), and a
      test asserts the null explicitly.
- [ ] Alternate shapes are covered (legacy/guest variants, second event
      types your handler routes on).
- [ ] No real secrets, no real customer data in any fixture; email-shaped
      values are `example.com`-style placeholders.

**Provenance**

- [ ] `PROVENANCE.md` sits next to the fixtures: source of each payload,
      date, field-name verification with URLs, verified-vs-illustrative
      split, and the auth scheme's byte-level spec if you test signatures.
- [ ] Any source you could NOT reach is named, with the substitute used.

**The real path**

- [ ] At least one test POSTs the fixture's **raw bytes over actual HTTP**
      to the handler on an ephemeral port — no in-process shortcut, no
      framework test client standing in for the wire.
- [ ] Signatures are computed over the exact fixture bytes with the
      provider's real scheme; a **forged** signature and a **stale**
      timestamp are both tested to be rejected.
- [ ] The happy-path test asserts the handler's *output* used the correct
      field (e.g. resolved email == the `customer_details.email` value) —
      not just a 200.
- [ ] Placeholders/formats your code emits (success URLs, redirect
      templates) are linted against the provider's actually-supported set.

**The meta-check**

- [ ] Ask of every green test: *"could this test have passed if my belief
      about the provider were wrong?"* If yes, it is decoration, not
      evidence. The suite must contain at least one artifact your memory
      did not produce.

## The one-sentence version

**A green suite proves your code matches your model; only a vendored
payload on the real path proves your model matches the provider.**

---

*Provenance of this chapter: distilled from the defect list and fix
requirements of the remediation order (`control/inbox.md` ORDER 003 @
`c99caa4`), the committed suites' assertion sets
(`candidates/stripe-webhook-test-kit/test_http_realpath.py` @ `dfe3332`,
`candidates/membership-kit/server/test_http_realpath.py` @ `dfe3332`), the
committed provenance files (both `fixtures/PROVENANCE.md` @ `dfe3332`), and
the standing floor rule in `docs/products/TEMPLATE.md` @ `53f6b65`. The
lane also applies the same bar to its own status claims — "verified every
claim against GitHub before writing" (`.sessions/2026-07-12-heartbeat-2026-07-12b.md`
@ `d7896f0`): executed evidence over remembered belief, everywhere.*
