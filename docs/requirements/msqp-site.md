# Project A: msqp.hamsci.org Requirements

**Owner:** Andrew Kusner (lead), with W2NAF. **Status:** DRAFT, 2026-11-10.
Method, tags and IDs: [`README.md`](README.md).

This document restates R1 to R13 from `docs/project_description.md` section 5 under permanent IDs,
and records what changes now that there is a second project. Each requirement's full text is
still the project description's until the capstone's requirements specification (deliverable 1)
replaces it. That specification is where these become testable statements.

## 1. Context

See `docs/project_description.md` sections 1 to 4. What is new: some MSQP stations will run a
PSWS node with the `meteor-scatter` client and the project B dashboard. Those stations already
reach PSKReporter like any other. In addition, they can talk to this site directly through the
interface in [`interface.md`](interface.md).

## 2. Requirements carried over from R1 to R13

| ID | From | Requirement (short form) | Tags | What changes with project B |
|---|---|---|---|---|
| `MSQP-F-001` | R1 | Event registry, as pages and a machine-readable feed | `[DOC]` ⬜ | The feed is now consumed by nodes, so its format is an interface requirement (`MSI-I-001`). It must be versioned and must carry the operating conventions as data a program can act on, not only as prose. |
| `MSQP-F-002` | R2 | Entrant registration with validation | `[DOC]` ⬜ | Adds a path for a node to enroll as a monitor-category entrant (`MSI-I-002`). Open: does a node entrant need a named human operator, and whose callsign does it enter under? AF8A decides. |
| `MSQP-F-003` | R3 | ADIF and `ALL.TXT` log ingest | `[DOC]` ⬜ | None. |
| `MSQP-F-004` | R4 | Scheduled PSKReporter spot ingest, filtered to MSK144 on MSQP frequencies | `[DOC]` ⬜ | If flow 3 is adopted, the same spot can arrive twice, through PSKReporter and directly from a node. Ingest must recognize the duplicate. |
| `MSQP-F-005` | R5 | Scoring engine: deterministic, auditable, overridable | `[DOC]` ⬜ | AF8A rules on how node monitor stations are scored, and whether node-only data (not in PSKReporter) may count. |
| `MSQP-F-006` | R6 | Live event dashboard | `[DOC]` ⬜ | Keeps the event-wide view **and** the per-station view for every entrant, from PSKReporter, because most entrants have no node. The deep single-station view of a node's own data belongs to project B. A links to a node's dashboard only if its host opts in. |
| `MSQP-F-007` | R7 | Zenodo deposit into the participant's own account | `[DOC]` ⬜ | Open: do nodes deposit audio too? If so, the metadata builder should serve both (see `MSD-F-008`). |
| `MSQP-F-008` | R8 | Public, versioned data API and bulk export | `[DOC]` ⬜ | Nodes become API consumers (`MSI-I-004`), so breaking changes need a version bump and notice. |
| `MSQP-F-009` | R9 | Results publication | `[DOC]` ⬜ | None. |
| `MSQP-F-010` | R10 | Accounts, roles, audit | `[DOC]` ⬜ | If flows 2 or 3 are adopted: a machine credential per node, separate from human accounts, revocable, with node actions in the audit trail. |
| `MSQP-Q-011` | R11 | Deployment, operations, handoff | `[DOC]` 🟡 | None. Server provisioning exists in the project's private repository; the application side is not built. |
| `MSQP-Q-012` | R12 | Graceful degradation | `[DOC]` ⬜ | Adds: the site SHALL NOT depend on any node being reachable, and a misbehaving node SHALL NOT be able to degrade the site for others (rate limits, input validation). |
| `MSQP-Q-013` | R13 | Privacy, licensing, accessibility | `[DOC]` ⬜ | The same privacy boundary applies to anything a node sends. PSWS station and instrument IDs, and node host names, are treated as non-public unless the host opts in. |

## 3. New requirements

| ID | Requirement | Tags |
|---|---|---|
| `MSQP-C-014` | The site SHALL implement its side of each interface flow adopted in `interface.md`, at the version recorded there. | `[NEW]` ⬜ |
| `MSQP-C-015` | The site's threshold tier (below) SHALL NOT depend on project B or on any interface flow. | `[NEW]` ⬜ |

## 4. Success tiers, updated

The tiers in `docs/project_description.md` section 5 stand. The interface work is placed as
follows:

- **Threshold**: unchanged (R1, R2, R3, R5, R10 at prototype level; replay of August and December
  2025). No interface work.
- **Objective**: adds the event feed in its versioned, node-readable form (`MSI-I-001`).
- **Stretch**: node enrollment (`MSI-I-002`), direct node observations (`MSI-I-003`), and links
  to node dashboards (`MSI-I-004`). This replaces the earlier stretch item "PSWS monitor stations
  enrolled automatically as entrants".

## 5. Open questions for this document

- AF8A: node entrants and scoring (under `MSQP-F-002` and `-005`).
- W2NAF: whether node audio deposits are in scope (`MSQP-F-007`).
- Andrew: the trade study should name what it assumes about the interface (polling or push,
  JSON schema tooling) so that B's lead can review it.
