# Claim — Owner-gate lint backport (PRODUCTS lane follow-up)

- `claude/owner-gate-lint` · **OCQK lint mode ported back into production**
  — new `scripts/lint_owner_gates.py` (strict lint of packet §7 OWNER-GATE
  blocks + keyword-map ⚑ OWNER conflicts, real-calendar-date validation) +
  `scripts/test_lint_owner_gates.py` + advisory `kit-tests.yml` step +
  (only-if-byte-identical) date-validation fix in
  `scripts/derive_owner_queue.py` + session card · 2026-07-13
