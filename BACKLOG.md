# Backlog

This is a Jira-style starter backlog. The first objective is not to assign all work immediately. It is to seed enough clear issues that contributors can claim work without needing a long meeting first.

Suggested sizing:

- S: 1-3 focused hours.
- M: 0.5-1 day.
- L: multiple days or needs decomposition before implementation.

## Seed Issues for Day One

These are the first 15 issues I would create before inviting the broader group:

| ID | Title | Labels | Size |
| --- | --- | --- | --- |
| DF-001 | Create project charter | `area:product`, `priority:p0` | S |
| DF-002 | Choose public repo owner and initialize repository | `area:infra`, `priority:p0` | S |
| DF-003 | Configure main branch protections | `area:infra`, `priority:p0` | S |
| DF-004 | Create issue labels and project board | `area:pm`, `area:infra`, `priority:p0` | S |
| DF-005 | Draft Circle/community kickoff update | `area:product`, `priority:p0` | S |
| DF-006 | Define media verification taxonomy | `area:research`, `good-first-issue` | S |
| DF-007 | Inventory candidate datasets | `area:data`, `area:research`, `good-first-issue` | M |
| DF-008 | Survey 3 open-source detectors | `area:ml`, `area:research` | M |
| DF-009 | Summarize C2PA and Content Credentials | `area:research`, `area:safety` | M |
| DF-010 | Propose evaluation metrics | `area:evaluation`, `area:research` | M |
| DF-011 | Draft image-first MVP user stories | `area:product`, `priority:p0` | S |
| DF-012 | Sketch high-level architecture diagram | `area:backend`, `area:infra`, `needs-design` | S |
| DF-013 | Draft responsible-use and privacy policy | `area:safety`, `area:docs` | M |
| DF-014 | Create report UI wireframe | `area:frontend`, `needs-design` | M |
| DF-015 | Write local development proposal | `area:infra`, `area:docs` | S |

## Epic: Repository Governance

### DF-001: Create project charter

As a contributor, I want a short charter so I understand the mission, scope, non-goals, and success criteria.

Acceptance criteria:

- Charter states the mission in one paragraph.
- Charter lists MVP scope and non-goals.
- Charter includes 3-4 month success criteria.
- Charter avoids definitive truth claims.

### DF-002: Choose public repo owner and initialize repository

As a co-lead, I want the repo owned in the right place so the project can survive individual availability changes.

Acceptance criteria:

- Decision made between personal repo and organization repo.
- At least two trusted admins or organization owners are assigned.
- Raw meeting notes and recordings are excluded from public commits.
- Default branch is `main`.

### DF-003: Configure main branch protections

As a maintainer, I want `main` protected so contributors cannot accidentally break or delete the project.

Acceptance criteria:

- Direct pushes to `main` are blocked.
- Pull requests are required.
- At least one approving review is required.
- Force pushes and branch deletion are blocked.
- Status checks are required once CI exists.

### DF-004: Create issue labels and project board

As a contributor, I want issues grouped by area and priority so I can find useful work quickly.

Acceptance criteria:

- Labels exist for frontend, backend, ML, data, evaluation, research, docs, safety, infra, product, good-first-issue, blocked, and priority.
- Project board has columns for Backlog, Ready, In Progress, Review, Done.
- At least 10 issues are added before the first broad invite.

### DF-005: Decide open-source license

As a project maintainer, I want a license decision before meaningful code lands.

Acceptance criteria:

- Maintainers compare MIT and Apache-2.0 at minimum.
- Decision is recorded in `docs/decisions/`.
- `LICENSE` file is added after the decision.

## Epic: Research and Product Definition

### DF-006: Define media verification taxonomy

As a contributor, I want shared vocabulary so the team does not blur deepfakes, cheapfakes, synthetic media, and misinformation.

Acceptance criteria:

- Glossary defines deepfake, synthetic media, cheapfake, face swap, voice clone, AI-generated image, AI-edited image, misinformation, disinformation, provenance, watermark, and manipulation detection.
- Each term includes one example.
- Terms that are out of MVP scope are marked clearly.

### DF-007: Inventory candidate datasets

As an ML contributor, I want a dataset inventory so we can choose legal and practical evaluation data.

Acceptance criteria:

- Inventory includes dataset name, media type, size, access process, license/terms, strengths, weaknesses, and citation/source.
- At least five candidate datasets are listed.
- Any dataset with uncertain license terms is marked as blocked.

### DF-008: Survey existing open-source detectors

As a research contributor, I want to understand prior work so the project does not start from scratch blindly.

Acceptance criteria:

- At least three detectors or model repos are summarized.
- Each summary includes model type, supported media, license, setup difficulty, strengths, weaknesses, and last visible maintenance date.
- Recommendation is made for one baseline integration candidate.

### DF-009: Summarize C2PA and Content Credentials

As a product contributor, I want to know how provenance standards fit the product.

Acceptance criteria:

- Brief explains what provenance can and cannot prove.
- Brief identifies at least one library or API option.
- Brief recommends whether C2PA belongs in MVP, Phase 2, or later.

### DF-010: Propose evaluation metrics

As a data contributor, I want agreed metrics so we can measure progress honestly.

Acceptance criteria:

- Proposal covers ROC-AUC, precision, recall, false positive rate, calibration, threshold selection, latency, and robustness.
- Proposal explains why false positives matter in this domain.
- Proposal includes a minimal benchmark plan for the MVP.

### DF-011: Draft image-first MVP user stories

As a PM, I want MVP stories so implementation can start without scope ambiguity.

Acceptance criteria:

- Stories cover upload, analysis status, report view, evidence display, limitations, and error handling.
- Stories specify what is not included.
- Stories are reviewed by at least one frontend, backend, and ML contributor.

