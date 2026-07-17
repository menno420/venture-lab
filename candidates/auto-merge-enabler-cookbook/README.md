# The Auto-Merge Enabler Cookbook

Land your AI agents' pull requests on green with **no human clicking
merge** — the exact merge-on-green enabler workflow this repo runs in
production, annotated line by line, plus the required-check gate and the
born-red HOLD that make it safe. Distilled from the workflow that
squash-merged five agent PRs in one night, `merged_by:
github-actions[bot]`, verifiable from the public GitHub API.

## What you get

- **`guide/`** — 8 chapters: the merge-on-green model (the agent never
  merges); the enabler workflow annotated line by line; required-checks
  gating (the zero-required-checks trap); the born-red HOLD (make "not
  finished" a red check); the `do-not-automerge` opt-out; why the agent is
  classifier-barred from self-arming (and why that's correct); a
  troubleshooting flow (why a green PR didn't land); and the copy-paste
  recipe set with a per-file honesty ledger.
- **`recipes/`** — 3 GitHub Actions files, ready for `.github/workflows/`:
  1. `auto-merge-enabler.yml` — arms native auto-merge on agent PRs at open
     (**production-proven, verbatim** — the exact file this repo runs; five
     citable `github-actions[bot]` merges).
  2. `substrate-gate.yml` — the required gate with the born-red HOLD +
     control fast lane (**production-proven, verbatim**).
  3. `auto-merge-enabler-minimal.yml` — the enabler reduced to its
     load-bearing skeleton for reading (**distillation, parse-verified**;
     header states when it's safe to prefer).

## The trust move (the whole idea in one sentence)

**The agent never merges and never even arms auto-merge — a repo-owned
workflow arms GitHub-native auto-merge at PR open, and GitHub itself
squash-merges the moment your required check goes green.** Arming is not
merging, so a policy layer that denies an agent's direct merge does not
deny the server-side arm+merge under the workflow's own token. The merging
identity is the workflow (`github-actions[bot]`), never the agent's seat.

## Honesty box (read first)

- **The subject is this repo's own live infrastructure.** The two
  production recipes are copied byte-for-byte from the workflows this public
  repo runs; every chapter ends with a Sources footer citing `file @ commit`
  so you can audit each claim. Evidence class: *verified-by-production* —
  cited to real merge events, not an HTTP test.
- **Provenance is labeled per file.** Two recipes are production-proven
  verbatim; one is a readability distillation, parse-verified only, and its
  header says so. The REST merge-on-green fallback is *not* shipped here as
  a production recipe (this repo lands via the native arm) — it's named as
  doctrine and pointed at the companion Merge-Wall Cookbook.
- **Platform workarounds rot.** GitHub changes its API and UI — required-check
  mechanics, auto-merge arming, and the `GITHUB_TOKEN` recursion guard are
  all platform behavior. Re-verify against current GitHub docs before
  betting a fleet on any of this.
- **This is a cookbook, not a managed service.** No warranty that your
  policy layer, org rules, or GitHub plan behave identically.

## What this does NOT do

- It does **not** bypass code review or your policy layer. The whole design
  is the opposite: the agent never merges; merging is done by GitHub's
  native auto-merge under a repo-owned token, gated by a required check you
  control. If your org requires human review, that requirement still holds.
- It does **not** ship a runnable REST merge-on-green fallback (see the
  honesty box). If the native arm is structurally refused on your repo
  shape, you need that fallback — the companion Merge-Wall Cookbook ships a
  parse-verified one.
- It is **not** the same product as the Agent Merge-Wall Cookbook. That one
  is about the *walls* a self-merging fleet hits and how to avoid conflict
  stalls; **this** one is the *enable* mechanism — the merge-on-green
  enabler itself, deep. Sibling audience, non-overlapping.

## Quick start

See `QUICKSTART.md` — the verify-parse command, the two one-time repo
settings the recipes need, and the install order.

## Who this is for

You are building agents that open PRs, and you want them to land on green
without a human in the loop — but a policy layer denies your agent's
self-merge, or auto-merge won't arm, or green PRs pile up. This cookbook is
the landing path this fleet actually runs, with the receipts.

## License

Single-user license; use the recipes in as many of your own projects as you
like. v0.1 — free updates to the v0.x line.
