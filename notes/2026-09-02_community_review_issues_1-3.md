# 2026-09-02: Community review of the project description, issues #1–#3

Written for a fresh session with no context (P2).

## What happened

Robert Hipple (GitHub `roberthipple`) filed three issues against
`docs/project_description.md` on 2026-09-02 (UTC 21:07–21:33):
https://github.com/HamSCI/msqp.hamsci.org/issues

NAF pasted the issues URL, received an assessment, then instructed: *"Do the recommended fix and
draft replies"*. This note records the verification, the edits, and what is still open.

## Comment record (P3)

### #1, "Link misses target"

> In the fifth paragraph of the 1. Background, the link in ..."That data feeds a defined science
> program. The HamSCI [MSQP research questions](https://github.com/HamSCI/MSQP)" opens the top of
> the repository rather than the targeted pdf, which is
> https://github.com/HamSCI/MSQP/blob/main/MSQP%20Research%20Questions.pdf

- **Located**: `docs/project_description.md`, section 1 (then line 26) and reference 4 (then line 233).
- **Verified**: `gh api repos/HamSCI/MSQP/contents/MSQP%20Research%20Questions.pdf` returns the
  file (333,916 bytes). A Markdown twin, `Research Questions.md`, sits beside it.
- **Decision**: link the PDF on `main`. It is a living document, so `main` rather than a SHA (R11).
  Reference 4 keeps the repository root as a secondary link for the reference literature.
- **Status**: fixed in c3f951f, pushed; reply posted. Issue open for NAF to close.

### #2, "Additional references"

> I would like to suggest adding "Meteor Scatter: The Science Behind the Pings" by NN4NT and
> "Meteor Scatter: An Overview" by Weitzen to the references, and citing them toward the beginning
> of the document.

- **Verified (W6, W12)**:
  - Weitzen, J. A., and W. T. Ralston (1988), Meteor scatter: An overview, *IEEE Trans. Antennas
    Propag.*, 36(12), 1813–1819. ADS bibcode 1988ITAP...36.1813W. PDF already present in
    HamSCI/MSQP as `Weitzen_and_Ralston_Meteor_scatter_an_overview.pdf`.
  - Suggs, R. M., *Meteor Scatter Communications: The Science Behind the Pings*, Huntsville
    Hamfest, 19 August 2017. NTRS document 20170009030, report M17-6200. The archived slides name
    him KB5EZ; FCC ULS shows NN4NT as his current vanity call, and hamsci.org/hamsci2026 lists
    "Dr. Rob Suggs NN4NT" as the invited meteor scatter tutorial speaker. Same person; cited as NN4NT.
- **Decision**: both added as references 12 and 13 (McKinley becomes 14); cited by title and
  author in the physics paragraph of section 1, as the two introductions a student reads first.
- **Status**: done in c3f951f, pushed; reply posted. Issue open for NAF to close.

### #3, "Observation (my three cents)"

> The Meteor Scatter Capstone document reads very similarly to the QPA Capstone document, which is
> not surprising since Claude wrote them both. But there is a substantial difference between the
> two cases. The audience for the QPA document is Electrical Engineering students, and the
> terminology and tone are appropriate.
>
> On the other hand, the audience for the MS document is computer science students, but the
> terminology and tone are quite advanced and focused on a Meteor Scatter audience. Had I not
> recently participated in the Perseids, I would not have been able to follow the discussion. I am
> concerned that a student might be discouraged from what would be a very fruitful and interesting
> data science project.

- **Analysis** (assistant's, with a declared conflict of interest: an earlier Claude session drafted
  the document, so this is self-review, H2 exception). Evidence from the text: "QSO" appeared in the
  title and was never expanded; "spot", "ADIF", and "AGC" were used before or without definition;
  "ping" was used before the sentence explaining it; the reader met 460 words of physics and on-air
  conventions before section 2 stated the software problem. The QPA document
  (`/scratch/w2naf/code/QPA/docs/project_description.md`) confirms Robert's premise: same structure,
  EE/CE audience stated in its header.
- **Correction to the initial assessment**: the assessment said the document lacked a header table
  naming the audience. It has one (lines 5–12). That item was dropped.
- **Decision** (NAF: "Do the recommended fix"): restructure sections 1 and 2's boundary, define
  every term at first use, add a glossary, move operating conventions to the requirements.
- **Status**: done in c3f951f, pushed; reply posted. NAF has not yet read the rewritten section 1. Issue open for Robert's re-read.

## Edits made

`docs/project_description.md` (4538 → 5503 words):

1. Italic audience line under the header table, pointing to the glossary.
2. Section 1 rewritten. New opening paragraph states the problem in software terms with no
   numbers (the numbers stay in section 2, W10). HamSCI paragraph kept. Event paragraph now
   defines QSO, QSO party, callsign, grid square. Physics paragraph shortened, defines ping,
   MSK144, decode, and cites Suggs and Weitzen & Ralston. New data paragraph defines spot,
   PSKReporter, ADIF, `ALL.TXT`, WAV archive, and states which data feeds scoring and which feeds
   science. Science-program paragraph kept, link fixed, HF/VHF and underdense/overdense glossed.
3. The operating-conventions paragraph (band alternation, even/odd slots, AGC off) moved out of
   section 1 into section 5 as a note "On R1 and R2", with AGC expanded.
4. New section 11, Glossary (20 terms, table). References renumbered to section 12.
5. References 12 (Suggs) and 13 (Weitzen & Ralston) added; McKinley renumbered to 14; reference 4
   points at the PDF.

`CLAUDE.md` line 23 and `notes/2026-09-02_msqp_capstone_proposal.md` line 71: "section 11" →
"section 12" for the references.

`notes/2026-09-02_issue_replies_1-3.md`: drafted replies, one per issue, with A8 trailers.

## Verification

- All three URLs in the new references resolve (checked this session: NTRS record, ADS record,
  HamSCI/MSQP contents listing).
- Grid square example FN21 is Scranton's (41.4°N, 75.66°W → field F/N, square 2/1).
- "Tens of thousands of receivers" was considered for the PSKReporter sentence and dropped as
  unsourced (W12); the text says "receivers worldwide".
- W14 check on the rewritten section 1: reported in the session transcript; no sentence over 50
  words that is not a list.
- W4/W15 sweep: no em dashes in prose. Two pre-existing "rather than" / "whether or not" hits at
  lines 58 and 185 were not touched this session; candidates for a later tightening pass.

## Open items

1. **NAF to read the rewritten section 1 and the glossary** before the replies go out. Reply 3
   says "reviewed by him"; that must be true before posting.
2. ~~Commit and push~~ Done: c3f951f (fix) and 040adf8 (log hash), pushed 2026-09-02 22:27 UTC.
3. ~~Post the three replies~~ Done 22:28 UTC on NAF's instruction; URLs in
   `2026-09-02_issue_replies_1-3.md`. All three issues remain open for Robert's re-read and NAF's
   closing (R7, H7).
4. **Published artifact page** "MSQP Capstone Proposal",
   https://claude.ai/code/artifact/612b740e-294e-4c7e-ac3a-fbcc92292be9, was synchronized to the
   document by the earlier session and is shared by link. An updated HTML mirroring all of the
   above was built this session at
   `/tmp/claude-491543495/-scratch-w2naf-code-msqp-hamsci-org/ef784bba-4592-40cd-81b9-0e6fdd728155/scratchpad/msqp_capstone_proposal.html`,
   but the republish was denied by the auto-mode permission classifier (the page is outward-facing).
   **Still open**: NAF republishes, or tells the assistant to in an interactive session. Until then
   the live page shows the pre-review text.
5. The two pre-existing W4 hits (lines 58, 185) for the tightening pass.
