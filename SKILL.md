---
name: operating-aip-content-system
description: "Use when a creator needs a repeatable, evidence-led WeChat Official Account AIP content system: clarify positioning, turn verified source material into WeChat articles and template-ready short-video handoffs, choose one safe publishing lane, or build a recurring reviewable workflow. Start with an AIP Brief and content evidence packet; do not use for Xiaohongshu production, one-off copy edits, or automatic publishing."
---

# Operating AIP Content System

## Outcome

Operate a WeChat AIP content system in which an **AIP Brief** defines the account and a **content evidence packet** is the single source of truth for each parent idea. Produce only the needed artifact: a positioning brief, evidence packet, Markdown article, video handoff, publishing-lane handoff, Workflow Contract, or weekly learning record.

The human owns facts, rights, judgment, and the final publication decision. Tools help with bounded analysis and production; none may replace the project record.

## Use this workflow

### 0. Decide the task size

Classify the request before creating deliverables:

| Request | Minimum path |
| --- | --- |
| New account, unclear audience, offer, proof, or content boundary | Create or update an AIP Brief. |
| One new topic, article, or video idea | Create one content evidence packet. |
| A repeated article or video process | Create a Workflow Contract before building the production path. |
| A locked article that needs formatting | Skip to phase 5, but require the article-review decision and the source Markdown. |

Do not force a full system on a one-off request. Mark missing information as an assumption, `needs-evidence`, or `needs-human-decision`; never invent it.

### 1. Define the account promise

Read or create `account/AIP_BRIEF.md` using [contracts](references/contracts.md). Capture:

- person: relevant lived experience, work context, and credible point of view;
- offer: the truthful help, knowledge, service, or product hypothesis;
- scene: where the reader gets value and where compliant conversion may happen;
- a one-sentence account promise, proof, boundaries, topics to own or avoid, and a next validation action.

**Gate:** do not move to production until the reader, recurring problem, useful outcome, and available proof are clear enough to state. Use `dbs-diagnosis` only for a focused gap; it does not own the account record.

### 2. Create the content evidence packet

Create `research/YYYY-MM-DD-slug/evidence-packet.md` for one parent idea. Record the reader problem, original angle, source ledger, evidence, asset rights, missing proof, article promise, video tension, selected route, and required human decision.

Set exactly one state:

- `ready`: key claims, rights, and decisions needed for the selected route are present;
- `needs-evidence`: factual proof, source date, or asset right is missing;
- `needs-human-decision`: evidence is adequate but the human must choose an angle, route, or external action.

Every factual or performance claim needs a source, access date, and status. Keep a light source ledger until an actual bounded archive justifies a larger content-system audit.

### 3. Route the work

Select the smallest capable route. Read [AIP architecture](references/aip-architecture.md) before choosing an upstream capability.

| Situation | Route | Boundary |
| --- | --- | --- |
| Study a competitor or reference article | `dbs-benchmark` + benchmark card | Retain reader problems, structure, and verified evidence; do not copy expression or assets. |
| Diagnose a ready topic or locked draft | `dbs-content`, then one specific hook/resonance/spread module if needed | Suggestions do not create facts or approve publication. |
| The process repeats | `codex-workflow-builder` | It owns the Workflow Contract and runbook, not claims or style. |
| New or unproven short-video format | 1–3 HyperFrames briefs | Review a repeatable winner before template work. |
| Stable, repeatable short-video format | `codex-remotion-daily-video` | Use structured JSON, reusable components, still-frame checks, and render checks. |
| Ready packet needs a narrow editorial task | The smallest applicable `wewrite-*` module | Never run the root `wewrite` pipeline or `wewrite-publish`. |
| Locked Markdown needs conversion, preview, or an explicitly requested draft | `md2wechat` | It is the only lane that may upload or create a draft. |
| Locked Markdown needs designed pasteable HTML | `gzh-design` | Validate with zero errors and warnings; end with human paste. |
| A human explicitly wants visual editing or private deployment | Doocs/MD | Preserve the source Markdown; the human selects the result. |
| `md2wechat` is unavailable and pasteable HTML is enough | `dbs-wechat-html` | Use it as the sole fallback formatter. |

