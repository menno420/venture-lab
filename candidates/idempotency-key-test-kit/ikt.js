#!/usr/bin/env node
"use strict";
/*
 * Idempotency Key Test Kit (ikt) — Node stdlib port of ikt.py.
 *
 * Point it at your own POST endpoint and prove your `Idempotency-Key` handling
 * is correct: safe retries trigger the side effect EXACTLY ONCE, key reuse with
 * a different body is rejected, concurrent retries don't double-execute, and
 * keys are scoped per endpoint. Stdlib only (http, fs, path, crypto, url) — no
 * npm install, no build step. Node 14+.
 *
 * NOT a webhook signature kit — it tests the DEDUP / SAFE-RETRY contract, not
 * HMAC verification. Behaviour specifics follow Stripe's widely-used model; the
 * header is the subject of the IETF draft "The Idempotency-Key HTTP Header
 * Field". See fixtures/PROVENANCE.md.
 *
 * Subcommands (mirror ikt.py exactly):
 *   check         --url [--fixture] [--variant] [--missing-key-mode required|passthrough]
 *   replay        --url [--fixture]
 *   mismatch      --url [--fixture] [--variant]
 *   distinct-keys --url [--fixture]
 *   concurrent    --url [--fixture] [--n N]
 *   missing-key   --url [--fixture] [--mode required|passthrough]
 *   demo          (bundled reference stubs, zero accounts, loud banner)
 *   list
 */
const http = require("http");
const fs = require("fs");
const path = require("path");
const crypto = require("crypto");
const { URL } = require("url");

const FIXTURES_DIR = path.join(__dirname, "fixtures");
const IDEMPOTENCY_HEADER = "Idempotency-Key";
const DEFAULT_ID_FIELD = "id";
const DEFAULT_PRIMARY = "charge_basic";
const DEFAULT_VARIANT = "charge_mismatch";

function fail(msg) {
  process.stderr.write(msg + "\n");
  process.exit(2);
}

// --------------------------------------------------------------------------- //
// Fixtures
// --------------------------------------------------------------------------- //
function loadManifest() {
  const m = JSON.parse(fs.readFileSync(path.join(FIXTURES_DIR, "MANIFEST.json"), "utf-8"));
  delete m._comment;
  return m;
}
function stemOf(name) {
  return name.replace(/\.json$/, "");
}
function entryFor(stem) {
  const m = loadManifest();
  stem = stemOf(stem);
  if (!(stem in m)) fail(`error: fixture '${stem}' has no entry in fixtures/MANIFEST.json. Run \`ikt list\`.`);
  return m[stem];
}
function loadFixture(stem) {
  const p = path.join(FIXTURES_DIR, stemOf(stem) + ".json");
  if (!fs.existsSync(p)) fail(`error: fixture not found: ${stem}. Run \`ikt list\`.`);
  return fs.readFileSync(p);
}
function pathFor(stem) {
  return entryFor(stem).path;
}
function contentTypeFor(stem) {
  return entryFor(stem).content_type || "application/json";
}
function listFixtures() {
  return Object.keys(loadManifest()).sort();
}

// --------------------------------------------------------------------------- //
// HTTP
// --------------------------------------------------------------------------- //
function newKey() {
  return "ikt_" + crypto.randomBytes(16).toString("hex");
}

function request(method, urlStr, body, headers, timeoutMs = 10000) {
  return new Promise((resolve) => {
    let u;
    try {
      u = new URL(urlStr);
    } catch (e) {
      resolve([0, `<invalid url: ${urlStr}>`]);
      return;
    }
    const opts = {
      method,
      hostname: u.hostname,
      port: u.port,
      path: u.pathname + u.search,
      headers: headers || {},
    };
    const req = http.request(opts, (res) => {
      const chunks = [];
      res.on("data", (c) => chunks.push(c));
      res.on("end", () => resolve([res.statusCode, Buffer.concat(chunks).toString("utf-8")]));
    });
    req.on("error", (e) => resolve([0, `<no HTTP response: ${e.message}>`]));
    req.setTimeout(timeoutMs, () => {
      req.destroy();
      resolve([0, "<no HTTP response: timeout>"]);
    });
    if (body && body.length) req.write(body);
    req.end();
  });
}

