# Session — kit upgrade v1.15.0 → v1.16.0

> **Status:** `complete`

- **📊 Model:** fable-5 · low · mechanical refactor
- **session:** substrate-kit distribution wave — upgraded this adopter from
  v1.15.0 to v1.16.0 via the canonical two-command recipe (`bootstrap.py.new
  upgrade` then `upgrade --apply-docs`), sha256 three-way verified,
  `python3 bootstrap.py check --strict` green (only the designed born-red
  hold pre-flip), landed through the live auto-merge enabler on this flip.
- **started (date -u):** Tue Jul 14 15:33:40 UTC 2026
- **closed (date -u):** Tue Jul 14 15:41:24 UTC 2026
- **PR:** #198

## What shipped

- bootstrap.py v1.16.0 (sha256
  `bba34e2102cbaf09394f39992f0501ea5cfd542d90301ef67e31a0854ca59170`,
  980026 B; downloaded asset == release.json == on-disk, three-way ✔);
  banked `.substrate/backup/bootstrap-1.15.0.py` (sha256 `25d22af9…` ==
  the v1.15.0 asset), all pre-existing banks byte-identical.
- `upgrade --apply-docs` applied: CONSTITUTION.md,
  docs/collaboration-model.md, docs/SKILLS.md, docs/ROUTINES.md,
  control/claims/README.md (`## Applied (--apply-docs)` verified in
  `.substrate/upgrade-report.md`).
- New plant `docs/reading-path.md`: its 3 interview slots
  (fleet_status_command / fleet_siblings / fleet_dark_repos) answered from
  fleet truth (fleet-manager generated `docs/roster.md`, fetched live) +
  `render --live`; minimal wiring hunk into the diverged
  AGENT_ORIENTATION clears the `[reachable]` orphan. Decide-and-flag:
  slot answers point at the generated roster rather than baking a hand
  roster (the retired fleet-manifest post-mortem is the rationale).
- Carve-out scan: live gate + enabler both "ran, 0 found", kept
  (kit-owned, already current).

## Lane-owed (untouched per Q-0261.3)

- docs/AGENT_ORIENTATION.md full template delta (diverged; only the
  reading-path wiring hunk applied) — delta in
  `.substrate/upgrade-report.md` § Template deltas.
- docs/CAPABILITIES.md diverged hunk (fleet master-copy path casing
  `docs/capabilities.md` → `docs/CAPABILITIES.md`).
- docs/seat-digest.md: NOT regenerated (hand-edited per ORDER 012 walls
  fold; `seat-digest-stale` advisory standing) — lane regenerates via
  `python3 bootstrap.py seat-digest` after folding findings.
- Heartbeat `kit:` bump in control/status.md (chronic class).
- New config default `preflight_scripts: scripts/preflight.py` — script
  not planted here yet (check NOTE, advisory).
- 17 `model-line` advisories on pre-existing sibling cards (new v1.16.0
  telemetry grammar: `model · effort · task-class`) — sibling cards not
  touched in a born-red PR (tail-shadowing doctrine); lane can true them
  up.

## ⟲ Previous-session review

Previous-session review: ORDER 012 (2026-07-14) restored the kit
capability-seed fence cleanly — verified this wave: the v1.16.0 upgrade
reported "capability-seed: fence already current — nothing to refresh",
retiring the two-wave-chronic HAND-ADOPT-ONCE debt. Its one miss: the
seat-digest was left hand-edit-flagged, so every later `check` (including
this wave's) carries the `seat-digest-stale` advisory; regenerating via
the sanctioned command in the same session would have closed it.

## 💡 Session idea

💡 The v1.16.0 `docs/reading-path.md` plant ships with three unfilled
interview slots, and `check --strict` reds on the `[unrendered-banner]`
finding immediately — so every fresh upgrade of an engaged adopter is
strict-red until someone answers fleet-topology questions mid-wave.
Kit-side idea: plant reading-path.md with the banner but grade
`unrendered-banner` on NEW plants as advisory for N days (or seed the
three slots fleet-wide from the manager's generated roster), so a
mechanical upgrade PR doesn't have to make editorial fleet-truth calls to
go green.
