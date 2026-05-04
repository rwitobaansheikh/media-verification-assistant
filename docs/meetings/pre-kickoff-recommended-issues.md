# Pre-Kickoff Recommended Issues

Status: Draft

Use these as copy-ready GitHub issue bodies for the five issues most worth adding before the May 4 team kickoff.

## Issue 11: Draft Image-First MVP User Stories

Labels:

- `area:product`
- `priority:p0`

Suggested assignee:

- Product/PM-oriented contributor, co-lead, or someone who wants to learn product scoping.

Body:

```markdown
## Goal

Draft the first set of image-first MVP user stories so the team has a clear product target before implementation starts.

The current working hypothesis is that the MVP accepts an image or image-like media input and returns an evidence-backed confidence report. This issue should turn that hypothesis into small stories that frontend, backend, ML, data/evaluation, and safety contributors can react to.

## Background

The project should not claim to determine truth with certainty. The MVP should help users reason about suspicious media by presenting evidence signals, confidence language, limitations, and suggested next steps.

Relevant repo docs:

- `README.md`
- `PROJECT_PLAN.md`
- `docs/research/problem-space-brief.md`
- `docs/research/dataset-landscape-brief.md`

## Scope

Write user stories for the first MVP flow:

- user submits or uploads one image;
- system creates an analysis job;
- user sees analysis status;
- system returns a report;
- report shows evidence cards;
- report shows confidence language and limitations;
- report handles unsupported files, failed analysis, and inconclusive results.

## Acceptance Criteria

- [ ] Stories cover upload/submission, analysis status, report view, evidence display, limitations, and error handling.
- [ ] Stories use a consistent format: `As a [user], I want [goal], so that [reason].`
- [ ] Each story includes basic acceptance criteria.
- [ ] MVP non-goals are explicitly listed.
- [ ] At least one story mentions privacy/media retention expectations.
- [ ] At least one story mentions inconclusive or low-confidence results.
- [ ] Draft is saved in `docs/product/mvp-user-stories.md` or another agreed docs path.

## Suggested Output

`docs/product/mvp-user-stories.md`

## Notes

Keep this narrow. The goal is not to design video, social-media scraping, browser extensions, moderation decisions, or a definitive truth detector.
```

## Issue 12: Sketch High-Level Architecture Diagram

Labels:

- `area:backend`
- `area:infra`
- `needs-design`

Suggested assignee:

- Backend, infra, full-stack, or senior engineering contributor.

Body:

```markdown
## Goal

Create a simple high-level architecture diagram for the MVP so contributors can see how frontend, backend, model adapters, storage, and report output fit together.

## Background

The MVP is currently framed as an image-first media verification assistant. It should accept a small media input and produce an evidence-backed report. The architecture should support a walking skeleton first, then allow real metadata/model/provenance signals to be added later.

Relevant repo docs:

- `PROJECT_PLAN.md`
- `BACKLOG.md`
- `docs/research/problem-space-brief.md`

## Scope

Sketch the MVP architecture at a practical level. Include:

- frontend upload/report UI;
- backend API;
- analysis job creation;
- async worker or job-processing placeholder;
- model adapter interface;
- metadata/provenance check placeholder;
- report/result schema;
- storage boundaries;
- later-phase items clearly separated from MVP.

## Acceptance Criteria

- [ ] Diagram includes frontend, API, job processing, model adapter, metadata/provenance checks, storage, and report output.
- [ ] MVP components are visually separated from later-phase/stretch components.
- [ ] Diagram includes a short written explanation of the main flow.
- [ ] Diagram calls out what data should not be stored permanently in the public demo.
- [ ] Diagram avoids locking the team into expensive cloud services.
- [ ] Draft is saved in `docs/architecture.md` or another agreed docs path.

## Suggested Output

`docs/architecture.md`

## Notes

This can be a Mermaid diagram, Excalidraw export, simple Markdown diagram, or linked image. Prefer something easy to update in the repo.
```

## Issue 13: Draft Responsible-Use And Privacy Policy

Labels:

- `area:safety`
- `area:docs`
- `priority:p0`

Suggested assignee:

- Safety/privacy-minded contributor, product contributor, or strong writer.

Body:

