#!/usr/bin/env python3
"""Tests for scripts/check_owner_queue_staleness.py — the OWNER-QUEUE staleness guard (ENG-7).

Run from the scripts/ directory:
    python3 -m unittest test_check_owner_queue_staleness -v

Covers:
  * the guard PASSES on the current clean repo tree, and it actually EXERCISED each of
    the three invariants (not a vacuous skip): the companion carries resolvable
    cross-refs, a live product carries dated checkpoints, and some click-run carries a
    proofread-gated row;
  * INV-1 CATCHES a companion citing a decision D<n> that the queue lacks (renumber
    drift), and a companion citing a queue §N that does not exist;
  * INV-1 does NOT false-red a `§N` that references some OTHER doc on a line that never
    names OWNER-QUEUE;
  * INV-1 resolves inclusive ranges ("D22–D25") — a range whose upper bound dangles is
    caught;
  * INV-2 CATCHES a malformed checkpoint date and a self-contradictory T+n kill clock
    (T+7 → T+14 that is not +7 days), WITHOUT any wall-clock comparison;
  * INV-3 CATCHES a click-run with a native-speaker-proofread row that is not
    hard-gated;
  * the guard SKIPS (exit 0, never a false red) on a tree with no packets and no
    companion cross-refs.

The catch-cases build tiny self-consistent synthetic fixtures (a minimal packet tree,
or a queue+companion pair) and perturb them, rather than copying the live tree — so the
tests never depend on the repo's exact SKU/decision list.
"""

import os
import shutil
import tempfile
import unittest

import check_owner_queue_staleness as guard
import derive_owner_queue as gen


# --- fixture builders -------------------------------------------------------------

def _write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


# A minimal, self-consistent vetting packet with a §7 OWNER-GATE block. `killcheck`
# optionally adds a packet-level KILL-CHECK line; `proofread`/`blocked` control an NL
# proofread row; `title` names the packet.
def _packet(title, *, killcheck=None, proofread=False, blocked_word=True):
    lines = [
        "# Title Vetting — {t}".format(t=title),
        "",
        "## 7. ⚑ OWNER-GATE — checklist",
        "",
        "1. ⚑ Storefront pick: Gumroad (default — the click-script's HOW).",
        "",
    ]
    if killcheck:
        lines.append("KILL-CHECK: {k}".format(k=killcheck))
        lines.append("")
    lines.append(
        "- [ ] ⚑ **Owner:** storefront pick (Gumroad (default)) — or Lemon Squeezy."
    )
    if proofread:
        row = "- [ ] ⚑ **Owner:** native-speaker proofread pass approved/commissioned"
        if blocked_word:
            row += " (blocking quality gate for this title)."
        else:
            row += "."
        lines.append(row)
    lines.append(
        "- [ ] ⚑ **Owner:** the publish click + preview/test purchase + public URL copied."
    )
    lines.append("")
    return "\n".join(lines)


# A packet whose publish is DONE (product live), optionally with a KILL-CHECK line — so
# the derived tree has a §4 live group carrying checkpoints.
def _live_packet(title, killcheck):
    return "\n".join(
        [
            "# Title Vetting — {t}".format(t=title),
            "",
            "## 7. ⚑ OWNER-GATE — checklist",
            "",
            "KILL-CHECK: {k}".format(k=killcheck),
            "",
            "- [x] ⚑ **Owner:** Gumroad listing published at $29 — DONE 2026-07-12",
            "",
        ]
    )


def _seed_packets(root, packets):
    for name, text in packets.items():
        _write(os.path.join(root, guard.VETTING_DIR_REL, name), text)


def _seed_queue_and_companion(root, queue_text, companion_text):
    _write(os.path.join(root, guard.OWNER_QUEUE_REL), queue_text)
    _write(os.path.join(root, guard.COMPANION_REL), companion_text)


# --- live-tree green --------------------------------------------------------------

