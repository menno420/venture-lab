#!/usr/bin/env node
"use strict";
/*
 * CORS Preflight Test Kit (cptk) — Node stdlib port of cptk.py.
 *
 * Point it at your own API endpoint and prove your CORS configuration is
 * correct: the cross-origin OPTIONS preflight returns an ok status,
 * Access-Control-Allow-Origin matches the request Origin (with Vary: Origin
 * when it echoes a specific origin), the preflight advertises the method and
 * headers the browser asked for, credentials are never paired with a `*`
 * origin, and the server does NOT reflect an arbitrary Origin. Stdlib only
 * (http, fs, path, url) — no npm install, no build step. Node 14+.
 *
 * NOT a webhook/idempotency/rate-limit/pagination/JWT kit — it tests the
 * BROWSER CROSS-ORIGIN (CORS) contract. Behaviour follows the WHATWG Fetch
 * Standard "CORS protocol" + MDN CORS. See fixtures/PROVENANCE.md.
 *
 * Subcommands (mirror cptk.py exactly):
 *   check             --url --origin [--fixture] [--bad-origin]
 *   preflight-status  --url --origin [--fixture]
 *   allow-origin      --url --origin [--fixture]
 *   allow-methods     --url --origin [--fixture]
 *   allow-headers     --url --origin [--fixture]
 *   credentials       --url --origin [--fixture]
 *   reflect-guard     --url --origin [--fixture] [--bad-origin]
 *   demo              (bundled reference stubs, zero accounts, loud banner)
 *   list
 */
const http = require("http");
const fs = require("fs");
const path = require("path");
const { URL } = require("url");

const FIXTURES_DIR = path.join(__dirname, "fixtures");
const DEFAULT_PRIMARY = "api_json_post";
const DEFAULT_BAD_ORIGIN = "https://cptk-probe.invalid";

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
  if (!(stem in m)) fail(`error: fixture '${stem}' has no entry in fixtures/MANIFEST.json. Run \`cptk list\`.`);
  return m[stem];
}
function loadFixture(stem) {
  const p = path.join(FIXTURES_DIR, stemOf(stem) + ".json");
  if (!fs.existsSync(p)) fail(`error: fixture not found: ${stem}. Run \`cptk list\`.`);
  return fs.readFileSync(p);
}
function methodFor(stem) {
  return (entryFor(stem).method || "GET").toUpperCase();
}
function pathFor(stem) {
  return entryFor(stem).path;
}
function contentTypeFor(stem) {
  return entryFor(stem).content_type || "application/json";
}
function requestHeadersFor(stem) {
  return entryFor(stem).request_headers || "";
}
function listFixtures() {
  return Object.keys(loadManifest()).sort();
}

// --------------------------------------------------------------------------- //
// HTTP
// --------------------------------------------------------------------------- //
function fire(baseUrl, method, p, extraHeaders, body, contentType, timeoutMs = 10000) {
  return new Promise((resolve) => {
    let u;
    try {
      u = new URL(baseUrl.replace(/\/$/, "") + p);
    } catch (e) {
      resolve([0, {}, `<invalid url>`]);
      return;
    }
    const sendBody = ["POST", "PUT", "PATCH"].includes(method) && body && body.length;
    const headers = Object.assign({}, extraHeaders || {});
    if (sendBody) {
      headers["Content-Type"] = contentType;
      headers["Content-Length"] = Buffer.byteLength(body);
    }
    const opts = { method, hostname: u.hostname, port: u.port, path: u.pathname + u.search, headers };
    const req = http.request(opts, (res) => {
      const chunks = [];
      res.on("data", (c) => chunks.push(c));
      res.on("end", () => resolve([res.statusCode, lowerHeaders(res.headers), Buffer.concat(chunks).toString("utf-8")]));
    });
    req.on("error", (e) => resolve([0, {}, `<no HTTP response: ${e.message}>`]));
    req.setTimeout(timeoutMs, () => {
      req.destroy();
      resolve([0, {}, "<no HTTP response: timeout>"]);
    });
    if (sendBody) req.write(body);
    req.end();
  });
}
function lowerHeaders(h) {
  const out = {};
  for (const k of Object.keys(h || {})) out[k.toLowerCase()] = h[k];
  return out;
}
function is2xx(s) {
  return s >= 200 && s < 300;
}
function preflight(baseUrl, p, origin, reqMethod, reqHeaders) {
  const h = { Origin: origin, "Access-Control-Request-Method": reqMethod };
  if (reqHeaders) h["Access-Control-Request-Headers"] = reqHeaders;
  return fire(baseUrl, "OPTIONS", p, h);
}
function actual(baseUrl, method, p, origin, body, contentType) {
  return fire(baseUrl, method, p, { Origin: origin }, body, contentType);
}
function fixtureCall(fixture) {
  return [methodFor(fixture), pathFor(fixture), loadFixture(fixture), contentTypeFor(fixture), requestHeadersFor(fixture)];
}
function splitList(value) {
  if (value == null) return [];
  return String(value).split(",").map((s) => s.trim()).filter(Boolean);
}
function varyHasOrigin(headers) {
  return splitList(headers.vary).some((v) => v.toLowerCase() === "origin");
}

