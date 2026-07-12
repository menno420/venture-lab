# Ledger-drift checker (advisory)

> **Status:** `reference`
>
> `scripts/check_ledger_drift.py` — an ADVISORY nag that surfaces when the
> living ledger silently falls behind merged reality. It compares the highest
> PR number cited in [`docs/current-state.md`](current-state.md)
> § "Recently shipped" against the newest MERGED PR on GitHub and prints one
> line. **It exits 0 on every path** (in-sync, trailing, skip, parse
> failure) — the same advisory contract as the kit's `claims-stale`; it must
> never be wired as a required gate.

## Why it exists (measured drift, not vibes)

`control/status.md` has a heartbeat rhythm that keeps it current; nothing
nagged when `docs/current-state.md` drifted. Evidence: at the instant PR #90
(the ledger refresh itself) merged, the ledger was already **3 merged PRs
behind** (#88–#90) — recorded by PR #91's session card
(`.sessions/2026-07-12-slow-word-vetting.md` § previous-session review); by
the time this checker was built the live gap had grown to 4 (#88–#91).
Origin: PR #90's session-card 💡 idea
(`.sessions/2026-07-12-current-state-refresh.md`).

## Usage

```
python3 scripts/check_ledger_drift.py [--ledger docs/current-state.md] [--repo owner/repo]
```

Stdlib only, system `python3`. Auth: `GITHUB_TOKEN` or `GH_TOKEN` from the
environment if present; with no token, or with the API unreachable, it
degrades to a graceful `skipped` line — never an error.

## Output (one line, always exit 0)

- `ledger-drift: in-sync (ledger cites #N, newest merged #N)`
- `ledger-drift: trailing by K — missing PRs: #a, #b, ...` — merged PR
  numbers above the cited one; a session should refresh the ledger's
  "Recently shipped" from merged work.
- `ledger-drift: skipped — <reason>` (no token / API unreachable / no
  parseable citation).

## Wiring

Runs as the `ledger-drift-advisory` job in the HOST-OWNED
[`kit-tests.yml`](../.github/workflows/kit-tests.yml) workflow —
`continue-on-error: true` on top of the script's own always-exit-0
contract, so it structurally cannot red a gate. Do not add it to the
required-checks ruleset.
