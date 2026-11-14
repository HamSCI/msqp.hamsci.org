# Interface Between msqp.hamsci.org and the MSQP Node Dashboard

**Owners:** Andrew Kusner and Robert Hipple, KE8UQV, jointly. A change needs both owners'
approval in the pull request. **Version:** 0.1 (draft), 2026-11-10.
Method, tags and IDs: [`README.md`](README.md).

## Principles

1. **Each side is authoritative for its own data.** msqp.hamsci.org owns events, entrants,
   scores and results. A node owns its own observations.
2. **Neither side depends on the other.** Either side keeps working when the other is down, slow
   or wrong (`MSQP-Q-012`, `MSD-Q-002`).
3. **The host decides what leaves the node.** Every flow from a node is off until the station's
   host turns it on (`MSD-Q-005`).
4. **No personal data crosses.** Callsigns and grid squares only, under `MSQP-Q-013`. No email,
   address, host name or IP address in any payload.
5. **Versioned.** Each flow has a version; a breaking change bumps it, and the old version keeps
   working for at least one MSQP event.

## Flows

Scope for 2026–27 is open decision 2 in `README.md`. The proposal is flows 1 and 4 for the
Quadrantids, and flow 2 as a stretch.

| ID | Direction | Flow | Proposed scope |
|---|---|---|---|
| `MSI-I-001` | Site → node | **Event feed.** The R1 schedule as machine-readable data | 2026–27, first |
| `MSI-I-002` | Node → site | **Enrollment.** A node registers as a monitor-category entrant | Stretch |
| `MSI-I-003` | Node → site | **Observations.** Data PSKReporter does not carry | Proposal only, decide later |
| `MSI-I-004` | Site → node | **Event context.** Links into the site, and optionally a leaderboard | 2026–27 |

### `MSI-I-001` Event feed `[NEW]` ⬜

- Public, unauthenticated, cacheable JSON over HTTPS, from msqp.hamsci.org.
- Per event: a stable ID, shower name, UTC start and end, bands with frequencies, mode, and the
  operating conventions as data: band-alternation interval and phase, the transmit-slot rule, the
  T/R period, and the receiver guidance.
- A feed `version` field and a JSON Schema published next to it.
- Nodes poll no more often than once an hour, keep the last good copy, and use it when the site
  cannot be reached.
- **To settle:** field names; the exact convention fields; how a convention change part-way
  through a season is shown.

### `MSI-I-002` Enrollment `[NEW]` ⬜

- The station host starts it on the node; the site records the node as a monitor entrant for an
  event.
- Needs a per-node credential issued by the site (`MSQP-F-010`), revocable by the host or an
  organizer.
- **To settle:** whose callsign the entry is under; whether enrollment is per event or standing;
  AF8A's ruling on scoring (`MSQP-F-005`).

### `MSI-I-003` Observations `[NEW]` ⬜

- Candidate content: per-ping measures (`MSD-F-005`), classifier output, and pointers to audio or
  its Zenodo DOI.
- Every record must carry a key that lets the site recognize the same spot already received
  through PSKReporter (`MSQP-F-004`).
- **Ask the SigMonD maintainers first:** whether the existing `hs-uploader` path to PSWS could
  carry this, rather than a new upload path.

### `MSI-I-004` Event context `[NEW]` ⬜

- Stable URL patterns on msqp.hamsci.org for an event page and a station-in-event page, so a
  node dashboard can link to them (`MSD-F-007`).
- Optional: a small JSON summary for the dashboard to show (event status, entrant count, this
  station's standing).

## Change log

| Version | Date | Change |
|---|---|---|
| 0.1 | 2026-11-10 | First draft. |
