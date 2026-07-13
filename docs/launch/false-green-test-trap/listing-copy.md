# The False-Green Test Trap — listing copy

> **Status:** `reference`

Ready-to-paste copy for a Gumroad / Lemon Squeezy digital-product page.

## Title
```
The False-Green Test Trap — why your webhook tests pass and production still drops the order
```

## Short description (≤ 200 chars)
```
Your webhook suite is green and your first real sale still fails. A documented-incident guide + offline fixture-vendoring tool: test real provider payloads, with provenance, on the real HTTP path.
```

## Long description
```
A shipped product had thirteen green webhook tests — and its first real Stripe purchase would have failed silently, because real checkout.session.completed events carry customer_email: null and every test payload, written from memory, said otherwise. The suite was green. The order would have been dropped. Nothing would have errored.

This guide is that incident, turned into a discipline you can apply to any JSON webhook or integration (Stripe, GitHub, payment and CI providers): seven compact chapters (~3,600 words — about 8 pages, dense on purpose) covering the war story with the actual two-line fix, the structural reason memory-authored tests cannot catch wrong beliefs, a source hierarchy for vendoring real payloads, the PROVENANCE.md pattern that keeps fixtures honest, HTTP-layer real-path testing (ephemeral port, raw bytes, forged and stale signature rejection, the insecure-handler canary), and a one-page pre-merge checklist.

Plus a tool: vendor_fixture.py — single-file, Python stdlib only, fully offline. Paste your provider's sample payload; it validates the JSON, enumerates every null field (nulls are where false greens hide), flags volatile fields, refuses secret-looking material fail-closed, optionally redacts real email addresses, and writes the fixture plus a PROVENANCE.md stub with the verification homework laid out as fill-in slots. Ships with its own 8-test suite and a real-shape sample payload so the worked run reproduces on your machine in under a minute.

Every claim traces to committed material in the public repo that lived the incident — each chapter ends with a provenance footer citing file @ commit. No invented case studies, no composite war stories.
```

## Bullets
```
- The real incident: 13 green tests, customer_email: null, a sale silently dropped — with the committed two-line fix
- Provider-agnostic method: vendor real payloads, keep the nulls, test the complete envelope
- PROVENANCE.md pattern from two shipped kits: source URLs, field-name verification, verified-vs-illustrative
- HTTP-layer real-path testing: ephemeral port, raw bytes, forged + stale rejection, insecure-handler canary
- One-page pre-merge checklist, copy-paste ready for your PR template
- vendor_fixture.py: stdlib-only, offline, fail-closed on secrets, nulls enumerated, optional email redaction
- 8-test suite for the tool + a real-shape sample payload for an instant worked run
- Every chapter cites its committed sources (file @ commit) in a public repo — auditably no invented stories
```

## FAQ
```
Q: Is the war story real?
A: Yes, and auditably so. The incident, the remediation order, the fix PR, and the test suites that came out of it are committed in the public menno420/venture-lab repo; every chapter ends with a provenance footer citing the exact files and commits. Nothing was invented for marketing effect.

Q: Is this Stripe-specific?
A: The incident was (that's what actually happened), so chapters 1 and 7's examples use Stripe shapes. The method — vendored fixtures, provenance, HTTP-layer assertions, the checklist — is written provider-agnostic and applies to any service that POSTs JSON at you.

Q: What does the tool actually do?
A: vendor_fixture.py takes a sample payload YOU paste from your provider (CLI, dashboard event log, or docs), validates it, enumerates null fields, flags volatile ones, refuses anything secret-looking, optionally redacts emails, and writes the fixture plus a PROVENANCE.md stub. It is offline by design — it fetches nothing and cannot verify your source for you; the stub makes that homework explicit.

Q: How long is the guide?
A: Seven chapters, ~3,600 words — about 8 pages of prose. It is deliberately compact: one discipline, taught completely, not padded to a page count.

Q: What was NOT machine-verified?
A: The prose chapters have no executable surface, so what was verified by execution is: the tool's 8-test suite passes from the extracted bundle, the tool runs end-to-end on the included sample (output reproduced verbatim in chapter 7), every file is valid UTF-8 markdown with balanced code fences, the archive rebuilds byte-identically, and a secret scan came back clean. The chapters' claims are verified by citation to committed material, not by tests.

Q: I write webhook code for a living — will I learn anything?
A: If your fixtures already carry written provenance and your suite already includes an insecure-handler canary and stale-timestamp rejection over real HTTP, you own this discipline; buy nothing. This guide is for everyone who believed a green suite until production disagreed.

Q: License?
A: Single-user license; use the tool and checklist in as many of your own projects as you like. v0.1 — free updates to the v0.x line.

Q: Support?
A: Best-effort, community-level. It's a guide plus a small tool, not a managed service.
```
