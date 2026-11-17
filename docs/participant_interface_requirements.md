# The MSQP Participant Interface: Requirements

**Draft requirements for the station-level web interface that each MSQP participant uses on their own system, linked to msqp.hamsci.org**

| | |
|---|---|
| **Status** | Draft for review, 2026-11-14. Nothing here is decided until the open decisions in section 8 are settled with the PI. |
| **Companion document** | [`project_description.md`](project_description.md), the contest-level platform (msqp.hamsci.org) built by the capstone team. Requirement numbers R1–R13 below refer to that document. |
| **Project advisor** | Dr. Nathaniel A. Frissell, W2NAF |
| **Primary stakeholders** | MSQP participants, two-way and monitor; Gary Mikitin, AF8A, organizer and scorer |
| **Related software** | HamSCI [`meteor-scatter`](https://github.com/HamSCI/meteor-scatter) and [`sigmond`](https://github.com/HamSCI/sigmond) (station side); WSJT-X |
| **Audience** | A reader who already operates meteor scatter. Radio terms are used without definition; software terms are explained where they first matter. |

---

## 1. Two Interfaces, One Event

MSQP needs two web interfaces, and they serve different people.

The **contest-level interface** is msqp.hamsci.org, described in `project_description.md` and built by the capstone team. It is one central site. It holds the event registry, registration, log and spot ingest, scoring, the event-wide live dashboard, results and the public data API. Its users are organizers, researchers, and participants looking at the event as a whole.

The **participant-level interface**, the subject of this document, runs on each participant's own system. It is what an operator opens in the shack: to get the station ready for a shower, to watch their own pings arrive, to review what they decoded, to build and deposit their submission, and later to see how they scored and why. It works with the station's own files and processes, which the central site never sees directly, and it talks to msqp.hamsci.org for everything event-wide.

The split follows where the data lives. Spots are public and arrive at the central site through PSKReporter whatever the participant does. Recordings, `ALL.TXT`, the ADIF log, the station's configuration, its calibration and its noise floor exist only on the participant's machine. Today the participant handles all of those by hand; this interface is the tool that handles them on the station, then hands the results to the central site and to Zenodo.

## 2. What Participants Do by Hand Today

The current procedure is documented in the MSQP how-to, the operating guidelines, and the MSQP repository's `Zenodo.md` (references 2–4). For a WSJT-X operator it runs as follows.

**Before the shower.** Set WSJT-X to MSK144, 15 s T/R, Rx 1500 Hz, F Tol 200 Hz, PSKReporter spotting on, Tx even for an east-pointed antenna or odd for west; add 28.145 MHz to the frequency table, since WSJT-X does not include it by default; turn receiver AGC off; set RF gain so noise reads about 30–40 dB on the WSJT-X meter; keep the clock on NTP; create a fresh save directory and choose Save Decoded. Dual-band stations alternate bands at xx:00, xx:20 and xx:40. Nothing checks any of this. A station that ran with AGC on or the wrong T/R period finds out afterward, if at all.

**During the shower.** Operate, and watch PSKReporter and PingJockey Central for who is hearing whom. There is no view of the station's own event in progress beyond the WSJT-X window.

**After the shower.** Open the log directory, zip the Save folder (Zenodo caps a deposit at 100 files), trim `wsjtx_log.adi` and `ALL.TXT` to the event times, create a Zenodo record in the HamSCI community, type the title to the convention (`CALL GRID6 YYYYMMDD-DD Meteor Scatter QSO Party`), type the description from the template (callsign or PSKReporter identifier, operator names and calls, contact email, grid, transmit-and-receive or receive-only, equipment, power, antenna, bands, AGC state, comments), choose the license, and submit for review. Then wait three to four months for results.

**Automated monitors already do part of this.** A PSWS station running `meteor-scatter` under `sigmond` records and decodes 6 m and 10 m MSK144 unattended and keeps every decoded slot's WAV with a JSON sidecar. Its command line calibrates each band's scale, totals the archive against Zenodo's limits, lists decodes it did not spot or flagged as suspect, builds the MSQP package (zip, a matching `ALL.TXT`, filled description, metadata) and leaves the deposit as a Zenodo draft that the operator checks and submits (reference 6, `docs/OPERATIONS.md`, section "MSQP"). All of it is `sudo` commands typed over ssh. The machinery exists; the interface does not.

## 3. Objective

Give every MSQP participant a web interface on their own system that:

1. checks the station is configured for the event before it starts;
2. shows the station's own pings, by band, while the event runs;
3. lets the operator review and annotate what was decoded, with the audio;
4. builds the submission (recordings, `ALL.TXT`, ADIF) for the event window and leaves the Zenodo deposit ready to submit, with nothing typed twice;
5. sends the station's registration, logs and DOI to msqp.hamsci.org and shows the station's score and its breakdown when the central site publishes it.

Two constraints govern every requirement.

**The station's own operation comes first.** The interface must never be the reason a station stops recording, restarts a receiver mid-shower, or loses a recording. On a sigmond station, restarting the wrong unit bounces radiod for every client on the host; the interface treats that as a hazard, not a button.

**The operator stays in control of what leaves the station.** Nothing is uploaded, deposited, submitted or published without the operator's explicit action, and a Zenodo record is never published by the software. This matches `meteor-scatter`'s existing rule that a person presses the last button, because Zenodo allows no change to a published record.

## 4. System Concept

```
  ┌─────────────────────────── Participant's system ───────────────────────────┐
  │                                                                            │
  │  Station profile A: sigmond / meteor-scatter        Station profile B:     │
  │  (PSWS, automated monitor)                          WSJT-X operator PC     │
  │   radiod → meteor-scatter daemon                    (two-way or monitor)   │
  │   archive: WAV + JSON sidecar per decoded slot      Save dir WAVs,         │
  │   noise log, calibration, inventory --json          ALL.TXT, wsjtx_log.adi │
  │            │                                                 │             │
  │            └──────────────┬──────────────────────────────────┘             │
  │                           ▼                                                │
  │        ┌───────────────────────────────────────────┐                       │
  │        │   Participant interface (local web UI)    │◄── operator's browser │
  │        │   Readiness · Live · Review · Package ·   │    (shack PC, phone   │
  │        │   Deposit · Results · History · Settings  │     on the LAN)       │
  │        └───────┬──────────────────────┬────────────┘                       │
  └────────────────┼──────────────────────┼────────────────────────────────────┘
                   │ registration, logs,  │ draft deposit
                   │ DOI, annotations;    │ (operator submits)
                   │ event feed, scores   ▼
                   ▼               ┌──────────────┐
        ┌──────────────────────┐   │ Zenodo       │
        │ msqp.hamsci.org      │◄──│ HamSCI       │── DOI
        │ (contest level,      │   │ community    │
        │  R1–R13)             │   └──────────────┘
        └──────────▲───────────┘
                   │ spots (unchanged path)
             PSKReporter ◄── WSJT-X / meteor-scatter spotting
```

Spots keep their present path. WSJT-X and `meteor-scatter` report to PSKReporter, and the central site pulls them from there (R4). The participant interface adds nothing to that path and must not duplicate it. What it adds is everything that today travels by hand: configuration, recordings, logs, metadata and the DOI.

**Two station profiles.** Most of the machinery already exists for profile A: the interface calls the `meteor-scatter msqp` commands and reads `inventory --json`, and should not reimplement them. Profile B is a WSJT-X station, usually a Windows PC. There the interface is a small companion program that reads WSJT-X's log directory and settings; it writes nothing to them. Whether profile B is in scope is the first open decision (section 8, D1).

## 5. Requirements

Initial targets, numbered P1–P15 to keep them distinct from the contest-level R1–R13. "Both" means both station profiles; "A" or "B" limits a requirement to one.

| # | Requirement (initial target) |
|---|---|
| P1 | **Station identity, entered once.** Callsign (or PSKReporter identifier for an SWL monitor), six-character grid, operator names and calls, category (two-way or monitor), bands, antenna description and heading, transmit slot (even for east, odd for west), transmitter power ("NA" for monitors), equipment, AGC state, and a contact email. Validated at entry: callsign syntax, grid syntax, slot consistent with heading. On profile A, pre-filled from `/etc/sigmond/coordination.env` and the `[msqp]` and `[station]` config, and written back through the existing `config apply` path. This record fills the central registration (R2), the Zenodo title and description, and the ADIF/`ALL.TXT` checks. (Both) |
| P2 | **Event awareness.** Read the event schedule from the central site's machine-readable feed (R1): shower, UTC window, bands, frequencies and the conventions in force for that event (band-alternation interval, slot rule, AGC). Show the next event, a countdown, and during the event the current band-alternation slot. Conventions are data from the feed, never hard-coded, because the Working Group may change them. Must still work from the last cached feed when the site is unreachable. (Both) |
| P3 | **Readiness check.** Before each event, a checklist that tests what can be tested and asks the operator to attest the rest. Tested on profile A: daemon running, each band's last front-end packet recent, clock synchronized, T/R period 15 s, calibration present and noise floor within 10 dB of its calibrated level, archive caps (`archive_max_days`, default 90; `archive_max_gb`, default 2) large enough to hold the whole shower, site upload mode set to `upload`, Zenodo token present with safe permissions. Tested on profile B where WSJT-X's settings file allows: MSK144, 15 s, Rx 1500 Hz, PSKReporter spotting on, Tx even/odd against the stated heading, 28.145 MHz in the frequency table, Save Decoded on and a fresh save directory, system clock offset. Attested: AGC off, RF gain set for 30–40 dB noise. Each failure names its fix. (Both) |
| P4 | **Calibration (profile A).** Run `msqp calibrate` from the interface with its dry-run shown first. Refuse during an event window and warn between showers if a calibration change would make a shower's recordings incomparable. A calibration that needs a daemon restart says so, says what the restart touches, and leaves the restart to an explicit second confirmation. (A) |
| P5 | **Live view.** During an event: the station's own decodes as they arrive, by band; pings per 10 minutes per band; SNR, distance and bearing per decode; a map of the paths heard; the current band slot and transmit period; the noise floor against calibration; and whether spots are leaving the station. Refreshes within one T/R period on profile A. Readable on a phone at night (dark theme, large type). Links out to the central site's event dashboard (R6) for the event-wide view rather than rebuilding it. (Both) |
| P6 | **Review.** A searchable list of the event's decodes with the classification `meteor-scatter` already assigns (spotted, rejected with reason, suspect, part of a heard exchange), each playable as audio with its waveform and amplitude envelope. The operator can annotate a decode (aircraft scatter, sporadic E, local QRM, overdense, a free note). Annotations are kept in a separate file in the package; they never change a recording, a sidecar or the classification. On profile B the same list is built from `ALL.TXT` and the saved WAVs. (Both) |
| P7 | **Package.** For the event window from P2, build the submission: recordings zipped by band, an `ALL.TXT` that agrees with the zip, the station's `wsjtx_log.adi` trimmed to the window (profile B, and profile A if it also runs WSJT-X), the annotations, the filled description and the Zenodo metadata. Show the counts per band and day, the size against Zenodo's limits (50 GB per record; profile B also packs the WAVs into a zip because of the 100-file limit), and any clipped or overloaded recordings, and let the operator read the description and metadata before anything leaves the station. On profile A this is `msqp totals` and `msqp package`. (Both) |
| P8 | **Zenodo deposit.** Leave the package on Zenodo as an unsubmitted draft in the participant's own account, in the HamSCI community, with the DOI reserved, then show the draft's link so the operator checks it and presses "Submit for review" on Zenodo. Resumable after a failure without creating a second draft. The software never submits and never publishes. How the station is authorized to Zenodo is open decision D2. (Both) |
| P9 | **Hand-off to msqp.hamsci.org.** With the operator's confirmation: create or update the station's registration (R2) from P1; upload the trimmed ADIF and `ALL.TXT` (R3) and show the central site's parse and validation messages; report the reserved DOI and draft link against entrant and event (R7); send the operator's annotations if the operator chooses. Every upload is queued and retried when the site is down, and nothing local depends on it succeeding. (Both) |
| P10 | **Results and score breakdown.** When the central site publishes, show the station's score, rank and category, and the breakdown the scoring engine exposes (R5): each QSO and spot that counted, each that did not, and why. Let the operator query a scoring decision and submit soapbox comments (R9) through the central site. Organizer overrides appear with their stated reason. (Both) |
| P11 | **History.** Per event: the readiness result, packages built, DOIs, uploads and their outcomes, scores. Survives upgrades. (Both) |
| P12 | **Does no harm to the station.** Read-only by default. No action restarts radiod, a recorder or WSJT-X without a warning that names what stops and a second confirmation, and none is offered during an event window. The interface runs as an unprivileged account; privileged steps go through the existing `meteor-scatter` commands or a narrow, audited helper. It never edits the WSJT-X configuration. Its CPU and disk use must not cost the decoder a slot; on profile A it stays within sigmond's resource arbitration. (Both) |
| P13 | **Access and secrets.** Served on the station's own network only, by default. On profile A, on a port chosen against sigmond's port table (not 8080, 8073, 9000 or the reserved 8090–8099) and added to the appliance's forwarding; remote use through sigmond's existing remote access, not a new tunnel. A local login protects every action that changes config or sends data. The Zenodo token and the msqp.hamsci.org credential are stored 0600 and never shown again after entry. (Both) |
| P14 | **Privacy.** Callsigns and grids are public. The contact email, and anything else personal, goes only where the operator sends it: to the organizers through the central site's private channel (R13), and into the Zenodo description only after the interface warns that a published Zenodo record is public and permanent. Nothing personal goes into logs, annotations or anything uploaded for publication. (Both) |
| P15 | **Install, update and help.** Profile A: a sigmond client, installed and updated with `smd`, configured from the interface or the existing wizard, documented in the client's own docs. Profile B: a single installer per supported OS (at least Windows), updating itself or telling the operator an update exists. Every screen links to the matching section of the MSQP how-to. Meets WCAG 2.2 AA, as R13 requires of the central site. (Both) |

**On P1.** The station record is entered once and feeds four places that today are typed separately: the registration form, the Zenodo title, the Zenodo description template, and WSJT-X's own grid setting. On profile A it must not become a second copy of sigmond's configuration. It reads and writes the existing files, so there is one source of truth.

**On P3 and P4.** The readiness check is where this interface adds the most science value. AGC-off, a fixed calibration across a shower, and a clock on NTP are what make one station's ping decay times comparable with another's, and today nothing confirms any of them. Readiness results should travel with the package, so the analyst knows which recordings came from a station that passed.

**On P6.** `meteor-scatter`'s classifier already separates "plainly wrong" decodes from suspect ones (for example a path longer than about 2500 km, which sporadic E can produce on 6 m) and marks heard exchanges. The operator's annotations add what only the operator knows, such as an aircraft overhead or a neighbor's QRM. Keeping them in a separate file keeps the original data unaltered and lets researchers decide whether to use them.

**On P8 and P9.** The DOI links the two halves. The station knows it once the draft exists; the central site needs it to join recordings to entrant, event and spots (R7, R8). Reporting it at draft time, not after publication, means the link exists even if the operator is slow to press Submit.

**On P12.** The `meteor-scatter` operations guide warns that restarting it through `smd` bounces radiod for the whole station. An interface that makes a restart one click away would turn that warning into an outage during a shower. P12 makes it two deliberate clicks, outside event windows only.

### Success tiers

As in `project_description.md`, three tiers keep the scope honest.

- **Threshold.** Profile A only: P1, P2 (from a cached or hand-entered schedule if the central feed does not exist yet), P3, P5, P7 and P8, wrapping the existing `meteor-scatter` commands. Acceptance test: a PSWS monitor runs a real MSQP, and its operator goes from readiness check to a Zenodo draft without typing a shell command.
- **Objective.** Threshold plus P4, P6, P9–P15 on profile A, linked live to msqp.hamsci.org; profile B readiness, review and package (P3, P6, P7) if D1 brings it into scope.
- **Stretch.** Profile B at parity with profile A; readiness results and annotations used in scoring and in the research catalog (R8); a station enrolling itself in an event from the interface, which is the participant side of the contest document's stretch goal of enrolling PSWS monitors automatically.

## 6. The Link to msqp.hamsci.org

Neither side can be finished without the other. The capstone team owns the central site's API; this interface is its first non-browser client. The participant side needs the following from the central site. These should go into the capstone team's requirements specification (their R1–R10) as early as possible, because changing an API after stations depend on it is expensive.

| Need | Central requirement | Direction |
|---|---|---|
| Machine-readable event schedule with per-event conventions | R1 | site → station |
| Create or update a registration from a station record | R2 | station → site |
| A per-station credential, issued at registration, revocable by the participant and organizers | R10 | site → station |
| Upload ADIF and `ALL.TXT`, with machine-readable validation messages | R3 | station → site |
| Record a DOI and draft link against entrant and event | R7 | station → site |
| Score, rank and the per-QSO, per-spot breakdown for one entrant | R5, R8 | site → station |
| Submit a scoring query or soapbox comment | R9, R10 | station → site |
| Optional: receive readiness results and annotations | R8 | station → site |

Two properties are required of the link itself. **It is versioned**, so an old station keeps working after the site changes. **Either side can be down**: the station queues and retries (P9), and the site never waits on a station.

## 7. Calendar

The participant interface has no fixed delivery date yet (D3). The fixed points that matter are the contest project's.

| Date | Event | Relevance here |
|---|---|---|
| 13–15 December 2026 | Geminids MSQP (0000 UTC 13 Dec to 2359 UTC 15 Dec) | Too soon for this interface. Useful to observe: run the existing `meteor-scatter msqp` commands on a monitor and note every point where an interface would have helped. |
| 2–4 January 2027 | Quadrantids MSQP | The capstone team's parallel run. A threshold-tier interface on even one or two PSWS monitors would test the link early. |
| 17–18 April 2027 | 2027 HamSCI Workshop, Scranton | Natural place to show both interfaces together. |
| May 2027 | Eta Aquariids (dates unpublished) | First event both interfaces could plausibly support in production. |

## 8. Open Decisions

These need the PI, and in some cases the `meteor-scatter` author, before design starts.

- **D1. Does the participant interface cover WSJT-X stations (profile B)?** Most two-way entrants run WSJT-X on a Windows PC and will never run sigmond. Option 1: profile A only; WSJT-X operators use the central site's participant pages and upload by hand. Option 2: a companion program for WSJT-X stations as well, which is a second, separate code base for another operating system. Option 2 reaches far more participants, at roughly twice the effort.
- **D2. How does the station reach Zenodo?** The contest document (R7, decided 2026-09-10) has the central site deposit through Zenodo OAuth into the participant's own account. `meteor-scatter` today drafts from the station with a personal access token scoped `deposit:write`. Both keep ownership with the operator. With the station route, the recordings never pass through HamSCI's servers, which matters for a multi-gigabyte shower. With the central route, there is one integration to maintain and no token on the station. Both could coexist, but that should be a decision, not an accident.
- **D3. Who builds and maintains it, and where does it live?** Candidates: inside the `meteor-scatter` repository as its web front end; a new HamSCI repository; or as part of sigmond's station web pages. Ownership after the capstone ends matters as much as who writes it.
- **D4. Contact email in the Zenodo description.** The MSQP description template asks for a contact email, which becomes public and permanent when the record is published. P14 warns the operator; the alternative is to drop the field from the template and send the email to the organizers only through the central site.
- **D5. Is the score shown on the station, or only linked?** P10 assumes the central API exposes a per-entrant breakdown. If the capstone team does not plan one, the interface links to the central site's results page instead.

## 9. References

1. `project_description.md` in this repository: the contest-level platform and requirements R1–R13.
2. MSQP How-To Guide: https://hamsci.org/msqp-how
3. MSQP Operating Guidelines: https://hamsci.org/msqp-rules
4. HamSCI MSQP repository, `Zenodo.md` (WAV access, zipping, Zenodo account and upload procedure, description template): https://github.com/HamSCI/MSQP
5. Mikitin, G., AF8A, *MSQP Scoring Functional Spec V0.1*, 2026-10-27, in the HamSCI MSQP repository (reference 4).
6. HamSCI `meteor-scatter`: https://github.com/HamSCI/meteor-scatter. Section "MSQP" of `docs/OPERATIONS.md` (archive, calibration, noise warning, operator fields, Zenodo token, package, draft); `docs/CONFIG.md` (`[msqp]` keys and defaults); `src/meteor_scatter/core/plausible.py` (decode classification). Read at commit `907c7b2`, 2026-11-13.
7. HamSCI `sigmond`: https://github.com/HamSCI/sigmond. `docs/ports.md` (station ports, reserved range, forwarding). Read 2026-11-14.
8. Zenodo, HamSCI community: https://zenodo.org/communities/hamsci
