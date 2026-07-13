# 5 · The fast lane: a required check must ALWAYS report

Once your gate is a required check (chapter 2) you inherit a new failure
mode, and it is nastier than a red X: a required context that **never
reports** stays pending forever, and a pending required context blocks
auto-merge indefinitely. No error, no red, just a PR that never lands.

## Never `paths-ignore` a required check

The intuitive optimization — "heartbeat and coordination commits don't
need the heavy test suite, add `paths-ignore: [control/**]`" — is exactly
the trap. With `paths-ignore`, the workflow doesn't run at all for those
diffs, so the required context never reports, so the armed PR waits for a
check that will never come. The production gate's header comment states
the rule:

> If this check is REQUIRED, prefer an in-job short-circuit … over
> `paths-ignore`: a required context that never reports stays pending and
> blocks auto-merge forever.

## The in-job short-circuit

The production gate runs on **every** PR, and its first step classifies
the diff: if every changed file is under `control/` (the fleet's
coordination namespace — heartbeats, inbox, claims), the heavy steps are
skipped **but the job still reports green**. Coordination PRs land in
seconds (PR #128 in chapter 3 merged 23 seconds after open on this lane);
code PRs get the full suite; the required context reports in both cases.
Two details worth stealing:

- **Fail safe onto the full lane.** An empty or unreadable diff is
  classified as NOT fast-lane. When the classifier is confused, you want
  the heavy gate, not the shortcut.
- **The fast lane still guards its own files.** The production gate
  learned that a fast lane which skips *everything* is a hole: a
  control-only PR edits exactly the coordination files the fleet's status
  checker validates, so the lane still runs the scoped status check — its
  comment records the incident ("a heartbeat-deleting control PR merges
  GREEN and pre-reddens the NEXT unrelated PR"). And because the fleet's
  append-only order inbox is a control file, the gate runs its
  pure-append/grammar check on BOTH lanes — a mixed PR could smuggle an
  inbox rewrite through the full lane too. A fast lane is a smaller gate,
  never an open door.

## Where this lives in the recipes

`recipes/born-red-hold-gate.yml` ships the short-circuit as its first step
(`fast=true` when the diff is entirely under your coordination prefix) with
the fail-safe default, and every subsequent step conditioned on
`fast != 'true'`. Adjust the prefix; keep the shape: one required context,
always reporting, cheap when it can be, thorough when it must be.

**Sources** (public repo `menno420/venture-lab`):
`.github/workflows/substrate-gate.yml` @ `4776045` (paths-ignore rule in
the header; control fast lane; control-status gate + heartbeat-deletion
incident comment; both-lanes inbox append-only gate); PR #128 merge event
(23 s open→merge on the fast lane, verified via the API 2026-07-13).