## Epic: Architecture and Walking Skeleton

### DF-012: Sketch high-level architecture diagram

As a technical lead, I want a simple architecture diagram so contributors can see how pieces fit.

Acceptance criteria:

- Diagram includes frontend, API, job queue or async worker, model adapter, storage, and report output.
- Diagram includes MVP and later-phase boundaries.
- Diagram is checked into `docs/architecture.md` or linked from it.

### DF-016: Define analysis result JSON schema

As a frontend or backend contributor, I want a stable report schema so UI and API work can happen in parallel.

Acceptance criteria:

- Schema includes media metadata, signals, confidence, evidence cards, limitations, and timestamps.
- Example response is included.
- Schema has version field.

### DF-017: Create FastAPI backend skeleton

As a backend contributor, I want a minimal API so the frontend and model adapter can integrate.

Acceptance criteria:

- Health endpoint exists.
- Create-analysis endpoint accepts a stub payload.
- Get-analysis endpoint returns stub report data.
- Basic tests or smoke checks exist.

### DF-018: Create React frontend skeleton

As a frontend contributor, I want a minimal app so the upload and report flows can be built.

Acceptance criteria:

- App runs locally.
- Routes or views exist for upload and report.
- API base URL can be configured.
- Empty, loading, success, and error states are represented.

### DF-019: Add Docker Compose local dev setup

As a contributor, I want one local command path so setup is not a blocker.

Acceptance criteria:

- Docker Compose starts frontend and backend or documents why one service is excluded.
- `.env.example` is provided.
- README includes local setup steps.

### DF-020: Add GitHub Actions CI skeleton

As a maintainer, I want automated checks before requiring status checks on PRs.

Acceptance criteria:

- Workflow runs on PRs to `main`.
- Workflow includes at least markdown lint or placeholder checks before app code exists.
- Job names are unique and stable.
- Branch protection is updated after CI is passing.

## Epic: Baseline Analysis Pipeline

### DF-021: Create model adapter interface

As an ML contributor, I want a stable interface so models can be swapped without rewriting the app.

Acceptance criteria:

- Interface accepts a local media reference or bytes.
- Interface returns normalized score, label, evidence, latency, and model metadata.
- Stub adapter is implemented.

### DF-022: Add metadata extraction utility

As a report user, I want to see basic media metadata when available.

Acceptance criteria:

- Utility extracts safe image metadata.
- Utility strips or avoids exposing sensitive fields in public demo output.
- Result is mapped into the report schema.

### DF-023: Integrate first baseline image detector

As an ML contributor, I want a working baseline so the project can produce real model signals.

Acceptance criteria:

- Candidate model license permits project use.
- Setup is documented.
- Adapter returns normalized output.
- Limitations are documented in a model card.

### DF-024: Create evaluation runner skeleton

As a data contributor, I want repeatable evaluation so model changes are measurable.

Acceptance criteria:

- Runner accepts a manifest of examples.
- Runner records predictions and metrics.
- Runner writes results to a reproducible output format.
- At least one tiny sample run is documented.

### DF-025: Draft dataset card template

As a contributor, I want dataset cards so data use is responsible and traceable.

Acceptance criteria:

- Template includes origin, license, consent/access, composition, intended use, limitations, and risks.
- Template includes citation/source fields.
- One candidate dataset is filled out as an example if terms allow.

## Epic: Report UX and Safety

### DF-026: Create report UI wireframe

As a user, I want a readable report that explains evidence without pretending to be certain.

Acceptance criteria:

- Wireframe includes summary, confidence, evidence cards, metadata, model signal, and limitations.
- Wireframe avoids alarmist wording.
- Wireframe works for inconclusive results.

### DF-027: Write confidence-language guidelines

As a maintainer, I want consistent language so results are not overstated.

Acceptance criteria:

- Guidelines define allowed phrases for low, medium, high, and inconclusive confidence.
- Guidelines ban definitive labels like "real" or "fake" unless clearly qualified.
- Guidelines include examples.

### DF-028: Draft responsible-use policy

As a project maintainer, I want safety boundaries before public demo use.

Acceptance criteria:

- Policy covers false positives, privacy, abuse, uploaded media, and prohibited uses.
- Policy explains that the tool supports investigation, not final judgment.
- Policy is linked from README.

### DF-029: Define media retention policy

As a user, I want to know what happens to uploaded media.

Acceptance criteria:

- MVP retention behavior is specified.
- Public demo storage limits are specified.
- Deletion and logging behavior are documented.

## Epic: Demo and Public Artifacts

### DF-030: Create demo script

As a PM, I want a repeatable demo flow for meetings and portfolio use.

Acceptance criteria:

- Script shows happy path and inconclusive path.
- Script calls out limitations honestly.
- Script names each workstream contribution.

### DF-031: Write architecture document

As a contributor, I want architecture docs so new contributors can join mid-project.

Acceptance criteria:

- Document explains components, data flow, and local development.
- Document includes MVP versus future architecture.
- Document links to relevant ADRs.

### DF-032: Write final evaluation report

As an ML contributor, I want a public artifact that shows technical maturity.

Acceptance criteria:

- Report includes methods, metrics, dataset notes, results, failure cases, and limitations.
- Report includes enough detail to reproduce a small run.
- Report avoids inflated claims.

## Suggested Labels

- `area:frontend`
- `area:backend`
- `area:ml`
- `area:data`
- `area:evaluation`
- `area:research`
- `area:docs`
- `area:safety`
- `area:infra`
- `area:product`
- `good-first-issue`
- `beginner-friendly`
- `needs-design`
- `needs-research`
- `needs-triage`
- `blocked`
- `priority:p0`
- `priority:p1`
- `priority:p2`
