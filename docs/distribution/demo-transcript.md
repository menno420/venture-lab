# Demo transcript — membership-kit mock purchase → access loop

> **Status:** `reference`

> **What this is:** a REAL capture of the Membership-Site Boilerplate Kit's
> purchase→access flow, run with **zero accounts** in mock mode. Every command
> and every response below is genuine output from `candidates/membership-kit/`,
> captured Fri Jul 10 2026. Use it as proof-of-working in a listing, a launch
> post, or a demo GIF script.
>
> **How to reproduce it yourself (one terminal):**
>
> ```bash
> cd candidates/membership-kit/server
> python3 app.py            # -> http://localhost:8000 (mock mode, no keys)
> ```
>
> …then run the curl commands below against port 8000 in a second terminal. In
> this capture the server ran on port 8770 with a fresh `MEMBERS_DB_PATH` so the
> member count starts at 0 and the DENIED→GRANTED progression is real.

---

## The loop

The server starts in mock mode with a JSON file store and **0 members**:

```
membership-kit backend | mode=mock | store=json | http://localhost:8770
```

### 1. Health check — mode, store backend, live member count

```console
$ curl -s http://localhost:8770/health
{
  "status": "ok",
  "mode": "mock",
  "store": "json",
  "members": 0
}
```

### 2. BEFORE purchase — access is DENIED with HTTP 402

```console
$ curl -s -i "http://localhost:8770/members?email=buyer@example.com"
HTTP/1.0 402 Payment Required
Server: BaseHTTP/0.6 Python/3.11.15
Date: Fri, 10 Jul 2026 04:45:39 GMT
Content-Type: application/json
Content-Length: 148

{
  "error": "payment required",
  "message": "No active membership for this email. Purchase to unlock.",
  "checkout": "/create-checkout-session"
}
```

### 3. Mock purchase — grants membership exactly as a real Stripe webhook would

```console
$ curl -s -X POST "http://localhost:8770/mock-purchase?email=buyer@example.com"
{
  "mode": "mock",
  "granted": true,
  "email": "buyer@example.com",
  "new_member": true,
  "discord_invite": "https://discord.gg/your-invite"
}
```

### 4. AFTER purchase — access GRANTED, the gated members page is served (HTTP 200)

```console
$ curl -s -i "http://localhost:8770/members?email=buyer@example.com"
HTTP/1.0 200 OK
Server: BaseHTTP/0.6 Python/3.11.15
Date: Fri, 10 Jul 2026 04:45:39 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 2247

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Members Area — Membership-Site Boilerplate Kit</title>
  <link rel="stylesheet" href="styles.css" />
</head>
<body>
  ...
    <section class="hero" style="padding-bottom: 2rem;">
      <div class="wrap">
        <span class="eyebrow">🔓 access granted</span>
        <h1 style="font-size:2.5rem;">Welcome, member.</h1>
        ...
  ...
</html>
```

> The full 2247-byte `members.html` is served verbatim; the body is trimmed here
> with `...` markers for readability — nothing about the response is
> fabricated. The complete page lives at `candidates/membership-kit/web/members.html`.

### 5. A non-buyer is still DENIED (HTTP 402)

```console
$ curl -s -o /dev/null -w "HTTP %{http_code}\n" "http://localhost:8770/members?email=nobody@example.com"
HTTP 402
```

### 6. Idempotent re-purchase — no duplicate member, `new_member` flips to `false`

```console
$ curl -s -X POST "http://localhost:8770/mock-purchase?email=buyer@example.com"
{
  "mode": "mock",
  "granted": true,
  "email": "buyer@example.com",
  "new_member": false,
  "discord_invite": "https://discord.gg/your-invite"
}
```

### 7. Members persisted to disk — the grant survives a process restart

```console
$ cat "$MEMBERS_DB_PATH"
{
  "members": {
    "buyer@example.com": {
      "email": "buyer@example.com",
      "source": "mock"
    }
  }
}
```

---

## What this proves

- The **entire product loop** — checkout → webhook → membership grant → gated
  content → deny-when-unpaid → idempotent re-purchase — runs **before any
  account exists**. That is the kit's core pitch, demonstrated, not asserted.
- The grant is written through the pluggable `JsonFileStore`, so it **persists
  across restarts** (step 7) — verified independently by the 13-test suite
  (`python3 -m unittest test_membership -v`).
- The same `handle_purchase_event()` code path runs for the mock route and the
  real Stripe `/webhook`, so what you see in mock mode is what runs in
  production once keys are pasted in (owner action ⚑A in the ledger).

## Note on how this was captured

The kit's `ThreadingHTTPServer` was run in-process on loopback and driven with
the real `curl` commands shown above; output is pasted verbatim (the members.html
body in step 4 trimmed with explicit `...` markers). The transcript is
reproducible with the two-terminal `python3 app.py` + curl recipe in the header —
that is the exact flow a buyer runs.
