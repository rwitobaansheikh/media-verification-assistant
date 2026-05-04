# Celeb-DF Dataset Notes

Status: Draft

Source:

- Title: Celeb-DF: A Large-Scale Challenging Dataset for DeepFake Forensics
- Authors: Yuezun Li, Xin Yang, Pu Sun, Honggang Qi, Siwei Lyu
- Venue: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 2020
- DOI: https://doi.org/10.1109/CVPR42600.2020.00327
- CVF open access page: https://openaccess.thecvf.com/content_CVPR_2020/html/Li_Celeb-DF_A_Large-Scale_Challenging_Dataset_for_DeepFake_Forensics_CVPR_2020_paper.html
- Official project page: https://cse.buffalo.edu/~siweilyu/celeb-deepfakeforensics
- Official GitHub repository: https://github.com/yuezunli/celeb-deepfakeforensics
- Local PDF reviewed from: `Li_Celeb-DF_A_Large-Scale_Challenging_Dataset_for_DeepFake_Forensics_CVPR_2020_paper.pdf`

## Why This Source Matters

Celeb-DF is one of the named datasets in CL-014 and appears repeatedly in cross-dataset generalization papers. It is important because it was designed to be more visually challenging than earlier DeepFake datasets.

For the project, Celeb-DF is useful less as an immediate download target and more as a reference point for why detector evaluation needs harder, more realistic test conditions.

## Dataset Summary

Based on the official project page and GitHub repository:

- Celeb-DF v2 includes 590 original celebrity videos collected from YouTube.
- It includes 5,639 corresponding synthesized DeepFake videos.
- The repository also lists 300 additional YouTube-real videos.
- The dataset structure includes `Celeb-real`, `YouTube-real`, `Celeb-synthesis`, and a test-video list.
- Access requires submitting a form and waiting for approval.

## What Makes It Challenging

The paper and project page frame Celeb-DF as a response to earlier datasets whose artifacts were easier to detect and less representative of DeepFake videos seen online.

Important challenge factors:

- higher visual quality than some earlier datasets;
- fewer obvious visual artifacts;
- celebrity face videos rather than generic image manipulation;
- stronger relevance to face-swap detector evaluation than to broad media verification.

## MVP Relevance

- Useful for the dataset landscape brief.
- Useful as an example of why in-dataset benchmark performance can overstate real-world detector reliability.
- Useful for explaining why FaceForensics++-trained detectors may perform differently on Celeb-DF.
- Not a likely first MVP dependency unless the team creates a data-handling and access plan.

## Limitations For Our Project

- It is a face-based video deepfake dataset, while the first MVP may focus on image media verification.
- It is not a provenance dataset and does not directly address C2PA or metadata evidence.
- Dataset access is controlled; terms and allowed uses must be reviewed before any download.
- It contains celebrity/source videos from YouTube, so ethical and privacy considerations matter.
- It is not a general misinformation dataset and does not cover cheapfakes, captions, context, or source verification.

## Product Language Implications

Celeb-DF reinforces this wording principle:

Do not say a detector is reliable just because it performs well on one benchmark. Explain what kind of media and evaluation conditions the model has been tested on.

Potential report wording:

- "This detector's reliability depends on how similar the submitted media is to its training and evaluation data."
- "High-quality face-swap videos can be harder for detectors than visibly artifact-heavy examples."
- "This result is one model signal and should be combined with other evidence."

## Follow-Up Questions

- What are the current Celeb-DF access terms?
- Are there license or redistribution restrictions that would prevent open-source reproduction?
- Can the team use published benchmark numbers without downloading the dataset?
- If the MVP is image-first, should Celeb-DF stay as background research rather than an evaluation dependency?
- What smaller, easier-to-access dataset could be used for a first evaluation dry run?

## Candidate Follow-Up Story

Title: Add Celeb-DF to dataset landscape brief

As a project co-lead, I want to summarize Celeb-DF in the dataset landscape so the team understands why it is useful but probably not a first MVP dependency.

Acceptance criteria:

- [ ] Summarize media type, scale, and access process.
- [ ] Explain why Celeb-DF is considered challenging.
- [ ] Identify ethical, privacy, and terms-of-use questions.
- [ ] Mark whether it is practical for MVP evaluation.
- [ ] Link this note from `docs/research/dataset-landscape-brief.md`.
