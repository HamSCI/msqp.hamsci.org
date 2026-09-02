# An Interactive Platform for the HamSCI Meteor Scatter QSO Party

**Computer Science Senior Capstone Project (two semesters)**

| | |
|---|---|
| **Project advisor** | Dr. Nathaniel A. Frissell, W2NAF, Department of Physics and Engineering, The University of Scranton (nathaniel.frissell@scranton.edu) |
| **Primary stakeholder** | Gary Mikitin, AF8A, HamSCI volunteer; MSQP organizer and scorer |
| **Additional mentors** | HamSCI Meteor Scatter Working Group; HamSCI volunteer software community; The University of Scranton Amateur Radio Club (W3USR) |
| **Team size** | 2–3 students (Computer Science) |
| **Duration** | Two semesters (Fall 2026 – Spring 2027) |
| **Disciplines** | Full-stack web development, REST API design, database and schema design, data engineering and ETL, geospatial data, DevOps, software testing |

*This description is written for computer science students with no amateur radio or physics background. Radio terms are defined where they first appear and collected in the glossary (section 11).*

---

## 1. Background

Six times a year, amateur radio operators around the world spend two nights listening for radio signals bounced off the ionized trails of meteors. Their software logs every contact and reports every signal heard to a public database, and the operators submit those logs and recordings afterward. Today one volunteer turns that data into scores and a results report by hand, and participants wait months to see it. This project builds the platform that does that work in days: a web application with a data pipeline, a scoring engine, a live dashboard, and a public API. The rest of this section explains the event and defines the terms used in the rest of the document. Section 2 states the problem in detail.

