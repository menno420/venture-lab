#!/usr/bin/env node
"use strict";
/*
 * Pagination Test Kit (pgtk) — Node stdlib port of pgtk.py.
 *
 * Point it at your own paginated API endpoint and prove your cursor/keyset
 * pagination is correct: cursor traversal with no overlap/gap, stable under a
 * controlled mid-traversal mutation, a consistent total order, a page-size limit
 * honored and clamped to a documented max, a terminal signal, and a forged
 * cursor rejected. Stdlib only (http, crypto, fs, path, url) — no npm install,
 * no build step. Node 14+.
 *
 * NOT a webhook signature kit, NOT the idempotency kit, NOT the rate-limit kit —
 * it tests RESULT-SET INTEGRITY across pages. There is no single RFC for cursor
 * pagination; the model is the keyset/cursor pattern (Stripe/Slack/GitHub cursor
 * docs + the keyset-vs-offset literature). See fixtures/PROVENANCE.md.
 *
 * Subcommands (mirror pgtk.py exactly):
 *   check                 --url [--fixture] [--limit N] [--max M]
 *   traversal             --url [--fixture] [--limit N]
 *   stable-under-mutation --url [--fixture] [--limit N]
 *   ordering              --url [--fixture] [--limit N]
 *   page-size             --url [--fixture] [--limit N] [--max M]
 *   terminal              --url [--fixture] [--limit N]
 *   cursor-tamper         --url [--fixture] [--limit N]
 *   demo                  (bundled reference stubs, zero accounts, loud banner)
 *   list
 */
const http = require("http");
const crypto = require("crypto");
const fs = require("fs");
const path = require("path");
const { URL } = require("url");

const FIXTURES_DIR = path.join(__dirname, "fixtures");
const DEFAULT_PRIMARY = "items_keyset";
const DEFAULT_LIMIT = 3;
const DEFAULT_MAX = 100;
const TRAVERSE_CAP = 1000;

