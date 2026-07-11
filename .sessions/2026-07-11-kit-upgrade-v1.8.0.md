# Session — substrate-kit upgrade v1.7.1 → v1.8.0

> **Status:** `complete`

- **📊 Model:** claude-fable-5 · kit-upgrade distribution wave
- **session:** kit-upgrade v1.8.0 (distribution worker, kit wave)
- **started (date -u):** Sat Jul 11 01:19:26 UTC 2026
- **completed (date -u):** Sat Jul 11 01:24 UTC 2026
- Delivered: substrate-kit v1.7.1 → v1.8.0 (pinned release asset,
  sha256-verified); live + staged gate regenerated; `control/claims/` +
  `scripts/env-setup.sh` planted; auto-merge enabler staged;
  `control/README.md` manual merge; pre-existing gen2-card grammar red
  fixed; `check --strict` green with this card complete.

## Purpose

Upgrade the vendored substrate-kit from v1.7.1 to the published v1.8.0
release (tag `v1.8.0` @ `63c6b39`, release asset sha256
`28c5dcb64b713dde8d64a513a9a1aa860b4a07bf17d832686f0009932dc89b9b`): place
the pinned release assets, run `bootstrap.py.new upgrade`, verify the v1.8.0
payload (control/claims/ plant, scripts/env-setup.sh plant, staged
auto-merge enabler, gate regen + carve-out scan, single-dist backup),
perform the report-prescribed manual merge for the one `diverged` doc
(`control/README.md`), verify `python3 bootstrap.py check --strict` green,
and land only kit-owned changes. Scope is the kit upgrade only — no domain
work, no `control/inbox.md` / `control/status.md` writes (the lane's own
next heartbeat updates the `kit:` line).

## Log

- Synced to `origin/main` @ `ab5f533`; vendored `bootstrap.py --version` →
  1.7.1, `.substrate/state.json` kit_version 1.7.1.
- Downloaded release assets via `github.com/.../releases/download/...`;
  `bootstrap.py.new` = 625,066 bytes, sha256 matched the pin
  `28c5dcb6...c89b9b`; engine re-verified sha256+version against
  `release.json` before archiving; inputs self-cleaned after the upgrade.
- `python3 bootstrap.py.new upgrade`: docs classified consumer-edited 3 ·
  diverged 1 · missing 2 · unchanged 15.
- **Backups:** exactly ONE new archive — `.substrate/backup/bootstrap-1.7.1.py`;
  no collision lines; `bootstrap-1.6.0.py` / `bootstrap-1.7.0.py` untouched.
- **Plants:** `control/claims/README.md` (unified per-file claim convention;
  `substrate.config.json` pins `claims_dir: control/claims`) and
  `scripts/env-setup.sh` (no pre-existing host wrapper — clean plant, no
  skip). NOTE: this repo also has a deliberate root `claims/` seeded by the
  gen-2 blueprint — legacy home, auto-detected advisory during the migration
  window; consolidation is a host decision, not this session's.
- **Gate regen:** live `.github/workflows/substrate-gate.yml` regenerated
  (kit-owned), byte-identical intent to staged `.substrate/ci/substrate-gate.yml`.
  Functional delta: mid-PR locked-door invariant — a PR that ADDS a card AND
  touches the gate workflow keeps the FULL locked door (the venture-lab #14
  class), so this very PR holds red until this card flips complete.
- **Carve-out scan:** ran against the live gate, **0 found** → no
  `substrate-gate.pre-regen-*.yml` bank (conditional by design, correct).
- **Auto-merge enabler:** STAGED at `.substrate/ci/auto-merge-enabler.yml`;
  no live enabler pre-existed in `.github/workflows/` → stays staged
  (gba-homebrew-shape outcome, expected).
- **control/README.md manual merge (`diverged`):** host file is fully
  consumer-rewritten (47 lines; none of the template anchors survive). The
  "Claiming work" template delta was appended as a new section; the three
  anchorless "Grammar source of truth" deltas were recorded as an inline
  provenance comment (gba-homebrew precedent).
- **Pre-existing red, fixed + flagged:** `.sessions/2026-07-11-gen2-archive-ender.md`
  (PR #15) lacked the `💡` and `📊 Model:` grammar tokens — bare
  `check --strict` exited 1 on it via the newest-by-mtime fallback, under
  BOTH the banked v1.7.1 engine and v1.8.0 (i.e. NOT upgrade-caused).
  Mechanical token fix, content preserved, provenance comment inline.
- Local `guard-fires.jsonl` appends restored, not committed (v1.7.1
  precedent).
- `python3 bootstrap.py check --strict` → exit 0 on the final tree with this
  card complete.

## 💡 Session idea

💡 The advisory-sentinel card path is exactly how PR #15's malformed card
merged green and pre-reddened every later bare `check --strict` run: an
ADDED card is never grammar-checked at all, only completeness-exempted. A
kit-side middle tier — grammar-lint the added card's *present* tokens
(reject a `## Model` section with no `📊 Model:` needle) while still
exempting born-red incompleteness — would keep the born-red flow intact and
make the PR-#15 drift class impossible at the door instead of caught by the
next upgrade wave.

## ⟲ Previous-session review

⟲ previous-session review: the gen2-archive-ender session (PR #15) did the
right operational thing (state repair on main, succession brief) but wrote
its card in free-form section headers instead of the kit grammar, which
silently reddened the repo's verify command for every subsequent session.
Improvement it surfaces: the card grammar is enforced only on MODIFIED
cards; a card written correctly once would never need this wave's cleanup —
see the 💡 above for the kit-side fix.

## ⚑ Flags

- Self-initiated (decide-and-flag): mechanical grammar fix to
  `.sessions/2026-07-11-gen2-archive-ender.md` — pre-existing `check
  --strict` red, verified NOT upgrade-caused by re-running the banked
  v1.7.1 engine; content untouched.
- Otherwise owner-directed distribution-wave task, hard scope (kit upgrade
  only; no `control/inbox.md` / `control/status.md` writes, no domain work).
- Host follow-up (not done here): root `claims/` (gen-2 blueprint seed) vs
  kit-planted `control/claims/` — two claim homes now coexist; consolidate
  or pin deliberately.
