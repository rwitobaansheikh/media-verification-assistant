# Media Verification Assistant

Working title for an open-source group project focused on suspicious media analysis.

The current framing is not "we will solve deepfake detection." The safer and more useful framing is:

> Build an open-source media verification assistant that analyzes suspicious images, videos, or social posts and produces an evidence-backed confidence report.

The project is in planning. The first goal is to create a clean repository, define a credible MVP, seed well-scoped issues, and give contributors work that can become real portfolio evidence.

## Planning Constraints

- Public and open source.
- No required paid APIs or paid cloud services for basic development.
- Deployable demo within roughly 3-4 months.
- Useful for contributors with mixed experience levels, including people learning AI/ML from scratch.
- Honest about limitations, false positives, and uncertainty.
- Research-first enough to avoid overclaiming, but not research-only.

## Initial MVP Hypothesis

The first MVP should accept a small media input, likely an image first, and return a transparent report with:

- basic metadata and provenance checks;
- one or more model-based signals;
- clear confidence language;
- evidence cards explaining why the system produced the result;
- known limitations and next-step suggestions.

Video, social-media link ingestion, browser extensions, ensembles, and advanced fact-checking should be treated as later phases unless research shows a smaller route is better.

## Repo Map

- [PROJECT_PLAN.md](PROJECT_PLAN.md): project framing, phases, workstreams, and open questions.
- [BACKLOG.md](BACKLOG.md): Jira-style stories broken into small issues.
- [docs/github-setup.md](docs/github-setup.md): no-cost GitHub setup and protection checklist.
- [docs/research/initial-research-plan.md](docs/research/initial-research-plan.md): first research sprint plan.
- [CONTRIBUTING.md](CONTRIBUTING.md): contribution workflow.
- [SECURITY.md](SECURITY.md): vulnerability and secret-handling guidance.

## Privacy Note

Do not commit raw meeting recordings, transcripts, participant notes, private planning exports, uploaded media, API keys, model weights, or datasets unless the group has explicitly agreed they are safe to publish.

