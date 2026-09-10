# 2026-09-10: Community review, issue #4 (Rob Suggs, NN4NT)

Written for a fresh session with no context (P2).

## What happened

Rob Suggs, NN4NT (GitHub `RobSuggsNN4NT`), filed issue #4 on 2026-09-04 against the artifact page
of the project description (https://claude.ai/code/artifact/612b740e-294e-4c7e-ac3a-fbcc92292be9).
Ten points in one issue. Issues #1–#3 (Robert Hipple) were closed by their reporter between
2026-09-02 and 2026-09-10.

NAF's instruction, 2026-09-10: *"Please address https://github.com/HamSCI/msqp.hamsci.org/issues/4.
I will want to review any responses before you post. Keep them concise adn to the point."*

Edits committed as c14d00c and pushed 2026-09-10 22:41 UTC after NAF's review. Reply posted 22:43 UTC on his
instruction: https://github.com/HamSCI/msqp.hamsci.org/issues/4#issuecomment-5626416830

## Comment record (P3), verbatim from the issue body

> 4th paragraph
> From "column of plasma that reflects radio waves" to "column of plasma that scatters radio waves"

- Accepted. Section 1 physics paragraph and glossary "Ping" entry.

> What is missing in all of this discussion is the fact that many of the spots are not meteor
> propagation but Es, F layer, tropo, aircraft scatter, etc. I know that from viewing and listening
> to many WAV files. I don't think that changes any of the data management plans described here but
> it wouldn't hurt to mention that many of the spots are not meteors, just so the developers
> understand that.

- Accepted. New paragraph appended to the section 1 data paragraph. Attributed to "members of the
  HamSCI Meteor Scatter Working Group who have reviewed MSQP audio" (Rob's own statement in this
  issue is the provenance, W12). Consistent with Weitzen & Ralston 1988, whose abstract lists
  sporadic E, auroral, ionospheric scatter, and tropospheric scatter as non-meteor mechanisms on
  meteor links, and with the classifier's aircraft-scatter class. The scoring implication was
  routed to the R5 conversation with AF8A; no scoring rule was invented.

> Paragraph titled "There is no live view of the event"
> The tone of this isn't entirely correct. Amateurs use pingjockey.net to coordinate contacts and
> commiserate on the level of meteor activity. This isn't science data but the idea of a lonely ham
> with no idea of what is going on in the sky is not correct. I suggest scrapping this paragraph or
> at least mentioning that pingjockey.net provides coordination. I can take a crack at this or you
> can ask Claude to consider pingjockey.

