# msqp.hamsci.org: An Interactive Platform for the HamSCI Meteor Scatter QSO Party

## Project Overview
This repository holds the proposal for, and eventually the implementation of, **msqp.hamsci.org**: an interactive web platform to coordinate HamSCI Meteor Scatter QSO Party (MSQP) events, ingest participant logs and PSKReporter spot data, score entries automatically and reproducibly, publish results within days of an event, and serve the resulting data to the research community through a documented public API.

The work is proposed as a two-semester Computer Science senior capstone project at The University of Scranton. Today the entire surrounding workflow (entry collection, spot interpretation, scoring, results publication) is performed by hand by one HamSCI volunteer, and participants wait three to four months for results.

**PI / project advisor**: Dr. Nathaniel A. Frissell, W2NAF, Department of Physics and Engineering, The University of Scranton
**Primary stakeholder**: Gary Mikitin, AF8A, HamSCI volunteer; MSQP organizer and scorer
**Advisory**: HamSCI Meteor Scatter Working Group; HamSCI volunteer software community; The University of Scranton Amateur Radio Club (W3USR)
**Funder**: Supports the HamSCI PSWS / DASI effort, funded by NSF grants AGS-2045755, AGS-2432821, AGS-2432822, AGS-2432824, AGS-2432823, AGS-2431666, and OPP-2332427; NASA grants 80NSSC23K1322, 80NSSC25K7026, and 80NSSC26K0051; and Frankford Radio Club and ARDC grants (per the acknowledgment in Frissell, *QST*, August 2026, p. 33).
**Project period**: Two academic semesters (Fall 2026 – Spring 2027)

**Status**: proposal stage. The Computer Science faculty have not yet been approached, and no students are recruited. `docs/project_description.md` is the document that will be used to make that case.

**Licensing**: source code under the MIT license (this repository's `LICENSE`).
**Student AI use**: Students will be given Claude Code accounts for this project. Their use is governed by `.claude/rules/ai-governance.md`, University of Scranton academic integrity policy, and the course instructor's rules.

## Project Goal
Replace a three-to-four-month manual scoring and publication cycle with a deployed, tested, documented platform that runs a live MSQP event end to end and publishes results within a week, while keeping the organizer in control of every score and keeping the manual path available as a fallback.

## MSQP Domain Facts
Facts a session should not have to re-derive. All are verified against the sources in section 12 of `docs/project_description.md`.

- **Mode**: MSK144 only. **Frequencies**: 50.260 MHz (6 m), 28.145 MHz (10 m).
- **Six events per year**, timed to the Quadrantids (Jan), Eta Aquariids (May), Daytime Arietids (Jun), Southern Delta Aquariids (Jul), Perseids (Aug), Geminids (Dec).
- **Categories**: two-way (transmit and receive) and monitor (receive only). Fixed locations; no rover or mobile.
- **Conventions**: dual-band stations alternate bands every 20 minutes (xx:00, xx:20, xx:40); east-pointing antennas transmit on even minutes, west-pointing on odd; receiver AGC off, so that ping decay time is measurable.
- **Data sources for scoring**: PSKReporter spots plus submitted ADIF logs (`wsjtx_log.adi`, and `ALL.TXT`).
- **Scale reference**: 280 million lines of PSKReporter data captured during the December 2025 event.
- **Latency today**: Aug 11–12 2025 event → results 16 Nov 2025. Dec 12–13 2025 event → results 15 Apr 2026.
- **Audio archive**: participants zip WSJT-X WAV files and deposit them on Zenodo in the HamSCI community, with a hand-typed title convention (`CALL GRID YYYYMMDD-DD Meteor Scatter QSO Party`).

## Fixed Calendar Anchors (project window)
Neither calendar moves. Verified against hamsci.org.

| Date | Event | Role |
|---|---|---|
| 13–15 December 2026 | Geminids MSQP | Shadow run (end of fall semester) |
| 2–4 January 2027 | Quadrantids MSQP | Parallel run, the validation event (winter break) |
| 17–18 April 2027 | [2027 HamSCI Workshop](https://hamsci.org/hamsci2027), U. of Scranton | Team presents |

The next MSQP after the Quadrantids is the Eta Aquariids in May 2027, which falls at or after the end of the spring semester; its exact dates are unpublished. The Quadrantids are therefore the only live MSQP inside the course.

## Related HamSCI Repositories
- [`HamSCI/MSQP`](https://github.com/HamSCI/MSQP) — research questions, reference literature, forward-scatter geometry figures.
- [`HamSCI/meteor-scatter`](https://github.com/HamSCI/meteor-scatter) — ka9q-radio MSK144 ping recorder and decoder; turns a PSWS station into an automated MSQP monitor. Publishes to `psk.spots` with `mode="msk144"`, then to PSKReporter via `hs-uploader`.
- [`HamSCI/Machine-Learning-Meteor-Scatter-Classification-Code`](https://github.com/HamSCI/Machine-Learning-Meteor-Scatter-Classification-Code) — four-class Random Forest classifier (underdense MS, overdense MS, aircraft scatter, noise) over MSQP WAV recordings.
- [`HamSCI/wsprsonde.hamsci.org`](https://github.com/HamSCI/wsprsonde.hamsci.org) — structural precedent for a HamSCI subdomain service repository, and the source of this project's privacy practice (host personal data never appears in tracked data or products).

## Repository Structure
This project starts from the `ai_project_template` scaffold.

```
msqp.hamsci.org/
├── CLAUDE.md
├── README.md
├── LICENSE
├── .gitignore
├── .claude/
│   ├── settings.json
│   ├── commands/commit.md        ← /commit workflow
│   └── rules/
│       ├── ai-governance.md
│       ├── latex-writing.md      ← for reports/posters
│       └── python-code.md
├── ai/
│   └── ai_usage_log.md           ← mandatory AI session log
├── docs/
│   └── project_description.md    ← the capstone project description presented to students
├── notes/                        ← dated session notes
└── reference/                    ← gitignored; local-only reference material
```

## Data Handling
Callsigns and Maidenhead grid squares are public by amateur radio convention. Email addresses, street addresses, phone numbers, and other personal details of participants are **not**, and must never be committed to this repository or appear in any public product. This follows the practice established in `wsprsonde.hamsci.org`.

## Submodules (optional)
If this project later adds submodules:
1. Make changes and commit **inside** the submodule first
2. Then commit the updated submodule pointer in this repo
3. Always use `[AI-assisted]` prefix on commits made with AI assistance
4. Ask before pushing to any remote

The `/commit` workflow auto-detects submodules via `git submodule status`.

## AI Governance
All AI-assisted work must comply with the policies in `.claude/rules/ai-governance.md`.
Every substantive AI session must be logged in `ai/ai_usage_log.md` before committing.
Use the `/commit` command to handle logging and committing in the correct order.