class CleanTreeTest(unittest.TestCase):
    """The guard must be green on the real repo tree, having exercised each invariant."""

    def test_live_tree_is_consistent(self):
        status, detail = guard.check(guard.REPO_ROOT)
        self.assertEqual(
            status,
            "ok",
            "live tree should be staleness-clean; got {s}:\n{d}".format(
                s=status, d="\n".join(detail) if isinstance(detail, list) else detail
            ),
        )

    def test_main_exit_zero_on_clean_tree(self):
        self.assertEqual(guard.main(["--quiet"]), 0)

    def test_inv1_actually_applicable_on_live_tree(self):
        applicable, findings = guard.check_companion_crossrefs(guard.REPO_ROOT)
        self.assertTrue(applicable, "expected the companion + queue to both be present")
        self.assertEqual(findings, [], findings)

    def test_inv2_actually_applicable_on_live_tree(self):
        # Guard against a vacuous pass: the live tree has a checkpointed live product.
        result, n = guard.parse_tree(guard.REPO_ROOT)
        self.assertGreater(n, 0)
        applicable, findings = guard.check_checkpoint_consistency(result)
        self.assertTrue(applicable, "expected a live product with dated checkpoints")
        self.assertEqual(findings, [], findings)

    def test_inv3_actually_applicable_on_live_tree(self):
        result, _n = guard.parse_tree(guard.REPO_ROOT)
        applicable, findings = guard.check_proofread_gate_integrity(result)
        self.assertTrue(applicable, "expected a click-run with a proofread-gated row")
        self.assertEqual(findings, [], findings)


# --- INV-1: companion cross-ref resolution ---------------------------------------

_QUEUE = "\n".join(
    [
        "# ⚑ Owner queue",
        "",
        "## 1. Decisions",
        "",
        "### D1 — Foo — Storefront pick",
        "",
        "### D2 — Bar — Storefront pick",
        "",
        "## 2. Click-run",
        "",
    ]
)


class Inv1CrossRefTest(unittest.TestCase):
    def setUp(self):
        self.root = tempfile.mkdtemp(prefix="stale-inv1-")

    def tearDown(self):
        shutil.rmtree(self.root, ignore_errors=True)

    def test_resolvable_refs_pass(self):
        companion = "See `OWNER-QUEUE.md` §1 and §2; decisions D1 and D2."
        _seed_queue_and_companion(self.root, _QUEUE, companion)
        applicable, findings = guard.check_companion_crossrefs(self.root)
        self.assertTrue(applicable)
        self.assertEqual(findings, [], findings)

    def test_catches_dangling_decision(self):
        # The companion cites D5, but the queue only has D1/D2 (renumber drift).
        companion = "Publish sequence D5 in `OWNER-QUEUE.md` §1."
        _seed_queue_and_companion(self.root, _QUEUE, companion)
        status = guard.check_companion_crossrefs(self.root)
        applicable, findings = status
        self.assertTrue(applicable)
        self.assertTrue(any("D5" in f and "DANGLING-DREF" in f for f in findings), findings)

    def test_catches_dangling_section(self):
        # §7 named on an OWNER-QUEUE line, but the queue has no ## 7. section.
        companion = "Full menu in `OWNER-QUEUE.md` §7."
        _seed_queue_and_companion(self.root, _QUEUE, companion)
        applicable, findings = guard.check_companion_crossrefs(self.root)
        self.assertTrue(any("§7" in f and "DANGLING-SECTION" in f for f in findings), findings)

    def test_range_upper_bound_dangling_is_caught(self):
        # "D1–D3" resolves D1/D2 but D3 is absent.
        companion = "Illustration decisions `OWNER-QUEUE.md` §1, D1–D3."
        _seed_queue_and_companion(self.root, _QUEUE, companion)
        applicable, findings = guard.check_companion_crossrefs(self.root)
        self.assertTrue(any("D3" in f for f in findings), findings)
        self.assertFalse(any("D1 " in f or "D2 " in f for f in findings), findings)

    def test_section_ref_to_other_doc_not_false_red(self):
        # §9 appears only on a line that references a DIFFERENT doc — not a queue ref.
        companion = "See `PUBLISHING-PLAN.md` §9 for the book lane. Queue: D1, D2."
        _seed_queue_and_companion(self.root, _QUEUE, companion)
        applicable, findings = guard.check_companion_crossrefs(self.root)
        self.assertEqual(findings, [], findings)

    def test_absent_companion_is_not_applicable(self):
        _write(os.path.join(self.root, guard.OWNER_QUEUE_REL), _QUEUE)
        applicable, findings = guard.check_companion_crossrefs(self.root)
        self.assertFalse(applicable)
        self.assertEqual(findings, [])


# --- INV-2: dated-checkpoint consistency ------------------------------------------