function post(baseUrl, p, body, contentType, key) {
  const headers = { "Content-Type": contentType, "Content-Length": Buffer.byteLength(body) };
  if (key != null) headers[IDEMPOTENCY_HEADER] = key;
  return request("POST", baseUrl.replace(/\/$/, "") + p, body, headers);
}
function get(baseUrl, p) {
  return request("GET", baseUrl.replace(/\/$/, "") + p, Buffer.alloc(0), {});
}

function resourceId(bodyText, idField) {
  try {
    const data = JSON.parse(bodyText);
    if (data && typeof data === "object" && idField in data) return `id:${JSON.stringify(data[idField])}`;
  } catch (e) {
    /* fall through */
  }
  return `raw:${bodyText}`;
}
function is2xx(s) {
  return s >= 200 && s < 300;
}

// --------------------------------------------------------------------------- //
// Properties — each resolves to [passed, detail]
// --------------------------------------------------------------------------- //
async function checkReplay(baseUrl, fixture, idField = DEFAULT_ID_FIELD) {
  const p = pathFor(fixture), ct = contentTypeFor(fixture), body = loadFixture(fixture);
  const key = newKey();
  const [s1, b1] = await post(baseUrl, p, body, ct, key);
  if (!is2xx(s1)) return [false, `first request was not accepted (HTTP ${s1}) — cannot test replay: ${b1.slice(0, 160)}`];
  const [s2, b2] = await post(baseUrl, p, body, ct, key);
  if (!is2xx(s2)) return [false, `the retry (same key + same body) was rejected (HTTP ${s2}); a safe retry must replay the stored response: ${b2.slice(0, 160)}`];
  const id1 = resourceId(b1, idField), id2 = resourceId(b2, idField);
  if (id1 === id2) return [true, `retry replayed the stored response (${id1}); exactly one side effect`];
  return [false, `the retry created a DIFFERENT resource (${id1} → ${id2}) — the side effect ran TWICE. A retried charge would double-charge.`];
}

async function checkMismatch(baseUrl, fixture, variant) {
  const p = pathFor(fixture), ct = contentTypeFor(fixture);
  const body = loadFixture(fixture), vbody = loadFixture(variant);
  if (body.equals(vbody)) return [false, `cannot test: '${fixture}' and '${variant}' have identical bodies`];
  const key = newKey();
  const [s1, b1] = await post(baseUrl, p, body, ct, key);
  if (!is2xx(s1)) return [false, `first request was not accepted (HTTP ${s1}) — cannot test mismatch: ${b1.slice(0, 160)}`];
  const [s2, b2] = await post(baseUrl, p, vbody, ct, key);
  if (s2 === 409 || s2 === 422) return [true, `same key + different body correctly rejected (HTTP ${s2})`];
  if (is2xx(s2)) return [false, `same key + a DIFFERENT body was ACCEPTED (HTTP ${s2}) — key reuse with a mismatched payload must be rejected (409/422).`];
  return [false, `same key + different body returned HTTP ${s2} (expected 409/422): ${b2.slice(0, 160)}`];
}

async function checkDistinctKeys(baseUrl, fixture, idField = DEFAULT_ID_FIELD) {
  const p = pathFor(fixture), ct = contentTypeFor(fixture), body = loadFixture(fixture);
  const [s1, b1] = await post(baseUrl, p, body, ct, newKey());
  const [s2, b2] = await post(baseUrl, p, body, ct, newKey());
  if (!(is2xx(s1) && is2xx(s2))) return [false, `one of two distinct-key requests was rejected (HTTP ${s1}, ${s2})`];
  const id1 = resourceId(b1, idField), id2 = resourceId(b2, idField);
  if (id1 !== id2) return [true, `two different keys produced two resources (${id1}, ${id2}) — keys are scoped`];
  return [false, `two DIFFERENT keys collapsed to one resource (${id1}) — the endpoint is keying on the body, not the Idempotency-Key.`];
}

