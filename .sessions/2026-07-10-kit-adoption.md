# Session — venture-lab substrate-kit adoption

> **Status:** `complete`

- **📊 Model:** claude-opus-4-8[1m] · high · kit-adoption
- **session:** venture-lab session 1 (continued) — kit adoption
- **started (date -u):** Fri Jul 10 02:54:04 UTC 2026
- **completed (date -u):** Fri Jul 10 02:55:29 UTC 2026
- Delivered: substrate-kit v1.6.0 vendored + adopted; interview filled + docs
  rendered; substrate-gate CI workflow installed; `check --strict` green.

## Purpose

Adopt substrate-kit into venture-lab so the mandated `check --strict` quality
floor can run, and wire the CI gate so PRs are born with a pending check —
closing REPO GAP 1 (no bootstrap.py) and REPO GAP 2 (no CI workflow) flagged
in the previous session's status close-out.

## ⟲ Previous-session review

⟲ previous-session review: session-001 shipped ORDER 001 (the venture-shortlist
evaluation, `docs/research/venture-eval-001.md` merged to main) and closed the
walking skeleton (PR #2). It closed RED on two repo gaps under ⚑ needs-owner:
no vendored `bootstrap.py` (quality floor un-runnable) and no CI workflow
(auto-merge-in-pending-window path un-exercisable). This session executes the
kit adoption that clears both, preserving the manager's ORDER 001 recommendation
and repo-gap flags in the reconciled `control/status.md`.

## 💡 Session idea

💡 The kit's CI gate is not just a quality floor — its control-plane fast lane
(control/**-only diffs short-circuit green while still validating the heartbeat)
is what makes the manager↔lane bus safe to auto-merge: coordination commits stop
jamming a required check without letting a heartbeat-deleting commit through.
That dual property is the real unlock for overnight autonomous operation.

## Log

- Vendored `/home/user/substrate-kit/dist/bootstrap.py` to repo root; confirmed
  stdlib-only and `--help` runs (kit v1.6.0).
- `adopt` planted the workflow docs and kept all three manager-owned control
  files (`control/README.md`, `control/inbox.md`, `control/status.md`). No
  existing venture-lab doc was modified (verified via `git status` / `git diff`).
- Filled all interview slots, `render --live` (0 unfilled placeholders),
  `mode guided`.
- Installed `.github/workflows/substrate-gate.yml` from the staged kit gate
  (invocations point at the repo-root vendored `bootstrap.py`).
- Reconciled `control/status.md`: added the kit-required `updated:` ISO-8601
  heartbeat while preserving every manager-semantic field (timestamp, phase,
  health, last-shipped PR, orders acked/done, blockers, and the two ⚑ needs-owner
  repo-gap flags + the ORDER 001 recommendation).
- Drove `check --strict` to exit 0 (plain + CI-mode with `--require-session-log`).
