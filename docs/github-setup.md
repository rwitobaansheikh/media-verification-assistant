# GitHub Setup and No-Cost Protections

## Assumption

This checklist assumes a public GitHub repository on GitHub Free or GitHub Free for organizations. That matters because several protections are free for public repositories, while private repositories can require paid plans for equivalent protection.

## Recommendation

Use a GitHub organization if possible. An organization gives the project better continuity and cleaner access control than a personal repo. Keep organization base permissions low, then grant higher access only to maintainers who need it.

Minimum governance:

- at least two trusted owners/admins;
- public repository;
- default branch named `main`;
- contributors use pull requests;
- raw meeting transcripts, recordings, uploaded media, secrets, datasets, and model weights are not committed.

## Current Free Options to Use

Verified against GitHub Docs on 2026-04-30:

- Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations.
- Rulesets are available in public repositories with GitHub Free and GitHub Free for organizations.
- CODEOWNERS is available in public repositories with GitHub Free and can be paired with branch protection.
- GitHub Actions standard hosted runners are free for public repositories.
- Code scanning is available for public repositories on GitHub.com.
- Secret scanning runs automatically for public repositories, and user alerts can be enabled on free public repositories.
- Dependabot alerts are available for organization-owned and user-owned repositories.

Sources:

- GitHub Docs, protected branches: https://docs.github.com/github/administering-a-repository/about-branch-restrictions
- GitHub Docs, rulesets: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets
- GitHub Docs, CODEOWNERS: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners
- GitHub Docs, organization base permissions: https://docs.github.com/organizations/managing-access-to-your-organizations-repositories/setting-base-permissions-for-an-organization
- GitHub Docs, Actions billing: https://docs.github.com/en/billing/managing-billing-for-github-actions/about-billing-for-github-actions
- GitHub Docs, code scanning: https://docs.github.com/en/code-security/concepts/code-scanning/about-code-scanning
- GitHub Docs, secret scanning alerts: https://docs.github.com/en/code-security/concepts/secret-security/about-alerts
- GitHub Docs, Dependabot alerts: https://docs.github.com/en/code-security/concepts/supply-chain-security/about-dependabot-alerts

## Setup Checklist

### 1. Create or Choose the Owner

Preferred:

- Create a GitHub organization for the project.
- Add both co-leads as owners.
- Set organization base permissions to Read.

Acceptable for a very small start:

- Use a personal public repo.
- Add co-lead as collaborator/admin-equivalent where possible.
- Plan a later transfer to an organization if the team grows.

### 2. Create the Repository

Recommended settings:

- Visibility: Public.
- Default branch: `main`.
- Initialize with README if creating on GitHub first, or push this local scaffold after `git init`.
- Disable unused features if they become noise.
- Enable Issues.
- Enable Discussions only if the group wants GitHub to be the discussion hub.
- Enable "Automatically delete head branches" after PR merge.

### 3. Add Branch Rule or Ruleset for `main`

Use either branch protection or a repository ruleset. Rulesets are more discoverable and can layer cleanly, but classic branch protection is also fine.

Initial rule:

- Target: `main`.
- Require a pull request before merging.
- Require at least 1 approval.
- Dismiss stale approvals when new commits are pushed.
- Require conversation resolution before merging.
- Block force pushes.
- Block branch deletion.
- Do not allow bypasses except emergency maintainers.
- Require status checks after CI exists.

Do not require a status check before the workflow exists and has passed at least once. Otherwise, you can block all merges by requiring a nonexistent check.

Later, once the maintainer pool is large enough:

- Increase required approvals to 2 for sensitive areas.
- Require review from CODEOWNERS.
- Require linear history if the team agrees on squash/rebase workflow.
- Require signed commits only if contributors are comfortable setting that up.

### 4. Create CODEOWNERS

Start with comments or broad ownership until GitHub usernames are known. Once maintainers are known, add actual owners and enable "Require review from Code Owners" in the branch rule.

Recommended ownership areas:

- `.github/` owned by co-leads or infra maintainers.
- `docs/safety` or safety docs owned by safety/privacy maintainers.
- backend owned by backend maintainers.
- frontend owned by frontend maintainers.
- model/evaluation code owned by ML/data maintainers.

### 5. Enable Security Features

In repository settings:

- Enable Dependabot alerts.
- Enable Dependabot security updates if available.
- Enable secret scanning alerts for users.
- Enable secret scanning push protection if available for the repo.
- Add CodeQL/code scanning once code exists.

### 6. Add Issue and PR Workflow

Create:

- bug report template;
- feature request template;
- research task template;
- PR template;
- labels from [BACKLOG.md](../BACKLOG.md);
- project board with Backlog, Ready, In Progress, Review, Done.

Recommended process:

1. Every task starts as an issue.
2. Contributors comment before starting work.
3. Maintainers assign the issue or acknowledge ownership.
4. PRs link the issue.
5. PRs stay small enough to review.

### 7. Keep Costs at Zero

- Use public GitHub Actions standard runners.
- Keep CI short and avoid large artifacts.
- Do not upload datasets or model weights to the repo.
- Prefer small sample fixtures.
- Use local development first.
- Require explicit maintainer approval before any cloud resource creates cost risk.

## First Repo Creation Command Path

If creating locally first:

```powershell
git init
git branch -M main
git add README.md PROJECT_PLAN.md BACKLOG.md CONTRIBUTING.md SECURITY.md .gitignore .github docs
git commit -m "Initialize project planning scaffold"
```

Then create the public GitHub repo, add the remote, push, and configure protections in the GitHub UI.

Do not run `git add .` until the raw transcript files are ignored or moved out of the public repo path.

