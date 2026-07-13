# CLI v2.0 Release

> Solo-repo pattern: no `gates/` directory — the gate section lives
> inside an ordinary doc in the repo root, and the deriver is pointed
> at the file directly:
>
> ```
> python3 ocq.py derive --gates RELEASE-GATE.md --output OWNER-QUEUE.md
> ```

The v2.0 build is tagged and the changelog is written. Publishing to
the package registry uses the maintainer's own token — owner-only.

## ⚑ OWNER-GATE — release clicks

**OWNER-ACTION — Publish v2.0**
1. **⚑ Version pick:** publish as **2.0.0 stable** (default — the
   breaking changes are documented and the migration guide shipped) or
   as `2.0.0-rc.1` first — maintainer's call.
2. **Registry:** `npm publish` (or the registry's web UI) with the
   maintainer token; agents never hold it.
3. **Announce:** paste the prepared release notes from
   `docs/release-notes-v2.md`.

- [ ] ⚑ **Owner:** version pick confirmed (**2.0.0 stable** (default)).
- [ ] ⚑ **Owner:** package published to the registry with YOUR token.
- [ ] ⚑ **Owner:** release notes pasted + release published on the
      repo host (VERIFIED-WHEN: the release URL loads and
      `npm info` shows 2.0.0).
