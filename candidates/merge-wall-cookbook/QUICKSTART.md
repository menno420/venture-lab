# Quick start

## 0. Verify the bundle (one minute, no network)

Every recipe is plain GitHub Actions YAML. Prove they parse on your
machine with a stock loader (PyYAML):

```sh
python3 -c "import yaml,glob; [yaml.safe_load(open(p)) for p in sorted(glob.glob('recipes/*.yml'))]; print('4 recipes parse OK')"
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

## 1. One-time repo settings (owner/admin UI — no recipe works without them)

1. **Settings → General → Pull Requests → "Allow auto-merge" = ON**
   (Recipe 1 needs it; harmless for the rest).
2. **A ruleset/branch protection on your default branch REQUIRING your
   gate check's context name** (Recipe 3's job reports as
   `required-gate`; rename consistently). Then verify from the API that a
   fresh PR shows `blocked` while the gate runs — guide chapter 2 explains
   why the settings page alone is not proof.

## 2. Install order

1. `recipes/born-red-hold-gate.yml` → `.github/workflows/` — the required
   gate. Adjust: your journal path (`.sessions/*.md`), your coordination
   prefix (`control/`), and append your real test steps at the marked
   line.
2. `recipes/auto-merge-enabler.yml` → `.github/workflows/` — the landing
   path. Adjust: your agent branch namespace (`claude/*`); optionally add
   a `MERGE_PAT` secret so merges attribute to a real user.
3. `recipes/advisory-check.yml` → optional, for drift/hygiene signals
   that must never block a merge. Point it at your own signal script.
4. `recipes/merge-on-green.yml` → ONLY if native arm is structurally
   refused on your repo shape (guide ch. 7). Read its header honesty
   label; trial on a scratch repo first.

## 3. Teach the fleet the choreography

Each agent session, in commit order: journal file first
(`Status: in-progress` — the gate holds the PR red by design), work
commits, ender commit flips the journal to `complete`, push, open PR
READY (never draft — ready-flips are GraphQL-only and quota-fragile at
fleet scale). The enabler arms at open; the gate greens on the flip; the
PR lands itself.

## 4. What to do when a merge is denied anyway

First denial is terminal — do not retry, and do not retry through a
synonym (guide ch. 1). Record the denial verbatim in a committed ledger so
the next session doesn't re-probe the same wall.
