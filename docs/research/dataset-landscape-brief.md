# Dataset Landscape Brief

Status: Draft

Related story: CL-014

Last updated: 2026-05-03

## Purpose

This brief gives the project leads a practical first map of common deepfake and synthetic-media datasets. The goal is not to choose a training dataset yet. The goal is to understand what each dataset is useful for, where it is risky or expensive, and which datasets are realistic for an early MVP.

## Summary Recommendation

For the first MVP, do not download large video datasets yet. Use DFDC, FaceForensics++, Celeb-DF, and WildDeepfake as research and evaluation background while the team clarifies the MVP media type, storage budget, compute budget, access terms, and data governance plan.

If the MVP becomes image-first, GenImage and the Unbiased GenImage work are more directly relevant than video face-swap datasets, but they are still large and have important bias caveats. Published findings may be enough for early planning.

Most important takeaway: dataset choice changes the meaning of any detector result. A model that works on one dataset may fail on another because of compression, resolution, generator type, face-cropping, source distribution, or hidden benchmark design.

## Dataset Landscape

| Dataset | Media Type | Main Use | Scale | Access and Terms | Strengths | Weaknesses | Known Bias / Preprocessing Caveats | MVP Practicality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DFDC | Face-swap video | Large-scale deepfake video detection benchmark | Paper reports 128,154 total videos and 104,500 unique fake videos; Meta page describes 124k videos and 8 facial modification algorithms; 3,426 paid actors | Official Meta dataset page; access requires AWS setup and terms review | Large, challenge-backed, multiple manipulation methods, consenting paid actors, public/private test split history | Video-focused, operationally heavy, likely storage/compute expensive, competition methods can be complex ensembles | Public leaderboard performance can overstate private/generalized performance; augmentations and realistic transformations affect results; prevalence and false positives matter | Important background, not a first-MVP dependency unless the team explicitly chooses video and data infrastructure |
| FaceForensics++ | Face-manipulation video and extracted images | Standard facial manipulation benchmark for classification and segmentation | 1,000 original video sequences from 977 YouTube videos; manipulated with Deepfakes, Face2Face, FaceSwap, and NeuralTextures; paper describes a hidden test set and more than 1.8 million manipulated images | Download access by form; data under FaceForensics terms of use; code under MIT license | Widely cited, benchmark-oriented, includes compression-aware evaluation and binary masks for segmentation | Constrained mostly frontal face videos; older manipulation methods; not a general misinformation dataset | Models can overfit to benchmark methods, face crops, source distribution, and compression levels; YouTube source data raises terms/ethics questions | Strong background dataset; possible later benchmark reference, but probably too video/face-specific for an image verification MVP |
| Celeb-DF v2 | Celebrity face-swap video | Harder high-quality deepfake video evaluation | 590 original celebrity videos, 5,639 synthesized DeepFake videos, and 300 YouTube-real videos | Access requires request/form approval; terms must be reviewed before use | Designed to be more visually challenging than earlier datasets; useful for cross-dataset generalization discussions | Celebrity/source-video focus; controlled access; face-swap video only; not a provenance or metadata dataset | Celebrity and YouTube source distribution may not match user-submitted media; high-quality examples expose detector brittleness | Good research reference; unlikely first-MVP dependency |
| WildDeepfake | Face sequences extracted from internet deepfake videos | In-the-wild deepfake robustness testing | 7,314 face sequences from 707 internet-sourced deepfake videos | Agreement/form required; repository says dataset is available through Hugging Face and is research-only with access controls | More realistic internet distribution than lab-created videos; smaller than DFDC; explicitly targets real-world detector degradation | Internet-sourced media creates ethics/privacy and source-quality concerns; manipulation methods and actor details are less controlled | Source distribution is opaque; released as face sequences rather than full videos; may not represent broad media verification or provenance cases | Useful for understanding real-world domain shift; not a first download without ethics and terms review |
| GenImage / Unbiased GenImage | Generated still images | AI-generated image detection and cross-generator robustness | GenImage is million-scale with real ImageNet images and generated images from models including Midjourney, Stable Diffusion, ADM, GLIDE, Wukong, VQDM, and BigGAN; Unbiased GenImage download notes cite roughly 500 GB | Project/GitHub download links; original dataset and derived metadata terms need review | Image-first; includes multiple generators; directly relevant if MVP includes generated-image detection rather than video face swaps | Large; not a face-swap dataset; ImageNet/class-prompt setup may not match real social-media media | Fake-or-JPEG work shows raw generated-image datasets can contain JPEG compression and image-size shortcuts; cross-generator and degraded-image tests are critical | Best conceptual fit for image-generation detection, but published findings may be enough before downloading data |

