# Session — sellable buyer zips + distribution assets

> **Status:** `complete`

- **📊 Model:** claude-opus-4-8[1m] · high · sellable-artifact-distribution
- **session:** venture-lab session — close the last gap between "built" and
  "sellable": produce the buyer-ready zip artifacts both publish steps need, plus
  the distribution assets (bundle listing, launch copy, demo capture) the eval
  weights but the repo lacks.
- **started (date -u):** Fri Jul 10 04:38:58 UTC 2026
- **completed (date -u):** Fri Jul 10 04:49:49 UTC 2026

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

## Evidence

### Buyer zip listings (`unzip -l`, verified byte-identical on re-run)

`candidates/membership-kit/dist/membership-kit-v0.2.zip` — 14 entries, 49894 B raw:

```
membership-kit-v0.2/QUICKSTART.md
membership-kit-v0.2/README.md
membership-kit-v0.2/design-tokens.json
membership-kit-v0.2/server/.env.example
membership-kit-v0.2/server/.gitignore
membership-kit-v0.2/server/README.md
membership-kit-v0.2/server/app.py
membership-kit-v0.2/server/test_membership.py
membership-kit-v0.2/web/index.html
membership-kit-v0.2/web/members.html
membership-kit-v0.2/web/styles.css
```

(excluded, verified: seller `LISTING.md`, runtime `members.json`, `__pycache__`,
`dist/`, `package.sh`.)

`candidates/template-packs/dist/template-packs-v0.1.zip` — 15 entries, 20684 B raw:

```
template-packs-v0.1/QUICKSTART.md
template-packs-v0.1/README.md
template-packs-v0.1/INCLUDED.md
template-packs-v0.1/pack/CLAUDE.md.template
template-packs-v0.1/pack/session-card.template.md
template-packs-v0.1/pack/session-discipline.md
template-packs-v0.1/pack/hooks/README.md
template-packs-v0.1/pack/hooks/settings.template.json
template-packs-v0.1/pack/hooks/scripts/agent-orient.sh
template-packs-v0.1/pack/hooks/scripts/post-edit-reminder.sh
template-packs-v0.1/pack/hooks/scripts/session-close-check.sh
```

(excluded, verified: seller `LISTING.md`, `package.sh`.) Both scripts are
idempotent — a second run produces a byte-identical archive (md5 unchanged).

### Demo loop — RAN (real output)

The membership-kit mock purchase→access loop was executed against the kit's own
`ThreadingHTTPServer` on loopback and driven with real `curl`; verbatim output
(health 0 members → 402 denied → mock-purchase grant → 200 gated page → non-buyer
402 → idempotent re-purchase `new_member=false` → persisted `members.json`) is in
[`docs/distribution/demo-transcript.md`](../docs/distribution/demo-transcript.md).
13/13 unit tests also green. (Sandbox note: a *long-lived background* server is
killed with signal 16 here, so the capture ran the server in-process,
short-lived — the two-terminal `python3 app.py` + curl recipe in the transcript
header is what a buyer reproduces.)

## Log (close)

- A — Wrote `package.sh` for both candidates + buyer `QUICKSTART.md` files; ran
  both, verified idempotent + no seller/runtime leaks; committed scripts + built
  `dist/*.zip` (3ef5682).
- B — `candidates/BUNDLE-LISTING.md` ($59 vs $68), `docs/distribution/launch-posts.md`
  (Show HN / Reddit / Claude-Code, `{{LISTING_URL}}` placeholders, no fabricated
  metrics), and the real demo capture; badged + linked from the ledger for
  doc-hygiene (9f2ac93).
- C — `venture-ledger.md`: packaging marked shipped for both candidates; ⚑B/⚑D
  now name the concrete `dist/*.zip` the owner uploads; this-session token-cost
  lines added under both. `control/inbox.md` and `control/status.md` untouched.
- `python3 bootstrap.py check --strict` → green apart from this card's
  intentional born-red badge (flipped to complete in this final commit) and the
  pre-existing advisory owner-action warning.

## Deliverable summary

The last gap between "built" and "sellable" is closed: two repeatable,
idempotent `package.sh` scripts and their **committed** buyer zips
(`membership-kit-v0.2.zip`, `template-packs-v0.1.zip`) mean the owner's publish
step is now pure download-and-upload; a bundle listing, honest ready-to-paste
launch copy, and a REAL captured purchase→access demo fill the previously-empty
distribution axis; and the ledger points ⚑B/⚑D at the exact zip paths with honest
per-session token-cost lines. Nothing owner-gated was performed — no accounts, no
publish, no spend.
