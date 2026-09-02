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
| ~~Project period: Fall 2027 – Spring 2028~~ | NAF, asked directly | **RETIRED 2026-09-02, superseded below. Do not act on this.** |
| Project period: **Fall 2026 – Spring 2027** | NAF, 2026-09-02 | Supersedes the row above, which was chosen from a menu earlier the same day. Matches the QPA capstone window. See the calendar section below for what this changes. |
| Team size: 2–3 CS students | NAF, asked directly | Matches QPA. |
| Technology stack left open | Assistant | Named as a semester-1 trade study with maintainability-after-handoff as an explicit weighted criterion, following QPA's trade-study pattern. Prescribing a stack in a proposal would remove the most instructive design decision in the project. |
| Scope handled by success tiers | Assistant | NAF asked for coordination and reporting, and separately that it "support the meteor scatter project". Threshold = registry, registration, ADIF ingest, scoring. Objective = PSKReporter ingest, live dashboard, Zenodo, public API, run a live event. Stretch = serving the science pipeline directly. |

## Decision record: project period moved to Fall 2026 – Spring 2027

> "The timeline is Fall 2026 - Spring 2027. Students are expected to present at the HamSCI workshop in Scranton April 17-18, 2027"
> — NAF, 2026-09-02

This reverses the Fall 2027 – Spring 2028 answer given earlier the same day and retires it. The 2028 workshop placeholder is resolved: the anchor is the **2027 HamSCI Workshop, 17–18 April 2027, at the University of Scranton** (verified against hamsci.org/hamsci2027).

### What the new window actually contains

Verified against hamsci.org/msqp. Neither calendar moves.

| Date | Event | Academic collision | Role assigned |
|---|---|---|---|
| 13–15 December 2026 | Geminids MSQP | Very end of the fall semester | Shadow run: observe and collect |
| 2–4 January 2027 | Quadrantids MSQP | Winter break, before spring classes | Parallel run: the validation event |
| 17–18 April 2027 | 2027 HamSCI Workshop, Scranton | Mid-spring, before finals | Present the work |

**Three consequences, all now written into section 6.**

1. **The live event moved from the Geminids to the Quadrantids.** December 2026 is roughly the last week of the first semester, which is too early for a production deployment. The Geminids became a shadow run, and the objective tier's live-dashboard demonstration moved to the January Quadrantids parallel run.
2. **The system that runs the Quadrantids must be built in the fall**, because 2–4 January precedes the spring semester. This is why the threshold tier is deliberately scoped to a replay against the already-published August and December 2025 events: it is a real, gradeable semester-1 milestone that needs no live event.
3. **The Quadrantids are the only live MSQP inside the course.** The next event is the Eta Aquariids in May 2027, at or after the end of the spring semester; its exact dates are unpublished, so none were invented. The proposal names the May event as the natural first authoritative run for whoever maintains the platform after handoff.

**Operating over winter break is a real ask** and is now stated plainly in the proposal, so that a team decides in the fall who is available for 2–4 January rather than discovering the problem in December.

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

Sources are listed in section 12 of the project description (section 11 is the glossary, added 2026-09-02).

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
3. ~~**2028 HamSCI Workshop** dates and venue are unannounced.~~ **RESOLVED 2026-09-02** by the move to Fall 2026 – Spring 2027: the anchor is the 2027 workshop, 17–18 April 2027 at Scranton, verified against hamsci.org/hamsci2027. The bracketed placeholder is gone.
4. **Development budget** carries `[Amount to be confirmed.]`, matching the same placeholder in QPA section 10.
5. **AF8A has not seen this.** He is named as the primary stakeholder and the proposal characterizes his workflow and its costs from published artifacts. He should read and approve section 2 before this document is shown to CS faculty.
6. **Scoring rules are unwritten.** Extracting them from AF8A's practice is called out as a semester-1 deliverable, and is the most likely place for the schedule to slip.
