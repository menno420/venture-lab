# 2026-07-11 — Wire kit tests into CI; flip ⚑B/⚑D owner-action scripts to UNFROZEN

> **Status:** `in-progress`

## 💡 Session idea
The ⚑B/⚑D freeze gate reads "PR #16 merged with real-path HTTP-layer tests green in CI" — PR #16 merged (912da3e), but no CI workflow actually executed the kit test suites (substrate-gate only runs bootstrap.py check variants). Close the gap honestly: add a host-owned `kit-tests` workflow that runs the membership-kit suites (incl. `test_http_realpath`) in CI, prove it green on this PR, THEN flip the two owner-action scripts from FROZEN ❄️ to UNFROZEN.

## Previous-session review
PR #16 (ORDER 003 real-Stripe-path fix) merged as 912da3e; PR #20 (launch/distribution assets, shipped the FROZEN owner-action scripts) merged as 2021bab. substrate-gate is KIT-OWNED and forbids hand edits, so the test execution lands in a separate workflow file per its own header.

## Model
- **📊 Model:** fable-5 · worker · coordinator unfreeze slice

## Deliverables
- `.github/workflows/kit-tests.yml` — CI execution of membership-kit server tests, including ORDER 003 real-path HTTP tests; fails red on any test failure.
- `docs/launch/membership-kit/owner-actions.md` + `docs/launch/template-packs/owner-actions.md` — FROZEN ❄️ → UNFROZEN (2026-07-11), gate-satisfaction citation added; live-purchase-unverified ⚑A caveat kept.
