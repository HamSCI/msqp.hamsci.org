# MSQP Requirements: Two Projects and the Interface Between Them

**Status: DRAFT for revision by the project leads.** Opened 2026-11-10. Nothing here is adopted
until it merges through review. First draft by Claude (Anthropic, `claude-opus-5-5`) at
N. A. Frissell's (W2NAF) direction, from `docs/project_description.md` and the public SigMonD and
`meteor-scatter` repositories. Every requirement below needs a human owner's review.

## Why this exists

The MSQP software effort is now two projects with different leads, platforms and audiences. They
need to work together without either one blocking the other.

| | **A. msqp.hamsci.org** | **B. MSQP node dashboard** (working name) |
|---|---|---|
| **Lead** | Andrew Kusner (`AndrewKusner`), University of Scranton CS senior capstone | Robert Hipple, KE8UQV (`roberthipple`), HamSCI volunteer |
| **What it is** | The central web platform: event registry, registration, log and spot ingest, scoring, live event view, Zenodo deposit, results, public API | A meteor-scatter dashboard that runs **on a PSWS node** as a SigMonD client, showing that station's own MSK144 reception |
| **Runs on** | HamSCI servers | The station host's own node, next to the `meteor-scatter` recorder |
| **Audience** | All MSQP entrants, the organizer (AF8A), researchers | The station's host |
| **Sees** | Every entrant, through PSKReporter and uploaded logs | One station, through its own SigMonD database, in more detail than PSKReporter carries |
| **Requirements** | [`msqp-site.md`](msqp-site.md) | [`node-dashboard.md`](node-dashboard.md) |

The **interface** between them is its own document, [`interface.md`](interface.md), owned by both
leads together. Neither project restates the interface in its own document; each points to it.

**Most MSQP entrants will never run a PSWS node.** They run WSJT-X at home. Project A has to
serve them fully on its own, and project B adds detail for the stations that do run a node. Neither
project may depend on the other being up (requirement `MSQP-Q-012` and `MSD-Q-002`).

## Method

We use the SigMonD suite's requirements method, so that B fits beside the other SigMonD clients
and A and B can cite each other:
[`HamSCI/sigmond/docs/REQUIREMENTS-TEMPLATE.md`](https://github.com/HamSCI/sigmond/blob/main/docs/REQUIREMENTS-TEMPLATE.md).

- **IDs** are `<PREFIX>-<TYPE>-<NNN>`, and once assigned they never change or get reused.
  - Prefixes (**provisional**, confirm none collide with an existing SigMonD component code):
    `MSQP` for project A, `MSD` for project B, `MSI` for the interface.
  - Types: `F` functional, `Q` quality (non-functional), `I` interface, `C` constraint, `D` data.
- **Provenance tag** on every requirement: `[DOC]` already written down somewhere (for A, the
  project description's R1 to R13), `[CODE]` implied by existing code, `[NEW]` first stated here.
- **Status tag**: ✅ built and verified, 🟡 partly built or unverified, ⬜ specified, not built.
- **SHALL** is a requirement, **SHOULD** a strong preference, **MAY** an option.
- A requirement is done being written when it is **testable**: someone other than the author
  could write the test that shows it is met.

The SigMonD client contract
([`CLIENT-CONTRACT.md`](https://github.com/HamSCI/sigmond/blob/main/docs/CLIENT-CONTRACT.md))
governs how B plugs into SigMonD. The SigMonD maintainers own it. B's requirements reference it
rather than restating it.

## Who decides what

| Who | Role | Decides |
|---|---|---|
| N. A. Frissell, W2NAF | PI and project advisor | Scope of both projects; anything touching the capstone; production deploys of A |
| Gary Mikitin, AF8A | MSQP organizer and scorer; primary stakeholder | Scoring rules; what counts as an entrant; event semantics |
| Andrew Kusner | Lead, project A (capstone) | A's requirements and design, with W2NAF |
| Robert Hipple, KE8UQV | Lead, project B (volunteer) | B's requirements and design |
| Both leads together | Interface owners | `interface.md`. A change needs both leads' approval |
| SigMonD maintainers (AC0G, AI6VN) | Owners of the client contract and the node platform | Anything B needs from SigMonD or the contract; consulted on the interface |
| HamSCI Meteor Scatter Working Group | Operating conventions | Band alternation, transmit-slot rules, AGC guidance |
| Other helpers | To be assigned | Join a project through its lead |

**The capstone boundary.** Project A is a graded capstone, so its student team carries the
majority of A's work and its management. Volunteers can advise, review, and contribute, but A's
threshold tier must not depend on volunteer work landing. The interface items sit in A's upper
tiers for that reason (see `msqp-site.md`).

## Calendar

| Date | Event | Project A | Project B |
|---|---|---|---|
| 13–15 Dec 2026 | Geminids MSQP | Shadow run: collect data alongside AF8A's process | Collect a full event's data from one or more nodes running `meteor-scatter`, to design the dashboard against |
| 2–4 Jan 2027 | Quadrantids MSQP | Parallel run, the validation event | First live use: a minimum dashboard on at least one node (proposed: `MSD-F-001`, `-002`, `-004`) |
| 17–18 Apr 2027 | 2027 HamSCI Workshop, U. of Scranton | Capstone presentation | Proposed: present alongside A |
| May 2027 | Eta Aquariids MSQP (dates unpublished) | First authoritative run, after the capstone | Fuller release |

B's dates are proposals. Robert sets B's schedule, and volunteer time is not a capstone deadline.

## Open decisions

Each needs an answer from the person named. Record the answer in the relevant document and remove
the item here.

1. **Where B's code lives** (Robert, with the SigMonD maintainers and W2NAF): a new public repo
   under `HamSCI`, inside `meteor-scatter`, or inside `sigmond`. Also whether B conforms to the
   client contract with its own `deploy.toml` or starts with a shim, as `gmag-webui` does.
2. **Interface scope for 2026–27** (W2NAF, both leads): flows 1 and 2 only, or flow 3 too (see
   `interface.md`).
3. **Project A's team** (W2NAF): Andrew alone, or other students or helpers?
4. **Meeting cadence** (both leads): proposed, a joint call every two weeks until the Quadrantids.
5. **Does SigMonD already have a path for flow 3?** (SigMonD maintainers): `hs-uploader` already
   ships to PSWS. Could MSQP observations ride that path rather than a new one?
6. **Prefixes** `MSQP`, `MSD`, `MSI` (SigMonD maintainers): any collision with existing codes?

## Proposed tracking setup (not yet done)

- One GitHub issue per piece of work, labeled `project:site`, `project:node-dashboard` or
  `interface`, and added to the HamSCI project board.
- Milestones on the calendar dates above.
- Requirement IDs in issue titles and commit messages, so a requirement links to its work.
- The project description (`docs/project_description.md`) will be revised to match these
  documents once they settle. Until then, where the two disagree, these documents are the newer
  intent, and the description still governs the capstone as presented.
