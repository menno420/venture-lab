# Quickstart — API Robustness Bundle

You downloaded `api-robustness-bundle-v0.1.zip`. It contains the four component
kits' own buyer bundles plus this documentation. Nothing here needs an account,
an API key, or a network connection — every kit is stdlib-only Python (with a JS
parity port alongside).

## 1. Unzip the bundle

```sh
unzip api-robustness-bundle-v0.1.zip
cd api-robustness-bundle-v0.1
ls kits/
# idempotency-key-test-kit-v0.1.zip
# jwt-auth-test-kit-v0.1.zip
# pagination-test-kit-v0.1.zip
# rate-limit-test-kit-v0.1.zip
```

## 2. Pick the robustness property you're hardening and unzip that kit

```sh
cd kits
unzip jwt-auth-test-kit-v0.1.zip      # or idempotency / rate-limit / pagination
cd jwt-auth-test-kit-v0.1
cat README.md          # the properties it checks + how to point it at your endpoint
```

## 3. Run that kit's test suite (one command, no accounts)

Each kit ships an HTTP real-path test suite that starts the correct/broken
reference stubs over loopback and drives the fixtures through them — the true
PASS case plus each failure/attack case the kit is built to catch:

```sh
python3 -m unittest test_http_realpath -v
```

## 4. Use the kit against your own endpoint

Each kit's README shows how to point its harness (`ikt` / `rltk` / `pgtk` /
`jatk`, each with a `*.js` Node parity port) at an endpoint you own and read
PASS/FAIL per property. The GOTCHAS.md in each kit lists the specific mistakes
that silently pass a naive implementation (a retry that mints a new resource id,
an off-by-one quota leak, a row skipped mid-walk, an `alg:none` bypass).

## Verify what you got (optional)

Every artifact is pinned by sha256 in `MANIFEST.json`. To confirm the four kit
zips are exactly the published ones:

```sh
cd kits
sha256sum *.zip
# compare against MANIFEST.json's per-component sha256 values
```

That's it — no build step, no dependencies, no signup.
