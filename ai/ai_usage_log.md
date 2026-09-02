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
- **Git Hash**: [pending]
