# The False-Green Test Trap — v0.1

Your webhook tests pass and production still drops the order. This guide
teaches the one discipline that catches it: **never test against payloads
you wrote from memory — vendor real provider payloads, with written
provenance, and assert on the real path over HTTP.**

It is built from a documented incident: a shipped kit with thirteen green
webhook tests whose first real Stripe purchase would have failed silently,
because real `checkout.session.completed` events carry
`customer_email: null` and every memory-authored test payload said
otherwise. Every claim in this guide traces to committed material in the
public repo that lived it (`menno420/venture-lab`) — each chapter ends with
a provenance footer citing file @ commit. No invented case studies.

## What's inside

- **`guide/`** — seven chapters: the war story (1), why green tests lie
  (2), vendoring fixtures (3), the PROVENANCE.md pattern (4), HTTP-layer
  real-path tests (5), a copy-paste pre-merge checklist (6), and the
  bundled tool (7).
- **`vendor_fixture.py`** — a single-file, stdlib-only, offline tool:
  paste a provider sample payload, get a validated fixture plus a
  provenance stub with every null field enumerated, volatile fields
  flagged, secrets refused fail-closed, optional email redaction.
- **`test_vendor_fixture.py`** — 8 unittest cases holding the tool to the
  guide's own bar.
- **`examples/`** — a real-shape `checkout.session.completed` sample (SDK
  source-verified provenance) so the worked run reproduces on your machine
  in under a minute.

## Requirements

Python 3.8+ standard library. No dependencies, no network access, no
accounts — the tool is offline by design and fetches nothing.

## Quick start

See `QUICKSTART.md`. Shortest path:

```
python3 vendor_fixture.py examples/checkout_session_completed.sample.json \
        --name checkout_session_completed --out fixtures
python3 -m unittest test_vendor_fixture -v
```

## Honesty box

- This is a methodology guide + a small tool, not a test framework. The
  chapters are compact (~3,600 words — about 8 pages of prose); the
  density is the point.
- The war story, fixtures, and test patterns are Stripe-flavored because
  that is the incident that actually happened; chapters 2–6 are written
  provider-agnostic and apply to any JSON webhook (GitHub, payment
  providers, CI systems).
- The tool validates, flags, and stubs — it cannot verify where your
  sample came from. That homework stays yours, on purpose.
- Want the Stripe-specific done-for-you version (signed-event firing,
  forged/stale probes, ready fixtures)? That is the same lane's separate
  $29 Stripe Webhook Test Kit; this guide stands alone without it.
