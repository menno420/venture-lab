# Quick start

## 0. Verify the bundle (one minute, no network)

All three recipes are plain GitHub Actions YAML. Prove they parse on your
machine with a stock loader (PyYAML):

```sh
python3 -c "import yaml,glob; [yaml.safe_load(open(p)) for p in sorted(glob.glob('recipes/*.yml'))]; print('3 recipes parse OK')"
```

No PyYAML installed? Run the stdlib structural check instead (weaker —
verifies UTF-8 + the required top-level keys, not full YAML grammar):

```sh
python3 - <<'EOF'
import glob
for p in sorted(glob.glob('recipes/*.yml')):
    t = open(p, encoding='utf-8').read()
    assert all(k in t for k in ('name:', 'on:', 'jobs:')), p
    print(p, 'structural OK')
EOF
```

## 1. Two one-time repo settings (owner/admin UI — nothing works without them)

The enabler is **INERT** until both exist. Neither can be set by a
workflow; an owner/admin flips them in the UI (chapter 6 explains why the
agent can't, and why that's correct):

1. **Settings → General → Pull Requests → "Allow auto-merge" = ON.**
2. **A ruleset on the default branch REQUIRING your gate's context name**
   (this repo's gate reports as `substrate-gate` — rename consistently).
   Then **verify from the API** that a fresh PR shows `blocked`/`pending`
   while the gate runs — guide chapter 3 explains why the settings page
   alone is not proof.

## 2. Install order

1. `recipes/substrate-gate.yml` → `.github/workflows/` — the required gate
   with the born-red HOLD. Adjust: your journal path (`.sessions/*.md`),
   your coordination prefix (`control/`), and swap this repo's
   `bootstrap.py check` steps for your own test/lint commands at the marked
   lines. Preserve the born-red HOLD rule.
2. `recipes/auto-merge-enabler.yml` → `.github/workflows/` — the landing
   path. Adjust: your agent branch namespace (`claude/*`); optionally add a
   `ROUTINE_PAT`/`MERGE_PAT` secret so merges attribute to a real user
   instead of `github-actions[bot]`. Confirm the gate name it waits on
   matches your required context.
3. `recipes/auto-merge-enabler-minimal.yml` — optional, for reading the
   skeleton, or as a starting point ONLY if none of your PRs get their
   opt-out label after open (its header states the condition). Don't run it
   alongside the full enabler.

## 3. Teach the fleet the choreography

Each agent session, in commit order: journal file **first**
(`Status: in-progress` — the gate holds the PR red by design), then work
commits, then the ender commit flips the journal to `complete`; push; open
the PR **READY** (never draft — ready-flips are GraphQL-only and
quota-fragile at fleet scale). The enabler arms at open; the gate greens on
the flip; the PR lands itself. The seat performs **no** merge and **no**
arm.

## 4. When a green PR doesn't land

Guide chapter 7 is the diagnostic flow. The two most common:

- **API/MCP-created PR fired no workflow at open** → push one commit (even
  `git commit --allow-empty`); the `synchronize` event arms the
  already-green PR. Better: push the branch first, then open the PR.
- **The required check never reported (pending forever)** → never
  `paths-ignore` a required check; make it an in-job short-circuit that
  always reports green.

## 5. When a self-merge is denied

First denial is terminal — do not retry, and do not retry through a synonym
(REST instead of GraphQL, arm instead of merge). The denial means it was
always the workflow's job: push and open READY, and let the enabler arm
(guide chapter 6). Record the denial verbatim so the next session doesn't
re-probe the same wall.