// --------------------------------------------------------------------------- //
// Properties — each resolves to [passed, detail]
// --------------------------------------------------------------------------- //
async function checkPreflightStatus(baseUrl, fixture, origin) {
  const [method, p, , , reqHeaders] = fixtureCall(fixture);
  const [status] = await preflight(baseUrl, p, origin, method, reqHeaders);
  if (status === 200 || status === 204) return [true, `the OPTIONS preflight returned ${status} (ok — the browser will proceed to the real request)`];
  if (status === 0) return [false, "the OPTIONS preflight got no HTTP response (endpoint down or refused the connection)"];
  return [false, `the OPTIONS preflight returned ${status} (needs 200 or 204) — a browser treats a non-ok preflight as a failure and never sends the real request; many frameworks 404/405 OPTIONS by default until CORS is wired.`];
}

function acaoOk(headers, origin, phase) {
  let acao = headers["access-control-allow-origin"];
  if (acao == null) return [false, `the ${phase} carried NO Access-Control-Allow-Origin — the browser blocks the cross-origin request (this is the #1 CORS error).`];
  acao = acao.trim();
  if (acao === "*") return [true, `the ${phase} allows \`*\` (any origin)`];
  if (acao === origin) {
    if (!varyHasOrigin(headers)) return [false, `the ${phase} echoes the specific origin (${origin}) but is missing \`Vary: Origin\` — a shared cache can serve this origin's Allow-Origin to a DIFFERENT origin, breaking CORS for everyone behind the cache.`];
    return [true, `the ${phase} echoes ${origin} with Vary: Origin`];
  }
  return [false, `the ${phase} Access-Control-Allow-Origin is '${acao}', which is neither the request origin (${origin}) nor \`*\` — the browser blocks the request.`];
}

async function checkAllowOrigin(baseUrl, fixture, origin) {
  const [method, p, body, ct, reqHeaders] = fixtureCall(fixture);
  const [ps, ph] = await preflight(baseUrl, p, origin, method, reqHeaders);
  if (ps !== 200 && ps !== 204) return [false, `cannot check Allow-Origin: the OPTIONS preflight returned ${ps} (see preflight-status).`];
  const [ok, detail] = acaoOk(ph, origin, "preflight");
  if (!ok) return [false, detail];
  const [, ah] = await actual(baseUrl, method, p, origin, body, ct);
  const [ok2, detail2] = acaoOk(ah, origin, "actual response");
  if (!ok2) return [false, detail2];
  return [true, `Access-Control-Allow-Origin correct on preflight AND actual response (${detail}; ${detail2})`];
}

async function checkAllowMethods(baseUrl, fixture, origin) {
  const [method, p, , , reqHeaders] = fixtureCall(fixture);
  const [ps, ph] = await preflight(baseUrl, p, origin, method, reqHeaders);
  if (ps !== 200 && ps !== 204) return [false, `cannot check Allow-Methods: the OPTIONS preflight returned ${ps} (see preflight-status).`];
  const acam = ph["access-control-allow-methods"];
  if (acam == null) return [false, `the preflight carried NO Access-Control-Allow-Methods — the browser blocks the ${method} request (a common 'I set Allow-Origin and thought that was enough' bug).`];
  const allowed = new Set(splitList(acam).map((m) => m.toUpperCase()));
  if (allowed.has("*")) return [true, "the preflight allows `*` methods (note: `*` is invalid with credentials — see the credentials check)"];
  if (allowed.has(method.toUpperCase())) return [true, `the preflight's Access-Control-Allow-Methods (${acam}) covers ${method}`];
  return [false, `the preflight's Access-Control-Allow-Methods (${acam}) does NOT include ${method} — the browser blocks the request.`];
}

