# Session — substrate-kit upgrade v1.7.0 → v1.7.1

> **Status:** `complete`

- **📊 Model:** claude-fable-5 · kit-upgrade distribution wave
- **session:** kit-upgrade v1.7.1 (distribution worker, kit wave)
- **started (date -u):** Fri Jul 10 22:00:26 UTC 2026
- **completed (date -u):** Fri Jul 10 22:03:29 UTC 2026
- Delivered: substrate-kit v1.7.0 → v1.7.1 (pinned release asset,
  sha256-verified); live + staged substrate-gate regenerated (kit-owned);
  `check --strict` green on the upgraded tree with this card complete.

## Purpose

Upgrade the vendored substrate-kit from v1.7.0 to the published v1.7.1 release
(tag `1cbd666`, release asset sha256
`2aa4feddf7de7e20b00f46866826985ca8fd11f40bc51ebe261bbdef3118486d`): place the
pinned release assets, run `bootstrap.py.new upgrade`, verify the v1.7.1
payload (live + staged gate regen, carve-out report, single-dist backup,
`--inbox-base` wiring), verify `python3 bootstrap.py check --strict` green,
and land only kit-owned changes. Scope is the kit upgrade only — no domain
work, no `control/inbox.md` / `control/status.md` writes (the lane's own next
heartbeat updates the `kit:` line).

## Log

- Synced to `origin/main` @ `ce22315`; vendored header confirmed v1.7.0.
- Placed the pre-verified pinned assets; `bootstrap.py.new` sha256 matched the
  pin `2aa4feddf7de7e20b00f46866826985ca8fd11f40bc51ebe261bbdef3118486d`;
  engine self-verified against `release.json` before archiving.
- `python3 bootstrap.py.new upgrade` (no `--apply-docs`, matching this repo's
  v1.7.0 precedent): docs classified consumer-edited 4 · unchanged 15 ·
  diverged 0 · template-improved 0 — nothing `--apply-docs` would apply, and
  the one v1.7.0 `diverged` row (`control/README.md`) is now consumer-edited.
- Vendored `bootstrap.py` now v1.7.1; `substrate.config.json` pin `1.7.1`.
- **Live gate regenerated in place** (`.github/workflows/substrate-gate.yml`
  is kit-owned as of v1.7.1), byte-identical to the staged
  `.substrate/ci/substrate-gate.yml`. Functional delta vs the old live gate:
  the new inbox append-only gate step (`check --strict --status-only
  --inbox-base "$basefile"`, self-skips when `control/inbox.md` untouched) +
  the added-card advisory sentinel (a card ADDED by a PR gates advisory;
  a MODIFIED card keeps the full locked-door gate) + KIT-OWNED header.
  Zero host carve-outs detected → no `substrate-gate.pre-regen-*.yml` bank
  (conditional by design); pre-upgrade live gate recoverable from git history.
- **#137 single-backup pass**: `.substrate/backup/bootstrap-1.7.0.py` was
  already banked byte-identical to the pre-upgrade vendored dist (pre-#137
  verb behavior during v1.6.0→v1.7.0); the verb printed `(already banked)`,
  created no new archive, and no `bootstrap-1.7.1.py` exists.
- `python3 bootstrap.py check --strict` → exit 0 with this card complete
  (exit 1 while born-red was the card itself via the mtime fallback —
  expected). Local `guard-fires.jsonl` appends restored, not committed.
- Out of scope, untouched (Q-0261.3): `control/inbox.md`, `control/status.md`
  (the lane's own next heartbeat records the `kit: v1.7.1` line).

## 💡 Session idea

💡 The v1.7.1 gate's added-card advisory sentinel means a born-red card no
longer holds the merge on this repo (same shape as gba-homebrew) — the hold
now lives entirely in *auto-merge timing discipline* (arm last). A kit-side
`upgrade` output line that says loudly "NOTE: gate regen changed born-red
semantics: added cards are now ADVISORY — arm auto-merge only after the
close-out flip" would convert that silent behavioral shift into an explicit
operator instruction at exactly the moment it matters.

## ⟲ Previous-session review

⟲ previous-session review: the v1.7.0 upgrade session's card was the single
most useful artifact for this run — it recorded the *expected absence* of the
live-gate regen ("kit PR #130 ships next release"), which turned this
session's biggest diff (a rewritten live workflow) from a red flag into a
predicted event. Improvement it surfaces: that card predicted the regen but
not its *consequence* (born-red hold semantics flipping to advisory); a
close-out that names the behavioral deltas the next session will inherit —
not just the file deltas — would have made the auto-merge-timing decision
here derivation-free.

## ⚑ Flags

- Self-initiated: none — owner-directed distribution-wave task, hard scope
  Q-0261.3 (kit upgrade only; no control/ writes, no domain work).
