# DFDC Dataset Notes

Status: Draft

Source:

- Title: The DeepFake Detection Challenge (DFDC) Dataset
- Authors: Brian Dolhansky, Joanna Bitton, Ben Pflaum, Jikuo Lu, Russ Howes, Menglin Wang, Cristian Canton Ferrer
- Organization: Facebook AI
- Venue/status: arXiv preprint
- arXiv: https://arxiv.org/abs/2006.07397
- PDF: https://arxiv.org/pdf/2006.07397
- DOI: https://doi.org/10.48550/arXiv.2006.07397
- Official dataset page: https://ai.meta.com/datasets/dfdc/
- Local PDF reviewed from: `2006.07397v4.pdf`

## Why This Source Matters

DFDC is one of the core datasets named in CL-014. It is a large face-swap video dataset created for the DeepFake Detection Challenge and Kaggle competition.

For this project, DFDC matters because it shows how serious deepfake detector evaluation becomes once scale, consent, hidden test sets, real-world distribution shift, augmentations, and false positives are considered.

## Dataset Summary

Based on the arXiv paper and Meta dataset page:

- The full DFDC dataset has more than 100,000 videos.
- Meta's dataset page describes the full dataset as 124k videos with eight facial modification algorithms.
- The paper describes 128,154 total videos and 104,500 unique fake videos.
- The source data came from 3,426 paid actors.
- Participants agreed to appear in a dataset where their likenesses could be manipulated.
- The challenge used public and private test sets, with the private set intended to better evaluate generalization.
- Access requires AWS setup and account details.

## What Makes It Useful

- Larger scale than many earlier deepfake datasets.
- Includes multiple face-swap and manipulation methods.
- Includes consenting paid actors, which is ethically important compared with datasets based on scraped public figures.
- Includes augmentations and distractors intended to make evaluation more realistic.
- The competition structure created a large benchmark history with thousands of submissions.

## What Makes It Hard

- It is video-focused, while the first MVP may be image-first.
- It is large and operationally heavy.
- Access requires AWS setup and likely significant storage/transfer planning.
- Many winning approaches used expensive training, ensembles, face detection, and video/frame pipelines.
- The public leaderboard alone did not fully reflect private/black-box performance.

## Evaluation Lessons

- Hidden/private test sets are valuable because public benchmark performance can overstate real-world readiness.
- Log loss can rank competition submissions, but precision and false positives matter more in realistic low-prevalence settings.
- Accuracy alone is not enough when manipulated media is rare compared with authentic media.
- Augmentations such as blur, encoding changes, resolution changes, overlays, filters, noise, and frame-rate changes affect detector performance.
- Top models can perform substantially worse on more realistic or private distributions than on public benchmark data.

## MVP Relevance

- Good source for the dataset landscape brief.
- Good source for evaluation-metric thinking.
- Good source for the risk register around consent and dataset ethics.
- Good source for explaining why video deepfake detection is likely beyond the first MVP.
- Not a practical first MVP dependency unless the team explicitly plans for storage, compute, access, and data governance.

## Product Language Implications

Prefer:

- "Detector performance depends on the evaluation set, prevalence assumptions, and media transformations."
- "A detector can be useful as an evidence signal even if deepfake detection remains unsolved."
- "False positives matter because real-world manipulated media may be rare compared with authentic media."

Avoid:

- "A strong leaderboard score means the detector is reliable in the wild."
- "Video deepfake detection is solved."
- "A dataset is safe to use just because it is publicly available."

## Follow-Up Questions

- What are DFDC's current access and use terms?
- How much storage and compute would be needed to use even a small subset?
- Can published DFDC benchmark findings be enough for initial planning without downloading data?
- Which evaluation metrics should the MVP borrow from DFDC and OpenMFC?
- Should the dataset landscape mark DFDC as "important but not first-MVP practical"?

## Candidate Follow-Up Story

Title: Add DFDC to dataset landscape brief

As a project co-lead, I want to summarize DFDC in the dataset landscape so the team understands its importance and why it may be too heavy for first MVP work.

Acceptance criteria:

- [ ] Summarize media type, scale, source/consent model, and access process.
- [ ] Explain why the private test set and competition results matter.
- [ ] Identify storage, compute, and governance barriers.
- [ ] Mark whether DFDC is practical for MVP evaluation.
- [ ] Link this note from `docs/research/dataset-landscape-brief.md`.
