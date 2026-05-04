# Synthetic Performance Ethics Notes

Status: Draft

Source:

- Title: AI and Actors: Ethical Challenges, Cultural Narratives and Industry Pathways in Synthetic Media Performance
- Author: Sarah Thomas
- Venue: Emerging Media, volume 2, issue 3, pages 523-546
- First published online: October 8, 2024
- DOI: https://doi.org/10.1177/27523543241289108
- SAGE full text: https://journals.sagepub.com/doi/full/10.1177/27523543241289108
- University of Liverpool repository record: https://livrepository.liverpool.ac.uk/id/eprint/3184938
- Local PDF reviewed from: `thomas-2024-ai-and-actors-ethical-challenges-cultural-narratives-and-industry-pathways-in-synthetic-media-performance.pdf`

## Why This Source Matters

This article is not a detector, dataset, or provenance-standards source. It is useful for the safety and responsible-use side of the project because it explains synthetic media as a question of identity, consent, labor, rights, and public trust.

For our project, the article helps prevent a narrow framing where synthetic media is only a technical detection problem. People whose likenesses, voices, or performances are copied can be harmed even when the media is not part of political misinformation or news verification.

## Core Ideas

The article focuses on synthetic performance in entertainment, especially screen and audio performers. It argues that responsible AI principles such as transparency, accountability, fairness, and consent can become too abstract unless they are tied to real workflows, contracts, power dynamics, and affected people.

Important distinctions:

- A synthetic performance may imitate a specific person's identity, voice, likeness, gesture, or brand.
- Synthetic media can be fraudulent or exploitative even when it is technically impressive.
- Stars and famous performers may have more bargaining power than ordinary performers, so protections can be uneven.
- Responsible AI needs stakeholders in the middle of the workflow, not only developers and end users.

## Relevance To This Project

This project is not trying to generate synthetic actors or manage entertainment-industry licensing. Still, the article is relevant because our media verification assistant may analyze media depicting real people.

Practical implications:

- Treat a person's likeness or voice as sensitive, even when the file is publicly available.
- Avoid turning identity harm into only a binary fake/real classification.
- Include consent and misuse as part of the safety discussion.
- Avoid product language that implies we can settle legal, labor, or rights questions.
- Consider performer/personhood harm in the risk register, not only misinformation harm.

## MVP Implications

- The MVP should not invite users to upload private, intimate, or non-consensual media.
- The MVP should not claim whether a person consented to the media.
- The MVP should avoid storing uploads unless there is an explicit retention plan.
- The evidence report should be careful when media depicts identifiable people.
- If example images are used, they should be public-domain, licensed, synthetic with consent, or otherwise clearly safe for demo use.

## Safety and Governance Implications

Potential risk-register items:

- The app could be used to scrutinize or target private individuals.
- Users could upload media involving non-consensual impersonation or harassment.
- A false positive could harm a person's reputation or work.
- A false negative could validate exploitative synthetic media.
- Public demo examples could accidentally normalize misuse if chosen poorly.

Potential mitigations:

- Add upload guidance before any public demo.
- Avoid storing uploads by default.
- Use cautious report language.
- Include "not a consent or rights determination" in relevant documentation.
- Use safe sample media only.

## What This Source Should Not Decide

- It should not decide the MVP architecture.
- It should not force the MVP into audio/video performer-rights analysis.
- It should not be treated as legal advice.
- It should not replace primary sources on C2PA, datasets, model evaluation, or privacy law.

## Follow-Up Questions

- Should our project have a short "media upload policy" before a demo exists?
- What kinds of sample media are safe for tutorials and screenshots?
- Should the evidence report include a warning when media appears to depict an identifiable person?
- Who could we interview about consent, harassment, or synthetic identity harms?
- Which risks from this article belong in `docs/risk-register.md`?

## Candidate Follow-Up Story

Title: Add identity and consent risks to the risk register

As a project co-lead, I want the risk register to include synthetic identity harms so the project does not treat media verification as only a technical detection problem.

Acceptance criteria:

- [ ] Add at least 3 risks related to identity, likeness, consent, or performer/personhood harm.
- [ ] Add mitigations for upload guidance, storage, demo samples, and report wording.
- [ ] Mark which risks matter before a public demo.
- [ ] Reference this note and the Partnership on AI synthetic media framework.

Suggested output:

`docs/risk-register.md`
