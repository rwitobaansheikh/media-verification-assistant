# Broadcast Provenance Authentication Paper Notes

Status: Draft

Source:

- Title: Interoperable Provenance Authentication of Broadcast Media using Open Standards-based Metadata, Watermarking and Cryptography
- Authors: John C. Simmons, Joseph M. Winograd
- Organization: Verance Corporation
- Venue/status: arXiv preprint; listed as submitted to the IBC2024 Technical Papers Programme
- arXiv: https://arxiv.org/abs/2405.12336
- PDF: https://arxiv.org/pdf/2405.12336
- DOI: https://doi.org/10.48550/arXiv.2405.12336
- Local PDF reviewed from: `2405.12336v1.pdf`

## Why This Source Matters

This paper is relevant to the provenance side of the project. It argues that broadcast-media provenance needs both cryptographically authenticated metadata and durable audio/video watermarking, especially when broadcast content is clipped, transcoded, reposted, or stripped of container metadata.

For our project, the paper is useful because it separates several ideas that can otherwise get mixed together:

- provenance: where the media came from and how it moved through systems;
- authenticity: whether a posted item is a faithful representation of a trusted original;
- detection: whether a model finds evidence of manipulation or synthetic generation.

## Core Idea

The paper analyzes a broadcast-news-to-social-media scenario. A broadcaster produces content, someone posts a clip to a social platform, and the platform needs a way to validate whether the clip can be connected back to an authoritative source.

The paper argues that:

- C2PA-style cryptographic manifests can validate media and associated assertions;
- container-level metadata can be stripped or invalidated during ordinary platform processing;
- watermarks can help reconnect a media stream to authoritative metadata;
- watermarks should not be treated as the root of trust;
- retrieved metadata still needs cryptographic validation.

## Product-Relevant Lessons

- Provenance is not the same as a deepfake detector.
- Missing provenance should not be treated as evidence that media is fake.
- Failed cryptographic validation may indicate innocent editing, transcoding, clipping, or malicious alteration.
- A useful product should distinguish "not validated" from "validated as altered" and "model says suspicious."
- Any provenance check in the MVP should report what was checked, what was present, what was missing, and what cannot be concluded.

## C2PA and Watermarking Relationship

The paper's architecture treats watermarks as a durable lookup mechanism and cryptographic manifests as the source of trust.

Plain-language version:

- A C2PA manifest can say who created or modified media and can be cryptographically validated.
- A watermark can survive some transformations that strip ordinary metadata.
- The watermark can point a validator back to the relevant manifest or canonical media.
- The manifest, not the watermark alone, is what should be trusted after validation.

## Relevance To MVP Scope

This paper does not imply that the first MVP should implement broadcast watermarking or full C2PA validation. It does suggest that a future evidence report could have a provenance section with careful states such as:

- C2PA manifest found and validation passed;
- C2PA manifest found but validation failed;
- no C2PA manifest found;
- watermark/provenance lookup not supported;
- provenance unavailable, so no conclusion can be drawn from provenance.

For an image-first MVP, the most practical near-term step is probably to learn C2PA and maybe test existing tools on sample images before attempting any broadcast or live-video workflow.

## Risks and Caveats

- The paper is an arXiv/industry technical paper, not a standard specification.
- The authors are affiliated with a watermarking company, so product recommendations should be checked against independent standards and implementations.
- Broadcast provenance is broader and more complex than the first MVP.
- Watermarking infrastructure depends on adoption by content producers, platforms, and validators.
- Provenance can help answer source/history questions; it cannot prove that the original scene itself was true.

## Follow-Up Questions

- Which parts of C2PA can be tested with open-source tooling today?
- Can `c2patool` inspect the image formats likely to be used in the MVP?
- What should the UI say when no provenance data is found?
- Should the MVP include a "provenance unavailable" state from the beginning?
- Who could we interview about C2PA adoption in real workflows?

## Candidate Follow-Up Story

Title: Draft provenance states for the evidence report

As a project co-lead, I want simple provenance result states so the MVP can communicate provenance without overclaiming.

Acceptance criteria:

- [ ] Define at least 5 provenance states.
- [ ] For each state, describe what the app can conclude.
- [ ] For each state, describe what the app cannot conclude.
- [ ] Include wording for missing provenance.
- [ ] Reference C2PA and this broadcast-provenance paper.

Suggested output:

`docs/research/provenance-result-states.md`