## What This Means For The MVP

For a first MVP, the safest path is to separate "research dataset knowledge" from "MVP dataset dependency."

Recommended early stance:

- Use published dataset papers and benchmark findings to shape claims, limitations, and evaluation design.
- Do not promise a trained detector until the team chooses a narrow media type and evaluation setup.
- Avoid large video datasets until storage, compute, access terms, and privacy handling are explicit.
- If the MVP is image-first, prioritize small, auditable experiments around metadata/provenance checks and carefully scoped detector signals.
- Treat detector output as one evidence signal, not an authenticity verdict.

## Dataset Questions To Track

Use these questions before adopting any dataset:

- What media type does it cover: still image, face crop, full video, audio, screenshot, or metadata?
- What task does it support: generated-image detection, face-swap video detection, manipulation localization, provenance validation, or OSINT context?
- How was the real media collected?
- Were subjects consenting, paid, public figures, scraped from the web, or unknown?
- What are the access terms, redistribution limits, and license constraints?
- How large is the dataset, and what storage/compute would be required?
- Are train/test splits public, hidden, cross-dataset, or private?
- What compression, resizing, re-encoding, or social-media transformations are represented?
- Could a model exploit shortcuts such as JPEG quality, image dimensions, face crops, watermarks, or source platform artifacts?
- Would use of the dataset be explainable and acceptable for an open learner project?

## Follow-Up Stories

### CL-014A: Verify Dataset Access And Terms

As a co-lead, I want a terms/access table so the team does not accidentally plan around data it cannot use.

Acceptance criteria:

- [ ] Check current access requirements for DFDC, FaceForensics++, Celeb-DF v2, WildDeepfake, and GenImage.
- [ ] Record license or terms-of-use links.
- [ ] Mark whether redistribution, public demos, and derived artifacts are allowed.
- [ ] Identify any academic-email or approval requirements.
- [ ] Do not download datasets.

Suggested output:

`docs/research/dataset-access-and-terms.md`

### CL-014B: Choose MVP Dataset Strategy

As a co-lead, I want to decide whether the MVP needs a dataset at all so the team can avoid premature data work.

Acceptance criteria:

- [ ] Decide whether MVP v0 uses published benchmark findings only, a tiny curated sample set, or an approved public dataset subset.
- [ ] State which media type the MVP covers first.
- [ ] State which datasets are out of scope for the first 3 months.
- [ ] Identify required data governance work before any upload or dataset download.

Suggested output:

`docs/decisions/ADR-0002-mvp-dataset-strategy.md`

### CL-014C: Add Dataset Bias Fields To Future Tables

As a co-lead, I want every dataset table to include preprocessing and bias fields so detector claims are not overinterpreted.

Acceptance criteria:

- [ ] Add fields for compression, resizing, source distribution, media transformations, and train/test split design.
- [ ] Include a note from the Fake-or-JPEG paper about JPEG and image-size shortcuts.
- [ ] Include a note from DFDC/OpenMFC about hidden or private test sets.
- [ ] Draft one limitation sentence to reuse in product/report language.

Suggested output:

`docs/research/dataset-evaluation-fields.md`

## Source Notes

- DFDC: see `docs/research/dfdc-dataset-notes.md` and SRC-021.
- FaceForensics++: see SRC-022.
- Celeb-DF v2: see `docs/research/celeb-df-dataset-notes.md` and SRC-017.
- WildDeepfake: see SRC-023.
- GenImage / Unbiased GenImage: see `docs/research/generated-image-dataset-bias-notes.md`, SRC-020, and SRC-024.
