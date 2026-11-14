# AI Usage Log — msqp.hamsci.org

This log records all substantive AI-assisted sessions for the project
"msqp.hamsci.org: An Interactive Platform for the HamSCI Meteor Scatter QSO Party".

Required per University of Scranton AI Policy, HamSCI Generative AI Use Agreement, NASA AI guidance, NSF AI guidance, and the project-specific expectations in `.claude/rules/ai-governance.md`.

---

<!-- Append new entries below this line, newest at the bottom. Use the format produced by the /commit command. -->

## [2026-09-02 14:42 UTC]
- **Tool**: Claude (Anthropic), claude-opus-5[1m]
- **Session Purpose**: Draft a Computer Science senior capstone project proposal for an interactive, automated msqp.hamsci.org website to coordinate HamSCI Meteor Scatter QSO Party events and serve their data, modeled on the QPA capstone proposal, and scaffold this repository to the `ai_project_template` standards. NAF's framing: MSQP coordination and reporting is currently done manually by volunteer Gary Mikitin AF8A; the HamSCI Meteor Scatter Working Group can advise; use the same funding acknowledgment as QPA.
- **Sections/Files Affected**: `docs/project_description.md` (new), `CLAUDE.md` (new), `README.md` (new), `notes/2026-09-02_msqp_capstone_proposal.md` (new), `ai/ai_usage_log.md` (new); `.claude/settings.json`, `.claude/commands/commit.md`, `.claude/rules/latex-writing.md`, `.claude/rules/python-code.md`, `LICENSE`, `.gitignore` (copied from the QPA repository's `ai_project_template` scaffold); `.claude/rules/ai-governance.md` (copied, with the project-specific paragraph rewritten for a Computer Science capstone supporting MSQP).
- **Nature of Contribution**: Research and draft. The project description was synthesized from primary sources (hamsci.org MSQP pages, the published August 2025 and December 2025 MSQP results announcements, the `HamSCI/MSQP`, `HamSCI/meteor-scatter`, `HamSCI/Machine-Learning-Meteor-Scatter-Classification-Code`, and `HamSCI/wsprsonde.hamsci.org` repositories) and structured to parallel `~/code/QPA/docs/project_description.md`. Two scoping decisions (project period Fall 2027 – Spring 2028; team size 2–3 students) were made by NAF when asked.
- **Human Review Status**: Pending review. NAF set the objectives and answered the two scoping questions; he has not read the resulting text.
- **Verification**:
  - **Every quantitative claim is sourced.** "280 million lines of PSKReporter data" and the PSKReporter-plus-ADIF scoring basis are from HamSCI's own December 2025 and August 2025 MSQP results announcements. The event and publication dates in the latency table (11–12 Aug 2025 → 16 Nov 2025; 12–13 Dec 2025 → 15 Apr 2026) are from those same two pages. Frequencies, mode, categories, band-alternation and even/odd conventions, and the AGC instruction are from the MSQP Operating Guidelines and How-To Guide. The Zenodo deposit procedure, the 100-file cap, and the title convention are from `Zenodo.md` in `HamSCI/MSQP`. The research questions in section 1 are paraphrased from `Research Questions.md` in the same repository.
  - **The funding acknowledgment is copied verbatim from the QPA repository** at NAF's instruction ("You can use all the same funding numbers as in the QPA project"). It was not re-derived from the QST article in this session.
  - **Not asserted: the membership of the HamSCI Meteor Scatter Working Group.** NAF stated that such a working group exists and can advise the project, and the proposal names it as an advisory body on that basis. No public HamSCI page found in this session names the group or its members, so no member names or callsigns were invented. A web search result appeared to associate two NJIT scientists with a HamSCI working group; that association was not corroborated and is deliberately absent from the proposal.
  - **Not asserted: the 2028 HamSCI Workshop dates or venue.** They are unannounced. The semester-2 plan carries a bracketed placeholder and states only the verified historical pattern (2025 and 2026 workshops in mid-March, the 2027 workshop 17–18 April at Scranton).
  - **Not asserted: exact 2027–2028 meteor shower dates.** The plan names "the December 2027 Geminids" and "the January 2028 Quadrantids" without inventing UTC windows, which HamSCI publishes per event.
  - **Corrected a premise in NAF's request.** He described AF8A as managing MSQP "at msqp.hamsci.org". That hostname does not resolve (NXDOMAIN as of this session), and the `HamSCI/msqp.hamsci.org` repository exists but has no commits. The proposal therefore treats msqp.hamsci.org as the deployment target the project creates, and does not describe it as an existing site.
  - **Scoring rules were not invented.** MSQP's scoring rules exist as AF8A's practice and are not published as a specification. R5 and its accompanying note direct the team to extract and write them down with AF8A, and explicitly warn against inferring them from the published result tables.
  - **Style compliance**: checked against the W conventions. Zero em dashes in prose; 51 body sentences with a median of 19 words, four over 40 (three of which are lists) and two over 50 (both lists, permitted under W14); W4 antithesis patterns swept and rewritten positively.
- **Git Hash**: 12c9698

## [2026-09-02 17:52 UTC]
- **Tool**: Claude (Anthropic), claude-opus-5[1m]
- **Session Purpose**: Apply NAF's correction to the project timeline. He stated: *"The timeline is Fall 2026 - Spring 2027. Students are expected to present at the HamSCI workshop in Scranton April 17-18, 2027"*, superseding the Fall 2027 – Spring 2028 window he had selected from a menu earlier the same day. Rework the two-semester plan around the meteor showers and the workshop that actually fall inside the new window.
- **Sections/Files Affected**: `docs/project_description.md` (metadata table duration; objective success tier; section 6 rewritten in full; deliverables 7 and 10; new reference 11 for the 2027 workshop, McKinley renumbered to 12). `CLAUDE.md` (project period; new "Fixed Calendar Anchors" section). `notes/2026-09-02_msqp_capstone_proposal.md` (decision record superseding the retired period, calendar analysis, open item 3 marked resolved). Published artifact page synchronized to the same content.
- **Nature of Contribution**: Edit, and analysis of the schedule consequences.
- **Human Review Status**: Partially reviewed. NAF dictated the timeline and the workshop anchor; the resulting restructure of the semester plan is the assistant's and he has not read it.
- **Verification**:
  - **2027 HamSCI Workshop dates confirmed**: 17–18 April 2027 at the University of Scranton, verified against hamsci.org/hamsci2027 in this session. This resolves the bracketed placeholder the previous commit carried for an unannounced 2028 workshop (W13 satisfied).
  - **Shower dates are taken from hamsci.org/msqp, not computed**: Geminids 13–15 December 2026, Quadrantids 2–4 January 2027. Both were captured from that page earlier in the session.
  - **No dates invented for the May 2027 Eta Aquariids.** HamSCI has not published them. The text names the month only, and says the event falls at or after the end of the spring semester.
  - **The live-event assignment changed as a consequence, and this is the substantive edit.** The previous plan had the team observe the December Geminids and then run the January Quadrantids on the platform. Under the new window, December 2026 sits at the very end of the first semester, which is too early for a production deployment. The Geminids therefore became a shadow run, and the objective tier's live-dashboard demonstration moved to a **parallel run** of the January 2027 Quadrantids, in which AF8A's manual process stays authoritative. Section 6 now states both consequences explicitly: the system that parallel-runs the Quadrantids must be built during the fall, and the Quadrantids are the only live MSQP inside the course.
  - **Academic-calendar collisions are described qualitatively, not asserted as fact.** The University's calendar was not consulted. The text states the verified event dates and directs the team to map them onto the academic calendar in the first week, and flags that operating over the winter break is a real commitment.
  - **P7 followed in the session notes**: the superseded Fall 2027 – Spring 2028 decision is struck through and marked retired with "do not act on this" rather than deleted, and the new decision records NAF's verbatim instruction.
- **Git Hash**: 1449121

## [2026-09-02 22:27 UTC]
- **Tool**: Claude (Anthropic), claude-fable-5-1
- **Session Purpose**: Act on the three community-review issues Robert Hipple (`roberthipple`) filed against `docs/project_description.md` on 2026-09-02 (HamSCI/msqp.hamsci.org#1, #2, #3): fix a link that opened the HamSCI/MSQP repository root instead of the research-questions PDF; add the two references he suggested (Suggs NN4NT 2017; Weitzen and Ralston 1988) and cite them early; and rework the front of the document for its actual audience, computer science students with no amateur radio background. NAF's instruction: *"Do the recommended fix and draft replies"*, then `/commit and push and post comments`.
- **Sections/Files Affected**: `docs/project_description.md` (audience line under the header table; section 1 rewritten with a software-terms opening, every radio term defined at first use, physics paragraph shortened and citing Suggs and Weitzen & Ralston, new data paragraph; operating conventions moved to section 5 as a note "On R1 and R2"; new section 11 Glossary, 20 terms; references renumbered to section 12 with Suggs and Weitzen & Ralston added as 12 and 13, McKinley now 14; reference 4 and the section 1 link point at the PDF). `CLAUDE.md` line 23 and `notes/2026-09-02_msqp_capstone_proposal.md` line 71 (section 11 → 12). New `notes/2026-09-02_community_review_issues_1-3.md` (comment record, verification, open items) and `notes/2026-09-02_issue_replies_1-3.md` (the three replies).
- **Nature of Contribution**: Analysis of the issues against the document and sources; edit and restructure of sections 1, 5, 11, 12; drafting of the issue replies and session note.
- **Human Review Status**: Partially reviewed. NAF read the assessment and instructed the fix, commit, push, and posting. He has not yet read the rewritten section 1 or the glossary.
- **Verification**:
  - **Issue 1 premise confirmed**: `MSQP Research Questions.pdf` exists at the path Robert gave (333,916 bytes, checked via the GitHub API). Linked on `main` because it is a living document (R11).
  - **Both suggested references verified against primary records (W6, W12)**: Weitzen & Ralston 1988, *IEEE Trans. Antennas Propag.* 36(12) 1813–1819 (ADS 1988ITAP...36.1813W; PDF already in HamSCI/MSQP). Suggs, *Meteor Scatter Communications: The Science Behind the Pings*, Huntsville Hamfest 19 Aug 2017, NTRS 20170009030. The NTRS slides carry his earlier call KB5EZ; FCC ULS and hamsci.org/hamsci2026 give NN4NT. Cited as NN4NT.
  - **Issue 3 self-review conflict declared (H2 exception)**: an earlier Claude session drafted the document being critiqued. Evidence for agreeing with Robert came from the text: QSO never expanded, spot/ADIF/AGC undefined at first use, 460 words of physics before the software problem. The QPA capstone document he compared against was opened and confirms his premise.
  - **Correction to the assistant's own assessment**: it claimed the document lacked a header table naming the audience; it had one. Dropped.
  - **Numbers kept out of the new section 1 opener** (W10) so section 2 remains the single statement of the 280-million-line and three-to-four-month figures. "Tens of thousands of receivers" was considered for PSKReporter and dropped as unsourced.
  - **W14 on the rewritten section 1**: 35 sentences, median 21 words, one over 50 and it is the list of research questions.
  - **Published artifact page not updated**: the republish of the shared "MSQP Capstone Proposal" page was denied by the auto-mode permission classifier. The updated HTML is built in the session scratchpad; path recorded in the session note. Live page shows pre-review text until NAF republishes.
- **Git Hash**: c3f951f

## [2026-09-10 22:41 UTC]
- **Tool**: Claude (Anthropic), claude-fable-5-1
- **Session Purpose**: Address HamSCI/msqp.hamsci.org#4, Rob Suggs NN4NT's ten-point review of the project description (terminology, non-meteor propagation in the spot stream, PingJockey and PSKReporter as existing live tools, the Zenodo submission framing, ALL.TXT in the diagram, R6, the R1/R2 conventions note, the 280-million-line volume framing, additional 2027 showers, and a 2026 replacement for the Suggs reference). NAF's instruction: *"Please address https://github.com/HamSCI/msqp.hamsci.org/issues/4. I will want to review any responses before you post. Keep them concise adn to the point."* NAF then reviewed and corrected two passages, decided the Zenodo deposit-ownership question, asked for a redraft of the reply, and instructed `/commit push and post`.
- **Sections/Files Affected**: `docs/project_description.md` (section 1 opener, physics paragraph, new non-meteor-spots paragraph; section 2 opener, first paragraph, "no live view" and "data submission" subsections rewritten, closing note; section 4 diagram, Ingest, Archive; section 5 R4, R6, R7 rows, notes On R1 and R2, On R4, new On R7; section 6 new note on additional showers; section 8 data-engineering bullet; section 11 glossary PingJockey and Ping entries; reference 12). `CLAUDE.md` (overview paragraph; domain facts: conventions under MSWG review, non-meteor spots). `README.md` (one sentence). New `notes/2026-09-10_community_review_issue_4.md` and `notes/2026-09-10_issue_4_reply_draft.md`. Artifact page republished as version 4.
- **Nature of Contribution**: Analysis of the review against the document and sources; edits; drafting of the reply and session note; artifact rebuild.
- **Human Review Status**: Reviewed. NAF read the assessment and the reply drafts, corrected two passages (verbatim in the session note), and selected the Zenodo OAuth option. He has not re-read every edited paragraph line by line.
- **Verification**:
  - **PingJockey Central verified** at https://www.pingjockey.net/cgi-bin/pingtalk ("Ping Jockey Central by NØUK"), a scheduling and chat page for meteor scatter operators. The earlier draft's "solitary activity with no way to know" premise was wrong and is gone (H4).
  - **Suggs 2026 verified**: the PDF's title slide reads "Forward Scatter Meteor Radar: the Science Behind the Pings", "Rob Suggs Ph.D., NN4NT", "HamSCI Workshop March 2026"; the video is titled "Meteor Scatter Science | HamSCI 2026 Workshop". The 2017 NTRS reference was dropped (W1).
  - **Non-meteor spots**: attributed to Working Group members who have reviewed MSQP audio (Rob's own statement in the issue is the provenance); consistent with Weitzen & Ralston 1988 and the classifier's aircraft-scatter class. No fraction asserted.
  - **"Tiny fraction" of MSK144 in the raw feed**: stated as "a small fraction" on Rob's authority; no number invented. R4 now asks the team to measure raw and retained volumes.
  - **NAF's corrections applied verbatim in intent**: "one volunteer" replaced in five places (document, CLAUDE.md, README, artifact); "build on them" replaced with an integrate-or-stand-alone design decision.
  - **Zenodo OAuth**: R7 and the new On R7 note record NAF's decision and the retired alternative (P7). Exact Zenodo OAuth scopes were not verified; flagged for the requirements phase.
  - **Diagram**: bar positions checked (column 54) after inserting ALL.TXT.
  - **Orionid dates** are Rob's (21–22 October 2026); Lyrids stated as "late April" with no date asserted (W13).
- **Git Hash**: c14d00c

## [2026-10-27 14:38 CDT]
- **Tool**: Claude (Anthropic), claude-opus-5-5
- **Session Purpose**: Rob Suggs (NN4NT) asked for a tool to analyze WSJT-X MSK144 WAV recordings from the MSQP: plot raw audio and a 72 ms FFT-filtered (500–2800 Hz) amplitude envelope for each file, title each plot with the matching ALL.TXT decodes, and fit the e-folding time of each underdense meteor echo; also to judge whether the FFT filtering is worth running on the full dataset. Earlier in the session: installed radioconda 2025.03.14 (Python 3.12, GNU Radio 3.10) locally and reviewed ephem for shower-radiant az/el (not committed).
- **Sections/Files Affected**: new `analysis/underdense_decay.py`; new `requirements.txt`; `.gitignore` (adds `data/` so participant logs, recordings and derived plots stay local).
- **Nature of Contribution**: Code generation and data analysis.
- **Human Review Status**: Partially reviewed. Rob reviewed all six output plots, listened to 260812_022800.wav, and confirmed the Fresnel-oscillation interpretation of decay ripple; the code itself has not been reviewed line by line.
- **Verification**:
  - Ran on six files from the 2026-08-12 Perseids MSQP (one station's ALL.TXT); 7 echoes fitted, τ = 87–271 ms (amplitude e-folding; power τ/2).
  - Found impulse noise producing false echoes in 2 files; added a 5× local-RMS blanker (≈0.05% of samples). Both false detections removed; real echoes kept 6–12 dB.
  - Filter vs. no filter: receivers already band-limit above ~3 kHz, so the filter gains ~1 dB. Unfiltered run gave one false echo and missed one decoded echo.
  - 260812_020130 (decode at −5 dB) has no echo measurable in amplitude; no τ forced.
  - 260812_022800 decay ripple is Fresnel oscillation per NN4NT (meteor-speed analysis deferred).
  - Detection thresholds (4 dB peak, 0.2 s rise, 2 s duration, R² ≥ 0.6) were tuned on these six files only; to be reviewed before bulk processing.
- **Git Hash**: 98e8e69

## [2026-11-10 17:23 UTC]
- **Tool**: Claude (Anthropic), claude-opus-5-5
- **Session Purpose**: NAF: *"We now have our students and volunteers set for the project. We will actually be dividing the project into two separate projects. One is going to be msqp.hamsci.org (which is currently defined). The other will be a Meteor Scatter-focused dashboard that will run under SigMonD on a local PSWS node. [...] Andrew Kusner will be student in charge of msqp.hamsci.org. roberthipple (KE8UQV) is the volunteer collaborator that will be leading the on-PSWS dashboard. Can you help us work out our new requirements and project managsment?"* Then: *"put this into a draft PR that Robert Hipple and Andrew Kusner can work together on"*, *"write this up into an issue explaining to them how to work on this. Assign the issue to them"*, and *"You can post it to the board."*
- **Sections/Files Affected**: new `docs/requirements/README.md`, `docs/requirements/msqp-site.md`, `docs/requirements/node-dashboard.md`, `docs/requirements/interface.md`; new `notes/2026-11-10_two-project-requirements.md`. Outside git: a GitHub issue assigned to AndrewKusner and roberthipple, added to HamSCI project #26.
- **Nature of Contribution**: Draft (requirements and project-management proposal), research (public SigMonD and meteor-scatter repositories).
- **Human Review Status**: Pending review. Opened as a draft PR for the two leads to revise; NAF approved the structure in conversation but has not read the documents line by line.
- **Verification**:
  - R1 to R13 mapping checked against `docs/project_description.md` section 5.
  - SigMonD facts (requirements template, client contract v0.9 §17.7 and §19, shared sink `psk.spots`, `hs-uploader` targets, `gmag-webui` shim) read from `HamSCI/sigmond` on GitHub, 2026-11-10.
  - `meteor-scatter` facts (`MTS-F-003`, `MTS-F-004`, `MTS-F-030`, 30 s README default) read from `HamSCI/meteor-scatter`, 2026-11-10; the 15 s / 30 s discrepancy is reported, not resolved.
  - Robert Hipple's GitHub profile name reads "Robert Hipple KE8UQV"; callsign as given by NAF. AC0G and AI6VN as given by NAF; no personal names attached to them.
  - All `[NEW]` requirements and the interface flows are proposals, not decisions.
- **Git Hash**: d804650 (draft PR HamSCI/msqp.hamsci.org#5; tracking issue #6, assigned to AndrewKusner and roberthipple, on HamSCI project #26)

## [2026-11-14 15:50 UTC]
- **Tool**: Claude (Anthropic), claude-opus-5-5
- **Session Purpose**: Review PR #5 with W2NAF and prepare it to merge as version 0.1, moving the requirements work to one pull request per change; add Tom McMahan, K1FR (`jtm5`), who works with both leads.
- **Sections/Files Affected**: `docs/requirements/README.md` (status line, Who decides what, open decision 3, new "How changes are made"), `docs/requirements/node-dashboard.md` (stakeholders), `notes/2026-11-14_requirements-workflow.md` (new).
- **Nature of Contribution**: Review and edit.
- **Human Review Status**: Pending review.
- **Git Hash**: 6d43c5f (PR HamSCI/msqp.hamsci.org#5)

## [2026-11-14 16:07 UTC]
- **Tool**: Claude (Anthropic), claude-opus-5-5
- **Session Purpose**: Take W2NAF out of the critical path for the requirements work: the leads own `README.md` jointly, reviews come from the leads, Tom McMahan (K1FR) and the Meteor Scatter Working Group leads, and the author merges once approved.
- **Sections/Files Affected**: `docs/requirements/README.md` (Who decides what, open decisions 1 and 2, How changes are made), `.github/CODEOWNERS` (new), `notes/2026-11-14_requirements-workflow.md` (addendum).
- **Nature of Contribution**: Edit.
- **Human Review Status**: Pending review.
- **Git Hash**: f8ba805 (branch reviews-without-w2naf)

## [2026-11-14 16:12 UTC]
- **Tool**: Claude (Anthropic), claude-opus-5-5
- **Session Purpose**: Scope requirements pull requests to one idea or work effort tied to an issue, instead of one document (W2NAF, 2026-11-14).
- **Sections/Files Affected**: `docs/requirements/README.md` (How changes are made), `notes/2026-11-14_requirements-workflow.md` (addendum).
- **Nature of Contribution**: Edit.
- **Human Review Status**: Pending review.
- **Git Hash**: 0ed8d19 (branch pr-scope-per-idea)

## [2026-11-14 16:21 UTC]
- **Tool**: Claude (Anthropic), claude-opus-5-5
- **Session Purpose**: Record W2NAF's answer to open decision 3: Andrew Kusner is the only capstone student on the project.
- **Sections/Files Affected**: `docs/requirements/README.md` (Who decides what, capstone boundary, open decision 3), `docs/requirements/msqp-site.md` (one word), `CLAUDE.md` (status line), `notes/2026-11-14_requirements-workflow.md` (addendum).
- **Nature of Contribution**: Edit.
- **Human Review Status**: Pending review.
- **Git Hash**: ce7f09d (branch capstone-team-of-one)

## [2026-11-14 16:24 UTC]
- **Tool**: Claude (Anthropic), claude-opus-5-5
- **Session Purpose**: Name AC1SN as Jay Weitzen (W2NAF, 2026-11-14) in the requirements README.
- **Sections/Files Affected**: `docs/requirements/README.md` (Who decides what; How changes are made), `notes/2026-11-14_requirements-workflow.md` (open item closed).
- **Nature of Contribution**: Edit.
- **Human Review Status**: Pending review.
- **Git Hash**: f7e8313 (branch name-ac1sn)

## [2026-11-14 16:36 UTC]
- **Tool**: Claude (Anthropic), claude-opus-5-5
- **Session Purpose**: Record that Andrew Kusner makes production deploys to msqp.hamsci.org (W2NAF, 2026-11-14).
- **Sections/Files Affected**: `docs/requirements/README.md` (Who decides what), `notes/2026-11-14_requirements-workflow.md` (addendum).
- **Nature of Contribution**: Edit.
- **Human Review Status**: Pending review.
- **Git Hash**: 97215dd (branch andrew-production-deploys)
