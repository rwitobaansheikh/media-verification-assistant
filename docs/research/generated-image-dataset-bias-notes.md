# Generated Image Dataset Bias Notes

Status: Draft

Source:

- Title: Fake or JPEG? Revealing Common Biases in Generated Image Detection Datasets
- Authors: Patrick Grommelt, Louis Weiss, Franz-Josef Pfreundt, Janis Keuper
- Venue/status: arXiv preprint
- arXiv: https://arxiv.org/abs/2403.17608
- PDF: https://arxiv.org/pdf/2403.17608
- DOI: https://doi.org/10.48550/arXiv.2403.17608
- Project page: https://www.unbiased-genimage.org/
- Code repository: https://github.com/gendetection/UnbiasedGenImage
- Local PDF reviewed from: `2403.17608v2.pdf`

## Why This Source Matters

This paper is directly relevant to dataset selection, detector evaluation, compression robustness, and MVP confidence language.

It shows that AI-generated image detectors may learn shortcuts from dataset artifacts rather than genuine generation-specific signals. In particular, natural images and generated images may differ in JPEG compression and image dimensions. A detector can then become partly a JPEG detector or size-distribution detector while appearing to solve synthetic-image detection.

## Core Research Question

How much of a generated-image detector's performance comes from real generation artifacts, and how much comes from unintended dataset bias such as compression format, JPEG quality, or image size?

## Reported Study Design

Based on the arXiv paper and project page, the study:

- analyzes generated-image detection datasets, especially GenImage;
- studies JPEG compression bias and image-size distribution bias;
- trains/evaluates ResNet50 and Swin-T detectors;
- compares raw GenImage training with constrained data designed to reduce compression and size bias;
- reports improved cross-generator performance and robustness after reducing those biases;
- provides project code and metadata for an "Unbiased GenImage" workflow.

## Key Lessons

- Dataset construction can create hidden shortcuts.
- Natural images and generated images should have similar compression and size distributions when used for detector training/evaluation.
- A high detector score may reflect file-format or preprocessing differences rather than true synthetic-media evidence.
- Compression can cause generated images to be classified as natural by biased detectors.
- Random JPEG augmentation can help, but it may not fully remove compression bias.
- Cross-generator evaluation is more meaningful when obvious dataset biases are controlled.

## MVP Implications

- Do not rely on detector benchmark numbers unless the evaluation explains preprocessing, compression, image size, and source distribution.
- Record whether a candidate detector was evaluated against JPEG compression, resizing, and generator shift.
- Treat uploaded screenshots, resized images, and recompressed social-media images as harder cases.
- If the MVP includes an AI-generated image detector, the evidence report should state that compression and resizing can affect results.
- Dataset landscape work should include "known biases and preprocessing caveats," not just dataset size and access.

## Product Language Implications

Prefer:

- "This score may be affected by compression, resizing, and upload history."
- "The model was evaluated under specific dataset and preprocessing conditions."
- "This is a model signal, not a final authenticity judgment."

Avoid:

- "The detector can identify AI-generated images reliably in the wild."
- "High benchmark accuracy means this result is trustworthy."
- "JPEG compression has no effect on this result."

## Relevance To Current Backlog

- CL-014 dataset landscape: include dataset bias and preprocessing caveats.
- CL-015 detector landscape: ask whether detector claims were tested under compression and resizing.
- CL-016 cross-dataset generalization: use as image-generation analogue to cross-dataset detector brittleness.
- CL-017 compression and re-upload effects: this is a strong starting source.

## Risks and Caveats

- This is an arXiv preprint, not a peer-reviewed venue record in the source log.
- The study is about AI-generated image detection, not face-swap video deepfake detection.
- It uses GenImage and specific baseline detectors, so findings should not be generalized without care.
- The dataset and code are large and not practical for a first MVP experiment without a deliberate data plan.

## Follow-Up Questions

- Which candidate detectors report robustness under JPEG compression and resizing?
- Do existing detector demos disclose compression sensitivity?
- Can we create a tiny local sanity test with safe sample images and controlled JPEG compression?
- Should the evidence report include a "file processing caveat" for all detector outputs?
- Should dataset landscape rows include compression format, image size, and preprocessing notes?

## Candidate Follow-Up Story

Title: Add compression and dataset-bias caveats to detector evaluation

As a project co-lead, I want detector evaluation notes to include compression and image-size bias so the team does not overtrust benchmark results.

Acceptance criteria:

- [ ] Add a "known dataset/preprocessing biases" field to the dataset landscape brief.
- [ ] Add a "compression/resizing robustness" field to the detector landscape brief.
- [ ] Summarize this paper in 5 bullets.
- [ ] Write one MVP report limitation statement about compression and resizing.
- [ ] Propose one small future robustness test.

Suggested outputs:

- `docs/research/dataset-landscape-brief.md`
- `docs/research/detector-landscape-brief.md`
- `docs/research/compression-and-reupload-effects.md`
