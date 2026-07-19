#!/usr/bin/env python3
"""Tests for scripts/sku_registry.py — the authoritative SKU-inference module.

Run from the scripts/ directory:
    python3 -m unittest test_sku_registry -v

Covers:
  * SKU ENUMERATION over a fixture tree (iter_skus sees built + unbuilt candidates,
    sorted; empty tree -> []);
  * the BUILT signal (is_built / built_skus keyed on the candidates/<sku>/dist/
    marker) — a candidate with no dist/ is not built;
  * REGISTERED surfaces (registered_surfaces + the launch/vetting/catalog set
    builders), including the catalog-ref whole-token match (no substring collision);
  * FUNNEL roles (funnel_roles / missing_roles / launch_files) under both live
    naming conventions and the enrichment-not-required rule;
  * the two documented ALLOWLISTS carry their live values;
  * fixture-ROOT support — every fact function accepts a `root` and reads only from
    it (nothing leaks from the live repo);
  * the live tree is non-vacuous — there really are built SKUs, launch rows, and
    vetting packets to enumerate (so a future regression can't pass as a silent
    empty tree).

Fixtures are tiny self-consistent synthetic trees, so the tests never depend on
the repo's exact SKU list.
"""

import os
import shutil
import tempfile
import unittest

import sku_registry as reg


