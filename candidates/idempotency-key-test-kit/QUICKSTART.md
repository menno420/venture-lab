# Quickstart — Idempotency Key Test Kit v0.1

Three minutes from unzip to a green check on your own endpoint. Stdlib only —
no `pip install`, no `npm install`, no account.

## 0. See the kit work (offline, no endpoint of your own)

```
python3 ikt.py demo      # or: node ikt.js demo
```

This spins up two bundled reference endpoints in-process — a **correct** one and
a deliberately **naive** (no-dedup) one — runs all five properties against each,
and prints a side-effect counter. Expect: the correct stub PASSES all five (and
its counter proves exactly-once); the naive stub is FLAGGED on `replay`,
`mismatch`, `concurrent`, and `missing-key` (and its counter shows it
over-executed). No accounts, no network, no money.

## 1. Start an endpoint

Either your own app, or the bundled correct reference endpoint:

```
python3 stub_handler.py 8000
```

It listens on `http://127.0.0.1:8000` and exposes `POST /charges`, `POST
/orders`, and a `GET /_debug/side_effects` counter.

## 2. Decide your missing-key policy

A request with **no** `Idempotency-Key` is a design choice, and the kit will not
guess it for you:

- `--missing-key-mode required` — a keyless request must be rejected (4xx). Pick
  this if idempotency is mandatory on the endpoint.
- `--missing-key-mode passthrough` — a keyless request is processed without
  idempotency (2xx). Pick this if the key is optional.

(The bundled stub defaults to `required`; set `IKT_REQUIRE_KEY=0` to run it in
pass-through mode.)

## 3. Run the full check

```
python3 ikt.py check --url http://localhost:8000 --missing-key-mode required
```

Expect all five properties `PASS`. Each `FAIL` line names the exact bug and
points at `GOTCHAS.md`.

## 4. Run one property at a time

```
python3 ikt.py replay        --url http://localhost:8000   # safe-retry / exactly-once
python3 ikt.py mismatch      --url http://localhost:8000   # same key, different body → 409/422
python3 ikt.py distinct-keys --url http://localhost:8000   # per-key scoping
python3 ikt.py concurrent    --url http://localhost:8000 --n 4   # in-flight lock
python3 ikt.py missing-key   --url http://localhost:8000 --mode required
```

The Node port is identical: `node ikt.js check --url http://localhost:8000`.

## 5. Run the kit's own test suite

```
python3 -m unittest -v
```

Every request is POSTed over actual HTTP to a reference stub on an ephemeral
port; a side-effect counter proves exactly-once. All green = the kit is intact
on your machine.

---

Next: read `GOTCHAS.md` (one page, five failure modes) and adapt
`stub_handler.py` into your framework of choice.