The Ham Radio Science Citizen Investigation (HamSCI, [hamsci.org](https://hamsci.org)) is an international collaboration of amateur radio operators, scientists, and students who use the amateur radio service as a distributed scientific instrument. HamSCI runs both a permanent instrument network, the Personal Space Weather Station (PSWS), and a series of coordinated on-air campaigns in which volunteers around the world operate to a common protocol so that their observations can be compared.

The **Meteor Scatter QSO Party (MSQP)** is one of those campaigns. In amateur radio, a *QSO* is a two-way contact between two stations, and a *QSO party* is an organized event in which stations make as many contacts as they can within a set window. Each station is identified by its government-issued *callsign* (W2NAF, AF8A) and located by its *grid square*, a short code such as FN21 that encodes latitude and longitude. MSQP runs six times per year, timed to major meteor showers: the Quadrantids in January, the Eta Aquariids in May, the Daytime Arietids in June, the Southern Delta Aquariids in July, the Perseids in August, and the Geminids in December. Participants operate on two frequencies, 50.260 MHz (the 6 meter band) and 28.145 MHz (the 10 meter band). Two categories of entrant take part: **two-way stations** that transmit and receive, and **monitor stations** that receive only. All stations operate from fixed locations.

The physics is simple to state. Every day, several tons of meteoroid material enter the atmosphere and ionize at roughly 80 to 120 km altitude. Each trail is a short-lived column of plasma that reflects radio waves, opening a path between two stations that would otherwise not hear each other. The path lasts from a few milliseconds to a few seconds, and the brief burst of signal it delivers is called a *ping*. Amateur operators have used the effect for decades. The **MSK144** mode of the free WSJT-X software is designed for it: a message is packed into a 72 ms frame with strong error correction, so that a single ping can carry a complete *decode*, a successfully received message. Two short introductions cover the science at the depth this project needs, and both are listed in section 12. *Meteor Scatter Communications: The Science Behind the Pings* (Suggs, NN4NT, 2017) is a tutorial written for amateur operators. *Meteor Scatter: An Overview* (Weitzen and Ralston, 1988) is a review paper. The team does not need to read further than those to build the platform.

Every MSQP station produces three kinds of data, and all three matter to this project. First, WSJT-X automatically reports every station it decodes to [PSKReporter](https://pskreporter.info), a public service that aggregates such reports from receivers worldwide. Each report, called a *spot*, records that receiver A heard station B at a given time and frequency with a given signal strength. Second, WSJT-X writes a log of the operator's completed contacts in *ADIF* (Amateur Data Interchange Format), a plain-text tagged format that every logging program reads, alongside a running text file, `ALL.TXT`, of every message decoded. Third, participants are asked to keep the raw audio recordings (WAV files) that WSJT-X saves, and to archive them on Zenodo so that researchers can study the pings themselves. Spots and logs are the inputs to scoring. The audio archive is the input to the science.

That data feeds a defined science program. The HamSCI [MSQP research questions](https://github.com/HamSCI/MSQP/blob/main/MSQP%20Research%20Questions.pdf) ask what factors influence meteor scatter propagation, how propagation differs between HF and VHF (the 10 and 6 meter bands, respectively), how long useful meteor scatter propagation lasts as a function of frequency and path length, what the minimum viable station is, and how meteor scatter can be distinguished from other propagation modes. Work is already underway against them. A four-class machine-learning classifier developed at Scranton separates two regimes of meteor scatter (underdense and overdense trails), aircraft scatter, and noise in participant audio recordings, and the HamSCI [`meteor-scatter`](https://github.com/HamSCI/meteor-scatter) client turns a PSWS station into an automated MSK144 monitor.

## 2. The Gap This Project Fills

**Everything that surrounds the data is done by hand, by one volunteer.**

Gary Mikitin, AF8A, organizes each MSQP, collects the entries, gathers the data, computes the scores, and writes the results. The scale of that job is stated plainly in HamSCI's own results announcements. Scoring rests on two sources, "interpreting PSKReporter data (spots) for a variety of entrants" together with submitted ADIF log files, and the December 2025 event alone captured **280 million lines of PSKReporter data**. AF8A reconciles those sources against a roster of entrants, produces a score for each one, and publishes the outcome as a written report.

The cost of doing this by hand shows up as latency. The August 2025 Perseids event ran on 11–12 August 2025; its results were announced on 16 November 2025. The December 2025 Geminids event ran on 12–13 December 2025; its results were published on 15 April 2026. **Participants wait three to four months to find out how they did**, by which time the next shower has come and gone. For an event whose purpose is to build a community of contributors, that delay is the single largest obstacle to growth.

Three further gaps follow from the same root cause.

**There is no live view of the event.** MSK144 operating is a solitary activity conducted at four in the morning. An operator hears pings and has no way to know whether the shower is producing, whether the band is open, or whether anyone is hearing them. Contest and campaign platforms in every other part of amateur radio solved this years ago with live maps and leaderboards. MSQP has nothing of the kind, so participants cannot tell a quiet band from a broken station.

**Data submission is a manual, error-prone ritual.** Each participant creates a Zenodo account, locates the WSJT-X save directory, zips the audio files (Zenodo caps a deposit at 100 files, so a zip is mandatory), selects the HamSCI community, generates a DOI, and types metadata by hand to a naming convention: callsign, six-character grid square, dates operated, and the event name. Every one of those fields is already known to the organizers from the entry form. Typing them again invites transcription errors into exactly the metadata that later analysis depends on.

**The archive has no index.** The audio recordings are safely preserved on Zenodo and the spots are on PSKReporter, but nothing connects them. A researcher who wants every 10 meter recording made by a station with a known antenna during a specific shower has no query that will answer that. The classifier work and the science questions in section 1 both need that index, and at present it must be reconstructed by hand for each study.

**None of this is a criticism of the current arrangement.** AF8A's results reports state that "every effort was made to be sure the reported numbers are accurate and reproducible," and the campaign has run successfully for years on that effort. The problem is that the effort does not scale, it concentrates in one volunteer, and it delivers results too slowly to reward the people who contributed them. This project is about building the machine that does the mechanical part, so that the volunteer's time goes to the parts that need judgment.

## 3. Project Objective

Design, build, test, and deploy **msqp.hamsci.org**: an interactive web platform that coordinates HamSCI Meteor Scatter QSO Party events, ingests participant logs and PSKReporter spot data, scores entries automatically and reproducibly, publishes results within days of an event, and serves the resulting data to the research community through a documented public API.

At the end of the project, a visitor should be able to watch a live MSQP in progress on a map, see their own station's spots appear as they are made, upload a log when the event closes, and read a scored, published result within the same week.

**This platform will be used.** MSQP is a real, recurring, publicized event with real participants, and the site is intended to run it. Two properties follow from that, and they are design inputs from the first week.

1. **The manual path must survive.** MSQP runs six times a year whether or not the software is working. The system must degrade gracefully, and an organizer must always be able to fall back to the current spreadsheet-and-PDF workflow without losing data. Never build a component that becomes a single point of failure for an event on a fixed astronomical schedule.
2. **The organizer stays in control.** Automated scoring supports AF8A's judgment; it does not replace it. Every computed score must be inspectable, overridable by an organizer, and auditable, with the reason for any override recorded.

## 4. System Concept

```
  Participants                              Automated PSWS monitors
  WSJT-X / MSK144                           HamSCI meteor-scatter client
  50.260 MHz (6 m), 28.145 MHz (10 m)       (ka9q-radio, MSK144 decoder)
       │                                             │
       │ registration, ADIF logs, WAV audio          │ MSK144 spots
       │                                             ▼
       │                                    ┌──────────────────────┐
       │                                    │  PSKReporter         │
       │                                    │  spot archive        │
       │                                    └──────────┬───────────┘
       │                                               │ scheduled pull,
       ▼                                               │ event-windowed
 ┌─────────────────────────────────────────────────────▼──────────┐
 │                      msqp.hamsci.org                           │
 │                                                                │
 │   Event registry ──── shower windows, bands, frequencies       │
 │   Entrant registry ── callsign, grid, station, category        │
 │   Log ingest ──────── ADIF / ALL.TXT parse, validate, store    │
 │   Spot ingest ─────── PSKReporter ETL, dedup, event-scoped     │
 │   Scoring engine ──── deterministic, auditable, overridable    │
 │   Live dashboard ──── map, leaderboard, band activity          │
 │   Results generator ─ tables, statistics, plots, soapbox       │
 │   Public data API ─── event → entrant → log → spots → DOI      │
 └───────────┬────────────────────────────────────┬───────────────┘
             │ guided deposit, metadata           │
             │ from registration                  │
             ▼                                    │
 ┌──────────────────────────┐                     │
 │  Zenodo                  │                     │
 │  HamSCI community        │── DOI recorded ─────┘
 │  (WAV audio archive)     │
 └──────────────────────────┘
             │
  ┌──────────┴──────────┬─────────────────┬──────────────────┐
  ▼                     ▼                 ▼                  ▼
 Operators          Organizers        Researchers         hamsci.org
 scores, live map   adjudication,     catalog API,        schedule feed,
 own-station view   results, comms    bulk export,        results links
                                      classifier input
```

**Coordination.** The event registry is the platform's canonical schedule: which shower, which UTC window, which bands and frequencies, and which operating conventions apply. It is published as human-readable pages and as a machine-readable feed, so that hamsci.org and any downstream tooling read one authoritative source.

**Ingest.** Two data streams arrive by different routes. Participant logs (WSJT-X `wsjtx_log.adi` ADIF files and `ALL.TXT`) are uploaded after the event and parsed into per-QSO records. PSKReporter spots are pulled on a schedule for the event window, filtered to the MSQP frequencies and to MSK144, deduplicated, and stored. Volume is the engineering challenge here; the reference figure is 280 million lines for a single event.

**Scoring.** The scoring engine implements the rules AF8A currently applies by hand, as code, with a stated input and a reproducible output. Every score decomposes into the spots and QSOs that produced it, so an entrant can see exactly why they scored what they scored, and an organizer can find and correct a disagreement.

**Archive.** The Zenodo deposit flow builds the deposit metadata from the entrant's registration, so the participant types nothing twice. It deposits into the HamSCI community, and records the returned DOI against the entrant and event. That DOI closes the loop: the public data API can then return, for any recording in the archive, the station that made it, its antenna and power, the event, the band, and the spots that station reported in the same window.

**An integration worth noticing.** The HamSCI `meteor-scatter` client already decodes MSK144 on a PSWS station and publishes spots through the same PSKReporter pipeline that carries FT8 and FT4. A PSWS site running that client is therefore an MSQP monitor station that requires no human present at four in the morning. The platform should treat those stations as first-class entrants, which grows the monitor network at no cost to volunteers.

## 5. Draft Technical Requirements

These are the advisor's and stakeholder's initial targets. Refining them into a complete, testable requirements specification, with each decision justified and each stakeholder need traced to a requirement, is the team's first deliverable.

| # | Requirement (initial target) |
|---|---|
| R1 | **Event registry.** Canonical schedule of MSQP events: shower, UTC start and end, bands, frequencies, mode, and operating conventions. Served as web pages and as a machine-readable feed for hamsci.org and downstream tooling. |
| R2 | **Entrant registration.** Replaces the current entry form. Captures callsign, six-character Maidenhead grid square, category (two-way or monitor), bands, transmit slot convention, and station description (power, antenna, transceiver). Validates callsign syntax and grid-square validity at entry. |
| R3 | **Log ingest.** Accept and parse WSJT-X ADIF (`wsjtx_log.adi`) and `ALL.TXT` uploads. Validate against the event window, bands, and mode; report parse errors back to the participant in terms they can act on; store normalized per-QSO records. |
| R4 | **Spot ingest.** Automated, scheduled retrieval and archival of PSKReporter data for each event window, scoped to MSK144 on the MSQP frequencies. Must sustain the observed volume (reference: 280 million lines for the December 2025 event) with a documented storage and query strategy. |
| R5 | **Scoring engine.** Implements the MSQP scoring rules as code. Deterministic: identical inputs produce identical scores. Auditable: every score decomposes into the contributing spots and QSOs. Overridable: an organizer can adjust a score, and the override and its stated reason are recorded and displayed. |
| R6 | **Live event dashboard.** During an event, a near-real-time public view: propagation paths on a map, band and grid activity, entrant leaderboard, and a per-station view an operator can watch while operating. Initial target: spots visible within 15 minutes of being reported. |
| R7 | **Zenodo deposit integration.** A guided upload flow that builds Zenodo metadata from the entrant's registration, deposits to the HamSCI community via the Zenodo API, and records the returned DOI against entrant and event. The existing manual path stays documented and available. |
| R8 | **Public data catalog and API.** A documented, versioned REST API and bulk export mapping event → entrant → station metadata → logs → spots → Zenodo DOI. Sufficient for the meteor-scatter classifier and the section 1 research questions to select a corpus by query. Machine-readable, with a stable schema and a published data dictionary. |
| R9 | **Results publication.** Generate the tables, statistics, maps, and plots that currently go into a hand-built PDF report, on demand and within days of an event close. Collect participant soapbox comments. Preserve every past event's published results. |
| R10 | **Accounts, roles, and audit.** Authentication with roles for participant, organizer, and administrator. Organizers can adjudicate scores and manage events; participants can manage only their own submissions. All privileged actions are logged to an audit trail. |
| R11 | **Deployment, operations, and handoff.** Runs on HamSCI infrastructure, reproducibly deployable from a documented procedure, with automated tests and continuous integration. Must be operable and maintainable by HamSCI volunteers after the team graduates: a runbook, a data backup and restore procedure, and a monitored health check. |
| R12 | **Graceful degradation.** MSQP runs on the calendar the sky sets. A failure in any automated component must not lose participant data and must not block the event. Ingest accepts submissions when scoring is down; organizers retain an export path to the current manual workflow. |
| R13 | **Privacy, licensing, and accessibility.** Callsigns and grid squares are public by amateur radio convention; email addresses, street addresses, and personal details are not, and must never appear in public pages, API responses, or bulk exports. Contributed data carries a clearly stated open license. The interface meets WCAG 2.2 level AA and works on a phone, because operators check it at four in the morning from the shack. |

**On R1 and R2.** The operating conventions are part of the event definition, and the registry and the registration form must capture them. Stations equipped for both bands alternate between them every 20 minutes (xx:00, xx:20, xx:40), which gives near-simultaneous 6 and 10 meter coverage of the same paths. Operators with directional antennas coordinate their transmit slots by heading: east-pointing stations transmit on even minutes and west-pointing stations on odd minutes. Participants are asked to disable receiver AGC (automatic gain control), because it destroys the amplitude information needed to measure how a ping decays. The first two conventions shape what the event registry publishes and what the dashboard shows. The third is a science requirement that the platform should carry into the guidance it gives participants.

**On R4.** The volume figure is the requirement that most often gets designed past. Read it as a systems requirement: 280 million lines needs a deliberate storage and query design, and it will defeat anything that scans the whole table to render a page. The team is to measure the real data early in semester 1, before committing to a storage design, and to record the measurement in the requirements specification.

**On R5.** The current scoring rules exist as AF8A's practice and as the published results reports; they are not written down as a specification anywhere. Extracting them, in conversation with AF8A, and writing them down as an unambiguous, testable specification is a genuine piece of requirements engineering and is expected to take real effort. Do not guess at them from the published tables.

**On R13.** The privacy rule follows established HamSCI practice on the PSWS side, where host names, addresses, and contact details are excluded from every published product. Treat the boundary as a hard one from the first schema design, because retrofitting it after personal data has spread through a database is far harder than drawing it correctly at the start.

### Success tiers

The requirements above define the full platform. To keep the required scope honest, the advisor defines three success tiers. The two-semester plan targets the objective tier; the threshold tier alone is a complete, successful capstone.

- **Threshold (a successful capstone).** Event registry, entrant registration, ADIF log ingest, and a working scoring engine with an organizer interface, deployed to a staging environment (R1, R2, R3, R5, R10 at prototype level). **The acceptance test is a replay:** load the August 2025 and December 2025 MSQP events into the system, run the scoring engine, and reproduce the scores AF8A published, with every difference explained. Reproducing a known-good human result is how the team proves the engine is right.
- **Objective (the project goal).** The threshold system in production at msqp.hamsci.org, running a live MSQP event end to end: automated PSKReporter ingest, the live dashboard during the January 2027 Quadrantids parallel run, Zenodo deposit integration, the public data API, and results published within a week of the event close (adds R4, R6, R7, R8, R9, with R11, R12, and R13 in force once the site is public).
- **Stretch (beyond expectations).** The data catalog serving the science pipeline directly: classifier outputs surfaced per recording, PSWS `meteor-scatter` monitor stations enrolled automatically as entrants, and cross-event analytics that let a researcher compare showers, bands, and path geometries without writing code.

Everything above the threshold is upside. Because the project is grant funded, significant resources are available to help the team reach the upper tiers, beyond what is normally available to capstone projects (section 10).

## 6. Two-Semester Plan

**Two fixed calendars drive this schedule, and neither of them moves.** The MSQP calendar is set by the sky, and the workshop at which the team presents is set a year in advance.

| Date | Event | Role in the project |
|---|---|---|
| 13–15 December 2026 | Geminids MSQP | Shadow run: observe and collect |
| 2–4 January 2027 | Quadrantids MSQP | Parallel run: the validation event |
| 17–18 April 2027 | [HamSCI Workshop](https://hamsci.org/hamsci2027), University of Scranton | Present the work |

Map these onto the University's academic calendar in the first week of the project, because two of the three fall awkwardly. The Geminids land at the very end of the fall semester, and the Quadrantids land in the winter break before spring classes begin. **Operating during the break is a real commitment**, and the team should decide early who is available and plan the January run around them.

### Semester 1 (Fall 2026): Requirements, Design, and Core Build
- Requirements elicitation with AF8A and the HamSCI Meteor Scatter Working Group; extract and write down the scoring rules (R5); finalize the specification.
- Data investigation: obtain real PSKReporter exports and real ADIF submissions from past events, measure them, and design the schema and storage strategy against the measured volume (R4).
- Technology selection, justified in a written trade study: language and framework, database, mapping and visualization libraries, hosting and deployment model. Maintainability by volunteers after handoff is an explicit criterion, weighted accordingly.
- Build the core: event registry, entrant registration, ADIF ingest, scoring engine, organizer interface.
- **Replay validation** against the August 2025 and December 2025 events (the threshold acceptance test). This milestone needs no live event, which is what makes it the right target for a first semester.
- **Shadow the Geminids MSQP, 13–15 December 2026.** Participate as operators or monitors if licensed, collect the event's data alongside AF8A's manual process, and use it as the first real end-to-end test case. Watching the existing workflow under load is worth more than any amount of interviewing.
- **Milestones:** requirements review (mid-semester), architecture and design review, threshold system demonstrated on staging, Geminids data collected.

### Semester 2 (Spring 2027): Integrate, Deploy, Demonstrate
- **Parallel-run the Quadrantids MSQP, 2–4 January 2027.** The platform ingests and scores the event live while AF8A runs the manual process, which stays authoritative. Compare the two results and reconcile every difference. A rough edge here is acceptable and expected; that is what a parallel run is for.
- Reconciliation and hardening against what the Quadrantids exposed; PSKReporter ingest at production volume; live dashboard; Zenodo deposit integration; public data API.
- Deploy to msqp.hamsci.org on HamSCI infrastructure; security review; accessibility audit against R13.
- Publish the Quadrantids results within a week of reconciliation, which is the project's headline demonstration.
- Handoff: runbook, backup and restore rehearsal, volunteer maintainer walkthrough, open-source release to the HamSCI GitHub organization.
- Present the project at the **[2027 HamSCI Workshop](https://hamsci.org/hamsci2027), 17–18 April 2027**, hosted at the University of Scranton.
- **Milestones:** Quadrantids parallel run, production readiness review, results published, workshop presentation, final report and poster, open-source release.

**The workshop sets the schedule.** It falls in mid-April, ahead of the end of the spring semester, so the team needs a working system and presentable results about a month before the course's own final deadline. Plan semester 2 backward from 17 April.

**Two consequences of the January date are worth stating plainly.** The system that parallel-runs the Quadrantids has to be built in the fall, which is why the threshold tier is scoped to a replay against past events rather than a live one. And the next MSQP after the Quadrantids is the Eta Aquariids in May 2027, which falls at or after the end of the spring semester. The Quadrantids are therefore the team's one live event inside the course, and the May event is the natural first authoritative run for whoever maintains the platform afterward.

## 7. Deliverables

1. Requirements specification, including the written MSQP scoring rules extracted from current practice (semester 1).
2. Technology trade study and architecture design document.
3. Working platform deployed at msqp.hamsci.org.
4. Documented, versioned public data API with a published schema and data dictionary.
5. Automated test suite and continuous integration configuration.
6. Operations runbook: deployment, backup and restore, monitoring, and incident response, written for a volunteer maintainer.
7. Validation report: the replay of past events against published results, and the parallel-run comparison from the January 2027 Quadrantids.
8. Final capstone report, poster, and public demonstration.
9. Open-source release to the HamSCI GitHub organization under the MIT license.
10. A presentation of the project at the [2027 HamSCI Workshop](https://hamsci.org/hamsci2027), 17–18 April 2027, at the University of Scranton. This is an expectation of the project, and it puts the team's work in front of the scientists and volunteer operators who will use it.

## 8. What You Will Learn

This project spans the full arc of a production software system inside an active, NSF-funded research collaboration, with real users and a deployment deadline set by astronomy.

- **Full-stack development:** interactive frontend with live data and geospatial visualization, backend services, REST API design, authentication and authorization, session and role management.
- **Data engineering:** schema design against measured data, high-volume ETL, deduplication and reconciliation across two independent sources, storage and query strategy at a scale where the naive approach fails.
- **Software engineering practice:** requirements elicitation from a stakeholder whose process exists only as practice, automated testing, continuous integration, code review, containerized deployment, monitoring, and a handoff that works.
- **Working with real users:** an operating volunteer organization, an event that cannot be postponed, and participants who will file bug reports. The parallel-run validation in semester 2 is the kind of cutover engineering that production systems actually require.
- **Open-source collaboration** with an international volunteer community, and software that stays in service after the semester ends.

This is also a deliberate career investment. The stack the project exercises (full-stack web, API design, data pipelines at volume, cloud or self-hosted deployment, CI/CD, and testing) is precisely what software engineering interviews are built around. A capstone that put a public, documented, tested system into production for a real organization, with the commit history to show for it, is a concrete answer to the interview question every new graduate faces: tell me about something you built and shipped.

An amateur radio license is helpful and the club (W3USR) will happily get you licensed, but it is optional. Operating during an MSQP is the fastest way to understand what the users need, and the club can put you on the air with a licensed operator regardless.

## 9. Team Roles (2–3 students)

- **Frontend and visualization lead:** participant-facing interface, live event dashboard, map and plot rendering, accessibility and mobile behavior.
- **Backend and data lead:** schema and API design, ADIF and PSKReporter ingest, the scoring engine, Zenodo integration.
- **Platform and quality lead:** deployment, CI, testing strategy, monitoring, security and privacy review, documentation and handoff. In a two-person team, these duties are shared across the other two roles.

**Expanding the team.** Capstone students are expected to carry the majority of the project work and its management. Within that, the team is encouraged to expand as needed and appropriate: members of the HamSCI volunteer software community, who have very significant industry experience, and underclassmen.

## 10. Resources Provided

This project is grant funded. Significant resources are available to help students, beyond what is normally available to capstone projects:

- **A real stakeholder and a real user base.** AF8A is available to the team as the domain expert and primary stakeholder, and the HamSCI Meteor Scatter Working Group advises the project. MSQP participants are available for user testing.
- **Real data from past events**, including PSKReporter exports, submitted ADIF logs, published results, and the Zenodo audio archive, for design, testing, and replay validation.
- **Hosting on HamSCI infrastructure**, with the msqp.hamsci.org domain and a staging environment.
- **Existing HamSCI codebases** to build on and integrate with: the [MSQP repository](https://github.com/HamSCI/MSQP) (research questions and reference material), [`meteor-scatter`](https://github.com/HamSCI/meteor-scatter) (automated MSK144 monitoring), and the [meteor scatter classification code](https://github.com/HamSCI/Machine-Learning-Meteor-Scatter-Classification-Code).
- Development budget through the advisor's grant funding for hosting, services, and tooling. [Amount to be confirmed.]
- Mentorship from the advisor and from HamSCI volunteer software engineers.
- Claude Code accounts for each team member, for use in design, software development, and documentation. AI use must follow University of Scranton academic integrity policy and the course instructor's rules, including disclosure of AI assistance in project reports.

## 11. Glossary

| Term | Meaning |
|---|---|
| **ADIF** | Amateur Data Interchange Format. A plain-text, tagged file format for contact logs, read and written by every amateur radio logging program. WSJT-X writes one as `wsjtx_log.adi`. |
| **AGC** | Automatic gain control. A receiver circuit that levels signal volume. MSQP asks operators to turn it off so that the true amplitude of each ping is recorded. |
| **`ALL.TXT`** | A running text file in which WSJT-X records every message it decodes, whether or not it became a contact. |
| **Band** | A range of frequencies allocated to amateur radio, named by approximate wavelength. MSQP uses the 6 meter band (50.260 MHz) and the 10 meter band (28.145 MHz). |
| **Callsign** | A station's government-issued identifier, such as W2NAF or AF8A. Public by convention. |
| **Decode** | A message successfully received and error-corrected by WSJT-X. |
| **DOI** | Digital Object Identifier. A permanent citable identifier that Zenodo assigns to each deposit. |
| **Grid square** | A Maidenhead locator: a four- or six-character code (FN21, FN21hg) that encodes a station's latitude and longitude. Public by convention. |
| **HF, VHF** | High frequency (3 to 30 MHz) and very high frequency (30 to 300 MHz). The 10 meter band is HF; the 6 meter band is VHF. |
| **Monitor station** | An MSQP entrant that receives only and reports what it hears. |
| **MSK144** | The WSJT-X digital mode designed for meteor scatter. Packs a message into a 72 ms frame so that a single ping can carry it. |
| **Ping** | A brief burst of signal, milliseconds to seconds long, reflected from a meteor trail. |
| **PSKReporter** | A public service that aggregates spots uploaded automatically by receiving software worldwide. |
| **PSWS** | Personal Space Weather Station. HamSCI's network of volunteer-hosted scientific radio receivers. |
| **QSO** | A two-way radio contact between two stations. A *QSO party* is an organized on-air event built around making contacts. |
| **Spot** | A report that receiver A decoded station B at a given time, frequency, and signal strength. |
| **Two-way station** | An MSQP entrant that transmits and receives. |
| **UTC** | Coordinated Universal Time. All MSQP event windows and logs use it. |
| **WSJT-X** | Free, open-source software for weak-signal digital modes, including MSK144. It produces the logs, `ALL.TXT`, spots, and audio recordings this project ingests. |
| **Zenodo** | An open research data repository operated by CERN. MSQP audio recordings are deposited in its HamSCI community. |

## 12. References

1. HamSCI Meteor Scatter QSO Party: https://hamsci.org/msqp
2. MSQP Operating Guidelines: https://hamsci.org/msqp-rules
3. MSQP How-To Guide: https://hamsci.org/msqp-how
4. MSQP research questions: https://github.com/HamSCI/MSQP/blob/main/MSQP%20Research%20Questions.pdf (repository with reference material: https://github.com/HamSCI/MSQP)
5. December 2025 MSQP results: https://hamsci.org/Dec-2025-MSQP-results
6. August 2025 MSQP results: https://hamsci.org/Aug-2025-MSQP-results
7. HamSCI `meteor-scatter` MSK144 monitoring client: https://github.com/HamSCI/meteor-scatter
8. Machine learning meteor scatter classification code: https://github.com/HamSCI/Machine-Learning-Meteor-Scatter-Classification-Code
9. PSKReporter: https://pskreporter.info
10. Zenodo, HamSCI community: https://zenodo.org
11. 2027 HamSCI Workshop, 17–18 April 2027, University of Scranton: https://hamsci.org/hamsci2027
12. Suggs, R. M., NN4NT (2017), *Meteor Scatter Communications: The Science Behind the Pings*, tutorial presented at the Huntsville Hamfest, 19 August 2017. NASA Technical Reports Server document 20170009030: https://ntrs.nasa.gov/citations/20170009030
13. Weitzen, J. A., and W. T. Ralston (1988), Meteor scatter: An overview, *IEEE Transactions on Antennas and Propagation*, 36(12), 1813–1819. Copy in the HamSCI MSQP repository (reference 4).
14. McKinley, D. W. R. (1961), *Meteor Science and Engineering*, McGraw-Hill, New York.

---

*Interested students should contact Dr. Frissell (nathaniel.frissell@scranton.edu).*

*This project supports the HamSCI Personal Space Weather Station effort, funded by NSF grants AGS-2045755, AGS-2432821, AGS-2432822, AGS-2432824, AGS-2432823, AGS-2431666, and OPP-2332427; NASA grants 80NSSC23K1322, 80NSSC25K7026, and 80NSSC26K0051; and Frankford Radio Club and ARDC grants.*
