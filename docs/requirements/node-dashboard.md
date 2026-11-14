# Project B: MSQP Node Dashboard Requirements

**Owner:** Robert Hipple, KE8UQV (lead). **Status:** DRAFT, 2026-11-10. Every requirement here is
`[NEW]` ⬜: a starting list for Robert to cut, change, and extend.
Method, tags and IDs: [`README.md`](README.md). This document follows the section layout of the
SigMonD
[`REQUIREMENTS-TEMPLATE.md`](https://github.com/HamSCI/sigmond/blob/main/docs/REQUIREMENTS-TEMPLATE.md)
in short form. When B's code repository is decided, this file moves there as its
`docs/REQUIREMENTS.md`, and the SigMonD requirements index gains a line for it.

## 1. Context and problem

A PSWS node running SigMonD's `meteor-scatter` client decodes MSK144 on 28.145 and 50.260 MHz and
writes each decode to the node's shared SQLite database (`psk.spots`, `mode = "msk144"`), from
which `hs-uploader` sends it to PSKReporter. The station's host has no view of that reception
made for meteor scatter: when pings arrive, on which band, from whom, and how this shower compares
with the last. PSKReporter shows spots, but not the node-side detail, and not in an MSQP frame.

## 2. Goals

- Let a station host see, live and on the node itself, what their station is hearing by meteor
  scatter.
- During an MSQP event, show the event context: the window, the current band-alternation slot, and
  a link to the event on msqp.hamsci.org.
- Make the node's data easy to hand on: to the host, to msqp.hamsci.org, and to researchers.

## 3. Non-goals

- Not a replacement for msqp.hamsci.org: no scoring, no event-wide leaderboard of its own.
- Not a recorder or decoder. It reads what `meteor-scatter` produces and changes nothing upstream.
- Not a transmit or QSO tool.

## 4. Stakeholders

Station hosts (the users); Robert Hipple, KE8UQV (lead); Tom McMahan, K1FR (meteor-scatter trail
geometry and Doppler); SigMonD maintainers AC0G and AI6VN
(client contract, node platform); `meteor-scatter` maintainers (the data source); AF8A and the
Meteor Scatter Working Group (event semantics and conventions); project A (interface partner);
researchers (exports).

## 5. Constraints

| ID | Requirement | Tags |
|---|---|---|
| `MSD-C-001` | SHALL install, start, stop and report status through SigMonD (`smd`), conforming to the client contract at the version current when B is adopted, or through a lifecycle shim as `gmag-webui` uses until it conforms. Which one: open decision 1 in `README.md`. | `[NEW]` ⬜ |
| `MSD-C-002` | SHALL run on node hardware beside the recorders without needing extra hardware. | `[NEW]` ⬜ |
| `MSD-C-003` | SHALL read the `meteor-scatter` output as that client defines it (sink rows per `MTS-F-030`, `reporter_id` per contract §19), and SHALL name the client version it was tested against. | `[NEW]` ⬜ |

## 6. Functional requirements

| ID | Requirement | Tags |
|---|---|---|
| `MSD-F-001` | SHALL list recent MSK144 decodes from the node's own sink, by band, with UTC time, callsign heard, grid if decoded, and SNR. New decodes SHALL appear within one T/R period of being written. | `[NEW]` ⬜ |
| `MSD-F-002` | SHALL show activity over time per band (decodes per minute, 6 m and 10 m together), for the current night and a selectable earlier window. | `[NEW]` ⬜ |
| `MSD-F-003` | SHALL map stations heard, from their decoded grid squares, with path lines to the node. | `[NEW]` ⬜ |
| `MSD-F-004` | **Event mode.** When an MSQP window from the event feed (`MSI-I-001`) is open, SHALL show the event, time remaining, and the current band-alternation slot; outside a window, the next event. | `[NEW]` ⬜ |
| `MSD-F-005` | SHOULD show per-ping measures (duration, peak SNR, decay time) where the recorder makes them available. Depends on `meteor-scatter` keeping or measuring audio; it deletes slot WAVs after decode by default (`MTS-F-004`). | `[NEW]` ⬜ |
| `MSD-F-006` | SHOULD compare this station's activity between showers (this event against earlier ones), from locally kept history. | `[NEW]` ⬜ |
| `MSD-F-007` | SHALL link to this station's page and the event's page on msqp.hamsci.org (`MSI-I-004`). | `[NEW]` ⬜ |
| `MSD-F-008` | SHOULD export a per-event bundle of this station's decodes (and audio, where kept) in a documented format, suitable for the host's Zenodo deposit or for upload under `MSI-I-003`. | `[NEW]` ⬜ |
| `MSD-F-009` | SHALL show the health of the chain it depends on: whether `meteor-scatter` is running, time of the last decode per band, and whether uploads to PSKReporter are flowing, using what SigMonD already reports. | `[NEW]` ⬜ |

## 7. Quality requirements

| ID | Requirement | Tags |
|---|---|---|
| `MSD-Q-001` | SHALL only read the sink. It SHALL NOT write to it, lock it for long, or take CPU the recorders need; its resource budget is set with the SigMonD maintainers. | `[NEW]` ⬜ |
| `MSD-Q-002` | SHALL work fully with no internet connection. Anything from msqp.hamsci.org is cached and optional. | `[NEW]` ⬜ |
| `MSD-Q-003` | SHALL be reachable only on the local network by default. Exposure through SigMonD remote access is an explicit host choice. | `[NEW]` ⬜ |
| `MSD-Q-004` | SHALL be usable on a phone and SHOULD meet WCAG 2.2 AA, matching `MSQP-Q-013`. | `[NEW]` ⬜ |
| `MSD-Q-005` | SHALL NOT send anything off the node except under an interface flow the host has turned on. | `[NEW]` ⬜ |

## 8. Data

| ID | Requirement | Tags |
|---|---|---|
| `MSD-D-001` | History kept locally SHALL have a stated retention limit, and SHALL respect SigMonD's storage policy (contract §17.7). | `[NEW]` ⬜ |

## 9. Open questions

- **T/R period.** The `meteor-scatter` README gives a default T/R period of 30 s, matching stock
  WSJT-X MSK144; its `docs/REQUIREMENTS.md` (`MTS-F-003`) says slots align to a 15 s cadence. The
  MSQP convention has east-pointing antennas transmit on even minutes and west on odd. Which
  period a node uses during MSQP, and whether that is set from the event feed, needs the
  `meteor-scatter` maintainers and the Working Group.
- **Audio retention** for `MSD-F-005` and `-008`: a `meteor-scatter` setting, a disk budget, or
  both.
- **Code location and contract conformance**: `README.md`, open decision 1.
- **Technology**: Robert's choice, with the SigMonD maintainers. `gmag-webui` (a static dashboard
  served by Deno) is the existing precedent on a node.
