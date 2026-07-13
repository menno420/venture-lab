#!/usr/bin/env python3
"""Tests for vendor_fixture.py — stdlib-only, offline, no network.

Run:  python3 -m unittest test_vendor_fixture -v   (from this directory)
"""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPT = HERE / "vendor_fixture.py"

SAMPLE = {
    "id": "evt_sample000000000000001",
    "object": "event",
    "api_version": "2024-06-20",
    "created": 1719849600,
    "type": "checkout.session.completed",
    "data": {
        "object": {
            "id": "cs_test_sample00000000000001",
            "object": "checkout.session",
            "customer_email": None,
            "customer_details": {"email": "real.person@somewhere.example"},
            "payment_intent": None,
        }
    },
}


def run(args, cwd):
    return subprocess.run(
        [sys.executable, str(SCRIPT)] + args,
        cwd=cwd, capture_output=True, text=True,
    )


class VendorFixtureTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.dir = Path(self.tmp.name)
        self.sample = self.dir / "sample.json"
        self.sample.write_text(json.dumps(SAMPLE), encoding="utf-8")

    def test_happy_path_writes_fixture_and_provenance(self):
        r = run(["sample.json", "--name", "checkout", "--out", "fx"], self.dir)
        self.assertEqual(r.returncode, 0, r.stderr)
        fixture = self.dir / "fx" / "checkout.json"
        prov = self.dir / "fx" / "checkout.PROVENANCE.md"
        self.assertTrue(fixture.exists())
        self.assertTrue(prov.exists())
        # fixture round-trips to the same object
        self.assertEqual(json.loads(fixture.read_text()), SAMPLE)
        # provenance carries the fixture sha printed on stdout
        sha_line = [l for l in r.stdout.splitlines() if l.startswith("sha256:")][0]
        self.assertIn(sha_line.split()[-1], prov.read_text())

    def test_null_fields_enumerated(self):
        r = run(["sample.json", "--out", "fx"], self.dir)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("data.object.customer_email", r.stdout)
        self.assertIn("data.object.payment_intent", r.stdout)
        self.assertIn("data.object.customer_email", (self.dir / "fx" / "sample.PROVENANCE.md").read_text())

    def test_volatile_fields_flagged(self):
        r = run(["sample.json", "--out", "fx"], self.dir)
        self.assertIn("created", r.stdout)
        self.assertIn("api_version", r.stdout)

    def test_secret_refused_nothing_written(self):
        # assembled at runtime so the literal never appears in this file
        # (keeps repo/bundle secret scans clean; the value is fake anyway)
        bad = dict(SAMPLE, secret="whsec_" + "ABCDEFGH" * 2)
        (self.dir / "bad.json").write_text(json.dumps(bad), encoding="utf-8")
        r = run(["bad.json", "--out", "fx"], self.dir)
        self.assertEqual(r.returncode, 2)
        self.assertIn("REFUSED", r.stderr)
        self.assertFalse((self.dir / "fx").exists())

    def test_invalid_json_refused(self):
        (self.dir / "nope.json").write_text("{not json", encoding="utf-8")
        r = run(["nope.json", "--out", "fx"], self.dir)
        self.assertEqual(r.returncode, 2)
        self.assertIn("not valid JSON", r.stderr)

    def test_bare_array_refused(self):
        (self.dir / "arr.json").write_text("[1,2]", encoding="utf-8")
        r = run(["arr.json", "--out", "fx"], self.dir)
        self.assertEqual(r.returncode, 2)
        self.assertIn("top level", r.stderr)

    def test_redact_emails_is_stable_and_applied(self):
        r = run(["sample.json", "--out", "fx", "--redact-emails"], self.dir)
        self.assertEqual(r.returncode, 0, r.stderr)
        fx = json.loads((self.dir / "fx" / "sample.json").read_text())
        self.assertEqual(fx["data"]["object"]["customer_details"]["email"],
                         "redacted-1@example.com")
        self.assertNotIn("real.person", (self.dir / "fx" / "sample.json").read_text())

    def test_existing_output_refused_without_force(self):
        self.assertEqual(run(["sample.json", "--out", "fx"], self.dir).returncode, 0)
        r = run(["sample.json", "--out", "fx"], self.dir)
        self.assertEqual(r.returncode, 2)
        self.assertIn("exists", r.stderr)
        self.assertEqual(run(["sample.json", "--out", "fx", "--force"], self.dir).returncode, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