Keep Xiaohongshu, image-card production, `wb-xhs-*`, and `dbs-xhs-title` outside version 1.0.

### 4. Produce the selected artifact

#### Article

Write Markdown only from a `ready` packet:

1. Open with a verified outcome, verified value, reader pain, or honest curiosity.
2. Give a usable method, decision, or clearly stated limitation backed by the source ledger.
3. Add the creator's real test, story, failure, or judgment only when it helps the reader understand the topic.
4. Close with a truthful interaction, summary, or scoped next action.

Transform any benchmark through a different audience, context, evidence, and voice. Without original proof, keep the work as research rather than publishing a near-copy.

#### Video

Create `content/video-handoffs/YYYY-MM-DD-slug.json` from the same packet, not by shortening the article. Include lane, hook, core tension, claims with evidence, scenes, captions, visual assets and rights, duration, human review point, and output path.

Use a manual editor for footage-first or one-off work. For a template-friendly lane, validate first; then fix shared components or schema rules rather than patching one daily timeline.

### 5. Select exactly one final HTML lane

Read [publishing lanes](references/publishing-lanes.md), then write the publishing-lane handoff. Start only from locked, human-reviewed Markdown.

- Do not pass HTML or inline styles from one renderer into another renderer.
- `md2wechat` must run `inspect` and meet the relevant readiness target before any upload or draft action.
- `gzh-design` must finish its validator with zero errors and warnings, then await human paste.
- Doocs/MD starts only on explicit request; do not launch it merely to inspect an article.
- `wechat-svg` is an optional static asset, not a second renderer.

Set `Requested external action` to `none`, `human paste`, `upload`, or `create draft`. Upload and draft require explicit current-task authorization, confirmed asset rights, and a ready target.

### 6. Review and learn

Before release, check source accuracy, originality, audience fit, voice, hook, asset rights, the sole HTML lane, and the human decision.

During weekly review, use only actual authorised account data. Change one evidence-backed rule in the AIP Brief, article structure, visual system, or video template, and link that decision to its packet and data source.

## Permanent safety boundaries

- Treat platform rules, API access, commercial eligibility, numerical thresholds, and product restrictions as time-sensitive; verify a current primary source when they affect a decision.
- Do not promise readership, revenue, follower growth, conversion, recommendation, or platform eligibility.
- Do not copy benchmark wording, visuals, screenshots, proprietary material, results, or implied endorsements.
- Never record AppSecret, AccessToken, API keys, or other credentials in content, screenshots, HTML, or repositories.
- Do not publish, upload, or create a draft without current-task, explicit human authorization.

## Definition of done

The task is complete only when the relevant records exist:

- AIP Brief or explicit, labelled assumptions;
- one complete evidence packet with a truthful state;
- article Markdown or a documented blocker;
- video handoff or a documented reason video is unsuitable;
- a Workflow Contract when the work repeats;
- exactly one selected final HTML lane and its handoff when formatting is requested;
- a human review decision and one next learning action.

## References

- [AIP architecture](references/aip-architecture.md): six-stage strategy and safety bottom lines.
- [Contracts](references/contracts.md): Brief, evidence packet, benchmark, topic, article-review, publishing, and video templates.
- [Publishing lanes](references/publishing-lanes.md): final HTML route selection and prohibited combinations.
- [Update policy](UPDATE_POLICY.md): source-version monitoring and review-only integration.

## Attribution

This original integration, maintained by `jackbauerxu`, adapts architecture from `wechat-aip-architect` and coordinates bounded use of `dbskill`, `codex-workflow-builder`, `codex-remotion-daily-video`, `md2wechat`, `gzh-design`, Doocs/MD, and WeWrite. It does not copy their full instructions or component libraries. See [third-party notices](THIRD_PARTY_NOTICES.md) for the project-by-project public maintainer, licence, and use-boundary record.