async function checkConcurrent(baseUrl, fixture, n = 2, idField = DEFAULT_ID_FIELD) {
  const p = pathFor(fixture), ct = contentTypeFor(fixture), body = loadFixture(fixture);
  const key = newKey();
  const results = await Promise.all(Array.from({ length: n }, () => post(baseUrl, p, body, ct, key)));
  const ok = results.filter((r) => is2xx(r[0]));
  const conflicts = results.filter((r) => r[0] === 409);
  const distinct = new Set(ok.map(([, b]) => resourceId(b, idField)));
  if (ok.length === 0) return [false, `no concurrent request succeeded (statuses ${results.map((r) => r[0])})`];
  if (distinct.size <= 1) {
    const extra = conflicts.length ? `, ${conflicts.length} got 409` : "";
    return [true, `${results.length} concurrent same-key requests → ONE side effect (1 distinct resource${extra})`];
  }
  return [false, `${results.length} concurrent same-key requests created ${distinct.size} resources ([${[...distinct]}]) — no in-flight lock; a retry storm double-executes.`];
}

async function checkMissingKey(baseUrl, fixture, mode) {
  const p = pathFor(fixture), ct = contentTypeFor(fixture), body = loadFixture(fixture);
  const [s, b] = await post(baseUrl, p, body, ct, null);
  if (mode === "required") {
    if (s >= 400 && s < 500) return [true, `missing key correctly rejected (HTTP ${s}) under the \`required\` policy`];
    return [false, `missing key was NOT rejected (HTTP ${s}) though the policy is \`required\`: ${b.slice(0, 160)}`];
  }
  if (mode === "passthrough") {
    if (is2xx(s)) return [true, `missing key processed (HTTP ${s}) under the \`passthrough\` policy`];
    return [false, `missing key returned HTTP ${s} though the policy is \`passthrough\` (expected 2xx): ${b.slice(0, 160)}`];
  }
  fail(`error: unknown missing-key mode '${mode}' (use required or passthrough)`);
}

// --------------------------------------------------------------------------- //
// Runner
// --------------------------------------------------------------------------- //
function printResult(name, passed, detail) {
  console.log(`[${passed ? "PASS" : "FAIL"}] ${name.padEnd(14)} ${detail}`);
}

async function runSuite(baseUrl, fixture, variant, missingKeyMode) {
  const checks = [
    ["replay", () => checkReplay(baseUrl, fixture)],
    ["mismatch", () => checkMismatch(baseUrl, fixture, variant)],
    ["distinct-keys", () => checkDistinctKeys(baseUrl, fixture)],
    ["concurrent", () => checkConcurrent(baseUrl, fixture)],
    ["missing-key", () => checkMissingKey(baseUrl, fixture, missingKeyMode)],
  ];
  let failures = 0;
  for (const [name, fn] of checks) {
    const [passed, detail] = await fn();
    printResult(name, passed, detail);
    if (!passed) failures += 1;
  }
  return failures;
}

