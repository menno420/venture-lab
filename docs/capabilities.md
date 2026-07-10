# venture-lab capability manifest

> **Status:** `living-ledger` — this lane's copy of the fleet capability
> manifest (`menno420/fleet-manager` `docs/capabilities.md`, carried over at
> seed 2026-07-09). **Read this before declaring anything impossible.** A new
> capability or wall discovered = append it here the same session. Verified
> walls with exact error text live in [`PLATFORM-LIMITS.md`](PLATFORM-LIMITS.md)
> — **probing a documented wall twice is a bug.**

## CAN — capabilities sessions routinely deny having (with the recipe)

### View video / audio files (.mp4, .webm, .mov, .mp3, …)
Sessions claim they can't view an .mp4. They CAN:

```bash
ffprobe -v error -show_format -show_streams <file>          # inspect codecs/duration first
ffmpeg -i <file> -vf "fps=0.5" -q:v 2 frames_%03d.jpg       # extract frames into the scratchpad
```

Then `Read` the extracted frames as images — one frame every 2 seconds at
`fps=0.5`; raise/lower the fps for denser/sparser sampling. Audio tracks:
extract with `ffmpeg -i <file> -vn audio.wav` and process from there.

### View images and PDFs
`Read` them directly — the Read tool renders images visually and reads PDFs
page-by-page (`pages` parameter). No conversion step needed.

### Use provisioned secrets
Sessions forget tokens exist. **CHECK THE ENVIRONMENT FIRST:**

```bash
printenv | grep -iE 'token|key|railway|discord'
```

Confirm **presence only** (names, not values) — **never echo full secret
values into logs, files, or transcripts**. Use them via the env var.

### First commit to an empty repo
`git push` to a truly empty repo fails through the proxy tooling. Make the
first commit via the **Contents API** (`create_or_update_file` / `push_files`)
— that creates `main`, and normal git works from then on. (Fleet playbook R13;
this repo was bootstrapped exactly this way, 2026-07-09.)

### Arm auto-merge while checks are pending
GitHub refuses to arm auto-merge on an already-green PR — arm it **at PR
creation, in the checks-pending window** (`enable_pr_auto_merge`). This is the
sanctioned merge path; see the self-merge wall in
[`PLATFORM-LIMITS.md`](PLATFORM-LIMITS.md). (Fleet playbook R5/R12.)

### Run any repo's own checkers locally
Clone (or fetch) the repo and run its own gates — `bootstrap.py check
--strict`, pytest suites — before pushing. Nothing restricts a session to the
repo it was launched for.

### Read files from other public repos without extra scope
`WebFetch` on `https://raw.githubusercontent.com/<owner>/<repo>/<ref>/<path>`
works cross-repo for public content — no token scope or `add_repo` needed for
read-only single-file pulls.

### Spawn subagents for parallel work
The Agent tool runs research/implementation/verification workers concurrently
— fan out independent lanes instead of serializing them. (Worker agents
themselves don't re-spawn; the manager/coordinator tier does.)

### Watch something over time
Use **blocking foreground waits** — `until [ $(date +%s) -ge $end ]; do sleep
5; done` — never background timers. Background timers silently drop the final
report. (Fleet playbook R4.)

### YouTube transcripts
`youtube_transcript_api` is IP-blocked from datacenter IPs — sessions conclude
transcripts are impossible. They aren't:

```bash
yt-dlp --skip-download --write-auto-sub <video-url>
```

works via its android-vr endpoint; then parse the resulting `.vtt` file.
(Discovered 2026-07-09, transcript+miner task.)

### Run parallel file-mutating workers in isolated worktrees
Parallel file-mutating subagents MUST run in isolated git worktrees (Agent
`isolation:'worktree'` or `EnterWorktree`), or be serialized. Observed
2026-07-10: two builders sharing one clone raced on git state —
candidate-02's `git add -A` swept candidate-01 v0.2's uncommitted files into
candidate-02's commit, landing both under one PR (#7, 6b4ad52) and muddling
attribution. Content was byte-identical/correct, but a dedicated PR per
workstream became impossible. Recipe: for concurrent builders touching the
working tree, pass `isolation:'worktree'` so each gets its own checkout; only
read-only parallel workers are safe in a shared clone.

## DISCOVERY RULE

Before declaring anything impossible:

1. **Check this file** and [`PLATFORM-LIMITS.md`](PLATFORM-LIMITS.md).
2. **Check `printenv`** (presence-grep above — the capability may be a
   provisioned credential).
3. **Attempt it once and capture the exact error** — verbatim, not paraphrased.

A new capability or wall discovered = **append it here the same session.** An
unrecorded discovery is a reminder the owner will have to give again.