async function checkAllowHeaders(baseUrl, fixture, origin) {
  const [method, p, , , reqHeaders] = fixtureCall(fixture);
  const requested = splitList(reqHeaders).map((h) => h.toLowerCase());
  if (!requested.length) return [true, "this request sends no non-simple headers, so the browser asks for none — nothing to check"];
  const [ps, ph] = await preflight(baseUrl, p, origin, method, reqHeaders);
  if (ps !== 200 && ps !== 204) return [false, `cannot check Allow-Headers: the OPTIONS preflight returned ${ps} (see preflight-status).`];
  const acah = ph["access-control-allow-headers"];
  if (acah == null) return [false, `the preflight carried NO Access-Control-Allow-Headers, but the request asks for ${requested.join(", ")} — the browser blocks it (the classic 'works in curl, fails in the browser' bug when a custom header like Authorization or Content-Type isn't allowed).`];
  const allowed = new Set(splitList(acah).map((h) => h.toLowerCase()));
  if (allowed.has("*")) {
    if (requested.includes("authorization")) return [false, "Access-Control-Allow-Headers is `*`, but the request asks for Authorization — per the Fetch standard the `*` wildcard does NOT cover Authorization; it must be named explicitly. The browser blocks this request."];
    return [true, "the preflight allows `*` headers (covers the requested headers; note: `*` excludes Authorization)"];
  }
  const missing = requested.filter((h) => !allowed.has(h));
  if (missing.length) return [false, `the preflight's Access-Control-Allow-Headers (${acah}) is missing ${missing.join(", ")} — the browser blocks the request.`];
  return [true, `the preflight's Access-Control-Allow-Headers covers every requested header (${requested.join(", ")})`];
}

async function checkCredentials(baseUrl, fixture, origin) {
  const [method, p, body, ct, reqHeaders] = fixtureCall(fixture);
  const [, ph] = await preflight(baseUrl, p, origin, method, reqHeaders);
  const [, ah] = await actual(baseUrl, method, p, origin, body, ct);
  let sawCreds = false;
  for (const [phase, headers] of [["preflight", ph], ["actual response", ah]]) {
    const acac = headers["access-control-allow-credentials"];
    if (acac == null || acac.trim().toLowerCase() !== "true") continue;
    sawCreds = true;
    const acao = (headers["access-control-allow-origin"] || "").trim();
    if (acao === "*") return [false, `the ${phase} sets Access-Control-Allow-Credentials: true together with Access-Control-Allow-Origin: * — browsers REJECT this combination; echo the specific origin instead.`];
    if (acao === "") return [false, `the ${phase} sets Access-Control-Allow-Credentials: true but no Allow-Origin — a credentialed request needs the specific origin echoed.`];
    if ((headers["access-control-allow-methods"] || "").trim() === "*") return [false, `the ${phase} sets credentials: true with Access-Control-Allow-Methods: * — the \`*\` wildcard is invalid under credentials; list the methods explicitly.`];
    if ((headers["access-control-allow-headers"] || "").trim() === "*") return [false, `the ${phase} sets credentials: true with Access-Control-Allow-Headers: * — the \`*\` wildcard is invalid under credentials; list the headers explicitly.`];
  }
  if (!sawCreds) return [true, "endpoint does not enable credentialed CORS (no Access-Control-Allow-Credentials: true) — nothing to check (credentials are optional)."];
  return [true, "Access-Control-Allow-Credentials: true is correctly paired with a specific origin (not `*`) and explicit methods/headers"];
}

async function checkReflectGuard(baseUrl, fixture, origin, badOrigin = DEFAULT_BAD_ORIGIN) {
  const [method, p, body, ct, reqHeaders] = fixtureCall(fixture);
  const [, ph] = await preflight(baseUrl, p, badOrigin, method, reqHeaders);
  const [, ah] = await actual(baseUrl, method, p, badOrigin, body, ct);
  for (const [phase, headers] of [["preflight", ph], ["actual response", ah]]) {
    let acao = headers["access-control-allow-origin"];
    if (acao == null) continue;
    acao = acao.trim();
    const acac = (headers["access-control-allow-credentials"] || "").trim().toLowerCase();
    if (acao === badOrigin) return [false, `the ${phase} REFLECTS an arbitrary Origin (${badOrigin}) back into Access-Control-Allow-Origin — this is open CORS: any website can read your authenticated responses. Validate the Origin against an allowlist instead of echoing it.`];
    if (acao === "*" && acac === "true") return [false, `the ${phase} answers a disallowed origin with Access-Control-Allow-Origin: * AND credentials: true — an open, credentialed CORS hole (browsers reject \`*\`+credentials, but the intent is unsafe).`];
  }
  return [true, `a disallowed probe origin (${badOrigin}) is NOT reflected — the server validates Origin against an allowlist rather than echoing it`];
}

