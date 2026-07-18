#!/usr/bin/env python3
"""Tests for scripts/check_catalog_drefs.py — the OWNER-QUEUE D-ref guard.

Run from the scripts/ directory:
    python3 -m unittest test_check_catalog_drefs -v

Covers:
  * the guard PASSES on the current clean repo tree (the #245 resync made every
    cross-ref resolve), and the map is built from OWNER-QUEUE.md §1;
  * the guard CATCHES a deliberately MISPOINTED ref (a kit named beside the
    wrong decision number) on a temp fixture — proving the guard works, not
    just that it is green;
  * the guard CATCHES a DANGLING ref (a number the queue does not contain);
  * the guard does NOT false-positive on a historical renumber-arrow line
    (proving the exclusion scoping holds).
"""

import os
import shutil
import tempfile
import unittest

import check_catalog_drefs as guard


def _write(root, rel, text):
    path = os.path.join(root, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


# A minimal but realistic OWNER-QUEUE §1: GitHub=D6, Idempotency=D7, JWT=D9.
FIXTURE_QUEUE = (
    "# Owner queue\n\n"
    "## 1. Decisions — pick the default or override\n\n"
    "### D6 — GitHub Webhook Test Kit — Storefront pick\n\n"
    "### D7 — Idempotency Key Test Kit — Storefront pick\n\n"
    "### D9 — JWT Auth Test Kit — Storefront pick\n\n"
    "## 2. Click-run\n"
)


class CleanTreeTest(unittest.TestCase):
    """The guard must be green on the real repo tree."""

    def test_map_built_from_owner_queue(self):
        id_to_sku = guard.build_decision_map(guard.REPO_ROOT)
        # A few anchors from the post-#244 (CORS-folded) numbering.
        self.assertEqual(id_to_sku.get(4), "CORS Preflight Test Kit")
        self.assertEqual(id_to_sku.get(6), "GitHub Webhook Test Kit")
        self.assertEqual(id_to_sku.get(9), "JWT Auth Test Kit")
        self.assertEqual(id_to_sku.get(18), "Rate-Limit Test Kit")

    def test_clean_tree_has_no_dangling_or_mispointed_refs(self):
        errors, ref_count, files = guard.scan(guard.REPO_ROOT)
        self.assertEqual(
            errors, [], "clean tree should have zero D-ref errors:\n" + "\n".join(errors)
        )
        self.assertGreater(ref_count, 0, "expected to actually scan some D-refs")
        self.assertGreater(len(files), 0, "expected the allowlist to match files")

    def test_main_exit_zero_on_clean_tree(self):
        self.assertEqual(guard.main(["--quiet"]), 0)


class MispointCatchTest(unittest.TestCase):
    """The guard must CATCH a mispointed / dangling ref on a fixture tree."""

    def setUp(self):
        self.root = tempfile.mkdtemp(prefix="drefguard-")
        _write(self.root, guard.OWNER_QUEUE_REL, FIXTURE_QUEUE)

    def tearDown(self):
        shutil.rmtree(self.root, ignore_errors=True)

    def test_catches_mispointed_ref(self):
        # The GitHub row is labelled D9 (JWT's number) — a mispoint. The JWT
        # row is correct and must NOT be flagged.
        _write(
            self.root,
            "docs/launch/CATALOG.md",
            "| Product | Price | Status | Decision |\n"
            "| GitHub Webhook Test Kit | $29 | READY | D9 |\n"
            "| JWT Auth Test Kit | $29 | READY | D9 |\n",
        )
        errors, ref_count, _ = guard.scan(self.root)
        self.assertEqual(ref_count, 2)
        mispoints = [e for e in errors if e.startswith("MISPOINTED")]
        self.assertEqual(len(mispoints), 1, "expected exactly one mispoint:\n" + "\n".join(errors))
        self.assertIn("GitHub Webhook Test Kit", mispoints[0])
        self.assertIn("D9", mispoints[0])
        # And the checker exits non-zero.
        self.assertEqual(guard.main(["--root", self.root, "--quiet"]), 1)

    def test_catches_mispointed_ref_in_bundle_prose(self):
        # Prose form, matching the real bundle docs' per-kit carriers: each kit
        # on its own paragraph with its own parenthesised D-ref. The JWT
        # paragraph mispoints at D7 (JWT is D9); the Idempotency one is correct.
        _write(
            self.root,
            "docs/launch/api-robustness-bundle/owner-actions.md",
            "> The Idempotency Key Test Kit (D7) publish click is queued.\n"
            ">\n"
            "> The JWT Auth Test Kit (D7) publish click is queued.\n",
        )
        errors, _, _ = guard.scan(self.root)
        mispoints = [e for e in errors if e.startswith("MISPOINTED")]
        self.assertEqual(len(mispoints), 1, "\n".join(errors))
        self.assertIn("JWT Auth Test Kit", mispoints[0])

    def test_catches_dangling_ref(self):
        _write(
            self.root,
            "docs/launch/CATALOG.md",
            "| GitHub Webhook Test Kit | $29 | READY | D99 |\n",
        )
        errors, _, _ = guard.scan(self.root)
        dangling = [e for e in errors if e.startswith("DANGLING")]
        self.assertEqual(len(dangling), 1, "\n".join(errors))
        self.assertIn("D99", dangling[0])

    def test_historical_renumber_arrow_line_not_flagged(self):
        # A migration/renumber note ("GitHub D5→D6") carries an OLD number
        # beside a kit name. It is history, not a live cross-ref, and must NOT
        # be flagged — the renumber-arrow line is excluded by design.
        _write(
            self.root,
            "docs/launch/CATALOG.md",
            "> The CORS fold shifted every later decision up by one: "
            "False-Green D4→D5, GitHub D5→D6, Idempotency Key D6→D7.\n",
        )
        errors, _, _ = guard.scan(self.root)
        self.assertEqual(
            errors, [], "historical arrow line must not be flagged:\n" + "\n".join(errors)
        )


if __name__ == "__main__":
    unittest.main()
