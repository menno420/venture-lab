#!/usr/bin/env node
"use strict";
/*
 * Rate-Limit Test Kit (rltk) — Node stdlib port of rltk.py.
 *
 * Point it at your own API endpoint and prove your rate limiter behaves
 * correctly: under-limit requests succeed, request limit+1 returns 429 with a
 * valid Retry-After, the RateLimit-* headers are consistent, and the window
 * resets when it says it will. Stdlib only (http, fs, path, url) — no npm
 * install, no build step. Node 14+.
 *
 * NOT a webhook signature kit and NOT the idempotency kit — it tests THROTTLING
 * correctness. 429 + Retry-After are RFC 6585 §4 / RFC 9110 §10.2.3; the
 * RateLimit-* fields follow the IETF draft "RateLimit header fields for HTTP"
 * (+ legacy X-RateLimit-*). The draft fields are NOT yet an RFC — see
 * fixtures/PROVENANCE.md.
 *
 * Subcommands (mirror rltk.py exactly):
 *   check                --url [--fixture] [--limit N] [--settle S] [--window S] [--max-delay N]
 *   under-limit          --url [--fixture] [--limit N] [--settle S]
 *   over-limit           --url [--fixture] [--limit N] [--settle S]
 *   retry-after          --url [--fixture] [--limit N] [--settle S] [--max-delay N]
 *   headers              --url [--fixture] [--limit N] [--settle S]
 *   window-reset         --url [--fixture] [--limit N] [--settle S] [--window S] [--max-delay N]
 *   retry-after-honored  --url [--fixture] [--limit N] [--settle S] [--max-delay N]
 *   demo                 (bundled reference stubs, zero accounts, loud banner)
 *   list
 */
const http = require("http");
const fs = require("fs");
const path = require("path");
const { URL } = require("url");

const FIXTURES_DIR = path.join(__dirname, "fixtures");
const DEFAULT_PRIMARY = "api_ping";
const DEFAULT_LIMIT = 5;
const DEFAULT_WINDOW = 1.2;
const DEFAULT_MAX_DELAY = 3600;
const TOLERANCE = 0.4;