function fail(msg) {
  process.stderr.write(msg + "\n");
  process.exit(2);
}
function sleep(ms) {
  return new Promise((r) => setTimeout(r, ms));
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
  if (!(stem in m)) fail(`error: fixture '${stem}' has no entry in fixtures/MANIFEST.json. Run \`pgtk list\`.`);
  return m[stem];
}
function loadFixture(stem) {
  const p = path.join(FIXTURES_DIR, stemOf(stem) + ".json");
  if (!fs.existsSync(p)) fail(`error: fixture not found: ${stem}. Run \`pgtk list\`.`);
  return fs.readFileSync(p);
}
function listFixtures() {
  return Object.keys(loadManifest()).sort();
}
function specFrom(stem) {
  const e = entryFor(stem);
  return {
    path: e.path,
    limitParam: e.limit_param || "limit",
    cursorParam: e.cursor_param || "cursor",
    itemsField: e.items_field || "items",
    nextCursorField: e.next_cursor_field || "next_cursor",
    idField: e.id_field || "id",
    sortField: e.sort_field || "created_at",
  };
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
      resolve([0, {}, "<invalid url>"]);
      return;
    }
    const sendBody = ["POST", "PUT", "PATCH"].includes(method) && body && body.length;
    const headers = {};
    if (sendBody) {
      headers["Content-Type"] = contentType || "application/json";
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
async function firePage(baseUrl, spec, limit, cursor) {
  const params = new URLSearchParams();
  params.set(spec.limitParam, String(limit));
  if (cursor !== null && cursor !== undefined && cursor !== "") params.set(spec.cursorParam, cursor);
  const [status, headers, text] = await fire(baseUrl, "GET", spec.path + "?" + params.toString());
  let obj = null;
  try {
    obj = JSON.parse(text);
  } catch (e) {
    obj = null;
  }
  return [status, headers, obj];
}
function extract(obj, spec) {
  const items = obj && typeof obj === "object" ? obj[spec.itemsField] || [] : [];
  const rows = items.filter((r) => r && typeof r === "object");
  const ids = rows.map((r) => r[spec.idField]);
  const nxt = obj && typeof obj === "object" ? obj[spec.nextCursorField] : null;
  return [ids, rows, nxt];
}
async function traverse(baseUrl, spec, limit, startCursor = "", cap = TRAVERSE_CAP) {
  const ids = [], rows = [], sizes = [];
  let cursor = startCursor;
  const seen = new Set();
  for (let i = 0; i < cap; i++) {
    const [status, , obj] = await firePage(baseUrl, spec, limit, cursor);
    if (status !== 200 || obj === null) return [ids, rows, sizes, false, `page fetch returned HTTP ${status}`];
    const [pageIds, pageRows, nxt] = extract(obj, spec);
    ids.push(...pageIds);
    rows.push(...pageRows);
    sizes.push(pageIds.length);
    if (!nxt) return [ids, rows, sizes, true, null];
    if (seen.has(nxt)) return [ids, rows, sizes, false, "next_cursor repeated — cursor loop"];
    seen.add(nxt);
    cursor = nxt;
  }
  return [ids, rows, sizes, false, `did not terminate within ${cap} pages (possible infinite loop)`];
}
async function reset(baseUrl) {
  const [s] = await fire(baseUrl, "POST", "/_debug/reset", Buffer.from("{}"), "application/json");
  return s === 200;
}
async function debugAll(baseUrl) {
  const [s, , text] = await fire(baseUrl, "GET", "/_debug/all");
  if (s !== 200) return null;
  try {
    return JSON.parse(text).ids;
  } catch (e) {
    return null;
  }
}
async function debugInsert(baseUrl, row) {
  const [s] = await fire(baseUrl, "POST", "/_debug/insert", Buffer.from(JSON.stringify(row)), "application/json");
  return s === 200;
}
async function debugDelete(baseUrl, id) {
  const [s] = await fire(baseUrl, "POST", "/_debug/delete", Buffer.from(JSON.stringify({ id })), "application/json");
  return s === 200;
}
function dupes(seq) {
  const seen = new Set(), dup = [];
  for (const x of seq) {
    if (seen.has(x) && !dup.includes(x)) dup.push(x);
    seen.add(x);
  }
  return dup;
}
async function pageMax(baseUrl, spec, fallback) {
  const [, h] = await firePage(baseUrl, spec, 1, "");
  const raw = h["x-page-size-max"];
  if (raw && /^-?\d+$/.test(raw) && parseInt(raw, 10) > 0) return [parseInt(raw, 10), true];
  return [fallback, false];
}

// --------------------------------------------------------------------------- //
// Properties — each resolves to [passed(bool|null), detail]. null == SKIP.
// --------------------------------------------------------------------------- //
async function checkTraversal(baseUrl, fixture, limit = DEFAULT_LIMIT) {
  const spec = specFrom(fixture);
  await reset(baseUrl);
  const [ids, , sizes, terminated, err] = await traverse(baseUrl, spec, limit);
  if (err) return [false, `traversal failed: ${err} (collected ${ids.length} ids so far)`];
  if (!terminated) return [false, "traversal never signalled a terminal page (no null next-cursor)"];
  const dup = dupes(ids);
  if (dup.length) return [false, `the same item appeared on more than one page (overlap): ${dup} — pages returned ${ids.length} ids, ${new Set(ids).size} distinct.`];
  const truth = await debugAll(baseUrl);
  if (truth !== null) {
    if (JSON.stringify(ids) !== JSON.stringify(truth)) {
      const missing = truth.filter((t) => !ids.includes(t));
      const extra = ids.filter((i) => !truth.includes(i));
      return [false, `traversal did not reproduce the full ordered set exactly once: missing ${missing.length ? missing : "none"}, unexpected ${extra.length ? extra : "none"} (got ${ids.length} vs ${truth.length} ground-truth rows).`];
    }
    return [true, `followed the cursor across ${sizes.length} pages → ${ids.length} items, no overlap, no gap; reproduces the full ordered set exactly once`];
  }
  return [true, `followed the cursor across ${sizes.length} pages → ${ids.length} items with no overlap (no /_debug/all ground truth to check for gaps — see GOTCHAS)`];
}

async function checkStableUnderMutation(baseUrl, fixture, limit = DEFAULT_LIMIT) {
  const spec = specFrom(fixture);
  if (!(await reset(baseUrl))) return [null, "SKIP: endpoint has no POST /_debug/reset hook, so the kit cannot drive a controlled mutation. Run this against the bundled stubs or a seeded test dataset you can mutate (see GOTCHAS)."];
  const truth = await debugAll(baseUrl);
  if (truth === null || truth.length < limit + 2) return [null, "SKIP: no GET /_debug/all ground truth (or too few rows) to run a controlled mid-traversal mutation — see GOTCHAS for wiring test hooks."];
  const [status, , obj] = await firePage(baseUrl, spec, limit, "");
  if (status !== 200 || obj === null) return [false, `page 1 fetch returned HTTP ${status}`];
  const [seenIds, , cursor] = extract(obj, spec);
  if (!cursor || seenIds.length < 2) return [null, "SKIP: the dataset paged into a single page (no mid-traversal point) — use a larger dataset or a smaller --limit to exercise this property."];
  const deleteId = seenIds[0];
  const insertId = "pgtk_inserted_zzz";
  const bigSort = 1e9;
  const row = { name: "pgtk-inserted" };
  row[spec.idField] = insertId;
  row[spec.sortField] = bigSort;
  if (!(await debugDelete(baseUrl, deleteId)) || !(await debugInsert(baseUrl, row)))
    return [null, "SKIP: /_debug/delete or /_debug/insert hook unavailable — cannot perform the controlled mutation (see GOTCHAS)."];
  const [restIds, , , , err] = await traverse(baseUrl, spec, limit, cursor);
  if (err) return [false, `post-mutation traversal failed: ${err}`];
  const returned = seenIds.concat(restIds);
  const dup = dupes(returned);
  const present = new Set(truth.filter((t) => t !== deleteId));
  const missing = [...present].filter((t) => !returned.includes(t)).sort();
  if (missing.length) return [false, `after deleting already-returned '${deleteId}' mid-traversal, item(s) present throughout were SKIPPED: ${missing} — the classic OFFSET skip (the offset window shifted when a prior row was removed).`];
  if (dup.length) return [false, `after the mid-traversal mutation, item(s) were DUPLICATED across pages: ${dup} — the offset window re-served a row.`];
  return [true, `deleted already-returned '${deleteId}' + inserted a tail row mid-traversal; all ${present.size} items present throughout still appear exactly once, none skipped or duplicated (keyset stays stable)`];
}

async function checkOrdering(baseUrl, fixture, limit = DEFAULT_LIMIT) {
  const spec = specFrom(fixture);
  await reset(baseUrl);
  const [ids, rows, , , err] = await traverse(baseUrl, spec, limit);
  if (err) return [false, `could not traverse to check ordering: ${err}`];
  const dup = dupes(ids);
  if (dup.length) return [false, `duplicate ids in the traversal — not a total order: ${dup}`];
  const haveSort = rows.length && rows.every((r) => spec.sortField in r);
  if (haveSort) {
    const keys = rows.map((r) => [r[spec.sortField], r[spec.idField]]);
    const cmp = (a, b) => (a[0] < b[0] ? -1 : a[0] > b[0] ? 1 : a[1] < b[1] ? -1 : a[1] > b[1] ? 1 : 0);
    for (let i = 0; i < keys.length - 1; i++)
      if (cmp(keys[i], keys[i + 1]) > 0) return [false, `order is not monotonic by (${spec.sortField}, ${spec.idField}) at position ${i}: ${keys[i]} then ${keys[i + 1]} — inconsistent sort.`];
    const uniq = new Set(keys.map((k) => JSON.stringify(k)));
    if (uniq.size !== keys.length) return [false, `the sort key (${spec.sortField}, ${spec.idField}) is not unique across rows — without a unique tiebreaker the order is unstable.`];
    return [true, `${rows.length} rows are in a consistent total order by (${spec.sortField}, ${spec.idField}), unique tiebreaker holds`];
  }
  const [ids2, , , , err2] = await traverse(baseUrl, spec, limit);
  if (err2) return [false, `second traversal failed: ${err2}`];
  if (JSON.stringify(ids) !== JSON.stringify(ids2)) return [false, `two traversals returned a different order — the ordering is not stable (no '${spec.sortField}' field exposed to check the sort key directly).`];
  return [true, `no '${spec.sortField}' field exposed, but two full traversals returned the identical ${ids.length}-item order (deterministic) with no duplicates`];
}

async function checkPageSize(baseUrl, fixture, limit = DEFAULT_LIMIT, maxArg = DEFAULT_MAX) {
  const spec = specFrom(fixture);
  await reset(baseUrl);
  const [maxPage, fromHeader] = await pageMax(baseUrl, spec, maxArg);
  const k = Math.max(1, Math.min(limit, maxPage));
  const [, , obj] = await firePage(baseUrl, spec, k, "");
  if (obj === null) return [false, "page fetch returned no JSON body"];
  const [ids, , nxt] = extract(obj, spec);
  if (nxt && ids.length !== k) return [false, `requested limit=${k} but the first (non-terminal) page returned ${ids.length} items — the page size is not honored.`];
  const over = maxPage * 10 + 50;
  const [, , obj2] = await firePage(baseUrl, spec, over, "");
  if (obj2 === null) return [false, "over-max page fetch returned no JSON body"];
  const [overIds] = extract(obj2, spec);
  const src = fromHeader ? "X-Page-Size-Max header" : `--max ${maxArg}`;
  if (overIds.length > maxPage) return [false, `requested limit=${over} and got ${overIds.length} items — OVER the documented max of ${maxPage} (${src}); the endpoint serves an unbounded page (a cheap DoS). It must clamp to ${maxPage}.`];
  return [true, `limit=${k} honored on full pages; over-max limit=${over} clamped to ${overIds.length} ≤ ${maxPage} (${src})`];
}

async function checkTerminal(baseUrl, fixture, limit = DEFAULT_LIMIT) {
  const spec = specFrom(fixture);
  await reset(baseUrl);
  const [ids, , sizes, terminated, err] = await traverse(baseUrl, spec, limit);
  if (err) return [false, `traversal did not terminate cleanly: ${err}`];
  if (!terminated) return [false, "the last page did not signal the end (no null/absent next-cursor)"];
  return [true, `traversal terminated after ${sizes.length} pages with a null/absent next-cursor (${ids.length} items) — no infinite loop`];
}

async function checkCursorTamper(baseUrl, fixture, limit = DEFAULT_LIMIT) {
  const spec = specFrom(fixture);
  await reset(baseUrl);
  const [, , obj] = await firePage(baseUrl, spec, Math.max(1, limit), "");
  let valid = null;
  if (obj && typeof obj === "object") valid = extract(obj, spec)[2];
  const forged = ["not-a-cursor", "%%%bogus%%%", "999999", "YWJj.Zm9vYmFy"];
  if (valid) {
    forged.push(valid.slice(0, -1) + (valid.slice(-1) !== "Z" ? "Z" : "Q"));
    forged.push(valid + "tampered");
  }
  const accepted = [];
  for (const f of forged) {
    const [status] = await firePage(baseUrl, spec, limit, f);
    if (is2xx(status)) accepted.push([f.slice(0, 24), status]);
  }
  if (accepted.length) return [false, `forged/garbage cursor(s) were ACCEPTED with a 2xx instead of rejected: ${JSON.stringify(accepted)} — the endpoint silently coerces a bad cursor to page 1 rather than returning 400.`];
  return [true, `all ${forged.length} forged/malformed cursors were rejected (4xx) — the opaque cursor is tamper-evident, not silently coerced to page 1`];
}

// --------------------------------------------------------------------------- //
// Runner
// --------------------------------------------------------------------------- //
function label(passed) {
  if (passed === null) return "SKIP";
  return passed ? "PASS" : "FAIL";
}
function printResult(name, passed, detail) {
  console.log(`[${label(passed)}] ${name.padEnd(22)} ${detail}`);
}
async function runSuite(baseUrl, fixture, limit, maxArg) {
  const checks = [
    ["traversal", () => checkTraversal(baseUrl, fixture, limit)],
    ["stable-under-mutation", () => checkStableUnderMutation(baseUrl, fixture, limit)],
    ["ordering", () => checkOrdering(baseUrl, fixture, limit)],
    ["page-size", () => checkPageSize(baseUrl, fixture, limit, maxArg)],
    ["terminal", () => checkTerminal(baseUrl, fixture, limit)],
    ["cursor-tamper", () => checkCursorTamper(baseUrl, fixture, limit)],
  ];
  let failures = 0;
  for (const [name, fn] of checks) {
    const [passed, detail] = await fn();
    printResult(name, passed, detail);
    if (passed === false) failures += 1;
  }
  return failures;
}

// --------------------------------------------------------------------------- //
// Reference stubs (Node) — used only by `demo`, mirror the Python stubs.
// --------------------------------------------------------------------------- //
const CANONICAL = [
  { id: "a1", created_at: 100, name: "alpha" },
  { id: "a2", created_at: 100, name: "alkaline" },
  { id: "b1", created_at: 105, name: "bravo" },
  { id: "c1", created_at: 110, name: "charlie" },
  { id: "c2", created_at: 110, name: "cobalt" },
  { id: "d1", created_at: 115, name: "delta" },
  { id: "e1", created_at: 120, name: "echo" },
  { id: "f1", created_at: 125, name: "foxtrot" },
  { id: "g1", created_at: 130, name: "golf" },
  { id: "g2", created_at: 130, name: "granite" },
  { id: "h1", created_at: 135, name: "hotel" },
  { id: "i1", created_at: 140, name: "india" },
];
const DEMO_SECRET = "pgtk-demo-cursor-key-not-a-secret";
function sortKey(r) {
  return [r.created_at, r.id];
}
function cmpRows(a, b) {
  const ka = sortKey(a), kb = sortKey(b);
  return ka[0] < kb[0] ? -1 : ka[0] > kb[0] ? 1 : ka[1] < kb[1] ? -1 : ka[1] > kb[1] ? 1 : 0;
}
function b64url(buf) {
  return Buffer.from(buf).toString("base64").replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
}
function unb64url(s) {
  return Buffer.from(s.replace(/-/g, "+").replace(/_/g, "/"), "base64");
}
function readBody(req) {
  return new Promise((resolve) => {
    const chunks = [];
    req.on("data", (c) => chunks.push(c));
    req.on("end", () => {
      try {
        resolve(chunks.length ? JSON.parse(Buffer.concat(chunks).toString("utf-8")) : {});
      } catch (e) {
        resolve({});
      }
    });
  });
}
function sendJSON(res, code, obj, extra) {
  const data = Buffer.from(JSON.stringify(obj));
  const headers = Object.assign({ "Content-Type": "application/json", "Content-Length": data.length }, extra || {});
  res.writeHead(code, headers);
  res.end(data);
}
function correctStub(maxPage) {
  let rows = CANONICAL.map((r) => Object.assign({}, r));
  const sign = (payload) => crypto.createHmac("sha256", DEMO_SECRET).update(payload).digest();
  const encode = (r) => {
    const payload = Buffer.from(JSON.stringify({ id: r.id, k: r.created_at }));
    return b64url(payload) + "." + b64url(sign(payload));
  };
  const decode = (token) => {
    if (!token || !token.includes(".")) throw new Error("not a signed token");
    const [pB64, sB64] = token.split(".");
    const payload = unb64url(pB64);
    const sig = unb64url(sB64);
    const expected = sign(payload);
    if (sig.length !== expected.length || !crypto.timingSafeEqual(sig, expected)) throw new Error("signature mismatch");
    const obj = JSON.parse(payload.toString("utf-8"));
    return [obj.k, obj.id];
  };
  return http.createServer(async (req, res) => {
    const u = new URL(req.url, "http://x");
    const body = await readBody(req);
    if (req.method === "GET" && u.pathname === "/_debug/all") {
      const ids = rows.slice().sort(cmpRows).map((r) => r.id);
      return sendJSON(res, 200, { ids, count: ids.length });
    }
    if (req.method === "POST" && u.pathname === "/_debug/reset") { rows = CANONICAL.map((r) => Object.assign({}, r)); return sendJSON(res, 200, { ok: true }); }
    if (req.method === "POST" && u.pathname === "/_debug/insert") { rows = rows.filter((r) => r.id !== body.id); rows.push(Object.assign({}, body)); return sendJSON(res, 200, { ok: true }); }
    if (req.method === "POST" && u.pathname === "/_debug/delete") { const b = rows.length; rows = rows.filter((r) => r.id !== body.id); return sendJSON(res, 200, { ok: rows.length < b }); }
    if (req.method === "GET" && u.pathname === "/items") {
      let n = parseInt(u.searchParams.get("limit") || "3", 10);
      if (isNaN(n)) return sendJSON(res, 400, { error: "limit must be an integer" });
      n = Math.max(1, Math.min(n, maxPage));
      const cursor = u.searchParams.get("cursor") || "";
      const ordered = rows.slice().sort(cmpRows);
      let start = 0;
      if (cursor) {
        let after;
        try {
          after = decode(cursor);
        } catch (e) {
          return sendJSON(res, 400, { error: "invalid cursor", detail: e.message });
        }
        start = ordered.length;
        for (let i = 0; i < ordered.length; i++) {
          const k = sortKey(ordered[i]);
          if (k[0] > after[0] || (k[0] === after[0] && k[1] > after[1])) { start = i; break; }
        }
      }
      const window = ordered.slice(start, start + n);
      const nxt = start + n < ordered.length && window.length ? encode(window[window.length - 1]) : null;
      return sendJSON(res, 200, { items: window, next_cursor: nxt }, { "X-Page-Size-Max": String(maxPage) });
    }
    return sendJSON(res, 404, { error: "not found" });
  });
}
function naiveStub(maxPage) {
  let rows = CANONICAL.map((r) => Object.assign({}, r));
  return http.createServer(async (req, res) => {
    const u = new URL(req.url, "http://x");
    const body = await readBody(req);
    if (req.method === "GET" && u.pathname === "/_debug/all") {
      const ids = rows.slice().sort(cmpRows).map((r) => r.id);
      return sendJSON(res, 200, { ids, count: ids.length });
    }
    if (req.method === "POST" && u.pathname === "/_debug/reset") { rows = CANONICAL.map((r) => Object.assign({}, r)); return sendJSON(res, 200, { ok: true }); }
    if (req.method === "POST" && u.pathname === "/_debug/insert") { rows = rows.filter((r) => r.id !== body.id); rows.push(Object.assign({}, body)); return sendJSON(res, 200, { ok: true }); }
    if (req.method === "POST" && u.pathname === "/_debug/delete") { const b = rows.length; rows = rows.filter((r) => r.id !== body.id); return sendJSON(res, 200, { ok: rows.length < b }); }
    if (req.method === "GET" && u.pathname === "/items") {
      // BUGS: offset "cursor", no clamp, bad cursor -> offset 0 (page 1).
      let n = parseInt(u.searchParams.get("limit") || "3", 10);
      if (isNaN(n)) n = 3;
      n = Math.max(1, n);
      let offset = parseInt(u.searchParams.get("cursor") || "0", 10);
      if (isNaN(offset) || offset < 0) offset = 0;
      const ordered = rows.slice().sort(cmpRows);
      const window = ordered.slice(offset, offset + n);
      const nxt = offset + n < ordered.length && window.length ? String(offset + n) : null;
      return sendJSON(res, 200, { items: window, next_cursor: nxt }, { "X-Page-Size-Max": String(maxPage) });
    }
    return sendJSON(res, 404, { error: "not found" });
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
function opts(a) {
  return {
    fixture: a.fixture || DEFAULT_PRIMARY,
    limit: a.limit ? parseInt(a.limit, 10) : DEFAULT_LIMIT,
    max: a.max ? parseInt(a.max, 10) : DEFAULT_MAX,
  };
}
async function cmdCheck(a) {
  const url = requireUrl(a);
  const o = opts(a);
  const spec = specFrom(o.fixture);
  console.log(`Pagination Test Kit — checking ${url}`);
  console.log(`  fixture: ${o.fixture} (GET ${spec.path}?${spec.limitParam}=N&${spec.cursorParam}=…)   page size: ${o.limit}`);
  console.log(`  (set --limit to the page size to traverse with; --max is the documented page-size cap fallback)\n`);
  const failures = await runSuite(url, o.fixture, o.limit, o.max);
  console.log("");
  if (failures === 0) { console.log("ALL PROPERTIES PASS/SKIP — this endpoint's pagination behaves correctly."); return 0; }
  console.log(`${failures} PROPERTY(IES) FAILED — see the FAIL lines above and GOTCHAS.md.`);
  return 1;
}
async function cmdSingle(name, fn) {
  const [passed, detail] = await fn();
  printResult(name, passed, detail);
  return passed === false ? 1 : 0;
}
function cmdList() {
  const m = loadManifest();
  console.log("bundled fixtures (docs-derived request templates — see fixtures/PROVENANCE.md):");
  for (const stem of listFixtures()) {
    const e = m[stem];
    console.log(`  ${stem.padEnd(16)}  GET ${(e.path || "?").padEnd(10)}  cursor=${e.cursor_param || "cursor"} items=${e.items_field || "items"}  — ${e.note || ""}`);
  }
  return 0;
}
async function cmdDemo() {
  console.log("=".repeat(74));
  console.log("  PGTK DEMO MODE — bundled REFERENCE stubs, in-process, on localhost.");
  console.log("  NO real endpoint, NO accounts, NO money. This proves the kit works");
  console.log("  before you point `pgtk check --url` at your own app.");
  console.log("=".repeat(74));
  const maxPage = 5;
  const correct = correctStub(maxPage);
  const naive = naiveStub(maxPage);
  const cport = await listen(correct);
  const nport = await listen(naive);
  let cf, nf;
  try {
    console.log(`\n--- CORRECT stub (keyset on (created_at, id), max_page ${maxPage}) — expect ALL PASS ---`);
    cf = await runSuite(`http://127.0.0.1:${cport}`, DEFAULT_PRIMARY, DEFAULT_LIMIT, DEFAULT_MAX);
    console.log(`\n--- NAIVE stub (OFFSET pagination, no clamp, forged cursor accepted) — expect the kit to FLAG it ---`);
    nf = await runSuite(`http://127.0.0.1:${nport}`, DEFAULT_PRIMARY, DEFAULT_LIMIT, DEFAULT_MAX);
  } finally {
    correct.close();
    naive.close();
  }
  console.log("\n" + "=".repeat(74));
  if (cf === 0 && nf > 0) {
    console.log(`  DEMO OK: correct stub passed all properties; naive stub flagged on ${nf} property(ies).`);
    console.log("  The kit distinguishes correct keyset pagination from a broken offset one.");
    console.log("=".repeat(74));
    return 0;
  }
  console.log(`  DEMO UNEXPECTED: correct failures=${cf}, naive failures=${nf} (expected 0 and >0).`);
  console.log("=".repeat(74));
  return 1;
}
async function main() {
  const argv = process.argv.slice(2);
  const cmd = argv[0];
  const a = parseArgs(argv.slice(1));
  let rc = 0;
  switch (cmd) {
    case "check": rc = await cmdCheck(a); break;
    case "traversal": { const o = opts(a); rc = await cmdSingle("traversal", () => checkTraversal(requireUrl(a), o.fixture, o.limit)); break; }
    case "stable-under-mutation": { const o = opts(a); rc = await cmdSingle("stable-under-mutation", () => checkStableUnderMutation(requireUrl(a), o.fixture, o.limit)); break; }
    case "ordering": { const o = opts(a); rc = await cmdSingle("ordering", () => checkOrdering(requireUrl(a), o.fixture, o.limit)); break; }
    case "page-size": { const o = opts(a); rc = await cmdSingle("page-size", () => checkPageSize(requireUrl(a), o.fixture, o.limit, o.max)); break; }
    case "terminal": { const o = opts(a); rc = await cmdSingle("terminal", () => checkTerminal(requireUrl(a), o.fixture, o.limit)); break; }
    case "cursor-tamper": { const o = opts(a); rc = await cmdSingle("cursor-tamper", () => checkCursorTamper(requireUrl(a), o.fixture, o.limit)); break; }
    case "demo": rc = await cmdDemo(); break;
    case "list": rc = cmdList(); break;
    default:
      fail("usage: pgtk {check|traversal|stable-under-mutation|ordering|page-size|terminal|cursor-tamper|demo|list} [--url ...] [--fixture ...] [--limit N] [--max M]");
  }
  process.exit(rc);
}

main();
