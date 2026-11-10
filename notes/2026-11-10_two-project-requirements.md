# 2026-11-10: Splitting MSQP into two projects; draft requirements

## Decided (W2NAF)

- The MSQP software effort is now **two projects**: (A) msqp.hamsci.org, led by Andrew Kusner as
  his capstone, and (B) a meteor-scatter dashboard running under SigMonD on a local PSWS node, led
  by volunteer Robert Hipple, KE8UQV (GitHub `roberthipple`). They are to interact. Other helpers
  will join, and the SigMonD team (AC0G, AI6VN) will be involved.
- Requirements for both, and the interface, go in a **draft PR** in this public repository that
  Andrew and Robert work on together, with an issue assigned to both explaining how, posted to the
  `msqp.hamsci.org` project board (HamSCI project #26).

## What was drafted (`docs/requirements/`)

- `README.md`: the split, method, who decides what, calendar, open decisions, tracking proposal.
- `msqp-site.md`: R1 to R13 restated as `MSQP-*` IDs, with what changes for each; interface work
  placed in the objective and stretch tiers so the capstone threshold does not depend on it.
- `node-dashboard.md`: a first `[NEW]` requirement list for B in SigMonD's template layout.
- `interface.md`: four flows (`MSI-I-001` event feed, `-002` enrollment, `-003` observations,
  `-004` event context), principles, version 0.1.

## Why these choices

- **SigMonD's requirements method** (`HamSCI/sigmond/docs/REQUIREMENTS-TEMPLATE.md`: permanent
  IDs, provenance and status tags) so B sits beside the other SigMonD clients and A can cite B.
- **Public repo**, so Robert and the SigMonD team can work without access to the private
  orchestration repository. Robert already had write access here (checked 2026-11-10).
- **Interface out of A's threshold tier**, because the capstone must not depend on volunteer
  timelines.

## Facts checked, from public GitHub on 2026-11-10

- `meteor-scatter` writes MSK144 rows to the SigMonD sink table `psk.spots` (`mode="msk144"`);
  `hs-uploader` ships to PSKReporter and to PSWS/HamSCI (sigmond README).
- `meteor-scatter` deletes slot WAVs after decode by default (`MTS-F-004`).
- **Discrepancy found:** `meteor-scatter` README says default T/R period 30 s; its
  `docs/REQUIREMENTS.md` `MTS-F-003` says a 15 s cadence. Recorded as an open question in
  `node-dashboard.md`.
- `gmag-webui` is a Deno-served static dashboard managed by SigMonD through a lifecycle shim.

## Open

The six open decisions in `docs/requirements/README.md`. Prefixes `MSQP`/`MSD`/`MSI` are
provisional until the SigMonD maintainers confirm no collision. `docs/project_description.md` and
this repo's `CLAUDE.md` ("no students are recruited") are now out of date and should be revised
after the requirements settle.
