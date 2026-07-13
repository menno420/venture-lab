# 5. Dead-session recovery: forward-only continuity

## The failure you should plan for

Long-form drafting runs die: the tool crashes, the API blips, the
session hits a limit mid-chapter. The question that decides whether
you lose a book is not "did it die" but **"what state did it leave,
and can a cold successor resume from it?"** This chapter is the
production lane's answer, anchored to a real worked case.

## The worked case

A drafting run for a 12-chapter holiday novella died on a transient
API error. Its chapter commits existed only locally — from the
outside, the work had died at **zero words pushed**. What made it
recoverable:

1. **The run had declared itself before working.** Its first pushed
   commit was a status record marked *in-progress* — so the dead run
   was visible AS a dead run, with its scope and plan readable, not a
   mystery branch.
2. **A closer marked the death honestly.** Rather than deleting the
   evidence or quietly restarting, the failed attempt was closed as
   incomplete *with a seam pointer left*: exactly what was done,
   exactly where a successor should pick up.
3. **The resume went forward-only, on the same record.** A new run
   picked up the same branch and the same status record, finished the
   draft, and adopted the corrective habit mid-slice: **push after
   every commit** from then on. Result: from zero words pushed to a
   merged, complete 15,995-word manuscript.

## The protocol, generalized

`templates/recovery-checklist.md` operationalizes it; the rules:

- **Declare before drafting** (the writing-lane version of a
  heartbeat): a committed plan/status note that says what run this
  is, its band, its chapter plan, and *in-progress*. Cost: one
  minute. Value: your successor — probably you, tomorrow — resumes
  from a record instead of archaeology.
- **Commit at chapter boundaries; push after every commit.** The
  worked case's only real loss window was local-only commits. Work
  that isn't pushed (or synced, in non-git terms: saved to the cloud
  folder, exported from the chat) does not exist for recovery
  purposes.
- **Diagnose before resuming — died-at-zero vs half-landed.** Count
  what actually survived (`wc -w` the files at the remote, not in
  your dead workspace). A half-landed draft needs a continuity
  re-read of the survived chapters against `CANON.md` before writing
  chapter N+1; a died-at-zero needs only the plan.
- **Forward-only, always.** Never rewrite the record of the failed
  attempt to look cleaner; append the resume to it. The failure
  record with its seam pointer IS the recovery mechanism, and
  scrubbing it re-creates the mystery you were preventing.
- **Bake the lesson in the same run.** The worked case didn't file
  "push more often" as future advice — it switched habit mid-resume
  and recorded that it had.

## Honesty block

This protocol was executed by agent sessions under a CI gate that
structurally refuses to merge work whose status record still says
in-progress — that enforcement made honesty *cheaper than lying*. A
solo writer gets the checklist but not the enforcement (chapter 1's
caveat, again). Also: one worked case is one worked case; the
protocol generalizes cleanly, but its production evidence is a single
death-and-resume, not a statistics table.

---

**Sources:** `candidates/adult-novels/the-twelfth-cake/DECISIONS.md@3b159d9`
("Production/metering": the transient-API death, local-only chapter
commits, close-as-incomplete with seam pointer, same-branch resume,
push-after-every-commit adopted mid-slice) ·
`docs/current-state.md@79a1987` (the case's ledger record: the failed
run resumed and MERGED, complete 15,995w manuscript on disk) ·
`.sessions/2026-07-13-twelfth-cake-manuscript.md@3b159d9` (the resume
run's own close-out record).
