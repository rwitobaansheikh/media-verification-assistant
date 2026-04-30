# ADR-0001: Initial Project Scope

## Status

Proposed

## Context

The project started from a broad "deepfake/disinformation detector" idea. That framing is too broad for a 3-4 month open-source group project and risks overclaiming. The group also wants a deployable, public, useful, resume-worthy project that supports multiple skill levels.

## Decision

Frame the project as a media verification assistant.

The initial MVP should focus on one media type, recommended as images unless research suggests otherwise. The product should generate an evidence-backed confidence report instead of a binary truth label.

## Consequences

Positive:

- Easier to ship a vertical slice.
- Leaves room for frontend, backend, ML, data, evaluation, safety, and docs contributors.
- More honest than claiming to solve deepfake detection.
- Easier to expand into video, provenance, and social link workflows later.

Negative:

- Some contributors may want video or social-post detection immediately.
- The first MVP may feel less ambitious than the full idea.
- Research must still clarify which baseline detector and datasets are practical.

## Open Questions

- Should the MVP be image-only or image-first with a video roadmap?
- Which baseline detector has the best license/setup tradeoff?
- Should public demo uploads be disabled, ephemeral, or local-only at first?

