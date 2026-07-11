# Session — CI wiring: stripe-webhook-test-kit real-path suite in kit-tests

> **Status:** `complete`

- **📊 Model:** claude-fable-5 · high · ci-wiring
- **session:** wire the freshly merged stripe-webhook-test-kit (PR #27) real-path
  HTTP suite into the host-owned `kit-tests` workflow so "real-path tests green
  in CI" becomes a named, enforced check — the intake's VERIFIED-WHEN evidence.
- **started (date -u):** Sat Jul 11 2026 (born-red first commit)

## ⟲ Previous-session review

Previous-session review: PR #27 landed the Stripe Webhook Test Kit v0.1
(merge `28ff800`) with a 14-test `test_http_realpath.py` suite that signs
vendored real-shape Stripe fixtures and drives them over real HTTP — but at
merge time only `membership-kit-tests` and `substrate-gate` ran in CI, so the
new suite was green locally and from-zip, not yet enforced by a check. The
binding lesson carried forward (PR #16 / PR #24 pattern): a suite only counts
as evidence once a named CI job fails the build when it fails.

## 💡 Session idea

Mirror the existing `membership-kit-tests` job with a second job
`stripe-webhook-test-kit-tests` in `.github/workflows/kit-tests.yml` that runs
`python3 -m unittest test_http_realpath -v` in
`candidates/stripe-webhook-test-kit`. unittest exits nonzero on any failure,
so a failing real-path test reds the check. No kit code is touched — this is
host-owned CI wiring only.

## Scope

- Add the `stripe-webhook-test-kit-tests` job to `.github/workflows/kit-tests.yml`.
- Born-red session card; `python3 bootstrap.py check --strict` green before push.
- Do NOT touch `control/` or `candidates/stripe-webhook-test-kit/` contents.

## Work log

- Branch `coordinator-swtk-ci` cut from `origin/main` at `28ff800` (the PR #27
  squash merge).
- Added the second job mirroring the membership-kit job's structure
  (checkout@v4, setup-python@v5 "3.x", working-directory
  `candidates/stripe-webhook-test-kit`, `python3 -m unittest
  test_http_realpath -v`).
- Evidence target: the new job's CI log on this PR's head must show
  `Ran 14 tests ... OK`.
