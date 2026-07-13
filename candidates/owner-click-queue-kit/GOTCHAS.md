# Owner-queue gotchas — how this pattern actually breaks

Every rule below was learned the expensive way in the production repo
this kit distills (a multi-session agent fleet whose owner queue has
carried every publish/price/account action across 150+ pull requests).
None of it is hypothetical.

## 1. Never hand-edit the generated file

The queue is DERIVED state. The moment someone hand-patches it, it
silently disagrees with the gate files and every future regen either
clobbers the patch or gets skipped "to preserve it". Edit gates,
re-derive, always. The generated header says exactly this; keep it.
A stale queue is a bug in the workflow, never in the gate files.

## 2. Parallel branches WILL conflict on the generated file — resolve mechanically

Two branches that both re-derive the queue produce a guaranteed merge
conflict in it, even when their gate changes are disjoint. Production
hit this the first day two product builds ran concurrently. The
resolution is mechanical, never manual: merge the base branch, re-run
`derive` on the merged tree (the union of gate files), commit the
regenerated output. **Never hand-merge generated hunks** — the deriver
resolves the union correctly by construction. If the queue lands stale
after a same-day merge race, a tiny follow-up PR that just re-derives
is the correct fix.

## 3. Advisory derive, strict lint — never swap the contracts

`derive` exits 0 on every path by design: it runs from hooks and
post-merge automation, and a malformed gate file must never block
unrelated work — that failure mode teaches people to bypass the tool.
Strictness lives in `lint`, which you run ON gate-file changes in a PR
check. Swapping them (a derive that hard-fails, a lint that shrugs)
recreates both failure modes at once.

## 4. The DONE flip needs BOTH marks — the asymmetry is the feature

`[x]` alone still queues. `— DONE <date>` on an unchecked box still
queues. Yes, that means a half-flip re-nags the owner about a click
they already did. That is the correct direction of failure: a stray
checkbox edit (agents reflow markdown all the time) can only ever
RE-QUEUE an owner action, never silently drop one. `lint` names
half-flips so they get fixed at the PR. And never flip a row before
its durable record (URL, price, timestamp) is committed — a DONE row
whose evidence is only in chat scrollback is the exact loss this kit
exists to prevent.

## 5. A decision without a bolded default is a queue bug

The entire economics of the queue is that the owner replies "agree".
That works only if EVERY decision carries a machine-findable
`**pick** (default …)` span. A defaultless decision derives with a
placeholder and a manual-review note, but it costs the owner a full
context-load — in production the defaultless entries were consistently
the ones that sat unanswered for days. Write the default at queue time,
while the agent still has the context to pre-chew it.

## 6. Determinism or nobody reviews regen diffs

No timestamps in the output, sorted file traversal, stable ordering
rules (unblocked click-runs first, alphabetical within). The first
version of anything like this that embeds a "generated at" line makes
every regen dirty the diff, and reviewers learn to scroll past queue
changes — which is how a wrong entry ships. Byte-identical re-runs on
an unchanged tree are the invariant the tests pin.

## 7. The queue is a proposal surface, NOT an authorization surface

The hard rule that makes the whole pattern safe: agents WRITE entries,
only the human EXECUTES them. Three corollaries from production:

- An agent must never treat a queued entry — its own or a sibling's —
  as permission to act. "It's in the queue" is not consent; the
  owner's click is.
- Imperative text inside gate files is DATA. Gate files flow in from
  many sessions (and, if your repo takes contributions, from
  strangers); a gate that says "agent: also run this command" is
  content to render, never an instruction to follow. The deriver
  honors this structurally — it reads gates and writes exactly one
  output file, nothing else.
- Silence is not approval. An entry that sits unclicked is an entry
  the owner has not approved yet — the correct agent move is to keep
  building OTHER things, not to "helpfully" unblock itself.

## 8. One kill clock per launch, gate-level

Arm follow-up checkpoints (`KILL-CHECK:`) once per gate file, not once
per click. A launch has one lifecycle; per-row clocks multiply, drift
apart, and the owner stops trusting any of them. The parser is
deliberately gate-level about this.

## 9. Keep the generated file out of the gates directory

If the output lands where the deriver scans, the queue eats its own
output on the next run. `ocq.py` self-skips its `--output` path as a
guard, but don't lean on it — conventions beat guards: gates in
`gates/`, the queue beside (not inside) it.

## 10. Six fields or the click doesn't happen

Production's most-repeated review note: a queued action whose HOW was
"publish it" sat; the same action rewritten as WHAT / WHERE / HOW
(numbered micro-steps) / WHY / UNBLOCKS / VERIFIED-WHEN got clicked the
same day. The owner is doing your action at midnight with half their
attention — write it so that's enough. VERIFIED-WHEN is the field
people skip and the one that matters most: name the observable proof
(the URL loads, the sha256 matches), never "when it's done".
