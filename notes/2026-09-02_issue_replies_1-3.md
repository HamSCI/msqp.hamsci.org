# Drafted replies to community-review issues #1–#3 (roberthipple, 2026-09-02)

Status: **posted 2026-09-02 22:28 UTC** on NAF's instruction (`/commit and push and post
comments`). Fix committed as c3f951f and pushed first, so reply 1 links the full SHA (R11).
As posted, the trailer reads "under Nathaniel Frissell's direction and posted on his
instruction. Decisions are his (A3, A5)." rather than "reviewed by him", because NAF had not yet
read the rewritten section 1 when he instructed the posting.

Posted comments:
- #1: https://github.com/HamSCI/msqp.hamsci.org/issues/1#issuecomment-5517324713
- #2: https://github.com/HamSCI/msqp.hamsci.org/issues/2#issuecomment-5517324884
- #3: https://github.com/HamSCI/msqp.hamsci.org/issues/3#issuecomment-5517325046

The texts below are the drafts as written before posting; the posted versions differ only in the
trailer wording above and in reply 1's resolved SHA link.

Issues: https://github.com/HamSCI/msqp.hamsci.org/issues

---

## Reply to #1, "Link misses target"

Fixed, thank you. Both the "MSQP research questions" link in section 1 and reference 4 in the
references list now point at the PDF, `MSQP Research Questions.pdf`, on `main` in HamSCI/MSQP.
Reference 4 keeps the repository root as a secondary link because the same repository holds the
reference literature. The change is in commit [SHA after push].

<sub>Drafted by Claude (Anthropic), `claude-fable-5-1`, under Nathaniel Frissell's direction and
reviewed by him. Co-Authored-By: Claude Fable 5.1 &lt;noreply@anthropic.com&gt;</sub>

---

## Reply to #2, "Additional references"

Added, thank you. Both are now in the references list and are cited in the Background section,
in the paragraph that introduces the physics, as the two introductions a student should read
first.

- Suggs, R. M., NN4NT (2017), *Meteor Scatter Communications: The Science Behind the Pings*,
  Huntsville Hamfest, 19 August 2017. The talk is archived on the NASA Technical Reports Server
  as document 20170009030. Rob gave it under his earlier callsign, KB5EZ, so the archived slides
  carry that call; the reference cites him as NN4NT.
- Weitzen, J. A., and W. T. Ralston (1988), Meteor scatter: An overview, *IEEE Transactions on
  Antennas and Propagation*, 36(12), 1813–1819. A copy was already in the HamSCI/MSQP repository,
  which the reference now says.

<sub>Drafted by Claude (Anthropic), `claude-fable-5-1`, under Nathaniel Frissell's direction and
reviewed by him. Co-Authored-By: Claude Fable 5.1 &lt;noreply@anthropic.com&gt;</sub>

---

## Reply to #3, "Observation (my three cents)"

Agreed, and thank you for saying it plainly. The comparison with the antenna-array document is
fair: that one is written for EE students who already own the vocabulary, and this one was written
in the same register for readers who do not. I have reworked the front of the document for a
computer science reader.

- Section 1 now opens with the problem in software terms (an event produces a large dataset that
  one volunteer scores by hand) before any physics appears.
- Every radio term is defined at first use: QSO, callsign, grid square, ping, MSK144, decode,
  spot, ADIF, `ALL.TXT`, and the rest. A new section 11 collects them in a glossary.
- The physics is one short paragraph that points to the two introductions you suggested in #2,
  with a note that the team does not need to read further to build the platform.
- The on-air operating conventions (band alternation, even/odd transmit slots, AGC off) moved out
  of the Background and into the requirements section, where they are needed.
- A line under the header table states the intended audience.

The technical sections (4 through 10) are largely unchanged, since they were already written in
software terms. If a term still trips you on a re-read, please say which one.

<sub>Drafted by Claude (Anthropic), `claude-fable-5-1`, under Nathaniel Frissell's direction and
reviewed by him. Co-Authored-By: Claude Fable 5.1 &lt;noreply@anthropic.com&gt;</sub>
