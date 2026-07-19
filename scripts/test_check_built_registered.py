#!/usr/bin/env python3
"""Tests for scripts/check_built_registered.py — the built↔registered inventory guard.

Run from the scripts/ directory:
    python3 -m unittest test_check_built_registered -v

Covers:
  * the guard PASSES on the current clean repo tree — every packaged candidate is
    registered and every launch row has its artifacts — and it actually saw some
    built SKUs (not a vacuous skip);
  * the guard CATCHES a BUILT-BUT-UNREGISTERED SKU (a packaged candidate with no
    launch row / vetting packet / catalog row) — the headline ENG-5 drift class;
  * the guard CATCHES a REGISTERED-BUT-MISSING-ARTIFACT SKU (a launch row whose
    build artifact / catalog row is missing);
  * the two documented exemptions hold (a compositional bundle scaffold with no
    build dir; an owner-gated lane excluded from the catalog) — so the guard is
    tolerant of the KNOWN current state without hiding real drift;
  * the catalog-ref token match does not false-positive on a substring collision;
  * the guard SKIPS (exit 0, never a false red) on a tree with no registries.

The catch-cases build a tiny self-consistent synthetic fixture (a built+launched+
vetted+cataloged SKU) and perturb it, rather than copying the live tree — so the
tests never depend on the repo's exact SKU list.
"""

import os
import shutil
import tempfile
import unittest

import check_built_registered as guard


def _write(path, text=""):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


def _register_sku(root, sku, *, built=True, launch=True, vetting=True, catalog=True):
    """Create the chosen registry entries for `sku` under `root`."""
    if built:
        os.makedirs(
            os.path.join(root, guard.CANDIDATES_DIR_REL, sku, guard.BUILD_MARKER),
            exist_ok=True,
        )
    if launch:
        _write(os.path.join(root, guard.LAUNCH_DIR_REL, sku, "listing-copy.md"), "x\n")
    if vetting:
        _write(os.path.join(root, guard.VETTING_DIR_REL, sku + ".md"), "# packet\n")
    return catalog  # catalog handled centrally by _seed_fixture


def _seed_fixture(root, skus=("foo-kit", "bar-kit"), catalog_slugs=None):
    """A self-consistent fixture: each sku built+launched+vetted+cataloged."""
    if catalog_slugs is None:
        catalog_slugs = list(skus)
    for sku in skus:
        _register_sku(root, sku)
    rows = "\n".join("- [{s}]({s}/LISTING.md)".format(s=s) for s in catalog_slugs)
    _write(
        os.path.join(root, guard.CATALOG_REL),
        "# Catalog\n\n" + rows + "\n",
    )


class CleanTreeTest(unittest.TestCase):
    """The guard must be green on the real repo tree."""

    def test_live_tree_is_consistent(self):
        status, detail = guard.check(guard.REPO_ROOT)
        self.assertEqual(
            status,
            "ok",
            "live tree should have built↔registered correspondence; got {s}:\n{d}".format(
                s=status, d="\n".join(detail) if isinstance(detail, list) else detail
            ),
        )

    def test_live_tree_actually_saw_built_skus(self):
        # Guard against a vacuous pass: there must be real built SKUs on the tree.
        reg = guard.collect(guard.REPO_ROOT)
        self.assertGreater(len(reg["built"]), 0, "expected packaged candidates on the live tree")
        self.assertGreater(len(reg["launch"]), 0, "expected launch rows on the live tree")

    def test_main_exit_zero_on_clean_tree(self):
        self.assertEqual(guard.main(["--quiet"]), 0)


