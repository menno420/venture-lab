# 2026-07-11 — capabilities case-collision fix (one ledger)

> **Status:** `in-progress`

- **📊 Model:** venture-lab worker · fix/capabilities-case-collision
- **session:** case-collision repair on the capability ledger

## Session idea
The repo carried BOTH `docs/CAPABILITIES.md` and `docs/capabilities.md` — a
case collision that breaks case-insensitive filesystems and splits the truth
ledger into two divergent copies. Merge them into ONE ledger at the
kit-canonical path and remove the loser, losing no verified finding.

## Previous-session review
The 2026-07-11 gen-2 archive-ender run (`ab5f533`, ORDER 004) re-stamped state
and wrote the succession brief but did not touch the docs tree. The two
capability files predate it: `docs/CAPABILITIES.md` is the kit-template ledger
(planted at adoption, `2026-07-10-kit-adoption.md`); `docs/capabilities.md` is
the fleet-manifest copy seeded 2026-07-09. Both claim to be the living ledger —
sessions appending to one never saw the other's findings. This session
collapses the split.

## Surviving path (kit convention)
`docs/CAPABILITIES.md` (uppercase) — `bootstrap.py:2727`
`CAPABILITIES_RELPATH = "docs/CAPABILITIES.md"` and `bootstrap.py:8542`
`("CAPABILITIES.md.tmpl", "docs/CAPABILITIES.md")` both name the uppercase path;
the kit's own orientation/CLAUDE templates reference `docs/CAPABILITIES.md`.

## Deliverables
- `docs/CAPABILITIES.md` = merged single ledger (every distinct entry from both
  sources, dupes folded, kit structure + `living-ledger` Status badge kept).
- `docs/capabilities.md` removed via `git rm` (true delete).
- Pointer fixes in README.md and any templates/cards referencing the loser.
- This card.
