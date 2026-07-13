# The Agent Merge-Wall Cookbook

Ship code with an AI-agent fleet without getting stuck at the merge: the
exact GitHub-automation walls a self-merging agent fleet hits — quoted
verbatim from the committed platform-limits ledger of a repo that hit them
— and the four runnable workflow recipes that land 10+ agent PRs a night
anyway.

## What you get

- **`guide/`** — 7 chapters: the self-merge classifier wall (verbatim
  denials), why native auto-merge won't arm (the zero-required-checks
  trap), the enabler pattern, the born-red HOLD gate, the required-check
  fast lane, never-red advisory checks, and the REST merge-on-green
  fallback.
- **`recipes/`** — 4 GitHub Actions workflows, ready to drop into
  `.github/workflows/`:
  1. `auto-merge-enabler.yml` — arm native auto-merge at PR open
     (**production-proven**: adapted from a live workflow with verifiable
     merge events, cited in ch. 3).
  2. `merge-on-green.yml` — `GITHUB_TOKEN` REST merge fallback
     (**parse-verified, not production-run** — its header says so; trial
     on a scratch repo first).
  3. `born-red-hold-gate.yml` — required gate that holds work-in-progress
     PRs red by design, with the fast-lane short-circuit (distilled from
     a live production gate).
  4. `advisory-check.yml` — the double-guarded check that can never turn
     red (adapted from a live production job).

## Honesty box (read first)

- **Every wall is quoted, not invented.** The denials, incidents, and
  design comments in the guide are quoted from committed files in the
  public `menno420/venture-lab` repo; every chapter ends with a Sources
  footer citing `file @ commit` so you can audit each claim.
- **Provenance varies by recipe and is labeled per recipe** — one is
  production-proven with citable merge events, two are distillations of a
  live production gate, one is assembled from documented doctrine and only
  parse-verified. Chapter 7's honesty ledger spells out which is which.
- **Platform workarounds rot.** GitHub changes its API and UI; the source
  ledger itself carries "re-verify the wall" notes. Re-verify against
  current GitHub docs before betting a fleet on any of this.
- **This is a cookbook, not a managed service.** No warranty that your
  policy layer, org rules, or GitHub plan behave identically.

## Quick start

See `QUICKSTART.md` — install order, the two one-time repo settings the
recipes need, and the verification commands (every recipe parses with a
stock YAML loader; the commands to prove it on your machine are included).

## Who this is for

You are building agents that open PRs and you have discovered they cannot
land them: self-merge denied by a policy layer, auto-merge won't arm, or
green PRs pile up waiting for a human click. This cookbook is the landing
path, with the receipts.

## License

Single-user license; use the recipes in as many of your own projects as
you like. v0.1 — free updates to the v0.x line.
