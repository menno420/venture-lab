#!/usr/bin/env python3
"""Tests for scripts/check_owner_queue_idempotent.py — the OWNER-QUEUE idempotence guard.

Run from the scripts/ directory:
    python3 -m unittest test_check_owner_queue_idempotent -v

Covers:
  * the guard PASSES on the current clean repo tree — the committed
    OWNER-QUEUE.md is byte-identical to a fresh regeneration (idempotent), and
    the guard actually parsed some packets (not a vacuous skip);
  * the guard CATCHES a HAND-EDIT to the generated file (someone edited the
    queue directly instead of the packets) — proving the guard works, not just
    that it is green;
  * the guard CATCHES an INPUT DRIFT — a vetting packet changed but the queue
    was not regenerated, so the committed file no longer reflects its inputs;
  * the guard SKIPS (exit 0, never a false red) on a tree with no packets.

The catch-cases build a self-consistent fixture: real vetting packets + the
keyword map are copied into a temp root, the "committed" queue is generated with
the guard's OWN `regenerate` (so the clean fixture is idempotent by
construction), then perturbed. This never depends on hard-coded queue bytes.
"""

import os
import shutil
import tempfile
import unittest

import check_owner_queue_idempotent as guard


def _seed_fixture(root):
    """Copy the real inputs into `root` and generate an idempotent queue there."""
    src = guard.REPO_ROOT
    shutil.copytree(
        os.path.join(src, guard.VETTING_DIR_REL),
        os.path.join(root, guard.VETTING_DIR_REL),
    )
    shutil.copy(
        os.path.join(src, guard.KEYWORD_MAP_REL),
        os.path.join(root, guard.KEYWORD_MAP_REL),
    )
    content, n = guard.regenerate(root)
    with open(os.path.join(root, guard.OWNER_QUEUE_REL), "w", encoding="utf-8") as fh:
        fh.write(content)
    return n


class CleanTreeTest(unittest.TestCase):
    """The guard must be green on the real repo tree."""

    def test_live_tree_is_idempotent(self):
        status, detail = guard.check(guard.REPO_ROOT)
        self.assertEqual(
            status,
            "ok",
            "committed OWNER-QUEUE.md should be idempotent under the generator; "
            "got {s}:\n{d}".format(s=status, d=detail),
        )

    def test_live_tree_actually_parsed_packets(self):
        # Guard against a vacuous pass: the regeneration must have consumed real
        # packets, otherwise "ok" would be meaningless.
        _content, n_packets = guard.regenerate(guard.REPO_ROOT)
        self.assertGreater(n_packets, 0, "expected the live tree to carry vetting packets")

    def test_main_exit_zero_on_clean_tree(self):
        self.assertEqual(guard.main(["--quiet"]), 0)


class DriftCatchTest(unittest.TestCase):
    """The guard must CATCH a hand-edit or an un-regenerated input drift."""

    def setUp(self):
        self.root = tempfile.mkdtemp(prefix="oqidem-")
        self.n = _seed_fixture(self.root)
        self.queue = os.path.join(self.root, guard.OWNER_QUEUE_REL)

    def tearDown(self):
        shutil.rmtree(self.root, ignore_errors=True)

    def test_clean_fixture_passes(self):
        # Sanity: the seeded fixture is idempotent by construction.
        self.assertGreater(self.n, 0)
        status, detail = guard.check(self.root)
        self.assertEqual(status, "ok", detail)
        self.assertEqual(guard.main(["--root", self.root, "--quiet"]), 0)

    def test_catches_hand_edit_of_generated_file(self):
        # Someone edits the GENERATED file directly (the exact thing its header
        # forbids) instead of the packets.
        with open(self.queue, "a", encoding="utf-8") as fh:
            fh.write("\n<!-- hand-edited by an owner, not regenerated -->\n")
        status, detail = guard.check(self.root)
        self.assertEqual(status, "drift", "expected a hand-edit to be caught")
        self.assertIn("hand-edited by an owner", detail)
        self.assertEqual(guard.main(["--root", self.root, "--quiet"]), 1)

    def test_catches_input_drift_without_regen(self):
        # A vetting packet's Title changes but the queue is NOT regenerated, so
        # the committed queue no longer reflects its inputs. Editing the Title
        # line propagates into every rendered "<Title> — ..." heading/label.
        vdir = os.path.join(self.root, guard.VETTING_DIR_REL)
        ppath = text = None
        for name in sorted(p for p in os.listdir(vdir) if p.endswith(".md")):
            candidate = os.path.join(vdir, name)
            with open(candidate, encoding="utf-8") as fh:
                body = fh.read()
            if "# Title Vetting" in body:
                ppath, text = candidate, body
                break
        self.assertIsNotNone(ppath, "no fixture packet carried a '# Title Vetting' line")
        drifted = text.replace(
            "# Title Vetting", "# Title Vetting — DRIFTED TITLE MARKER", 1
        )
        self.assertNotEqual(text, drifted, "fixture packet lacked the expected Title line")
        with open(ppath, "w", encoding="utf-8") as fh:
            fh.write(drifted)
        status, detail = guard.check(self.root)
        self.assertEqual(status, "drift", "expected an un-regenerated input drift to be caught")
        self.assertEqual(guard.main(["--root", self.root, "--quiet"]), 1)


class NoPacketsSkipTest(unittest.TestCase):
    """A tree with no packets must SKIP (exit 0), never false-red."""

    def test_no_packets_skips_green(self):
        root = tempfile.mkdtemp(prefix="oqidem-empty-")
        try:
            status, _detail = guard.check(root)
            self.assertEqual(status, "skip")
            self.assertEqual(guard.main(["--root", root, "--quiet"]), 0)
        finally:
            shutil.rmtree(root, ignore_errors=True)


if __name__ == "__main__":
    unittest.main()