// --------------------------------------------------------------------------- //
// Runner
// --------------------------------------------------------------------------- //
function printResult(name, passed, detail) {
  console.log(`[${passed ? "PASS" : "FAIL"}] ${name.padEnd(18)} ${detail}`);
}
async function runSuite(baseUrl, fixture, origin, badOrigin) {
  const checks = [
    ["preflight-status", () => checkPreflightStatus(baseUrl, fixture, origin)],
    ["allow-origin", () => checkAllowOrigin(baseUrl, fixture, origin)],
    ["allow-methods", () => checkAllowMethods(baseUrl, fixture, origin)],
    ["allow-headers", () => checkAllowHeaders(baseUrl, fixture, origin)],
    ["credentials", () => checkCredentials(baseUrl, fixture, origin)],
    ["reflect-guard", () => checkReflectGuard(baseUrl, fixture, origin, badOrigin)],
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
const ALLOWED_METHODS = "GET, POST, PUT, DELETE, OPTIONS";

function correctStub(allowedOrigins) {
  const allowed = new Set(allowedOrigins);
  return http.createServer((req, res) => {
    const origin = req.headers["origin"];
    const chunks = [];
    req.on("data", (c) => chunks.push(c));
    req.on("end", () => {
      if (req.method === "OPTIONS") {
        const headers = { "Content-Length": "0" };
        if (origin && allowed.has(origin)) {
          const acrh = req.headers["access-control-request-headers"];
          headers["Access-Control-Allow-Origin"] = origin;
          headers["Vary"] = "Origin";
          headers["Access-Control-Allow-Methods"] = ALLOWED_METHODS;
          headers["Access-Control-Allow-Headers"] = acrh || "Content-Type, Authorization";
          headers["Access-Control-Allow-Credentials"] = "true";
          headers["Access-Control-Max-Age"] = "600";
        }
        res.writeHead(204, headers);
        return res.end();
      }
      const body = Buffer.from(JSON.stringify({ id: "res_" + Math.random().toString(16).slice(2), status: "ok" }));
      const headers = { "Content-Type": "application/json", "Content-Length": body.length };
      if (origin && allowed.has(origin)) {
        headers["Access-Control-Allow-Origin"] = origin;
        headers["Vary"] = "Origin";
        headers["Access-Control-Allow-Credentials"] = "true";
      }
      res.writeHead(200, headers);
      res.end(body);
    });
  });
}

function naiveStub() {
  return http.createServer((req, res) => {
    const origin = req.headers["origin"];
    const chunks = [];
    req.on("data", (c) => chunks.push(c));
    req.on("end", () => {
      if (req.method === "OPTIONS") {
        // BUGS: reflect any origin, credentials, NO Vary/Methods/Headers.
        const headers = { "Content-Length": "0" };
        if (origin) {
          headers["Access-Control-Allow-Origin"] = origin;
          headers["Access-Control-Allow-Credentials"] = "true";
        }
        res.writeHead(204, headers);
        return res.end();
      }
      const body = Buffer.from(JSON.stringify({ id: "res_" + Math.random().toString(16).slice(2), status: "ok" }));
      const headers = { "Content-Type": "application/json", "Content-Length": body.length };
      if (origin) {
        headers["Access-Control-Allow-Origin"] = origin;
        headers["Access-Control-Allow-Credentials"] = "true";
      }
      res.writeHead(200, headers);
      res.end(body);
    });
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
      if (next === undefined || next.startsWith("--")) args[k] = true;
      else { args[k] = next; i++; }
    } else args._.push(a);
  }
  return args;
}
function requireUrl(a) {
  if (!a.url || a.url === true) fail("error: --url is required (your endpoint base, e.g. http://localhost:8000)");
  return a.url;
}
function requireOrigin(a) {
  if (!a.origin || a.origin === true) fail("error: --origin is required (your app's browser origin, e.g. https://app.example.com)");
  return a.origin;
}
function opts(a) {
  return {
    fixture: a.fixture || DEFAULT_PRIMARY,
    badOrigin: a["bad-origin"] && a["bad-origin"] !== true ? a["bad-origin"] : DEFAULT_BAD_ORIGIN,
  };
}

async function cmdCheck(a) {
  const url = requireUrl(a), origin = requireOrigin(a), o = opts(a);
  console.log(`CORS Preflight Test Kit — checking ${url}`);
  console.log(`  fixture: ${o.fixture} (${methodFor(o.fixture)} ${pathFor(o.fixture)})   origin: ${origin}`);
  console.log(`  (--origin is the browser origin your app is served from; --bad-origin is the disallowed probe the reflect-guard check sends, default ${DEFAULT_BAD_ORIGIN})\n`);
  const failures = await runSuite(url, o.fixture, origin, o.badOrigin);
  console.log("");
  if (failures === 0) { console.log("ALL PROPERTIES PASS — this endpoint's CORS configuration behaves correctly for this origin."); return 0; }
  console.log(`${failures} PROPERTY(IES) FAILED — see the FAIL lines above and GOTCHAS.md.`);
  return 1;
}
async function cmdSingle(name, fn) {
  const [passed, detail] = await fn();
  printResult(name, passed, detail);
  return passed ? 0 : 1;
}
async function cmdDemo() {
  const allowed = "https://app.example.com";
  const bad = "https://evil.example";
  console.log("=".repeat(72));
  console.log("  CPTK DEMO MODE — bundled REFERENCE stubs, in-process, on localhost.");
  console.log("  NO real endpoint, NO accounts, NO money. This proves the kit works");
  console.log("  before you point `cptk check --url` at your own app.");
  console.log(`  allowed origin: ${allowed}   disallowed probe: ${bad}`);
  console.log("=".repeat(72));
  const correct = correctStub([allowed]);
  const naive = naiveStub();
  const cport = await listen(correct);
  const nport = await listen(naive);
  let cf, nf;
  try {
    console.log(`\n--- CORRECT stub (allowlist = ${allowed}) — expect ALL PASS ---`);
    cf = await runSuite(`http://127.0.0.1:${cport}`, DEFAULT_PRIMARY, allowed, bad);
    console.log(`\n--- NAIVE stub (reflects any origin, no Vary, no Allow-Methods/Headers) — expect the kit to FLAG it ---`);
    nf = await runSuite(`http://127.0.0.1:${nport}`, DEFAULT_PRIMARY, allowed, bad);
  } finally {
    correct.close();
    naive.close();
  }
  console.log("\n" + "=".repeat(72));
  if (cf === 0 && nf > 0) {
    console.log(`  DEMO OK: correct stub passed all 6; naive stub flagged on ${nf} property(ies).`);
    console.log("  The kit distinguishes a correct CORS config from a broken one.");
    console.log("=".repeat(72));
    return 0;
  }
  console.log(`  DEMO UNEXPECTED: correct failures=${cf}, naive failures=${nf} (expected 0 and >0).`);
  console.log("=".repeat(72));
  return 1;
}
function cmdList() {
  const m = loadManifest();
  console.log("bundled fixtures (docs-derived request templates — see fixtures/PROVENANCE.md):");
  for (const stem of listFixtures()) {
    const e = m[stem];
    console.log(`  ${stem.padEnd(14)}  ${(e.method || "GET").padEnd(6)} ${(e.path || "?").padEnd(12)}  headers=[${e.request_headers || ""}]  — ${e.note || ""}`);
  }
  return 0;
}

async function main() {
  const argv = process.argv.slice(2);
  const cmd = argv[0];
  const a = parseArgs(argv.slice(1));
  let rc = 0;
  const single = (name, fn) => cmdSingle(name, () => fn(requireUrl(a), opts(a).fixture, requireOrigin(a)));
  switch (cmd) {
    case "check": rc = await cmdCheck(a); break;
    case "preflight-status": rc = await single("preflight-status", checkPreflightStatus); break;
    case "allow-origin": rc = await single("allow-origin", checkAllowOrigin); break;
    case "allow-methods": rc = await single("allow-methods", checkAllowMethods); break;
    case "allow-headers": rc = await single("allow-headers", checkAllowHeaders); break;
    case "credentials": rc = await single("credentials", checkCredentials); break;
    case "reflect-guard": rc = await cmdSingle("reflect-guard", () => checkReflectGuard(requireUrl(a), opts(a).fixture, requireOrigin(a), opts(a).badOrigin)); break;
    case "demo": rc = await cmdDemo(); break;
    case "list": rc = cmdList(); break;
    default:
      fail("usage: cptk {check|preflight-status|allow-origin|allow-methods|allow-headers|credentials|reflect-guard|demo|list} --url ... --origin ... [--fixture ...] [--bad-origin ...]");
  }
  process.exit(rc);
}

main();