class DriftCatchTest(unittest.TestCase):
    """The guard must CATCH both drift directions."""

    def setUp(self):
        self.root = tempfile.mkdtemp(prefix="builtreg-")
        _seed_fixture(self.root)

    def tearDown(self):
        shutil.rmtree(self.root, ignore_errors=True)

    def test_clean_fixture_passes(self):
        status, detail = guard.check(self.root)
        self.assertEqual(status, "ok", detail)
        self.assertEqual(guard.main(["--root", self.root, "--quiet"]), 0)

    def test_catches_built_but_unregistered(self):
        # A packaged candidate with no launch row / vetting packet / catalog row.
        os.makedirs(
            os.path.join(self.root, guard.CANDIDATES_DIR_REL, "orphan-kit", guard.BUILD_MARKER)
        )
        status, detail = guard.check(self.root)
        self.assertEqual(status, "drift", "expected a built-but-unregistered strand to be caught")
        self.assertTrue(
            any("BUILT-BUT-UNREGISTERED" in v and "orphan-kit" in v for v in detail),
            detail,
        )
        self.assertEqual(guard.main(["--root", self.root, "--quiet"]), 1)

    def test_catches_registered_but_missing_artifact(self):
        # A launch row + vetting packet + catalog row, but no built artifact.
        _register_sku(self.root, "ghost-kit", built=False)
        # add its catalog row so ONLY the missing build artifact trips the guard
        with open(os.path.join(self.root, guard.CATALOG_REL), "a", encoding="utf-8") as fh:
            fh.write("- [ghost-kit](ghost-kit/LISTING.md)\n")
        status, detail = guard.check(self.root)
        self.assertEqual(status, "drift", "expected a registered-but-missing-artifact to be caught")
        self.assertTrue(
            any(
                "REGISTERED-BUT-MISSING-ARTIFACT" in v
                and "ghost-kit" in v
                and "no built artifact" in v
                for v in detail
            ),
            detail,
        )
        self.assertEqual(guard.main(["--root", self.root, "--quiet"]), 1)

    def test_catches_launch_row_missing_catalog(self):
        # A launch row + vetting + build, but never added to the catalog.
        _register_sku(self.root, "uncataloged-kit")  # built+launch+vetting, no catalog row
        status, detail = guard.check(self.root)
        self.assertEqual(status, "drift")
        self.assertTrue(
            any("uncataloged-kit" in v and "CATALOG.md" in v for v in detail), detail
        )


class ExemptionTest(unittest.TestCase):
    """The documented known-current-state exemptions must NOT red."""

    def setUp(self):
        self.root = tempfile.mkdtemp(prefix="builtreg-exempt-")
        _seed_fixture(self.root)

    def tearDown(self):
        shutil.rmtree(self.root, ignore_errors=True)

    def test_bundle_template_needs_no_build_dir(self):
        # A compositional bundle scaffold: launch + vetting + catalog, no build dir.
        bundle = next(iter(guard.BUNDLE_TEMPLATES))
        _register_sku(self.root, bundle, built=False)
        with open(os.path.join(self.root, guard.CATALOG_REL), "a", encoding="utf-8") as fh:
            fh.write("- [{s}]({s}/LISTING.md)\n".format(s=bundle))
        status, detail = guard.check(self.root)
        self.assertEqual(status, "ok", detail)

    def test_owner_gated_lane_needs_no_catalog_or_build(self):
        # An owner-gated lane: launch + vetting only, no catalog row, no build dir.
        lane = next(iter(guard.OWNER_GATED_LANES))
        _register_sku(self.root, lane, built=False, catalog=False)
        status, detail = guard.check(self.root)
        self.assertEqual(status, "ok", detail)


class CatalogRefTest(unittest.TestCase):
    """The catalog-ref token match must not false-positive on a substring."""

    def test_substring_collision_is_not_a_match(self):
        refs = guard._catalog_refs("see [pro](foo-kit-pro/LISTING.md) here\n")
        self.assertIn("foo-kit-pro", refs)
        self.assertNotIn("foo-kit", refs)

    def test_plain_slug_paths_match(self):
        refs = guard._catalog_refs(
            "[a](membership-kit/LISTING.md) and [b](../vetting/jwt-auth-test-kit.md)\n"
        )
        self.assertIn("membership-kit", refs)
        self.assertIn("jwt-auth-test-kit", refs)


class NoRegistriesSkipTest(unittest.TestCase):
    """A tree with no registries must SKIP (exit 0), never false-red."""

    def test_empty_tree_skips_green(self):
        root = tempfile.mkdtemp(prefix="builtreg-empty-")
        try:
            status, _detail = guard.check(root)
            self.assertEqual(status, "skip")
            self.assertEqual(guard.main(["--root", root, "--quiet"]), 0)
        finally:
            shutil.rmtree(root, ignore_errors=True)


if __name__ == "__main__":
    unittest.main()
