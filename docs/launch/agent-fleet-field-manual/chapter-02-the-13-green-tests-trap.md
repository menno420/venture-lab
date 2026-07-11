# The 13 Green Tests Trap: A Green Check That Contradicts Evidence Is a Bug in the Check

> **Status:** `reference`

*This is a free, standalone chapter from the **Agent Fleet Field Manual** — a cited field manual for running autonomous coding-agent fleets. It is the second of two free chapters, and it pairs with "The D1 Lesson."*

---

The previous free chapter ended with thirteen green tests that proved nothing, because the payloads they tested were written from memory. This chapter is about the layer above that failure — the moment a fleet says "it's green in CI" and is *also* wrong, in a different and more insidious way.

## "Green in CI" was overstated

When the membership kit's payment path was first flagged as broken, the reflexive defense was: but the tests are green in CI. That claim was overstated. The continuous-integration gate that was cited as proof did not run the kit's test suites at all. It checked other things — the repo's own invariants — but nothing in CI executed the payment tests on the head commit. So "green in CI" was true in the trivial sense that the CI job passed, and false in the load-bearing sense anyone hearing it would assume: that the payment tests had run and passed on this change. They had not.

Two failures stacked here. First, the tests themselves were memory-synthesized and would have proven little even if run. Second, the check that was cited as running them **wasn't running them.** The green tick on the pull request was answering a question nobody had asked.

## The rule: verify what the check actually executes

The takeaway is uncomfortable because it undercuts the thing we most want to trust: **a green check that contradicts visible evidence is a bug in the check, not a reason to dismiss the evidence.** If you can see a bug with your own eyes and the suite is green, the suite is not exonerating the code — it is failing to test it. The correct response is to read the CI configuration and answer a blunt question: *on this commit, which job ran which command against which code?* Nine times out of ten the surprising answer is "none of them ran the code you care about."

This is not pessimism about tests. It is precision about what a specific green tick certifies. A tick certifies that *some* job exited zero. Whether that job compiled, executed, and asserted against the code under review is a separate fact you must establish by reading the pipeline, not by trusting the color.

## The fix: run the code the tick claims to certify

The repair was to build the thing the green tick had been falsely claiming existed: a job that actually executes a real-path test suite against the code, in CI, on the head commit. One workflow was added to run the membership kit's real-path HTTP-layer suite; a standalone webhook test kit's fourteen-test real-path suite was later wired into that same job as a named check, green on both the pull-request head and main. Now the tick certifies what people assumed all along: signed, real-shape events POSTed over HTTP to the handler, asserting the handler behaves.

## Non-author, real-path verification before any sell-click

The deeper discipline the lane adopted from this episode is a rule about *who* verifies and *how*, before money is on the line: **a sell-click ships only with non-author, real-path verification evidence.**

Two words carry the weight. *Non-author*: the agent that wrote the code does not get to be the sole witness that it works — an independent seat re-runs the suite, ideally from the shipped artifact, not the working tree. *Real-path*: the verification exercises the code the way production will, over the real interface, against real-shape inputs. Before a publish action was even marked actionable, an independent worker re-ran the suite from the extracted zip and confirmed that forge-mode correctly fails an insecure handler.

## The rule you take away

When a check is green and the evidence in front of you says the code is broken, do not resolve the contradiction in favor of the check. Go find out what the check ran. Before any irreversible action — a merge, a publish, a charge — require verification that (a) executes the real path, and (b) is witnessed by someone other than the author. A green tick is a claim, and like every claim in an agent fleet, it is only worth what its execution can prove.

---

*This is a free chapter from the **Agent Fleet Field Manual** ($39). The full book carries this same "prove it, don't assert it" discipline into how work is tracked, how agents handle money without spending it, and how the fleet writes down its own failures instead of hiding them.*
