# Project Plan

## Source Inputs

This plan is synthesized from:

- the April 17 group brainstorm;
- the April 29 co-lead planning meeting;
- the initial roadmap notes.

It is intentionally written as a public-safe planning artifact. The raw transcripts should stay out of the public repo unless participants explicitly consent.

## Mission

Build an open-source media verification assistant that helps people evaluate suspicious media by combining provenance, metadata, forensic, and model-based signals into a transparent confidence report.

The product should help users reason about evidence. It should not claim to determine truth with certainty.

## Why This Project

The group values:

- real-world usefulness;
- credible AI/ML, product, system design, and open-source experience;
- a project large enough for multiple contributors but small enough to ship;
- public artifacts contributors can reference in interviews;
- careful handling of social impact, privacy, and model limitations.

## MVP Scope

The recommended MVP starts with image analysis. Image-first is smaller than video-first, easier to demo, and still leaves room for backend, frontend, ML, data, evaluation, safety, and documentation work.

### In Scope

- Upload or submit one image.
- Create an analysis job.
- Extract safe metadata where available.
- Run a baseline image-manipulation or synthetic-media detector.
- Produce a structured report with confidence language and evidence cards.
- Store minimal result data for demo use.
- Document model limitations and false-positive risks.
- Provide an evaluation plan and at least one baseline benchmark result.

### Out of Scope for MVP

- Definitive truth claims.
- Automated moderation or takedown decisions.
- Broad misinformation fact-checking.
- Social platform scraping at scale.
- Paid-only APIs as required infrastructure.
- Storing user-uploaded media indefinitely.
- Training a state-of-the-art detector from scratch before a baseline demo exists.

## Success Criteria

By the end of the first 3-4 month cycle, the project should have:

- a public repo with protections, templates, labels, and contributor docs;
- a deployed demo or documented local demo path;
- a working vertical slice from media submission to report display;
- at least one baseline model adapter;
- dataset and model cards for anything used in evaluation;
- an evaluation report covering metrics and known failure modes;
- a clear README with honest project positioning;
- merged contributions across multiple workstreams.

## Workstreams

### Product and PM

Owns project charter, roadmap, user stories, issue priority, meeting notes, demo scripts, and contributor coordination.

### Research

Owns literature review, dataset review, model survey, provenance systems, open-source detector landscape, and limitation writeups.

### Data and Evaluation

Owns dataset cards, access process, splits, metrics, benchmark runner, reproducibility notes, and result reporting.

### ML Model Adapters

Owns baseline detector integration, frame sampling later, model interfaces, output normalization, and calibration experiments.

### Backend

Owns FastAPI service, analysis job schema, queue/storage design, media hashing, result persistence, and API contracts.

### Frontend

Owns upload flow, report UI, loading states, evidence cards, confidence visualization, and accessibility.

### Infrastructure and DevEx

Owns GitHub setup, local dev environment, Docker Compose, CI, linting, testing, dependency updates, and release process.

### Safety, Privacy, and Policy

Owns responsible-use policy, media retention rules, privacy language, abuse cases, disclaimers, and vulnerability process.

### Documentation and Education

Owns onboarding, glossary, architecture docs, tutorials, demo walkthroughs, and educational writeups.

## 3-4 Month Roadmap

### Phase 0: Repository and Alignment, Week 1

- Create public GitHub repo or organization repo.
- Add protections, issue templates, PR template, labels, and project board.
- Publish mission, MVP framing, and contribution workflow.
- Seed 10-15 issues before inviting broad contribution.
- Schedule follow-up group meeting for MVP alignment.

### Phase 1: Research and MVP Definition, Weeks 1-3

- Define taxonomy: deepfake, synthetic media, cheapfake, provenance, watermark, manipulation detection, misinformation, disinformation.
- Inventory datasets and licenses.
- Survey existing open-source detectors and detection methods.
- Summarize C2PA and Content Credentials.
- Propose evaluation metrics and failure-mode categories.
- Decide image-first versus video-first based on evidence.

### Phase 2: Walking Skeleton, Weeks 2-5

- Create frontend, backend, and shared schema skeletons.
- Implement upload or mock-submission flow.
- Implement async analysis job stub.
- Return deterministic fake report data.
- Display report UI with evidence cards.
- Add minimal CI and local setup docs.

### Phase 3: Baseline Analysis Pipeline, Weeks 4-9

- Add metadata extraction.
- Add first model adapter interface.
- Integrate one baseline detector or placeholder model with documented limitations.
- Create result normalization and confidence-language mapping.
- Add evaluation runner skeleton.

### Phase 4: Evaluation, Safety, and Demo, Weeks 8-14

- Run first baseline benchmark on a small approved dataset or sample.
- Write model card and dataset card.
- Add failure-case analysis.
- Add privacy and responsible-use docs.
- Deploy demo using no-cost infrastructure where possible.
- Record demo walkthrough and create contributor credits.

### Phase 5: Stretch Scope, After MVP

- Video frame sampling and temporal signals.
- C2PA/provenance integration.
- Browser extension or URL ingestion.
- Multi-model ensemble.
- Social-media re-encoding robustness tests.
- LLM-assisted report explanation grounded only in collected evidence.

## First 7 Days

1. Create the repo foundation and protection checklist.
2. Create the first project board with seeded issues.
3. Assign co-lead ownership for GitHub settings and issue triage.
4. Run a short research sprint using the briefs in [docs/research/initial-research-plan.md](docs/research/initial-research-plan.md).
5. Hold an MVP alignment meeting and decide the first vertical slice.

## Open Decisions

- Repository owner: personal repo, new GitHub organization, or existing organization.
- Final project name.
- License: MIT, Apache-2.0, GPL family, or another OSI-approved license.
- Default stack: recommended starting point is React, Python/FastAPI, PyTorch, Docker Compose, and GitHub Actions, but this still needs confirmation.
- MVP media type: recommended starting point is images, pending research.
- Hosting plan for demo: Vercel or GitHub Pages for frontend, Render/Fly.io/free-tier alternative/local-only for backend, or a static demo first.
- Whether to allow uploaded media in a public demo at all.

