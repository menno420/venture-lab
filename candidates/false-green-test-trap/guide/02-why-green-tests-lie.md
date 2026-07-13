# 2 · Why green tests lie: the false-green mechanism

The false-green test trap is not a testing-skill problem. The thirteen green
tests in chapter 1 were competently written: they set up the handler, posted
events, asserted on grants. The trap is structural:

**A test you author from memory encodes the same beliefs as the code it
tests. Shared beliefs cannot disagree, so shared wrong beliefs go green.**

Walk the mechanism:

1. You read the provider's docs (or remember reading them) and form a mental
   model: "the event carries `customer_email`."
2. You write the handler against that model.
3. You write the test against that model — you synthesize the event payload
   from the same memory.
4. The test passes, because handler and payload were minted from one belief.
5. Production sends what the provider *actually* sends. If your belief was
   wrong anywhere — a field that is null in live traffic, a name that
   differs, a nesting you flattened — the code fails **with a green suite
   behind it**.

Notice what the green suite is actually evidence of: *internal consistency*.
It proves your code implements your model. It proves nothing about whether
your model matches the provider. Those are different claims, and only the
second one pays out when a real buyer checks out.

## Where the trap bites hardest

- **Nullable fields.** Docs and examples show fields populated; live traffic
  has them null. `customer_email: null` is the canonical case — a normal
  Checkout completion nulls the top-level field and puts the address in
  `customer_details.email`. Handwritten payloads almost never contain the
  nulls, because nobody types a field to set it to null.
- **Envelope vs object.** Providers wrap the resource in an event envelope
  (`data.object`, `api_version`, `request`, …). Memory-authored fixtures
  routinely flatten or trim the envelope, so parsing bugs at the wrapper
  layer never execute in tests.
- **In-process shortcuts.** Calling the handler function directly skips the
  HTTP layer — raw-body reading, content-length, header casing, signature
  verification over exact bytes. Bugs there don't run at all under
  synthetic injection (the membership kit had **zero** HTTP-layer tests
  when the trap fired).
- **Placeholders and formats.** `{CHECKOUT_EMAIL}` looked plausible; only
  `{CHECKOUT_SESSION_ID}` exists. Plausible-from-memory is exactly the
  material false greens are made of.

## The general rule

The lane distilled it into its product template as a standing floor rule,
which this guide adopts as its thesis:

> Green synthetic tests cannot catch a wrong belief about what the real
> service sends.

The escape is to introduce an artifact your memory did not produce: a
**vendored** payload, copied from the provider's own sources, with written
provenance — and to run it through the **real** entry path, over HTTP. The
next three chapters are those two moves, in order.

---

*Provenance of this chapter: the standing floor rule quoted above —
`docs/products/TEMPLATE.md` @ `53f6b65` (stage 3, "the 13 green tests
trap"); the zero-HTTP-layer-tests fact and the null/placeholder specifics —
`control/inbox.md` (ORDER 003) @ `c99caa4`; the null-email real shape —
`candidates/stripe-webhook-test-kit/fixtures/PROVENANCE.md` @ `dfe3332`.*
