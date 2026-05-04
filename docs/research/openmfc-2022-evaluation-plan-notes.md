# OpenMFC 2022 Evaluation Plan Notes

Status: Draft

Source:

- NIST publication page: https://www.nist.gov/publications/open-media-forensics-challenge-2022-evaluation-plan
- OpenMFC site: https://mfc.nist.gov/
- Local PDF reviewed from: `OpenMFC2022EvaluationPlan.pdf`

## Why This Source Matters

The Open Media Forensics Challenge (OpenMFC) is a primary source for how a formal media forensics evaluation defines tasks, inputs, outputs, metrics, and submission protocols. It is useful for shaping our evaluation plan even if our MVP is much smaller.

NIST describes the OpenMFC 2022 Evaluation Plan as covering resources, task definitions, task conditions, file formats for system inputs and outputs, evaluation metrics, scoring procedures, and submission protocols.

## Relevant OpenMFC Task Categories

OpenMFC 2022 includes three task categories:

- Manipulation Detection (MD)
- Deepfakes Detection (DD)
- Steganography Detection (StegD)

The most relevant categories for our project are Manipulation Detection and Deepfakes Detection.

## Image-Relevant Tasks

### Image Manipulation Detection

The system determines whether an image has been manipulated and may spatially localize edited regions.

MVP implication:

- This is broader than deepfake detection.
- It supports the idea that the assistant should report manipulation evidence, not just synthetic-media likelihood.

### Image Splice Manipulation Detection

OpenMFC added an image-splice task intended to support entry-level public participants.

MVP implication:

- This is a useful reference for a small image-first task because it is narrower than full media verification.
- A splice-focused or image-manipulation-focused demo may be easier than a broad multimodal deepfake detector.

### Image Deepfakes Detection

The task evaluates whether a system can detect deepfaked or GAN-manipulated images while not confusing those with other manipulation types.

MVP implication:

- This supports separating different suspicious-media categories in the report.
- The MVP should avoid treating every manipulation as a deepfake.

## Evaluation Conditions

For image tasks, OpenMFC evaluation conditions use image pixel content only and exclude image headers or other metadata.

MVP implication:

- Our product can still use metadata and provenance, but model evaluation should distinguish pixel-only detector performance from metadata/provenance evidence.
- The report should separate "forensic model signal" from "metadata/provenance signal."

## Metrics To Consider

OpenMFC emphasizes:

- AUC for detection performance;
- Correct Detection Rate at a fixed false alarm rate;
- Matthews Correlation Coefficient for localization performance.

MVP implication:

- ROC-AUC is a reasonable model-level metric.
- A fixed low false-positive operating point is especially relevant for product safety.
- Localization metrics are useful only if the MVP attempts manipulated-region masks or heatmaps.

## What To Borrow For Our MVP

- Define tasks narrowly before evaluating.
- Separate detection from localization.
- Separate image, video, and deepfake-specific tasks.
- Require confidence scores for every probe/example.
- Report performance at low false-positive rates, not only global accuracy.
- Keep evaluation conditions explicit.

## What Is Too Heavy For Our MVP

- Full leaderboard infrastructure.
- Multiple media categories at once.
- Steganography detection.
- Formal localization scoring unless we choose a localization-capable baseline.
- Large controlled challenge datasets before the project has a working vertical slice.

## Open Questions

- Should our first evaluation be image manipulation detection, image deepfake detection, or simply report-schema validation with a baseline stub?
- Do we want a pixel-only detector benchmark separate from metadata/provenance report checks?
- Which metric should become the first "must report" MVP metric: ROC-AUC, precision/recall at a chosen threshold, or low-FPR operating behavior?