// --------------------------------------------------------------------------- //
// Reference stubs (Node) — used only by `demo`, mirror the Python stubs.
// --------------------------------------------------------------------------- //
const PREFIX = { "/charges": "ch_", "/orders": "or_" };
function fingerprint(raw) {
  return crypto.createHash("sha256").update(raw).digest("hex");
}
function sleep(ms) {
  return new Promise((r) => setTimeout(r, ms));
}
function makeResource(p, payload) {
  return {
    id: (PREFIX[p] || "obj_") + crypto.randomBytes(16).toString("hex"),
    object: p.replace(/^\//, "").replace(/s$/, "") || "object",
    amount: payload.amount != null ? payload.amount : null,
    currency: payload.currency != null ? payload.currency : null,
    status: "succeeded",
    created: Math.floor(Date.now() / 1000),
  };
}
function readBody(req) {
  return new Promise((resolve) => {
    const chunks = [];
    req.on("data", (c) => chunks.push(c));
    req.on("end", () => resolve(Buffer.concat(chunks)));
  });
}
// A correct idempotent stub with a per-key in-flight lock (chained promise per key).
function correctStub(requireKey, delayMs) {
  const store = new Map();      // (path|key) -> {fingerprint, status, body}
  const chains = new Map();     // key -> Promise (serialises same-key requests)
  let sideEffects = 0;
  const send = (res, code, obj, replayed) => {
    const data = Buffer.from(JSON.stringify(obj));
    res.writeHead(code, { "Content-Type": "application/json", "Idempotent-Replayed": replayed ? "true" : "false" });
    res.end(data);
  };
  const sendRaw = (res, code, buf, replayed) => {
    res.writeHead(code, { "Content-Type": "application/json", "Idempotent-Replayed": replayed ? "true" : "false" });
    res.end(buf);
  };
  return http.createServer(async (req, res) => {
    if (req.method === "GET" && req.url === "/_debug/side_effects") return send(res, 200, { count: sideEffects }, false);
    const raw = await readBody(req);
    if (req.method === "POST" && req.url === "/_debug/reset") { store.clear(); chains.clear(); sideEffects = 0; return send(res, 200, { ok: true }, false); }
    const key = req.headers[IDEMPOTENCY_HEADER.toLowerCase()];
    const parse = () => { try { return raw.length ? JSON.parse(raw) : {}; } catch (e) { return null; } };
    if (!key) {
      if (requireKey) return send(res, 400, { error: `${IDEMPOTENCY_HEADER} header required` }, false);
      const payload = parse();
      if (payload === null) return send(res, 400, { error: "unparseable body" }, false);
      sideEffects += 1; if (delayMs) await sleep(delayMs);
      return send(res, 200, makeResource(req.url, payload), false);
    }
    const ident = req.url + "|" + key;
    const fp = fingerprint(raw);
    // serialise on the key: chain this handler after any in-flight same-key op.
    const prior = chains.get(key) || Promise.resolve();
    let release;
    chains.set(key, new Promise((r) => (release = r)));
    await prior;
    try {
      const rec = store.get(ident);
      if (rec) {
        if (rec.fingerprint !== fp) return send(res, 422, { error: `${IDEMPOTENCY_HEADER} reused with a different request body (idempotency conflict)`, code: "idempotency_key_reuse" }, false);
        return sendRaw(res, rec.status, rec.body, true);
      }
      const payload = parse();
      if (payload === null) return send(res, 400, { error: "unparseable body" }, false);
      sideEffects += 1; if (delayMs) await sleep(delayMs);
      const body = Buffer.from(JSON.stringify(makeResource(req.url, payload)));
      store.set(ident, { fingerprint: fp, status: 201, body });
      return sendRaw(res, 201, body, false);
    } finally {
      release();
    }
  });
}
// A naive stub: ignores the key, executes every request.
function naiveStub(delayMs) {
  let sideEffects = 0;
  const send = (res, code, obj) => { res.writeHead(code, { "Content-Type": "application/json" }); res.end(JSON.stringify(obj)); };
  return http.createServer(async (req, res) => {
    if (req.method === "GET" && req.url === "/_debug/side_effects") return send(res, 200, { count: sideEffects });
    const raw = await readBody(req);
    if (req.method === "POST" && req.url === "/_debug/reset") { sideEffects = 0; return send(res, 200, { ok: true }); }
    let payload; try { payload = raw.length ? JSON.parse(raw) : {}; } catch (e) { return send(res, 400, { error: "unparseable body" }); }
    sideEffects += 1; if (delayMs) await sleep(delayMs);
    send(res, 201, makeResource(req.url, payload));
  });
}
function listen(server) {
  return new Promise((resolve) => server.listen(0, "127.0.0.1", () => resolve(server.address().port)));
}

// --------------------------------------------------------------------------- //
// CLI
// --------------------------------------------------------------------------- //
function parseArgs(argv) {
  const args = { _: [] };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a.startsWith("--")) {
      const k = a.slice(2);
      const next = argv[i + 1];
      if (next === undefined || next.startsWith("--")) { args[k] = true; } else { args[k] = next; i++; }
    } else args._.push(a);
  }
  return args;
}

async function cmdCheck(a) {
  const url = requireUrl(a);
  const fixture = a.fixture || DEFAULT_PRIMARY;
  const variant = a.variant || DEFAULT_VARIANT;
  const mode = a["missing-key-mode"] || "required";
  console.log(`Idempotency Key Test Kit — checking ${url}`);
  console.log(`  primary fixture: ${fixture} (POST ${pathFor(fixture)})   variant: ${variant}`);
  console.log(`  missing-key policy assumed: ${mode}  (set --missing-key-mode to match your documented behaviour)\n`);
  const failures = await runSuite(url, fixture, variant, mode);
  console.log("");
  if (failures === 0) { console.log("ALL PROPERTIES PASS — this endpoint's Idempotency-Key handling is correct."); return 0; }
  console.log(`${failures} PROPERTY(IES) FAILED — see the FAIL lines above and GOTCHAS.md.`);
  return 1;
}

