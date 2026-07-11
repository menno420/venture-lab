# NEXT SESSION — venture-lab resume brief

> Rewritten at archive close-out 2026-07-11. Cold-start brief for the session
> that resumes venture-lab after the coordinator chat is archived. Read this
> first, then docs/retro/2026-07-11-coordinator-retro.md.

## Boot ritual

1. Land on `origin/main` HEAD (`git fetch origin main && git reset --hard origin/main`).
2. Read `control/inbox.md` at HEAD — MANAGER-written, append-only, orders stay
   `status: new`. **Never edit it.** Diff inbox orders against status.md `done=`
   lines to see what is unexecuted.
3. `python3 bootstrap.py check --strict` must be **exit 0** before any push.
4. Overwrite `control/status.md` **wholesale as the last step** of a turn.
5. Re-arm the wake chain per **ORDER 002** (see Wake mechanics).

## Repo map — what exists

### 4 sellable digital products (all UNPUBLISHED — sell-clicks are owner ⚑)
- **membership-kit** — $49 (⚑B). Real-Stripe-path fixed; fail-closed on partial config (#49).
- **template-packs** — $19 (⚑D).
- **Stripe webhook test-kit** — $29 (⚑E).
- **Agent Fleet field manual** — $39 (⚑F).

### Creative library (locations)
- Children's-book concepts — corpus + PRs #45 (6 originals) / #47 (adaptation track + Star Pirates).
- **DREAMLINE** series bible + Book 1 outline & ch 1–3 — PR #44.
- **Bababoefoe** plushy brand (stories + QR story-site + phased plan) — PR #46; needs ⚑G GitHub Pages.
- **photo-packs** — compliant watermarked previews merged (#52); originals exposure via #51 (see retro).

## Merge topology (critical)

Child seats **cannot self-land** — relayed or file-encoded authorization is never
genuine (4+ terminal classifier denials on 2026-07-11). Merges run from the
**coordinator seat** under the owner's **genuine in-session standing
instruction**, cited per action. **Never encode the grant into repo files** — an
[Instruction Poisoning] denial ruled that laundered authorization. A denial is
**terminal**: record verbatim, leave the PR READY + green, ⚑ the owner. Full
detail: docs/retro/2026-07-11-coordinator-retro.md.

## Wake mechanics

Coordinator seat lacks `send_later`; arm wake links via **Agent workers** calling
`mcp__claude-code-remote__send_later`. Idle cadence **45 min**; dedupe by
checking pending one-shots first. Failsafe cron was
`trig_01X1dw1L1Udgt8atzzNWEJic` (`0 */2 * * *`) — **not re-armed at archive**; a
fresh session re-arms per ORDER 002.

## Owner actions (⚑) — HOT first

1. **⚑ Close PR #51 + delete branch `menno420-patch-1`** (photo exposure). HOT.
2. **⚑ Disposition PR #38** (stale codex pre-publish review, superseded by #49).
3. **⚑B** membership-kit $49 · **⚑D** template-packs $19 · **⚑E** test-kit $29 · **⚑F** field manual $39.
4. **⚑** gotcha article · **⚑G** Bababoefoe GitHub Pages · **⚑A** Stripe test keys · **⚑** photo sales channel · **⚑** optional Supabase.

## Owner creative picks

- Manuscripts: Star Pirates / Comet Biscuit / Tummel / Dormouse (shortlist).
- Language per title · Star Pirates band · DREAMLINE 4 names + continue past ch3.

## Where the retro lives

- Chat-only knowledge: `docs/retro/2026-07-11-coordinator-retro.md`
- One-paragraph true state + full ⚑ list: `docs/retro/archive-ready-2026-07-11.md`