```markdown
## Goal

Draft the project's first responsible-use and privacy policy so the team has guardrails before building upload flows, public demos, or model outputs.

## Background

This project deals with potentially sensitive media. Uploaded images may include identifiable people, private contexts, metadata, or misleading accusations. False positives and false negatives can cause harm. The project must be clear that it supports human investigation and does not make definitive truth claims.

Relevant repo docs:

- `README.md`
- `PROJECT_PLAN.md`
- `SECURITY.md`
- `docs/research/problem-space-brief.md`
- `docs/research/synthetic-performance-ethics-notes.md`

## Scope

Draft policy language covering:

- what users should and should not upload;
- whether uploaded media is stored;
- how long media or results may be retained;
- how model results should be interpreted;
- false-positive and false-negative risks;
- restrictions against harassment, doxxing, stalking, or targeting private individuals;
- disclaimers for legal, journalistic, employment, law-enforcement, and safety-critical decisions;
- contributor handling of sample media, datasets, and model weights.

## Acceptance Criteria

- [ ] Policy says the app does not determine truth or authenticity with certainty.
- [ ] Policy explains false-positive and false-negative risks.
- [ ] Policy includes a default media-retention recommendation.
- [ ] Policy includes rules for public demos and sample uploads.
- [ ] Policy mentions identifiable people, consent, and sensitive media.
- [ ] Policy says datasets/model weights should not be added without approval and terms review.
- [ ] Draft is saved in `docs/safety/responsible-use-and-privacy.md` or another agreed docs path.

## Suggested Output

`docs/safety/responsible-use-and-privacy.md`

## Notes

This is not legal advice. The goal is a practical first policy draft for project safety and contributor alignment.
```

## Issue 14: Create Report UI Wireframe

Labels:

- `area:frontend`
- `needs-design`

Suggested assignee:

- Frontend, UX, design, product, or contributor interested in report communication.

Body:

```markdown
## Goal

Create a first wireframe for the media verification report UI so the team can align on what the user sees after submitting an image.

## Background

The MVP should produce an evidence-backed confidence report, not a binary real/fake verdict. The UI needs to communicate evidence, uncertainty, and limitations clearly.

Relevant repo docs:

- `README.md`
- `PROJECT_PLAN.md`
- `docs/research/problem-space-brief.md`
- `docs/research/dataset-landscape-brief.md`

## Scope

Design a low-fidelity wireframe for:

- upload or submit image screen;
- loading/analysis state;
- report summary;
- media metadata section;
- provenance/content credentials section;
- model signal section;
- evidence cards;
- limitations and next steps;
- error or unsupported-file state;
- inconclusive result state.

## Acceptance Criteria

- [ ] Wireframe includes upload, loading, report, error, and inconclusive states.
- [ ] Report avoids binary "real/fake" framing as the primary UI.
- [ ] Evidence cards explain why a signal matters.
- [ ] Limitations are visible in the report.
- [ ] Wireframe includes mobile or narrow-screen considerations.
- [ ] Draft is saved or linked from `docs/product/report-ui-wireframe.md` or another agreed docs path.

## Suggested Output

`docs/product/report-ui-wireframe.md`

## Notes

This does not need polished visual design. A clear Markdown layout, screenshot from a design tool, or simple Figma/Excalidraw link is enough for this issue.
```

## Issue 15: Define Analysis Result JSON Schema

Labels:

- `area:backend`
- `area:frontend`
- `area:ml`
- `priority:p0`

Suggested assignee:

- Backend/full-stack contributor, with frontend and ML review.

Body:

```markdown
## Goal

Define the first version of the analysis result JSON schema so frontend, backend, and ML work can proceed in parallel.

## Background

The app needs a stable contract for the report output. Even before real models are integrated, the walking skeleton can return stub report data that matches the planned schema.

Relevant repo docs:

- `PROJECT_PLAN.md`
- `BACKLOG.md`
- `docs/research/problem-space-brief.md`

## Scope

Draft a versioned JSON schema or example response covering:

- analysis ID;
- schema version;
- submitted media summary;
- safe metadata fields;
- provenance result state;
- model/detector signals;
- confidence or concern level;
- evidence cards;
- limitations;
- recommended next steps;
- timestamps;
- error states.

## Acceptance Criteria

- [ ] Schema includes `schema_version`.
- [ ] Schema includes media metadata, signals, confidence/concern level, evidence cards, limitations, and timestamps.
- [ ] Schema distinguishes model score from product confidence language.
- [ ] Schema supports inconclusive and failed-analysis states.
- [ ] Example successful response is included.
- [ ] Example error/inconclusive response is included.
- [ ] Draft is saved in `docs/api/analysis-result-schema.md` or another agreed docs path.

## Suggested Output

`docs/api/analysis-result-schema.md`

## Notes

Keep this implementation-neutral. The goal is a first contract, not perfect validation logic.
```
