# msqp.hamsci.org

An interactive platform to coordinate the [HamSCI](https://hamsci.org) **[Meteor Scatter QSO Party](https://hamsci.org/msqp)** (MSQP) and to serve the data it produces to the research community.

Proposed as a two-semester **Computer Science senior capstone project** at The University of Scranton, sponsored by Dr. Nathaniel A. Frissell, W2NAF.

## The problem

MSQP runs six times a year, timed to major meteor showers. Amateur operators around the world work each other on 6 and 10 meters using MSK144, bouncing signals off the ionized trails of meteors, and the resulting logs, spots, and audio recordings feed an active research program on meteor scatter propagation.

Everything around that data is done by hand, by one volunteer. Scoring means reconciling submitted ADIF logs against PSKReporter spot data; the December 2025 event alone captured **280 million lines** of it. The consequence is latency:

| Event | Ran | Results published |
|---|---|---|
| Perseids | 11–12 Aug 2025 | 16 Nov 2025 |
| Geminids | 12–13 Dec 2025 | 15 Apr 2026 |

Participants wait three to four months to learn how they did. There is no live view during an event, audio deposits to Zenodo are typed by hand, and nothing indexes the archive for the researchers who need it.

## The project

Build, test, and deploy the platform that does the mechanical part: event registry, entrant registration, ADIF and PSKReporter ingest, a deterministic and auditable scoring engine, a live event dashboard, Zenodo deposit integration, automated results publication, and a documented public data API. The organizer keeps control of every score, and the manual workflow stays available as a fallback.

The headline demonstration is to run a real MSQP event on the platform and publish its results within one week.

The full project description presented to students is in [docs/project_description.md](docs/project_description.md).

## Repository Contents

| Path | Purpose |
|---|---|
| `docs/project_description.md` | Capstone project description for students and faculty |
| `notes/` | Dated session notes |
| `ai/ai_usage_log.md` | Log of all substantive AI-assisted work sessions |
| `.claude/` | AI governance rules and the `/commit` workflow |
| `reference/` | Local-only reference material (gitignored; never committed) |

## Related HamSCI repositories

- [`HamSCI/MSQP`](https://github.com/HamSCI/MSQP) — MSQP research questions and reference literature
- [`HamSCI/meteor-scatter`](https://github.com/HamSCI/meteor-scatter) — automated MSK144 monitoring for PSWS stations
- [`HamSCI/Machine-Learning-Meteor-Scatter-Classification-Code`](https://github.com/HamSCI/Machine-Learning-Meteor-Scatter-Classification-Code) — meteor scatter signal classifier

## Data handling

Callsigns and Maidenhead grid squares are public by amateur radio convention. Participant email addresses, street addresses, and phone numbers are not, and must never be committed to this repository or published in any product.

## AI Governance

This repository follows the [`ai_project_template`](https://github.com/w2naf-academia/ai_project_template) standards: every substantive AI-assisted session is logged in `ai/ai_usage_log.md` before committing, AI-assisted commits carry the `[AI-assisted]` prefix, and all work complies with the policies in `.claude/rules/ai-governance.md`.

## License

MIT license; see [LICENSE](LICENSE).