class Inv2CheckpointTest(unittest.TestCase):
    def setUp(self):
        self.root = tempfile.mkdtemp(prefix="stale-inv2-")

    def tearDown(self):
        shutil.rmtree(self.root, ignore_errors=True)

    def _result(self):
        result, _n = guard.parse_tree(self.root)
        return result

    def test_consistent_kill_clock_passes(self):
        _seed_packets(
            self.root,
            {"live.md": _live_packet(
                "Live Kit",
                "⏲ 2026-07-19 T+7 funnel checkpoint · ⏲ 2026-07-26 T+14 deadline",
            )},
        )
        applicable, findings = guard.check_checkpoint_consistency(self._result())
        self.assertTrue(applicable)
        self.assertEqual(findings, [], findings)

    def test_catches_contradictory_tplus_arithmetic(self):
        # T+7 → T+14 rendered 11 days apart (2026-07-30), not 7 — a self-contradiction.
        _seed_packets(
            self.root,
            {"live.md": _live_packet(
                "Live Kit",
                "⏲ 2026-07-19 T+7 funnel checkpoint · ⏲ 2026-07-30 T+14 deadline",
            )},
        )
        applicable, findings = guard.check_checkpoint_consistency(self._result())
        self.assertTrue(applicable)
        self.assertTrue(any("CHECKPOINT-ARITHMETIC" in f for f in findings), findings)

    def test_catches_malformed_date(self):
        # Month 13 is date-SHAPED but not a real calendar date.
        _seed_packets(
            self.root,
            {"live.md": _live_packet(
                "Live Kit", "⏲ 2026-13-19 T+7 funnel checkpoint",
            )},
        )
        applicable, findings = guard.check_checkpoint_consistency(self._result())
        self.assertTrue(any("BAD-CHECKPOINT-DATE" in f for f in findings), findings)

    def test_no_checkpoints_not_applicable(self):
        _seed_packets(self.root, {"plain.md": _packet("Plain Kit")})
        applicable, findings = guard.check_checkpoint_consistency(self._result())
        self.assertFalse(applicable)
        self.assertEqual(findings, [])


# --- INV-3: proofread-gate integrity ----------------------------------------------

class Inv3ProofreadGateTest(unittest.TestCase):
    def setUp(self):
        self.root = tempfile.mkdtemp(prefix="stale-inv3-")

    def tearDown(self):
        shutil.rmtree(self.root, ignore_errors=True)

    def _result(self):
        result, _n = guard.parse_tree(self.root)
        return result

    def test_hard_gated_proofread_row_passes(self):
        # A proofread row carrying the "blocking" continuation → group is blocked.
        _seed_packets(
            self.root, {"nl.md": _packet("NL Edition", proofread=True, blocked_word=True)}
        )
        result = self._result()
        applicable, findings = guard.check_proofread_gate_integrity(result)
        self.assertTrue(applicable)
        self.assertEqual(findings, [], findings)

    def test_catches_proofread_row_that_lost_hard_gate(self):
        # Sanity: the generator's own logic treats a bare proofread row as blocking,
        # so INV-3 can only fire if that logic regresses. Assert the invariant's
        # contract directly against a synthetic group whose `blocked` was forced False
        # despite carrying a proofread click — the exact drift INV-3 guards.
        group = gen.ClickGroup(title="Broken NL Edition", where="x", blocked=False)
        group.clicks.append(
            {
                "what": "native-speaker proofread pass approved/commissioned",
                "default": "",
                "linked": False,
            }
        )
        result = gen.ParseResult()
        result.groups.append(group)
        applicable, findings = guard.check_proofread_gate_integrity(result)
        self.assertTrue(applicable)
        self.assertTrue(any("PROOFREAD-GATE-DRIFT" in f for f in findings), findings)

    def test_no_proofread_row_not_applicable(self):
        _seed_packets(self.root, {"plain.md": _packet("Plain Kit")})
        applicable, findings = guard.check_proofread_gate_integrity(self._result())
        self.assertFalse(applicable)
        self.assertEqual(findings, [])


# --- skip / edge ------------------------------------------------------------------

class SkipTest(unittest.TestCase):
    def test_empty_tree_skips_green(self):
        root = tempfile.mkdtemp(prefix="stale-empty-")
        try:
            status, _detail = guard.check(root)
            self.assertEqual(status, "skip")
            self.assertEqual(guard.main(["--root", root, "--quiet"]), 0)
        finally:
            shutil.rmtree(root, ignore_errors=True)

    def test_full_check_catches_and_exits_nonzero(self):
        # An end-to-end STALE tree via INV-3: one packet whose group would be blocked
        # is fine; instead drive main() over a queue+companion with a dangling D-ref.
        root = tempfile.mkdtemp(prefix="stale-e2e-")
        try:
            _seed_queue_and_companion(root, _QUEUE, "Publish D9 in `OWNER-QUEUE.md` §2.")
            status, findings = guard.check(root)
            self.assertEqual(status, "stale")
            self.assertTrue(any("D9" in f for f in findings), findings)
            self.assertEqual(guard.main(["--root", root, "--quiet"]), 1)
        finally:
            shutil.rmtree(root, ignore_errors=True)


if __name__ == "__main__":
    unittest.main()
