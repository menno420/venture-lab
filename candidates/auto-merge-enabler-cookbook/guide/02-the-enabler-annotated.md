# 2 · The enabler workflow, annotated line by line

`recipes/auto-merge-enabler.yml` is the exact production workflow this
repo runs — copied verbatim, not paraphrased. This chapter walks every
guard in it and says what each one is defending against. Read it with the
file open; the annotations below follow the file top to bottom.

## The trigger

```yaml
on:
  pull_request:
    types: [opened, reopened, ready_for_review, synchronize]
```

Four events, and `synchronize` is the non-obvious one. `synchronize` fires
on **every push to the PR head**, so the enabler re-arms on every push.
Arming is idempotent and never merges anything itself (the merge stays
gated by the required check), so re-arming is free — and it closes the
green-behind stall: a fix-push after a red run, or a `git merge origin/main`
to catch up the base, re-arms on the up-to-date head without anyone
remembering to. `ready_for_review` covers the draft→ready flip; `reopened`
covers a closed-then-reopened PR.

## The permissions and concurrency

```yaml
permissions:
  contents: write
  pull-requests: write
concurrency:
  group: auto-merge-enabler-${{ github.event.pull_request.number }}
  cancel-in-progress: false
```

`contents: write` + `pull-requests: write` are the minimum to arm
auto-merge. The concurrency group is keyed per PR with
`cancel-in-progress: false`: two rapid pushes to the same PR serialize
their arm attempts instead of cancelling each other, so a late push never
kills the arm from an earlier one mid-flight.

## The eligibility gate (the `if:`)

```yaml
if: >-
  github.event.pull_request.head.repo.full_name == github.repository &&
  github.event.pull_request.draft == false &&
  (startsWith(github.head_ref, 'claude/')) &&
  !contains(github.event.pull_request.labels.*.name, 'do-not-automerge')
```

Four conjuncts, each a door you do not want open:

- **Same-repo head only.** Never arm a PR from a fork — a fork head is
  attacker-controlled and arming it would auto-merge untrusted code.
- **Non-draft only.** Drafts are work-in-visible-progress; don't arm them.
- **Your agent namespace only** (`claude/*` here — change it to yours).
  You are building a landing strip for your fleet, not for every branch.
- **Not opted out.** The `do-not-automerge` label means never arm
  (chapter 5). This payload-level check is the *first* line; a fresh
  API re-read (below) is the second, because the payload can be stale.

## Guard 1 — refuse to arm on zero required contexts

```yaml
- name: Refuse to arm unless the base branch requires status CONTEXTS
  id: rules
  run: |
    contexts="$(gh api "repos/$GITHUB_REPOSITORY/rules/branches/${{ github.base_ref }}" \
      --jq '[.[] | select(.type == "required_status_checks")
             | .parameters.required_status_checks // [] | .[].context]')"
    count="$(printf '%s' "$contexts" | python3 -c 'import json,sys; print(len(json.load(sys.stdin)))')"
    echo "required=$count" >> "$GITHUB_OUTPUT"
    if [ "$count" = "0" ]; then
      echo "::warning::… Refusing to arm; make 'substrate-gate' a required check first."
    fi
```

This is chapter 3's trap turned into a guard. If the base branch requires
zero status contexts, a PR is `clean` the instant it opens — there is
nothing pending, so arming auto-merge merges the PR *immediately* with no
gate. The guard counts required **contexts, not rules**: a
`required_status_checks` rule with an empty context list is still zero
contexts, still a hole. It refuses to arm on zero rather than inverting its
own gate. Every subsequent step is conditioned on `steps.rules.outputs.required
!= '0'`.

## Guard 2 — re-read the opt-out label FRESH

```yaml
- name: Re-check the do-not-automerge label FRESH (stale-payload race guard)
  id: label
  if: steps.rules.outputs.required != '0'
  run: |
    sleep 15
    labels="$(gh api "repos/$GITHUB_REPOSITORY/issues/$PR/labels" --jq '[.[].name] | join(",")')"
    case ",$labels," in
      *,do-not-automerge,*) echo "skip=1" >> "$GITHUB_OUTPUT" ;;
      *)                    echo "skip=0" >> "$GITHUB_OUTPUT" ;;
    esac
```

The event payload snapshots the PR's labels at open time. But an
API/MCP-created PR is typically opened first and *labeled in a second call
right after* — so the payload the `if:` above saw may not include the
opt-out label that exists a moment later. This guard sleeps a grace beat,
re-reads the labels from the API, and refuses to arm if the label is
present *now*. The file's own comment names the incident class that taught
it ("the kit #22 incident class" — a stale payload arming an opted-out PR).
This is why the minimal variant is labeled "only if none of your PRs get
their opt-out label after open."

## The arm itself

```yaml
- name: Enable native auto-merge (squash)
  if: steps.rules.outputs.required != '0' && steps.label.outputs.skip == '0'
  run: |
    if gh pr merge --auto --squash "$PR" --repo "$GITHUB_REPOSITORY"; then
      echo "Auto-merge enabled for PR #$PR — it merges when 'substrate-gate' is green."
    else
      echo "::warning::Could not enable auto-merge … REST merge-on-green is the landing path instead …"
    fi
```

`gh pr merge --auto --squash` is the arm. `--auto` is the whole point: it
does **not** merge now, it registers "merge when the requirements are met."
The requirement is the required check going green. If the arm succeeds, the
PR is now pre-armed and GitHub will squash it the moment `substrate-gate`
reports success. If the arm *fails* — a repo shape where GitHub
structurally refuses it — the failure message points at the fallback (REST
merge-on-green), so a refused arm is a signposted branch, not a dead end.

## The token choice

```yaml
env:
  GH_TOKEN: ${{ secrets.ROUTINE_PAT || secrets.GITHUB_TOKEN }}
```

Every step prefers a PAT and falls back to `GITHUB_TOKEN`. The file's
comment states the reason: a PAT attributes the eventual merge to a real
user. The fallback works — the five 2026-07-17 merges (chapter 1) are
`github-actions[bot]` doing exactly that, the `GITHUB_TOKEN` path in
action. There is a downstream consequence of the fallback that matters for
CI on `main`; chapter 7 covers it.

**Sources** (public repo `menno420/venture-lab`):
`.github/workflows/auto-merge-enabler.yml` @ `aa04700` (every guard,
comment, and the token/`if:`/trigger lines quoted above are verbatim from
this file); the arm's real effect verified via the five 2026-07-17
`github-actions[bot]` merge events in chapter 1.
