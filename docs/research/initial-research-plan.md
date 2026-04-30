# Initial Research Plan

The research goal is to make the MVP decision defensible. The team does not need a full academic survey before building, but it does need enough evidence to avoid vague scope and inflated claims.

## Research Principles

- Prefer primary sources: papers, official dataset pages, standards docs, maintained repos, and benchmark reports.
- Use AI research tools as accelerators, not as sources of truth.
- Capture citations and retrieval dates for every factual claim.
- Separate "what the source says" from "our interpretation."
- Record license, consent, and access constraints for datasets and model weights.
- Treat any result from Perplexity, Gemini Deep Research, ChatGPT Deep Research, or similar tools as a draft that needs verification.

## Recommended Research Methods

### AI-Assisted Literature Review

Use one or more deep research tools to produce draft surveys, then verify claims against primary sources.

Useful prompts:

- "Find recent surveys and benchmarks on image and video deepfake detection. Prioritize papers with cross-dataset evaluation and robustness analysis."
- "Compare open-source deepfake detection repositories by license, maintenance, supported media type, setup difficulty, and model architecture."
- "Summarize C2PA, Content Credentials, and watermarking approaches for media provenance. Distinguish provenance from detection."

### Manual Source Verification

For each candidate source:

- check publication date or commit activity;
- check license and usage terms;
- check whether code or data is available;
- check if results are in-domain for the MVP;
- check whether evaluation is cross-dataset or only in-distribution.

### Expert Interviews

If the group can reach experts, prioritize:

- digital forensics researchers;
- journalists or fact-checkers who handle manipulated media;
- trust and safety practitioners;
- cybersecurity or incident response people familiar with evidence workflows;
- C2PA/content provenance practitioners;
- ML researchers who work on robustness and calibration.

Interview goals:

- learn actual user workflows;
- identify common failure modes;
- understand what evidence users trust;
- learn what claims are legally or ethically risky;
- identify useful demo scenarios.

## Research Briefs to Produce

### R-001: Problem Taxonomy

Question: What exactly are we detecting or reporting on?

Output:

- glossary of key terms;
- MVP scope recommendation;
- list of terms the product should avoid or qualify.

### R-002: Existing Detector Landscape

Question: What has already been built, and what can we reuse?

Output:

- 3-5 open-source detectors summarized;
- model type, media type, license, setup difficulty, maintenance status;
- recommendation for one baseline candidate.

### R-003: Dataset Inventory

Question: What data can we legally and practically use for evaluation?

Output:

- dataset table with media type, size, access, license/terms, strengths, weaknesses;
- blocked/uncertain datasets flagged;
- recommendation for MVP evaluation sample.

### R-004: Detection Methods

Question: Which methods are credible enough to consider?

Output:

- summary of CNN/Xception/ResNet baselines, vision transformers, frequency methods, temporal methods, audio-video sync, metadata/provenance, and ensembles;
- recommendation for MVP and post-MVP methods.

### R-005: Evaluation Plan

Question: How do we know if the system is useful and honest?

Output:

- proposed metrics;
- false-positive and false-negative risk analysis;
- robustness tests for compression, resizing, and social-media re-encoding;
- threshold and calibration plan.

### R-006: Provenance and C2PA

Question: How should provenance fit into a verification assistant?

Output:

- what provenance can prove;
- what missing provenance cannot prove;
- library/API options;
- MVP recommendation.

### R-007: Safety, Privacy, and Legal Risk

Question: What must we avoid before public demo?

Output:

- responsible-use notes;
- uploaded media retention recommendation;
- disclaimer language;
- abuse cases;
- data handling rules.

## Research Definition of Done

Each brief should include:

- author;
- date;
- question answered;
- sources with links;
- summary;
- implications for MVP;
- unresolved questions;
- recommended issues to create.

