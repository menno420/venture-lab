#!/usr/bin/env python3
"""Assembly / inventory check for the Webhook Verifier Bundle.

This is NOT a fifth product test suite — each component kit ships its own
`test_http_realpath` suite inside its zip and runs the same way it always has
(all four are green: run `python3 -m unittest test_http_realpath` in any
component dir). This check verifies the BUNDLE is assembled honestly:

  1. MANIFEST.json is internally consistent — four $29 components, the stated
     $79 price, $37 savings, and the discount percentage all reconcile.
  2. Every component kit named in the manifest exists on disk and its committed
     dist zip matches the pinned sha256 (no silent drift of a component).
  3. The built bundle zip (dist/webhook-verifier-bundle-v0.1.zip) contains
     exactly the four component zips (byte-for-byte, sha256-matched) plus the
     four docs — so what the buyer downloads is what the manifest promises.

Stdlib only. No network. Run: python3 -m unittest test_bundle -v
"""

from __future__ import annotations

import hashlib
import json
import unittest
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[1]
MANIFEST = json.loads((HERE / "MANIFEST.json").read_text(encoding="utf-8"))
BUNDLE_ZIP = HERE / "dist" / "webhook-verifier-bundle-v0.1.zip"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


class ManifestConsistency(unittest.TestCase):
    def test_four_components_each_29(self):
        comps = MANIFEST["components"]
        self.assertEqual(len(comps), 4, "bundle must name exactly four kits")
        self.assertEqual(
            [c["price_usd"] for c in comps], [29, 29, 29, 29],
            "each component is priced $29",
        )

    def test_pricing_math_reconciles(self):
        comps = MANIFEST["components"]
        total = sum(c["price_usd"] for c in comps)
        self.assertEqual(total, MANIFEST["components_sum_usd"])
        self.assertEqual(total, 116)
        price = MANIFEST["price_usd"]
        self.assertEqual(price, 79, "bundle price is $79")
        self.assertEqual(MANIFEST["savings_usd"], total - price)
        self.assertEqual(MANIFEST["savings_usd"], 37)
        # discount percent rounds to the manifest's stated figure
        self.assertEqual(
            round((total - price) / total * 100, 1), MANIFEST["discount_pct"]
        )
        # honest discount: a real cut, and never zero (that would void the bundle)
        self.assertGreater(price, 0)
        self.assertLess(price, total)

    def test_component_names_unique(self):
        kits = [c["kit"] for c in MANIFEST["components"]]
        self.assertEqual(sorted(kits), sorted(set(kits)), "no duplicate kit")


class ComponentsPresentAndPinned(unittest.TestCase):
    def test_each_component_dist_matches_pin(self):
        for comp in MANIFEST["components"]:
            kit_dir = REPO_ROOT / "candidates" / comp["kit"]
            self.assertTrue(
                kit_dir.is_dir(), f"component kit dir missing: {comp['kit']}"
            )
            dist = kit_dir / "dist" / comp["dist"]
            self.assertTrue(dist.is_file(), f"component dist missing: {dist}")
            got = sha256_file(dist)
            self.assertEqual(
                got, comp["sha256"],
                f"{comp['kit']} dist sha256 drifted from the manifest pin",
            )


class BundleZipAssembled(unittest.TestCase):
    def test_bundle_zip_exists(self):
        self.assertTrue(
            BUNDLE_ZIP.is_file(),
            "dist/webhook-verifier-bundle-v0.1.zip missing — run ./package.sh",
        )

    def test_bundle_contains_pinned_component_zips(self):
        with zipfile.ZipFile(BUNDLE_ZIP) as zf:
            names = set(zf.namelist())
            for comp in MANIFEST["components"]:
                inner = f"webhook-verifier-bundle-v0.1/kits/{comp['dist']}"
                self.assertIn(inner, names, f"bundle missing component: {inner}")
                packed = zf.read(inner)
                self.assertEqual(
                    sha256_bytes(packed), comp["sha256"],
                    f"packed {comp['kit']} zip differs from the pinned artifact",
                )

    def test_bundle_contains_docs(self):
        with zipfile.ZipFile(BUNDLE_ZIP) as zf:
            names = set(zf.namelist())
        base = "webhook-verifier-bundle-v0.1"
        for doc in ("README.md", "QUICKSTART.md", "PROVENANCE.md", "MANIFEST.json"):
            self.assertIn(f"{base}/{doc}", names, f"bundle missing doc: {doc}")

    def test_bundle_holds_no_extra_kits(self):
        with zipfile.ZipFile(BUNDLE_ZIP) as zf:
            packed_kits = {
                n.split("/")[-1]
                for n in zf.namelist()
                if n.startswith("webhook-verifier-bundle-v0.1/kits/")
                and n.endswith(".zip")
            }
        expected = {c["dist"] for c in MANIFEST["components"]}
        self.assertEqual(
            packed_kits, expected, "bundle kits/ must hold exactly the four pins"
        )


if __name__ == "__main__":
    unittest.main()
