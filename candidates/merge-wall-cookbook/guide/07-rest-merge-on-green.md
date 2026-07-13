# 7 · Recipe 2: REST merge-on-green (the fallback) + the honesty ledger

Native auto-merge (Recipes 1+3+4 working together) is the primary landing
path, but there are repo shapes where the arm itself is structurally
refused. The production enabler names them in its own failure message:

> On a repo shape where GitHub structurally refuses the arm (born-red
> required checks with no pending window, or PR-required-but-no-CI), REST
> merge-on-green is the landing path instead.

And the fleet's platform ledger records the other reason you may need
REST paths at scale: **GraphQL quota exhausts at fleet scale (~hourly)** —
REST merge-on-green is the documented fallback, with one asymmetric
gotcha: draft→ready flips are GraphQL-only, so the cheapest fix is
cultural, not technical — *never open drafts* ("READY, never draft" in
the fleet's conventions).

## How Recipe 2 works

`recipes/merge-on-green.yml` is the same trust move as the enabler — the
merging identity is a repo-owned workflow token, never the agent — but the
workflow performs the merge itself instead of delegating to native
auto-merge:

1. Fires on `workflow_run: completed` of your required gate, success only.
2. Finds open, non-draft, same-repo, agent-namespace PRs on that exact
   head sha.
3. Re-reads labels fresh from the API (the stale-payload race guard,
   inherited from the production enabler).
4. Requires **every** check run on the head to be concluded green — not
   just the gate that triggered it. One pending or red run: no merge.
5. Squash-merges via REST, **pinned to the verified sha** (`sha=` on the
   merge call) — a race-pushed newer head makes the merge 409 instead of
   landing code no one checked.

## The honesty ledger (read before you ship any of this)

This cookbook's credibility mechanic is that its claims trace to committed
material in a public repo — so here is exactly what is and is not
production-proven:

- **Recipe 1 (enabler): production-proven.** Live file, 13 merges on
  2026-07-13 alone, two independently verifiable via the API (chapter 3).
- **Recipe 3 (born-red hold) and the fast lane: production-proven in
  engine form.** The live gate enforces these rules via a committed Python
  engine; the recipes are self-contained bash distillations of the same
  rules, parse-checked but simplified — the simplification is yours to
  own.
- **Recipe 4 (advisory): production-proven.** Live job, pattern lifted
  near-verbatim.
- **Recipe 2 (this chapter): NOT production-run in the source repo.** The
  source repo lands PRs via the native arm, so its REST fallback exists
  there as documented doctrine (ledger + enabler failure message), and
  this YAML is assembled from that doctrine and parse-verified only.
  Additionally, `GITHUB_TOKEN`-created merges generally do not trigger
  downstream workflow runs (GitHub's recursion guard) — verify against
  current GitHub docs and use a PAT/App token if your `main` runs
  post-merge automation. Trial Recipe 2 on a scratch repo before trusting
  it with a fleet.

That is the standard this cookbook holds itself to: the walls are quoted
verbatim from a committed ledger, the primary path is cited to real merge
events, and the one recipe that isn't production-run tells you so in its
own header.

**Sources** (public repo `menno420/venture-lab`):
`.github/workflows/auto-merge-enabler.yml` @ `305646f` (structural-refusal
failure message naming the REST fallback); `docs/PLATFORM-LIMITS.md` @
`2044dc6` (GraphQL quota / R8 REST fallback, ready-flips-are-GraphQL-only,
"READY, never draft" pointer, PR #9 fix naming the `GITHUB_TOKEN`
merge-on-green workflow as the alternative path).
