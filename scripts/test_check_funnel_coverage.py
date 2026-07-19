#!/usr/bin/env python3
"""Tests for scripts/check_funnel_coverage.py — the funnel-coverage advisory.

Run from the scripts/ directory:
    python3 -m unittest test_check_funnel_coverage -v

Covers:
  * the checker is GREEN on the current clean repo tree — every cross-sell
    cluster resolves to a linked `*-lead-magnet.md` funnel-top, so it warns on
    none (the LM-1/LM-2 magnets, #250/#251, closed the last gaps);
  * on a temp fixture it CORRECTLY WARNS on an UNCOVERED cluster (a SKU list
    with no funnel-top) — proving the advisory fires, not just that it is quiet;
  * on the same fixture a COVERED cluster (its funnel-top file present) is NOT
    warned — proving coverage is detected via the actual magnet, not hardcoded;
  * the script ALWAYS exits 0 (advisory contract), covered or uncovered.
"""

import os
import shutil
import tempfile
import unittest

import check_funnel_coverage as checker


def _write(root, rel, text):
    path = os.path.join(root, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


# A minimal but realistic Cross-sell clusters section: a Payments cluster with a
# linked funnel-top row (COVERED), an Analytics cluster whose magnet FILE exists
# (COVERED via the file), and a Scheduling cluster with a SKU list but no
# funnel-top anywhere (UNCOVERED — the case the advisory must catch).
FIXTURE_CATALOG = (
    "# Catalog\n\n"
    "## Bundles & cross-sell map\n\n"
    '**Cross-sell clusters (for storefront "you may also like"):**\n'
    "- **Payments-cluster funnel-top (free discovery asset):** the free "
    "lead-magnet article "
    "[`payments-lead-magnet.md`](payments-lead-magnet.md) — teaches the shared "
    "payments pain and funnels the payments cluster.\n"
    "- **Payments cluster:** Checkout Kit → Refund Kit → Payments Bundle.\n"
    "- **Analytics cluster:** Events Kit ↔ Dashboard Kit → Analytics Bundle.\n"
    "- **Scheduling cluster:** Cron Kit → Calendar Kit → Scheduling Bundle.\n\n"
    "---\n"
)


class CleanTreeTest(unittest.TestCase):
    """The checker must be green (zero warnings) on the real repo tree."""

    def test_live_tree_has_no_uncovered_clusters(self):
        results, note = checker.evaluate(checker.REPO_ROOT)
        self.assertEqual(note, "", "unexpected skip on the live tree: " + note)
        self.assertGreater(len(results), 0, "expected to find cross-sell clusters")
        uncovered = [name for name, by in results if by is None]
        self.assertEqual(
            uncovered,
            [],
            "clean tree should have zero uncovered clusters, got: "
            + ", ".join(uncovered),
        )

    def test_main_exits_zero_on_clean_tree(self):
        self.assertEqual(checker.main([]), 0)


class FixtureCoverageTest(unittest.TestCase):
    """On a controlled fixture: warn the uncovered cluster, spare the covered."""

    def setUp(self):
        self.root = tempfile.mkdtemp(prefix="funnelcov-")
        _write(self.root, checker.CATALOG_REL, FIXTURE_CATALOG)
        # The Analytics funnel-top exists only as a FILE (no section link),
        # proving file-existence coverage. Payments is covered by the section
        # link + a file; Scheduling has neither.
        _write(
            self.root,
            "docs/launch/payments-lead-magnet.md",
            "# The payments funnel-top\n\nBody.\n",
        )
        _write(
            self.root,
            "docs/launch/analytics-lead-magnet.md",
            "# Everything wrong with your analytics pipeline\n\nBody.\n",
        )

    def tearDown(self):
        shutil.rmtree(self.root, ignore_errors=True)

    def test_uncovered_cluster_is_flagged(self):
        results, note = checker.evaluate(self.root)
        self.assertEqual(note, "")
        by_name = {name: by for name, by in results}
        self.assertIn("Scheduling", by_name)
        self.assertIsNone(
            by_name["Scheduling"],
            "Scheduling has a SKU list but no funnel-top — must be uncovered",
        )

    def test_covered_clusters_are_not_flagged(self):
        results, _ = checker.evaluate(self.root)
        by_name = {name: by for name, by in results}
        # Payments — covered by the section funnel-top row.
        self.assertIsNotNone(by_name.get("Payments"))
        # Analytics — covered by the existing magnet FILE (no section link).
        self.assertIsNotNone(by_name.get("Analytics"))

    def test_advisory_always_exits_zero_even_when_uncovered(self):
        # An uncovered cluster is a nudge, never a locked door.
        self.assertEqual(checker.main(["--root", self.root]), 0)


if __name__ == "__main__":
    unittest.main()