def _write(path, text="x\n"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


def _make_built(root, sku):
    """Mark `sku` BUILT — candidates/<sku>/dist/ present."""
    os.makedirs(
        os.path.join(root, reg.CANDIDATES_DIR_REL, sku, reg.BUILD_MARKER),
        exist_ok=True,
    )


def _make_candidate(root, sku):
    """A candidate dir with NO build marker (present in the universe, not built)."""
    os.makedirs(os.path.join(root, reg.CANDIDATES_DIR_REL, sku), exist_ok=True)


def _make_launch(root, sku, files):
    """Create docs/launch/<sku>/ containing the named files."""
    for fname in files:
        _write(os.path.join(root, reg.LAUNCH_DIR_REL, sku, fname))


def _make_vetting(root, sku):
    _write(os.path.join(root, reg.VETTING_DIR_REL, sku + ".md"), "# packet\n")


def _write_catalog(root, slugs):
    rows = "\n".join("- [{s}]({s}/LISTING.md)".format(s=s) for s in slugs)
    _write(os.path.join(root, reg.CATALOG_REL), "# Catalog\n\n" + rows + "\n")


class EnumerationTest(unittest.TestCase):
    def setUp(self):
        self.root = tempfile.mkdtemp(prefix="skureg-enum-")

    def tearDown(self):
        shutil.rmtree(self.root, ignore_errors=True)

    def test_iter_skus_sees_built_and_unbuilt_sorted(self):
        _make_built(self.root, "beta-kit")
        _make_candidate(self.root, "alpha-kit")  # no dist/
        self.assertEqual(reg.iter_skus(self.root), ["alpha-kit", "beta-kit"])

    def test_iter_skus_empty_tree(self):
        self.assertEqual(reg.iter_skus(self.root), [])


class BuiltSignalTest(unittest.TestCase):
    def setUp(self):
        self.root = tempfile.mkdtemp(prefix="skureg-built-")

    def tearDown(self):
        shutil.rmtree(self.root, ignore_errors=True)

    def test_is_built_true_only_with_marker(self):
        _make_built(self.root, "packaged-kit")
        _make_candidate(self.root, "wip-kit")  # candidate dir, no dist/
        self.assertTrue(reg.is_built("packaged-kit", self.root))
        self.assertFalse(reg.is_built("wip-kit", self.root))
        self.assertFalse(reg.is_built("does-not-exist", self.root))

    def test_built_skus_set(self):
        _make_built(self.root, "packaged-kit")
        _make_candidate(self.root, "wip-kit")
        self.assertEqual(reg.built_skus(self.root), {"packaged-kit"})


class RegisteredSurfacesTest(unittest.TestCase):
    def setUp(self):
        self.root = tempfile.mkdtemp(prefix="skureg-reg-")

    def tearDown(self):
        shutil.rmtree(self.root, ignore_errors=True)

    def test_surfaces_reflect_present_registries(self):
        _make_launch(self.root, "foo-kit", ("listing-copy.md",))
        _make_vetting(self.root, "foo-kit")
        _write_catalog(self.root, ["foo-kit"])
        self.assertEqual(
            reg.registered_surfaces("foo-kit", self.root),
            {"launch", "vetting", "catalog"},
        )

    def test_surfaces_partial(self):
        _make_launch(self.root, "bar-kit", ("listing-copy.md",))
        # no vetting, no catalog
        self.assertEqual(reg.registered_surfaces("bar-kit", self.root), {"launch"})

    def test_set_builders(self):
        _make_launch(self.root, "foo-kit", ("listing-copy.md",))
        _make_vetting(self.root, "foo-kit")
        _write_catalog(self.root, ["foo-kit"])
        self.assertEqual(reg.launch_skus(self.root), {"foo-kit"})
        self.assertEqual(reg.vetting_skus(self.root), {"foo-kit"})
        # catalog_refs returns every whole path token (the slug AND the trailing
        # `md` of `LISTING.md`) — the sku slug must be among them.
        self.assertIn("foo-kit", reg.catalog_refs(self.root))

    def test_catalog_refs_whole_token_no_substring_collision(self):
        refs = reg.catalog_refs_from_text("see [pro](foo-kit-pro/LISTING.md) here\n")
        self.assertIn("foo-kit-pro", refs)
        self.assertNotIn("foo-kit", refs)

    def test_catalog_refs_absent_file_is_empty(self):
        self.assertEqual(reg.catalog_refs(self.root), set())


class FunnelRolesTest(unittest.TestCase):
    def setUp(self):
        self.root = tempfile.mkdtemp(prefix="skureg-funnel-")

    def tearDown(self):
        shutil.rmtree(self.root, ignore_errors=True)

    def test_modern_convention_satisfies_all(self):
        _make_launch(self.root, "modern-kit", ("listing-copy.md", "owner-actions.md"))
        self.assertEqual(
            reg.funnel_roles("modern-kit", self.root),
            {"landing/sales copy", "owner publish action"},
        )
        self.assertEqual(reg.missing_roles(reg.launch_files(self.root, "modern-kit")), [])

    def test_legacy_convention_satisfies_all(self):
        _make_launch(self.root, "legacy-kit", ("LISTING.md", "publish-owner-action.md"))
        self.assertEqual(
            reg.funnel_roles("legacy-kit", self.root),
            {"landing/sales copy", "owner publish action"},
        )

    def test_enrichment_only_satisfies_nothing(self):
        _make_launch(self.root, "bare-kit", ("one-pager.md",))
        self.assertEqual(reg.funnel_roles("bare-kit", self.root), set())
        missing = reg.missing_roles(reg.launch_files(self.root, "bare-kit"))
        self.assertEqual(len(missing), 2)

    def test_launch_files_absent_dir_is_none(self):
        self.assertIsNone(reg.launch_files(self.root, "no-such-kit"))

    def test_funnel_roles_absent_folder_is_empty(self):
        self.assertEqual(reg.funnel_roles("no-such-kit", self.root), set())


class AllowlistTest(unittest.TestCase):
    def test_documented_allowlists_carry_live_values(self):
        self.assertIn("bundle-starter", reg.BUNDLE_TEMPLATES)
        self.assertIn("photo-packs", reg.OWNER_GATED_LANES)
        self.assertEqual(reg.BUILD_MARKER, "dist")


class FixtureRootIsolationTest(unittest.TestCase):
    """Every fact function reads ONLY from its `root` — nothing leaks from the repo."""

    def test_empty_fixture_root_sees_nothing(self):
        root = tempfile.mkdtemp(prefix="skureg-iso-")
        try:
            self.assertEqual(reg.iter_skus(root), [])
            self.assertEqual(reg.built_skus(root), set())
            self.assertEqual(reg.launch_skus(root), set())
            self.assertEqual(reg.vetting_skus(root), set())
            self.assertEqual(reg.catalog_refs(root), set())
            self.assertEqual(reg.registered_surfaces("anything", root), set())
            self.assertEqual(reg.funnel_roles("anything", root), set())
        finally:
            shutil.rmtree(root, ignore_errors=True)


class LiveTreeNonVacuityTest(unittest.TestCase):
    """The live repo really has SKUs to enumerate — a regression can't pass as empty."""

    def test_live_tree_has_built_launch_vetting(self):
        self.assertGreater(len(reg.built_skus(reg.REPO_ROOT)), 0)
        self.assertGreater(len(reg.launch_skus(reg.REPO_ROOT)), 0)
        self.assertGreater(len(reg.vetting_skus(reg.REPO_ROOT)), 0)


if __name__ == "__main__":
    unittest.main()
