#!/bin/sh
# package.sh — assemble a clean, buyer-facing bundle of the Membership-Site
# Boilerplate Kit into candidates/membership-kit/dist/membership-kit-v0.2.zip
#
# Buyer bundle = the product the customer runs. It deliberately EXCLUDES:
#   - LISTING.md          (seller marketing, not part of the product)
#   - members.json / .tmp (runtime member data — never ship customer data)
#   - dist/               (build output; never nest a zip inside itself)
#   - __pycache__, .pyc   (Python build cruft)
#   - .git, package.sh    (repo/build tooling)
#
# Deterministic-ish + idempotent: staged files are copied then stamped to a
# fixed mtime, listed via `find | sort`, and zipped with `zip -X` (no extra
# attributes), so re-running produces the same archive. Safe to re-run.
#
# Usage:  sh package.sh        (from anywhere; paths are script-relative)
set -eu

# --- locate ourselves so the script works from any CWD ---
SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
SRC="$SCRIPT_DIR"
BUNDLE_NAME="membership-kit-v0.2"
DIST_DIR="$SRC/dist"
ZIP_PATH="$DIST_DIR/$BUNDLE_NAME.zip"
SOURCE_DATE="200001010000.00"   # fixed timestamp for reproducible archives

# --- clean staging area ---
STAGE=$(mktemp -d)
trap 'rm -rf "$STAGE"' EXIT
ROOT="$STAGE/$BUNDLE_NAME"
mkdir -p "$ROOT/server" "$ROOT/server/fixtures" "$ROOT/web"

# --- copy the buyer-facing tree (explicit allow-list, not a blanket copy) ---
cp "$SRC/QUICKSTART.md"        "$ROOT/QUICKSTART.md"
cp "$SRC/README.md"            "$ROOT/README.md"
cp "$SRC/design-tokens.json"  "$ROOT/design-tokens.json"

cp "$SRC/server/app.py"                "$ROOT/server/app.py"
cp "$SRC/server/test_membership.py"    "$ROOT/server/test_membership.py"
cp "$SRC/server/test_http_realpath.py" "$ROOT/server/test_http_realpath.py"
cp "$SRC/server/README.md"             "$ROOT/server/README.md"
cp "$SRC/server/.env.example"          "$ROOT/server/.env.example"
cp "$SRC/server/.gitignore"            "$ROOT/server/.gitignore"

# Real, source-verified Stripe event fixtures + their provenance (the evidence
# the real webhook path is tested against real payloads).
cp "$SRC/server/fixtures/checkout_session_completed.json"              "$ROOT/server/fixtures/checkout_session_completed.json"
cp "$SRC/server/fixtures/checkout_session_completed_legacy_email.json" "$ROOT/server/fixtures/checkout_session_completed_legacy_email.json"
cp "$SRC/server/fixtures/PROVENANCE.md"                                "$ROOT/server/fixtures/PROVENANCE.md"

cp "$SRC/web/index.html"   "$ROOT/web/index.html"
cp "$SRC/web/members.html" "$ROOT/web/members.html"
cp "$SRC/web/styles.css"   "$ROOT/web/styles.css"

# --- normalize mtimes for a reproducible archive ---
find "$ROOT" -exec touch -t "$SOURCE_DATE" {} +

# --- build the zip deterministically (sorted entries, no extra attrs) ---
mkdir -p "$DIST_DIR"
rm -f "$ZIP_PATH"
( cd "$STAGE" && find "$BUNDLE_NAME" -print | sort | zip -X -q "$ZIP_PATH" -@ )

echo "built: $ZIP_PATH"
unzip -l "$ZIP_PATH"