- Accepted (H4: the earlier draft's premise was wrong). PingJockey Central verified:
  https://www.pingjockey.net/cgi-bin/pingtalk, "Ping Jockey Central by NØUK", a scheduling and
  chat page for meteor scatter operators. Paragraph rewritten and retitled "There is no
  event-scoped live view"; credits PingJockey and PSKReporter; defines the remaining gap as the
  event-level view. Glossary entry added.

> Paragraph titled "Data submission is a manual, error-prone ritual"
> Claude seems to be trying to sell the idea that this project is to fix manual entry problems. That
> is incorrect. Each ham has to enter this stuff, especially the radio used, whether TX or RX,
> antennas, power levels, etc. Perhaps the idea is to have the hams enter this info in some form
> once and let this system build the metadata "Zenodo comments section" input we need. R8 seems to
> be addressing that. I'd delete the last 2 sentences "Every one of those fields is already known …
> analysis depends on." because they are confusing and might lead the student team to waste time on
> that.

- Accepted. Both sentences deleted; paragraph retitled "Zenodo metadata is typed by hand" and now
  states the enter-once, build-metadata idea, pointing at R7 (the Zenodo requirement; Rob wrote R8,
  which is the data API).

> System Concept flow diagram
> ALL.TXT is missing and should be added to "registration, ADIF logs, ALL.TXT files, WAV audio

- Accepted. Column alignment preserved (bar positions checked).

> R6 Live event dashboard
> I'd note that PSKReporter provides much of this feedback and display capability already, faster
> than the 15 minute requirement. I regularly watch PSKReporter filtered for my callsign, band and
> mode and get the display of who is hearing me. There is no harm in including this in this project
> but be aware that it already exists. Claude might not be aware of that since it is a
> visual/graphical kind of thing.

- Accepted. Sentence added to R6.

> Sidebar after R13
> On R1 and R2 - we need to reexamine that timing (xx:00, xx:20, etc.) since QSOs can take longer
> than that. We'll discuss this at the MSWG and provide a consideration. I don't believe it affects
> the development of the website software so it could be removed. It is just something scraped from
> the MSQP website.

- Accepted with one retained point. Specific timings removed from the note. Kept a software-relevant
  consequence: conventions are MSWG-set and changeable, so the registry holds them as per-event
  data. `CLAUDE.md` domain facts marked "under MSWG review" rather than deleted (the current
  published rules still say 20 minutes).

> On R4 and other mentions of the 280 million PSKReporter lines. It should be noted that not all of
> these are MSK144 spots, in fact, a tiny fraction are. Most of this huge volume just needs to be
> filtered through and doesn't need to be stored or manipulated beyond that.

- Accepted. R4 row, the "On R4" note, section 4 "Ingest", and the section 8 data-engineering bullet
  all reframed from storage-at-volume to filter-then-store. Section 2 still quotes the 280 million
  figure from the results announcement, unchanged, because it is a quotation of the workload as
  published (W10: the fraction is stated in R4 and once in section 4).

> Two Semester Plan
> Claude is right that the next 2 shower events fall at an inconvenient time in the academic year.
> We could consider an Orionid test run (Oct 21-22) but that is likely too soon for any meaningful
> work to be done. The MSWG will be discussing other 2027 showers but there aren't many good ones
> early in the year with the exception of the Lyrids in April which may be too late.

- Accepted as information. Short note added to section 6. Orionid dates are Rob's; the Lyrids are
  stated as "late April" with no date asserted (W13).

> References
> 12 Suggs - that is a really old presentation from 2017.
> This is a more recent hardcopy [HamSCI workshop 2026](…RevB.pdf) With the presentation video at
> [HamSCI 2026 video presentation](https://www.youtube.com/watch?v=8vOfv4Kp7hs…)

- Accepted. Verified: the PDF's title slide reads "Forward Scatter Meteor Radar: the Science Behind
  the Pings", "Rob Suggs Ph.D., NN4NT", "HamSCI Workshop March 2026". The video is titled "Meteor
  Scatter Science | HamSCI 2026 Workshop". Reference 12 replaced; the 2017 NTRS entry dropped (W1).
  In-text citation in section 1 updated.

## NAF's review corrections, 2026-09-10 (verbatim, H5)

> "**Everything that surrounds the data is done by hand, by one volunteer.**":
> There are actually a couple of volunteers and students. But, it is still largely a manual
> process. Most of the amateur radio community analysis falls on AF8A's shoulders, while students,
> volunteers, and researchers have been doing the science analysis.

- Applied to section 1 opener, section 2 opener and first paragraph, the section 2 closing note,
  `CLAUDE.md` overview, and `README.md`. The artifact deck text carries the same phrase and is
  corrected at republish.

> "Two live tools already exist, and the platform should build on them.": I don't think "build on
> them" is necessarily correct. We certainly want to be aware of them, and we can consider the
> possibility of integration. But, we may also want our tool to be stand-alone. This would be a
> design decision.

- Applied: the sentence now says the team should know the tools, and that integration versus
  stand-alone is a design decision for the trade study (section 6, semester 1).

## Decision record: Zenodo deposit ownership (P7)

**Decision (NAF, 2026-09-10):** the platform deposits on the participant's behalf, into the
participant's own Zenodo account, via OAuth. NAF asked *"Should we consider the possibility of
Zenodo integration in our app to automate the process?"*; the assistant pointed at R7 (already in
the document) and recommended participant-owned deposits via OAuth over a HamSCI service account;
NAF selected: *"This one: 'Recommendation: the platform deposits on the participant's behalf, into
the participant's own Zenodo account, via OAuth.'"*

- Applied: R7 row rewritten (OAuth, participant's account, community submission, sandbox for
  testing, manual path retained); new "On R7" note in section 5 records the decision and the
  alternative set aside; section 4 "Archive" paragraph aligned.
- Retired alternative, **do not act on this**: a HamSCI service account owning every deposit.
  Set aside because it changes the authorship of the archive.
- Not verified this session: the exact Zenodo OAuth scopes needed for deposit and community
  submission. The requirements phase confirms them against developers.zenodo.org.

## Other

- Rob asked whether to split into separate issues. Reply says one issue is fine.
- **Artifact page republished** 2026-09-10 as version 4 on NAF's instruction ("Did you update the
  artifact?"), carrying every change above plus the glance tile relabelled "raw PSKReporter
  lines". The read before publishing reported that link viewers see the pinned version and will
  not see future publishes until the share pin is moved; NAF moves the pin in the artifact view
  if Rob is to see version 4 through the shared link.

## Open items

1. ~~NAF reviews~~ Done 2026-09-10.
2. ~~Commit, push, post~~ Done: c14d00c, 3c0f415; comment posted. **Still open: move the artifact share pin to version 4** (NAF, in the artifact view).
3. Issue #4 stays open for Rob to close (R7, H7).
