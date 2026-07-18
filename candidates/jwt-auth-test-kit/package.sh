#!/bin/sh
# Build the buyer bundle for JWT Auth Test Kit v0.1.
# Bundles: the harness (jatk.py + jatk.js), the CORRECT + NAIVE reference
# verifiers, the HTTP-layer test suite, the endpoint/claim fixtures + MANIFEST +
# PROVENANCE + the test public key + illustrative sample tokens, README, GOTCHAS,
# QUICKSTART, .env.example.
# EXCLUDES: INTAKE.md (internal), package.sh (build tooling), dist/, .git,
# __pycache__. Allow-list copy + fixed mtimes + sorted entries + zip -X so the
# build is byte-reproducible (same convention as the webhook + idempotency +
# rate-limit + pagination kits).
set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
SRC="$SCRIPT_DIR"
BUNDLE_NAME="jwt-auth-test-kit-v0.1"
DIST_DIR="$SRC/dist"
ZIP_PATH="$DIST_DIR/$BUNDLE_NAME.zip"
SOURCE_DATE="200001010000.00"

STAGE=$(mktemp -d)
trap 'rm -rf "$STAGE"' EXIT
ROOT="$STAGE/$BUNDLE_NAME"
mkdir -p "$ROOT/fixtures"

cp "$SRC/README.md"                   "$ROOT/README.md"
cp "$SRC/QUICKSTART.md"               "$ROOT/QUICKSTART.md"
cp "$SRC/GOTCHAS.md"                  "$ROOT/GOTCHAS.md"
cp "$SRC/.env.example"                "$ROOT/.env.example"
cp "$SRC/jatk.py"                     "$ROOT/jatk.py"
cp "$SRC/jatk.js"                     "$ROOT/jatk.js"
cp "$SRC/stub_handler.py"             "$ROOT/stub_handler.py"
cp "$SRC/stub_handler_naive.py"       "$ROOT/stub_handler_naive.py"
cp "$SRC/test_http_realpath.py"       "$ROOT/test_http_realpath.py"
cp "$SRC/fixtures/PROVENANCE.md"      "$ROOT/fixtures/PROVENANCE.md"
cp "$SRC"/fixtures/*.json             "$ROOT/fixtures/"
cp "$SRC/fixtures/test_public_key.pem" "$ROOT/fixtures/test_public_key.pem"

find "$ROOT" -exec touch -t "$SOURCE_DATE" {} +

mkdir -p "$DIST_DIR"
rm -f "$ZIP_PATH"
( cd "$STAGE" && find "$BUNDLE_NAME" -print | sort | zip -X -q "$ZIP_PATH" -@ )

echo "built: $ZIP_PATH"
unzip -l "$ZIP_PATH"