function requireUrl(a) {
  if (!a.url || a.url === true) fail("error: --url is required (your endpoint base, e.g. http://localhost:8000)");
  return a.url;
}

async function cmdSingle(name, fn) {
  const [passed, detail] = await fn();
  printResult(name, passed, detail);
  return passed ? 0 : 1;
}

async function cmdDemo() {
  console.log("=".repeat(72));
  console.log("  IKT DEMO MODE — bundled REFERENCE stubs, in-process, on localhost.");
  console.log("  NO real endpoint, NO accounts, NO money. This proves the kit works");
  console.log("  before you point `ikt check --url` at your own app.");
  console.log("=".repeat(72));
  const correct = correctStub(true, 60);
  const naive = naiveStub(60);
  const cport = await listen(correct);
  const nport = await listen(naive);
  let cf, nf;
  try {
    console.log(`\n--- CORRECT stub (http://127.0.0.1:${cport}) — expect ALL PASS ---`);
    cf = await runSuite(`http://127.0.0.1:${cport}`, DEFAULT_PRIMARY, DEFAULT_VARIANT, "required");
    console.log(`        (side-effect counter on the correct stub: ${(await get(`http://127.0.0.1:${cport}`, "/_debug/side_effects"))[1]})`);
    console.log(`\n--- NAIVE stub (http://127.0.0.1:${nport}) — expect the kit to FLAG it ---`);
    nf = await runSuite(`http://127.0.0.1:${nport}`, DEFAULT_PRIMARY, DEFAULT_VARIANT, "required");
    console.log(`        (side-effect counter on the naive stub: ${(await get(`http://127.0.0.1:${nport}`, "/_debug/side_effects"))[1]} — it over-executed)`);
  } finally {
    correct.close();
    naive.close();
  }
  console.log("\n" + "=".repeat(72));
  if (cf === 0 && nf > 0) {
    console.log(`  DEMO OK: correct stub passed all 5; naive stub flagged on ${nf} property(ies).`);
    console.log("  The kit distinguishes correct idempotency from a broken (no-dedup) one.");
    console.log("=".repeat(72));
    return 0;
  }
  console.log(`  DEMO UNEXPECTED: correct failures=${cf}, naive failures=${nf} (expected 0 and >0).`);
  console.log("=".repeat(72));
  return 1;
}

function cmdList() {
  const m = loadManifest();
  console.log("bundled fixtures (docs-derived request payloads — see fixtures/PROVENANCE.md):");
  for (const stem of listFixtures()) {
    const e = m[stem];
    console.log(`  ${stem.padEnd(16)}  ${(e.method || "POST").padEnd(4)} ${(e.path || "?").padEnd(12)}  ${e.content_type || "application/json"}  — ${e.note || ""}`);
  }
  return 0;
}

async function main() {
  const argv = process.argv.slice(2);
  const cmd = argv[0];
  const a = parseArgs(argv.slice(1));
  let rc = 0;
  switch (cmd) {
    case "check": rc = await cmdCheck(a); break;
    case "replay": rc = await cmdSingle("replay", () => checkReplay(requireUrl(a), a.fixture || DEFAULT_PRIMARY)); break;
    case "mismatch": rc = await cmdSingle("mismatch", () => checkMismatch(requireUrl(a), a.fixture || DEFAULT_PRIMARY, a.variant || DEFAULT_VARIANT)); break;
    case "distinct-keys": rc = await cmdSingle("distinct-keys", () => checkDistinctKeys(requireUrl(a), a.fixture || DEFAULT_PRIMARY)); break;
    case "concurrent": rc = await cmdSingle("concurrent", () => checkConcurrent(requireUrl(a), a.fixture || DEFAULT_PRIMARY, parseInt(a.n || "2", 10))); break;
    case "missing-key": rc = await cmdSingle("missing-key", () => checkMissingKey(requireUrl(a), a.fixture || DEFAULT_PRIMARY, a.mode || "required")); break;
    case "demo": rc = await cmdDemo(); break;
    case "list": rc = cmdList(); break;
    default:
      fail("usage: ikt {check|replay|mismatch|distinct-keys|concurrent|missing-key|demo|list} [--url ...] [--fixture ...]");
  }
  process.exit(rc);
}

main();