function fail(msg) {
  process.stderr.write(msg + "\n");
  process.exit(2);
}
function sleep(s) {
  return new Promise((r) => setTimeout(r, s * 1000));
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
  if (!(stem in m)) fail(`error: fixture '${stem}' has no entry in fixtures/MANIFEST.json. Run \`rltk list\`.`);
  return m[stem];
}
function loadFixture(stem) {
  const p = path.join(FIXTURES_DIR, stemOf(stem) + ".json");
  if (!fs.existsSync(p)) fail(`error: fixture not found: ${stem}. Run \`rltk list\`.`);
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
function listFixtures() {
  return Object.keys(loadManifest()).sort();
}

// --------------------------------------------------------------------------- //
// HTTP
// --------------------------------------------------------------------------- //
function fire(baseUrl, method, p, body, contentType, timeoutMs = 10000) {
  return new Promise((resolve) => {
    let u;
    try {
      u = new URL(baseUrl.replace(/\/$/, "") + p);
    } catch (e) {
      resolve([0, {}, `<invalid url>`]);
      return;
    }
    const sendBody = ["POST", "PUT", "PATCH"].includes(method) && body && body.length;
    const headers = {};
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
async function reset(baseUrl) {
  const [s] = await fire(baseUrl, "POST", "/_debug/reset", Buffer.from("{}"), "application/json");
  return s === 200;
}
async function freshWindow(baseUrl, settle) {
  const ok = await reset(baseUrl);
  if (!ok && settle > 0) await sleep(settle);
}
function is2xx(s) {
  return s >= 200 && s < 300;
}
function rl(headers, ...names) {
  for (const n of names) if (n in headers) return headers[n];
  return null;
}
function fixtureCall(fixture) {
  return [methodFor(fixture), pathFor(fixture), loadFixture(fixture), contentTypeFor(fixture)];
}
async function fireUntil429(baseUrl, fixture, cap) {
  const [method, p, body, ct] = fixtureCall(fixture);
  const statuses = [];
  let hdrs429 = null;
  for (let i = 0; i < cap; i++) {
    const [s, h] = await fire(baseUrl, method, p, body, ct);
    statuses.push(s);
    if (s === 429) {
      hdrs429 = h;
      break;
    }
  }
  return [statuses, hdrs429];
}
function parseRetryAfter(headers, maxDelay) {
  const ra = rl(headers, "retry-after");
  if (ra == null) return [false, "the 429 carried NO Retry-After header — a client has no idea when to retry", null];
  const t = String(ra).trim();
  if (/^-?\d+$/.test(t)) {
    const secs = parseInt(t, 10);
    if (secs <= 0) return [false, `Retry-After is ${secs} (must be positive)`, null];
    if (secs > maxDelay) return [false, `Retry-After is ${secs}s — larger than the sane cap (${maxDelay}s)`, null];
    return [true, `Retry-After: ${secs}s (positive, sane delay-seconds)`, secs];
  }
  const when = Date.parse(t);
  if (isNaN(when)) return [false, `Retry-After '${t}' is neither delay-seconds nor a valid HTTP-date`, null];
  const delta = (when - Date.now()) / 1000;
  if (delta <= 0) return [false, `Retry-After HTTP-date '${t}' is in the PAST`, null];
  if (delta > maxDelay) return [false, `Retry-After HTTP-date is ${Math.floor(delta)}s out — larger than the sane cap`, null];
  return [true, `Retry-After: '${t}' (future HTTP-date, ~${Math.floor(delta)}s)`, delta];
}
function resetNotFuture(value) {
  if (value > 1000000000) {
    if (value <= Math.floor(Date.now() / 1000)) return `RateLimit-Reset ${value} is an absolute timestamp in the PAST (stale reset)`;
    return null;
  }
  if (value <= 0) return `RateLimit-Reset ${value} is not positive — the window never resets`;
  return null;
}

// --------------------------------------------------------------------------- //
// Properties — each resolves to [passed, detail]
// --------------------------------------------------------------------------- //
async function checkUnderLimit(baseUrl, fixture, limit = DEFAULT_LIMIT, settle = 0) {
  await freshWindow(baseUrl, settle);
  const [method, p, body, ct] = fixtureCall(fixture);
  const statuses = [];
  for (let i = 0; i < limit; i++) statuses.push((await fire(baseUrl, method, p, body, ct))[0]);
  const throttled = statuses.map((s, i) => (s === 429 ? i + 1 : 0)).filter(Boolean);
  if (throttled.length) return [false, `request #${throttled[0]} of the first ${limit} was throttled (429) — the endpoint 429s BEFORE its own limit (statuses ${statuses}).`];
  if (statuses.every(is2xx)) return [true, `the first ${limit} requests all returned 2xx (statuses ${statuses})`];
  return [false, `a request under the limit did not return 2xx (statuses ${statuses})`];
}

async function checkOverLimit(baseUrl, fixture, limit = DEFAULT_LIMIT, settle = 0) {
  await freshWindow(baseUrl, settle);
  const [method, p, body, ct] = fixtureCall(fixture);
  const statuses = [];
  for (let i = 0; i < limit + 1; i++) statuses.push((await fire(baseUrl, method, p, body, ct))[0]);
  const early = statuses.slice(0, limit).map((s, i) => (s === 429 ? i + 1 : 0)).filter(Boolean);
  if (early.length) return [false, `request #${early[0]} was throttled BEFORE the limit of ${limit} (statuses ${statuses}).`];
  const last = statuses[limit];
  if (last === 429) return [true, `request #${limit + 1} correctly returned 429 (statuses ${statuses})`];
  if (is2xx(last)) return [false, `request #${limit + 1} was ACCEPTED (HTTP ${last}) — off-by-one quota leak: a limit of ${limit} let ${limit + 1} through (statuses ${statuses}).`];
  return [false, `request #${limit + 1} returned HTTP ${last} (expected 429): statuses ${statuses}`];
}

async function checkRetryAfter(baseUrl, fixture, limit = DEFAULT_LIMIT, settle = 0, maxDelay = DEFAULT_MAX_DELAY) {
  await freshWindow(baseUrl, settle);
  const [statuses, hdrs] = await fireUntil429(baseUrl, fixture, limit + 6);
  if (hdrs == null) return [false, `no 429 in ${statuses.length} requests — the endpoint did not enforce a limit (statuses ${statuses}).`];
  const [ok, detail] = parseRetryAfter(hdrs, maxDelay);
  return [ok, detail];
}

async function checkHeaders(baseUrl, fixture, limit = DEFAULT_LIMIT, settle = 0) {
  await freshWindow(baseUrl, settle);
  const [method, p, body, ct] = fixtureCall(fixture);
  const remainings = [], limits = [], resets = [];
  let sawAny = false;
  for (let i = 0; i < limit; i++) {
    const [, h] = await fire(baseUrl, method, p, body, ct);
    const lim = rl(h, "ratelimit-limit", "x-ratelimit-limit");
    const rem = rl(h, "ratelimit-remaining", "x-ratelimit-remaining");
    const rst = rl(h, "ratelimit-reset", "x-ratelimit-reset");
    if (lim != null || rem != null || rst != null) sawAny = true;
    if (lim != null) limits.push(lim);
    if (rem != null && /^-?\d+$/.test(rem)) remainings.push(parseInt(rem, 10));
    if (rst != null && /^-?\d+$/.test(rst)) resets.push(parseInt(rst, 10));
  }
  if (!sawAny) return [true, "endpoint emits no RateLimit-*/X-RateLimit-* headers (optional per the draft) — nothing to check"];
  if (limits.length && !limits.every((v) => /^-?\d+$/.test(v) && parseInt(v, 10) > 0)) return [false, `RateLimit-Limit is not a positive integer (${limits})`];
  if (!remainings.length) return [false, "RateLimit-Remaining is present but non-numeric — a client cannot read its budget"];
  for (let i = 0; i < remainings.length - 1; i++) if (remainings[i + 1] > remainings[i]) return [false, `RateLimit-Remaining did not decrement monotonically (${remainings})`];
  if (remainings.length > 1 && remainings[remainings.length - 1] >= remainings[0]) return [false, `RateLimit-Remaining never decreased across ${remainings.length} requests (${remainings}) — it is stuck; a client can't see itself running out.`];
  if (remainings[remainings.length - 1] !== 0) return [false, `RateLimit-Remaining did not reach 0 at the limit boundary (ended at ${remainings[remainings.length - 1]}, values ${remainings}).`];
  if (!resets.length) return [false, "RateLimit-Reset is present but non-numeric — a client can't tell when the window resets"];
  const bad = resetNotFuture(resets[0]);
  if (bad) return [false, bad];
  return [true, `headers consistent: Limit ok, Remaining ${remainings[0]}→${remainings[remainings.length - 1]} (hits 0 at the boundary), Reset points to the future`];
}

async function checkWindowReset(baseUrl, fixture, limit = DEFAULT_LIMIT, settle = 0, window = DEFAULT_WINDOW, maxDelay = DEFAULT_MAX_DELAY) {
  await freshWindow(baseUrl, settle);
  const [statuses, hdrs] = await fireUntil429(baseUrl, fixture, limit + 6);
  if (hdrs == null) return [false, `no 429 in ${statuses.length} requests — cannot test reset (no enforced limit).`];
  const [ok, , secs] = parseRetryAfter(hdrs, maxDelay);
  const wait = (ok && secs ? secs : window) + TOLERANCE;
  await sleep(wait);
  const [method, p, body, ct] = fixtureCall(fixture);
  const [s] = await fire(baseUrl, method, p, body, ct);
  if (is2xx(s)) return [true, `after ~${wait.toFixed(1)}s the window reset and a request succeeded again (HTTP ${s})`];
  return [false, `still throttled (HTTP ${s}) ~${wait.toFixed(1)}s after the advertised reset — the window did not reset when it said it would.`];
}

async function checkRetryAfterHonored(baseUrl, fixture, limit = DEFAULT_LIMIT, settle = 0, maxDelay = DEFAULT_MAX_DELAY) {
  await freshWindow(baseUrl, settle);
  const [statuses, hdrs] = await fireUntil429(baseUrl, fixture, limit + 6);
  if (hdrs == null) return [false, `no 429 in ${statuses.length} requests — nothing to honour (no enforced limit).`];
  const [ok, detail, secs] = parseRetryAfter(hdrs, maxDelay);
  if (!ok || !secs) return [false, `the 429 carried no usable Retry-After (${detail}) — a client cannot honour a delay it was never given.`];
  const [method, p, body, ct] = fixtureCall(fixture);
  const [sBefore] = await fire(baseUrl, method, p, body, ct);
  if (is2xx(sBefore)) return [false, `the service resumed (HTTP ${sBefore}) IMMEDIATELY, before the advertised Retry-After of ${secs}s elapsed — the advertised delay overstates the wait.`];
  await sleep(secs + TOLERANCE);
  const [sAfter] = await fire(baseUrl, method, p, body, ct);
  if (is2xx(sAfter)) return [true, `still 429 before the ${secs}s Retry-After, 2xx after it (within tolerance) — the advertised delay is honoured.`];
  return [false, `still throttled (HTTP ${sAfter}) after waiting the advertised ${secs}s Retry-After — the delay understates the real wait; a client that trusts it still gets 429s.`];
}

// --------------------------------------------------------------------------- //
// Runner
// --------------------------------------------------------------------------- //
function printResult(name, passed, detail) {
  console.log(`[${passed ? "PASS" : "FAIL"}] ${name.padEnd(20)} ${detail}`);
}
async function runSuite(baseUrl, fixture, limit, settle, window, maxDelay) {
  const checks = [
    ["under-limit", () => checkUnderLimit(baseUrl, fixture, limit, settle)],
    ["over-limit", () => checkOverLimit(baseUrl, fixture, limit, settle)],
    ["retry-after", () => checkRetryAfter(baseUrl, fixture, limit, settle, maxDelay)],
    ["headers", () => checkHeaders(baseUrl, fixture, limit, settle)],
    ["window-reset", () => checkWindowReset(baseUrl, fixture, limit, settle, window, maxDelay)],
    ["retry-after-honored", () => checkRetryAfterHonored(baseUrl, fixture, limit, settle, maxDelay)],
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
function correctStub(limit, windowMs, headerStyle) {
  const windowS = windowMs / 1000;
  let windowStart = process.hrtime.bigint();
  let count = 0;
  const emitRL = headerStyle === "ratelimit" || headerStyle === "both";
  const emitLegacy = headerStyle === "legacy" || headerStyle === "both";
  const take = () => {
    const now = process.hrtime.bigint();
    if (Number(now - windowStart) / 1e9 >= windowS) {
      windowStart = now;
      count = 0;
    }
    count += 1;
    const remaining = Math.max(0, limit - count);
    const resetSecs = Math.max(1, Math.ceil(windowS - Number(now - windowStart) / 1e9));
    return [count <= limit, remaining, resetSecs];
  };
  return http.createServer(async (req, res) => {
    const body = await readBody(req);
    if (req.method === "GET" && req.url === "/_debug/state") return sendJSON(res, 200, { limit, count }, false, {});
    if (req.method === "POST" && req.url === "/_debug/reset") { windowStart = process.hrtime.bigint(); count = 0; return sendJSON(res, 200, { ok: true }, false, {}); }
    void body;
    const [allowed, remaining, resetSecs] = take();
    const rlHeaders = {};
    if (emitRL) { rlHeaders["RateLimit-Limit"] = String(limit); rlHeaders["RateLimit-Remaining"] = String(remaining); rlHeaders["RateLimit-Reset"] = String(resetSecs); }
    if (emitLegacy) { rlHeaders["X-RateLimit-Limit"] = String(limit); rlHeaders["X-RateLimit-Remaining"] = String(remaining); rlHeaders["X-RateLimit-Reset"] = String(resetSecs); }
    if (allowed) return sendJSON(res, 200, { id: "req_" + Math.random().toString(16).slice(2), status: "ok" }, false, rlHeaders);
    rlHeaders["Retry-After"] = String(resetSecs);
    return sendJSON(res, 429, { error: "rate limit exceeded", code: "too_many_requests" }, false, rlHeaders);
  });
}
function naiveStub(limit, windowMs) {
  const windowS = windowMs / 1000;
  const STALE = 1600000000;
  let windowStart = process.hrtime.bigint();
  let count = 0;
  return http.createServer(async (req, res) => {
    const body = await readBody(req);
    if (req.method === "GET" && req.url === "/_debug/state") return sendJSON(res, 200, { limit, count }, false, {});
    if (req.method === "POST" && req.url === "/_debug/reset") { windowStart = process.hrtime.bigint(); count = 0; return sendJSON(res, 200, { ok: true }, false, {}); }
    void body;
    const now = process.hrtime.bigint();
    if (Number(now - windowStart) / 1e9 >= windowS) { windowStart = now; count = 0; }
    count += 1;
    // BUGS: off-by-one, stuck Remaining, stale (past) Reset, no Retry-After.
    const stale = { "X-RateLimit-Limit": String(limit), "X-RateLimit-Remaining": String(limit), "X-RateLimit-Reset": String(STALE) };
    if (count <= limit + 1) return sendJSON(res, 200, { id: "req_" + Math.random().toString(16).slice(2), status: "ok" }, false, stale);
    return sendJSON(res, 429, { error: "rate limit exceeded" }, false, stale);
  });
}
function readBody(req) {
  return new Promise((resolve) => {
    const chunks = [];
    req.on("data", (c) => chunks.push(c));
    req.on("end", () => resolve(Buffer.concat(chunks)));
  });
}
function sendJSON(res, code, obj, _unused, extraHeaders) {
  const data = Buffer.from(JSON.stringify(obj));
  const headers = Object.assign({ "Content-Type": "application/json", "Content-Length": data.length }, extraHeaders || {});
  res.writeHead(code, headers);
  res.end(data);
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
function opts(a) {
  return {
    fixture: a.fixture || DEFAULT_PRIMARY,
    limit: a.limit ? parseInt(a.limit, 10) : DEFAULT_LIMIT,
    settle: a.settle ? parseFloat(a.settle) : 0,
    window: a.window ? parseFloat(a.window) : DEFAULT_WINDOW,
    maxDelay: a["max-delay"] ? parseInt(a["max-delay"], 10) : DEFAULT_MAX_DELAY,
  };
}

async function cmdCheck(a) {
  const url = requireUrl(a);
  const o = opts(a);
  console.log(`Rate-Limit Test Kit — checking ${url}`);
  console.log(`  fixture: ${o.fixture} (${methodFor(o.fixture)} ${pathFor(o.fixture)})   assumed limit: ${o.limit}/window`);
  console.log(`  (set --limit to your window budget; --window <seconds> is the reset fallback; --settle <seconds> starts each check in a fresh window)\n`);
  const failures = await runSuite(url, o.fixture, o.limit, o.settle, o.window, o.maxDelay);
  console.log("");
  if (failures === 0) { console.log("ALL PROPERTIES PASS — this endpoint's rate limiter behaves correctly."); return 0; }
  console.log(`${failures} PROPERTY(IES) FAILED — see the FAIL lines above and GOTCHAS.md.`);
  return 1;
}
async function cmdSingle(name, fn) {
  const [passed, detail] = await fn();
  printResult(name, passed, detail);
  return passed ? 0 : 1;
}
async function cmdDemo() {
  console.log("=".repeat(72));
  console.log("  RLTK DEMO MODE — bundled REFERENCE stubs, in-process, on localhost.");
  console.log("  NO real endpoint, NO accounts, NO money. This proves the kit works");
  console.log("  before you point `rltk check --url` at your own app.");
  console.log("=".repeat(72));
  const limit = 5, windowMs = 800, windowS = windowMs / 1000;
  const correct = correctStub(limit, windowMs, "both");
  const naive = naiveStub(limit, windowMs);
  const cport = await listen(correct);
  const nport = await listen(naive);
  let cf, nf;
  try {
    console.log(`\n--- CORRECT stub (limit ${limit}/${windowMs}ms) — expect ALL PASS ---`);
    cf = await runSuite(`http://127.0.0.1:${cport}`, DEFAULT_PRIMARY, limit, 0, windowS, DEFAULT_MAX_DELAY);
    console.log(`\n--- NAIVE stub (off-by-one, no Retry-After, stale headers) — expect the kit to FLAG it ---`);
    nf = await runSuite(`http://127.0.0.1:${nport}`, DEFAULT_PRIMARY, limit, 0, windowS, DEFAULT_MAX_DELAY);
  } finally {
    correct.close();
    naive.close();
  }
  console.log("\n" + "=".repeat(72));
  if (cf === 0 && nf > 0) {
    console.log(`  DEMO OK: correct stub passed all 6; naive stub flagged on ${nf} property(ies).`);
    console.log("  The kit distinguishes a correct limiter from a broken one.");
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
    console.log(`  ${stem.padEnd(14)}  ${(e.method || "GET").padEnd(5)} ${(e.path || "?").padEnd(14)}  ${e.content_type || "application/json"}  — ${e.note || ""}`);
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
    case "under-limit": { const o = opts(a); rc = await cmdSingle("under-limit", () => checkUnderLimit(requireUrl(a), o.fixture, o.limit, o.settle)); break; }
    case "over-limit": { const o = opts(a); rc = await cmdSingle("over-limit", () => checkOverLimit(requireUrl(a), o.fixture, o.limit, o.settle)); break; }
    case "retry-after": { const o = opts(a); rc = await cmdSingle("retry-after", () => checkRetryAfter(requireUrl(a), o.fixture, o.limit, o.settle, o.maxDelay)); break; }
    case "headers": { const o = opts(a); rc = await cmdSingle("headers", () => checkHeaders(requireUrl(a), o.fixture, o.limit, o.settle)); break; }
    case "window-reset": { const o = opts(a); rc = await cmdSingle("window-reset", () => checkWindowReset(requireUrl(a), o.fixture, o.limit, o.settle, o.window, o.maxDelay)); break; }
    case "retry-after-honored": { const o = opts(a); rc = await cmdSingle("retry-after-honored", () => checkRetryAfterHonored(requireUrl(a), o.fixture, o.limit, o.settle, o.maxDelay)); break; }
    case "demo": rc = await cmdDemo(); break;
    case "list": rc = cmdList(); break;
    default:
      fail("usage: rltk {check|under-limit|over-limit|retry-after|headers|window-reset|retry-after-honored|demo|list} [--url ...] [--fixture ...] [--limit N]");
  }
  process.exit(rc);
}

main();
