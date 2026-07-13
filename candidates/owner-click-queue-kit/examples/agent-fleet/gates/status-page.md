# Status Page

> Gate file written by the infra agent, session 2026-07-11. Pure
> click-run: no open decisions, the agent pre-chewed everything.

The uptime page is generated and committed at `site/status/`; serving
it needs a DNS record only the owner's registrar account can create.

## ⚑ OWNER-GATE — DNS click-run

1. **Registrar sign-in:** owner signs into the registrar (the one
   account agents are firewalled from).
2. **Record:** add `CNAME status → pages.example-host.net` (TTL 300 —
   pre-chewed, no decision needed).

- [ ] ⚑ **Owner:** CNAME `status` → `pages.example-host.net` added at
      the registrar (TTL 300).
- [ ] ⚑ **Owner:** confirm `https://status.example.com` loads the
      committed page (VERIFIED-WHEN: the page shows build id `7f3a2`).
