# Session — sellable buyer zips + distribution assets

> **Status:** `in-progress`

- **📊 Model:** claude-opus-4-8[1m] · high · sellable-artifact-distribution
- **session:** venture-lab session — close the last gap between "built" and
  "sellable": produce the buyer-ready zip artifacts both publish steps need, plus
  the distribution assets (bundle listing, launch copy, demo capture) the eval
  weights but the repo lacks.
- **started (date -u):** Fri Jul 10 04:38:58 UTC 2026
- **completed (date -u):** —

## Purpose

Both owner publish steps (⚑B membership-kit, ⚑D template-packs) tell the owner to
"upload the zip" — but no zip exists, and the 35%-weighted distribution axis is
empty. This session ships the missing concrete artifacts so the owner's remaining
work is literally download-and-upload:

- **A — Packaging:** repeatable `package.sh` scripts + committed buyer-ready
  `dist/*.zip` bundles for both candidates (clean, buyer-facing, no seller
  marketing, no member data).
- **B — Distribution:** a bundle listing (membership-kit + template-packs at a
  discount), ready-to-paste honest launch posts (Show HN / Reddit / Claude-Code
  community), and a REAL demo transcript of the mock purchase→access loop.
- **C — Ledger + honesty:** mark packaging shipped, point ⚑B/⚑D at the concrete
  zip paths, add honest token-cost lines. No owner-gated action performed.

## ⟲ Previous-session review

⟲ previous-session review: the round-2 close-out (PR #8, d621866) established
ground truth — candidate #1 at v0.2 (pluggable restart-surviving persistence, 13
green tests) and candidate #2 at publish-ready v0.1 (drop-in pack + $19 PWYW
listing) — with a green `check --strict` and current ledger. What it left
undone: both ⚑ publish actions say "attach the zip" but the zip was never built,
so the owner-click still had an unbuilt dependency. This session removes it.

## 💡 Session idea

💡 "Built" and "sellable" are different milestones, and the gap between them is
unglamorous packaging. An agent fleet naturally over-invests in code (the fun
part) and under-invests in the boring last mile — the clean buyer bundle, the
channel copy, the recorded demo — which is exactly the part that converts a
finished artifact into first revenue. The cheapest credible path to revenue is
often not more product; it's making the product one download away from being
uploaded, and giving the owner the exact words to post.

## Plan

1. Heartbeat: this born-red card (first commit).
2. A — `package.sh` for both candidates → deterministic-ish, idempotent zips;
   run them; paste `unzip -l` listings here as evidence; commit scripts + zips.
3. B — `candidates/BUNDLE-LISTING.md`, `docs/distribution/launch-posts.md`,
   `docs/distribution/demo-transcript.md` (run the real loop, paste real output).
4. C — ledger updates (packaging shipped, ⚑B/⚑D → zip paths, token-cost lines).
5. Open a READY PR against main; arm squash auto-merge; do NOT merge.
6. Flip this card to `complete` as the deliberate last commit.

## Log

- Synced to `origin/main` @ d621866; branched
  `ship/sellable-artifact-distribution`. Confirmed HEAD ≥ d621866.
- CI state: `bootstrap.py` present at repo root; `.github/workflows/` holds
  `substrate-gate.yml`. `python3 bootstrap.py check --strict` → exit 0 (only
  advisory owner-action + session-001 warnings, non-blocking). Will re-run green
  before every push.

## Evidence (filled during build)

- Packaging zip listings: _pending — pasted below once `package.sh` runs._
- Demo transcript: _pending — real curl loop captured in
  `docs/distribution/demo-transcript.md`._

## Deliverable summary

_pending — filled at close._
