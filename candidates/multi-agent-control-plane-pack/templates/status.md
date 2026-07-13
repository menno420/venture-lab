# <lane> heartbeat

updated: <ISO8601 from date -u>

- **phase / health:** <what the lane is doing; blocked or clear>
- **last shipped:** PR #<n> (squash `<sha>`) — <one line>
- **orders:** <acked/done by number — e.g. "001 done (PR #n); 002
  acked, execution next wake"; claimed-by annotations here>
- **blockers:** <verbatim errors, or "none">
- **⚑ needs-owner / needs-manager:** <parked decisions, click-level,
  plain language — or "none">
- **next (baton):** <1–3 items a successor session could pick up cold>

<!-- Overwritten by the lane each session; re-stamped LAST, after a
final inbox re-read at HEAD. One writer: the lane. -->
