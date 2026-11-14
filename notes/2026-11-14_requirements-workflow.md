# 2026-11-14: Requirements move to one pull request per change; Tom McMahan joins

## Decided (W2NAF)

- **PR #5 merges as version 0.1** of the requirements documents, instead of staying open as a
  shared draft branch. The leads then revise their own documents through their own pull requests.
  > "Let's merge PR#5 and update Issue 6 to explain the work flow." (W2NAF, 2026-11-14)
- **Tom McMahan, K1FR (GitHub `jtm5`), works with both Andrew and Robert.** Added as an assignee
  on #6 by W2NAF on 2026-11-14.
  > "JTM is Tom McMahan K1FR, who will work with both Andrew and Robert Hipple." (W2NAF, 2026-11-14)

## Why

- Nobody had started on the shared branch four days after #6 was posted, so switching cost only a
  rewrite of #6.
- Three people committing to one branch, each appending to `ai/ai_usage_log.md` through `/commit`,
  would produce a merge conflict for whoever pulls second. Separate branches avoid that.
- One pull request per document matches ownership, and `main` already requires an approving
  review, so every change is reviewed.
- Merging adopts nothing: every document still reads "Status: DRAFT" until its owner changes it.

## Changed

- `docs/requirements/README.md`: status line (merged as 0.1; adoption is by status line); Tom in
  "Who decides what"; open decision 3 notes Tom; new section "How changes are made".
- `docs/requirements/node-dashboard.md`: Tom among the stakeholders.
- Issue #6 rewritten for the new workflow (after #5 merges).

## Where Tom's work may fit (proposals for Tom and the leads)

From his public repositories, checked 2026-11-14:

- `jtm5/ms-trail-geometry`: for a transmitter, receiver, shower radiant and time, where trails can
  give a specular echo, with a relative rate index through the day. Its README calls it an early
  prototype, not validated. A possible source for an "expected geometry" view on the node
  dashboard, or for event context on the site.
- `jtm5/MS-3D-Visualization` and `MS-3D-Visualization-Notebook`: forward-scatter Doppler for a
  given trail. Relevant to per-ping measures (`MSD-F-005`).
- `jtm5/Flex-DAXiqRec`: IQ recording from a Flex radio. Relevant to the audio-retention question
  in `node-dashboard.md`.

## Open

- Content problems found in review on 2026-11-14, left for the owners' first pull requests: the
  2026–27 interface scope disagrees between `README.md` (decision 2), `interface.md`, and
  `msqp-site.md` section 4; `MSD-F-004` (Quadrantids event mode) depends on the site's event feed,
  which is in the site's objective tier, not its threshold; `MSD-F-007` requires links that
  `MSI-I-004` makes a stretch item; `MSD-F-001` is timed against the unsettled T/R period.
- `docs/project_description.md` and `CLAUDE.md` ("no students are recruited") are out of date.

## Later the same day: W2NAF steps out of the critical path

> "They can edit the README together. I don't want to do anything but review. I need to be out of
> the critical path. I even want to get things set up so they can review each other, or have
> approvals from RobSuggsNN4NT and AC1SN (the HamSCI-Meteor working group leads). The less I need
> to get involved, the better." (W2NAF, 2026-11-14)

- `README.md` is now owned by both leads, like `interface.md`.
- Any one approval from Andrew, Robert, Tom, or the working-group leads (`RobSuggsNN4NT`, `AC1SN`)
  is enough to merge; a change to a shared document also needs the other lead. The author merges.
- `.github/CODEOWNERS` requests all five as reviewers on any change under `docs/requirements/`.
  Branch protection is unchanged (one approving review; code-owner review not required). All five
  already had write access on 2026-11-14, so their approvals count.
- W2NAF keeps only open decision 3 (project A's team) and production deploys of A, both of which
  touch the capstone or HamSCI infrastructure. Open decisions 1 and 2 no longer name W2NAF.
- Open: AC1SN's name, for the README.

## Pull requests scoped to an idea

> "PRs can be scoped a bit bigger. Rather than scoping to one document, they should be scoped to
> an idea or work effort addressing an issue." (W2NAF, 2026-11-14)

`README.md` "How changes are made" and #6 now say one pull request per idea or work effort, tied
to an issue, touching whichever documents it needs; each document's owner approves changes to it.

## Open decision 3 answered: a capstone team of one

> "Andrew Kusner is the only capstone student working on this project." (W2NAF, 2026-11-14)

Recorded in `docs/requirements/README.md` (decision 3 marked answered and kept in place so decisions
4 to 6 keep their numbers; "Who decides what"; the capstone boundary), `msqp-site.md` (one word),
and `CLAUDE.md` (status line). Not changed: `docs/project_description.md`, which still plans for
2–3 students (its "Team size" row and section 9, "Team Roles"). It is the description as presented,
and its revision waits until the requirements settle, as `README.md` already says.
