# Session — kit upgrade v1.15.0 → v1.16.0

> **Status:** `in-progress`

- **📊 Model:** Claude Fable · kit-upgrade distribution wave v1.16.0
- **session:** substrate-kit distribution wave — upgrade this adopter from
  v1.15.0 to v1.16.0 via the canonical two-command recipe (`bootstrap.py.new
  upgrade` then `upgrade --apply-docs`), verify sha256 three-way, run
  `python3 bootstrap.py check --strict` green, land through the live
  auto-merge enabler on card flip.
- **started (date -u):** Tue Jul 14 15:33:40 UTC 2026

## Scope

- Download release asset v1.16.0 (sha256
  bba34e2102cbaf09394f39992f0501ea5cfd542d90301ef67e31a0854ca59170,
  980026 bytes) + release.json; three-way verify.
- Two-command upgrade; verify `## Applied (--apply-docs)` in
  `.substrate/upgrade-report.md`; note lane-owed deltas.
- Rails (Q-0261.3): only bootstrap.py, `.substrate/**`, --apply-docs docs,
  staged gate, kit pin. No control/**, no hooks, no product code.
