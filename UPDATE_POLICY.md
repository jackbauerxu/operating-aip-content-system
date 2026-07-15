# Skill Update Policy

## Workflow Contract

- Goal: detect changes in every public Skill project covered by this system and in every explicitly declared upstream.
- Trigger: weekly schedule or manual GitHub Actions dispatch.
- Inputs: `skill-sources.json` and public GitHub repository metadata.
- Outputs: a deterministic `upstream-lock.json` update and a pull request only when a tracked commit or Skill file changes.
- Project folder: this repository.
- Human review point: inspect the generated PR before any content integration.
- Quality checks: all configured repositories and Skill paths resolve; no source content is executed; no outside repository is written.
- Stop conditions: a repository/path cannot be read, a source is missing, or an update would require copying content across an unapproved licence boundary.

## What is automatic

The scheduled workflow checks all configured commits and Skill-file blob identifiers. When something has changed, it updates only the lock file and opens a PR in `jackbauerxu/operating-aip-content-system`.

This gives every update a visible source, commit, and affected Skill path. It can run safely without a cross-repository personal token.

## What is automatic at task runtime

When a task invokes a declared external program or package, the Skill checks its current version against the latest stable compatible release. A missing or outdated project dependency is installed or updated automatically in the project environment, followed by a version check and minimal diagnostic. This applies to the selected video, HTML, browser, converter, and renderer tools, not to unrelated software.

The runtime gate prefers a repository lockfile and project-local installation. Network downloads and system-level changes still use the environment's approval mechanism. The host Codex application itself is not silently replaced; if it cannot be updated from the current environment, the workflow reports that handoff instead.

## What remains human-reviewed

The workflow never copies upstream Skill instructions into this repository, overwrites a sibling Skill, creates a WeChat draft, or modifies a local Codex installation. Those actions can change functionality, permissions, or publishing behavior and require a deliberate compatibility review.

For a source-of-truth repository, a changed `SKILL.md` is recorded as current state. For a review-only upstream, a changed commit becomes a PR signal to inspect the upstream release notes, licence, and relevant instructions before integrating a targeted update.

## Manual run

Open the repository's **Actions** tab, select **Skill source audit**, and choose **Run workflow**. The report is deterministic: if nothing changed, no PR is created.
