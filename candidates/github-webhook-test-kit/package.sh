#!/bin/sh
# Build the buyer bundle for GitHub Webhook Test Kit v0.1.
# Bundles: the harness (gwtk.py + gwtk.js), the example handler, the HTTP-layer
# test suite, the vendored real-shape fixtures + EVENTS.json + PROVENANCE,
# README, GOTCHAS.
# EXCLUDES: INTAKE.md (internal), package.sh (build tooling), dist/, .git,
# __pycache__. Allow-list copy + fixed mtimes + sorted entries + zip -X so the
# build is byte-reproducible (same convention as stripe-webhook-test-kit).
set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
SRC="$SCRIPT_DIR"
BUNDLE_NAME="github-webhook-test-kit-v0.1"
DIST_DIR="$SRC/dist"
ZIP_PATH="$DIST_DIR/$BUNDLE_NAME.zip"
SOURCE_DATE="200001010000.00"

STAGE=$(mktemp -d)
trap 'rm -rf "$STAGE"' EXIT
ROOT="$STAGE/$BUNDLE_NAME"
mkdir -p "$ROOT/fixtures"

cp "$SRC/README.md"              "$ROOT/README.md"
cp "$SRC/GOTCHAS.md"             "$ROOT/GOTCHAS.md"
cp "$SRC/gwtk.py"                "$ROOT/gwtk.py"
cp "$SRC/gwtk.js"                "$ROOT/gwtk.js"
cp "$SRC/stub_handler.py"        "$ROOT/stub_handler.py"
cp "$SRC/test_http_realpath.py"  "$ROOT/test_http_realpath.py"
cp "$SRC/fixtures/PROVENANCE.md" "$ROOT/fixtures/PROVENANCE.md"
cp "$SRC"/fixtures/*.json        "$ROOT/fixtures/"

find "$ROOT" -exec touch -t "$SOURCE_DATE" {} +

mkdir -p "$DIST_DIR"
rm -f "$ZIP_PATH"
( cd "$STAGE" && find "$BUNDLE_NAME" -print | sort | zip -X -q "$ZIP_PATH" -@ )

echo "built: $ZIP_PATH"
unzip -l "$ZIP_PATH"
