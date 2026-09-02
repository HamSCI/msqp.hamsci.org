# 2026-09-02 — MSQP capstone proposal: first draft

Written for a fresh session with no context.

## What NAF asked for

> "we also have a Meteor Scatter QSO Party project. You can read about that at hamsci.org/msqp. We need an interactive website to keep track of MSQP reports and coordinate MSQP activities. Right now, we have our volunteer Gary Mikitin AF8A managing all of that manually at msqp.hamsci.org.
>
> I am thinking that the development of an interactive and automated msqp.hamsci.org website would be a great student project for undergradate computer science students, possibly as a senior capstone project. I have not yet talked to the Computer Science professors about this, but I think if we come up with a good proposal, they may let me try to recruit some students to work on this.
>
> So, can you help me write a proposal like we did for the QPA project? The main differences are that this would be for a senior computer science student capstone instead of engineering. It would also support the meteor scatter project. You can use all the same funding numbers as in the QPA project... they are all related. We also have a Meteor Scatter Working group on HamSCI that can help advise the project."
> — NAF, 2026-09-02

## What was produced

`docs/project_description.md`, structured to parallel `~/code/QPA/docs/project_description.md` section for section (background, gap, objective, system concept, requirements with success tiers, two-semester plan, deliverables, what you will learn, team roles, resources, references). Repository scaffolded from the QPA copy of `ai_project_template`.

## Decisions

| Decision | Made by | Note |
|---|---|---|
| Project period: Fall 2027 – Spring 2028 | NAF, asked directly | Gives a year to recruit CS faculty and students. Puts the December 2027 Geminids and January 2028 Quadrantids MSQP events inside the project window as live integration tests. |
| Team size: 2–3 CS students | NAF, asked directly | Matches QPA. |
| Technology stack left open | Assistant | Named as a semester-1 trade study with maintainability-after-handoff as an explicit weighted criterion, following QPA's trade-study pattern. Prescribing a stack in a proposal would remove the most instructive design decision in the project. |
| Scope handled by success tiers | Assistant | NAF asked for coordination and reporting, and separately that it "support the meteor scatter project". Threshold = registry, registration, ADIF ingest, scoring. Objective = PSKReporter ingest, live dashboard, Zenodo, public API, run a live event. Stretch = serving the science pipeline directly. |

## The argument the proposal makes

The case rests on measured latency, from HamSCI's own published announcements:

| Event | Ran | Results published | Gap |
|---|---|---|---|
| Perseids | 11–12 Aug 2025 | 16 Nov 2025 | ~3 months |
| Geminids | 12–13 Dec 2025 | 15 Apr 2026 | ~4 months |

with the cause stated in HamSCI's own words: "Most of the MSQP scoring effort revolves around interpreting PSKReporter data (spots) for a variety of entrants", against 280 million lines of it for the December 2025 event.

Two framing choices worth preserving:

1. **The threshold acceptance test is a replay.** Load the August 2025 and December 2025 events, run the scoring engine, and reproduce AF8A's published scores with every difference explained. Reproducing a known-good human result is how the team proves the engine is right, and it is a self-contained, gradeable semester-1 milestone that needs no live event.
2. **Two constraints are design inputs from week one**: the manual path must survive (MSQP runs on an astronomical schedule whether or not the software works), and the organizer stays in control (every score inspectable, overridable, and audited). Both protect AF8A, who is the reason the campaign exists.

## Verified facts (do not re-derive)

Sources are listed in section 11 of the project description.

- MSK144 only; 50.260 MHz (6 m) and 28.145 MHz (10 m).
- Six events per year: Quadrantids, Eta Aquariids, Daytime Arietids, Southern Delta Aquariids, Perseids, Geminids.
- Categories: two-way and monitor (receive only). Fixed locations only.
- Dual-band stations alternate bands at xx:00, xx:20, xx:40. East-pointing antennas transmit on even minutes, west-pointing on odd. Receiver AGC off, so ping decay time is measurable.
- Scoring inputs: PSKReporter spots plus submitted ADIF (`wsjtx_log.adi`, `ALL.TXT`).
- Audio: participants zip WSJT-X WAV files (Zenodo caps a deposit at 100 files) and deposit to the HamSCI Zenodo community with a hand-typed title: `CALL GRID YYYYMMDD-DD Meteor Scatter QSO Party`.
- `HamSCI/meteor-scatter` decodes MSK144 on a PSWS station and publishes to `psk.spots` with `mode="msk144"`, reaching PSKReporter through `hs-uploader`. A PSWS site running it is an unattended MSQP monitor station.
- A four-class Random Forest classifier (underdense MS, overdense MS, aircraft scatter, noise) over MSQP WAV files exists as Nina Tormann's Scranton BS thesis work.

## Open items

1. **`msqp.hamsci.org` does not exist yet.** The hostname returned NXDOMAIN in this session, and the `HamSCI/msqp.hamsci.org` GitHub repository has no commits. NAF's request described AF8A as managing MSQP "at msqp.hamsci.org"; the proposal treats the hostname as the deployment target the project creates. **Confirm with NAF whether AF8A works from some other surface today** (a spreadsheet, a mailbox, a hamsci.org page), because the requirements elicitation in semester 1 needs to start from whatever that surface actually is.
2. **Meteor Scatter Working Group membership is unrecorded.** No public HamSCI page found in this session names the group or its members. The proposal names it as an advisory body on NAF's statement alone. Names and callsigns should be added once NAF supplies them.
3. **2028 HamSCI Workshop** dates and venue are unannounced; the semester-2 plan carries a bracketed placeholder (W13).
4. **Development budget** carries `[Amount to be confirmed.]`, matching the same placeholder in QPA section 10.
5. **AF8A has not seen this.** He is named as the primary stakeholder and the proposal characterizes his workflow and its costs from published artifacts. He should read and approve section 2 before this document is shown to CS faculty.
6. **Scoring rules are unwritten.** Extracting them from AF8A's practice is called out as a semester-1 deliverable, and is the most likely place for the schedule to slip.
