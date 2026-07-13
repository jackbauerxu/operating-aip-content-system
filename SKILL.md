---
name: operating-aip-content-system
description: Use when a creator needs a repeatable WeChat Official Account AIP content system, wants to turn verified insights into WeChat articles and template-ready short videos, or needs to connect positioning, benchmarking, production, formatting, and weekly review without automatic publishing.
---

# Operating AIP Content System

Build a repeatable WeChat Official Account AIP system around one source of truth: the **content evidence packet**. It records the reader, account promise, original angle, proof, asset rights, and approval state before any platform-specific output is made.

## Scope and operating order

This Skill combines a platform-safe AIP architecture with workflow, editorial, video, and formatting capabilities:

1. Positioning
2. Account setup
3. Benchmark
4. Topic
5. Writing
6. Format

Read [AIP architecture](references/aip-architecture.md) before choosing a production route. The sequence is deliberate: no writing, renderer, or publishing tool may compensate for an unclear account promise, unverified claim, missing asset right, or missing human decision.

Keep Xiaohongshu, image-card/image-first production, `wb-xhs-*`, and `dbs-xhs-title` outside version 1.0.

## Permanent safety boundaries

- Treat platform rules, API access, monetization eligibility, product restrictions, and numeric thresholds as time-sensitive. Verify a current primary source when they affect a decision.
- Do not promise revenue, readership, growth, conversion, recommendation, or platform eligibility.
- Extract benchmark patterns without copying wording, visual assets, screenshots, results, or implied endorsement.
- Never write AppSecret, AccessToken, API keys, or other credentials into content artifacts, screenshots, repositories, or HTML.
- Keep final publication as an explicit human decision.

## Capability ownership

| Layer | Primary capability | Boundary |
| --- | --- | --- |
| AIP strategy | Person-offer-scene positioning, account promise, trust path, benchmark learning, and weekly learning | Project records take precedence over tool configuration. |
| Editorial diagnosis | `dbs-diagnosis`, `dbs-benchmark`, `dbs-content`, `dbs-hook`, `dbs-resonate`, `dbs-spread` | They improve a packet or locked draft; they do not make facts, publish, or own final HTML. |
| Content intelligence | Selected `wewrite-*` modules | They are optional upstream assistants, never the root full pipeline, final renderer, or publisher. |
| Recurring operations | `codex-workflow-builder` | It owns the reusable runbook, not the claims or visual style. |
| Short-video production | `codex-remotion-daily-video` | It receives a reviewable video handoff; it does not mechanically shorten an article. |
| Final HTML | One selected HTML lane | A second renderer must never restyle, reconvert, upload, or draft the first renderer's output. |

## Choose the route

| Situation | Required route |
| --- | --- |
| Positioning, offer, trust proof, or conversion scene is unclear | Draft or update an AIP brief. Use `dbs-diagnosis` for a focused diagnosis. |
| A new account needs name, bio, avatar direction, topic boundary, or monetization hypothesis | Complete the positioning and account-setup contracts. Treat policy-dependent details as `needs-evidence`. |
| A benchmark needs study | Use `dbs-benchmark` and the three-level benchmark card. Retain only reader problems, structure, and verified evidence. |
| A ready topic needs an editorial diagnosis | Use `dbs-content`; use hook, resonance, or spread modules only for the specific weakness. |
| There are at least about 50 bounded source files or 80,000 words across two source types | Audit first with `dbs-content-system`; preserve originals and start with a sample. |
| One article will not recur | Draft directly from the evidence packet. Do not create a workflow. |
| The process repeats | **Required:** use `codex-workflow-builder` to create a Workflow Contract and runbook. |
| A video lane is new or uncertain | Create 1–3 HyperFrames briefs and review samples before template work. |
| A video lane is stable and repeats | **Required:** use `codex-remotion-daily-video` for JSON, reusable components, still-frame checks, and render loop. |
| A ready packet needs topic candidates, drafting, review, visuals, or actual metric analysis | Use the smallest relevant `wewrite-*` module under **Controlled WeWrite use**. |
| An approved Markdown article needs automated conversion, preview, or a possible draft | Select the `md2wechat` automation lane. |
| An approved Markdown needs agent-designed pasteable HTML | Select the `gzh-design` lane. |
| A human wants hands-on visual editing or private editor deployment | Select the Doocs/MD lane only on explicit request. |
| `md2wechat` is unavailable and only pasteable HTML is needed | Select `dbs-wechat-html` as the fallback lane. |

## Create the evidence packet

1. Read `account/AIP_BRIEF.md`, or create an assumptions-marked draft with person, offer, scene, account promise, proof, boundaries, and next validation action.
2. Create `research/YYYY-MM-DD-slug/evidence-packet.md` for one parent insight. Include reader problem, original angle, source ledger, evidence, asset rights, missing proof, article promise, video tension, and required human decision.
3. Label the packet `ready`, `needs-evidence`, or `needs-human-decision`.
4. Use the templates in [contracts](references/contracts.md). Every performance or factual claim needs a source, date, and status.

Do not build a heavy content-asset library from a few notes. Keep a lightweight source ledger and reuse map until an audit shows a large, bounded archive.

## Write an article

Draft Markdown from a ready packet:

1. Open with a verified outcome, verified value, reader pain, or honest curiosity.
2. Deliver a usable method, decision, or clearly stated limitation with evidence.
3. Use the creator's real test, story, failure, or judgment only where it serves the reader's problem.
4. Close with a truthful interaction, summary, or scoped next action.

If a benchmark inspired the structure, transform it through a different audience, context, evidence, and voice. If original proof cannot be added, retain it as research rather than publish a near-copy.

## Controlled WeWrite use

- `wewrite-topic`: candidate angles after the reader and account boundary are known.
- `wewrite-write`: structured Markdown drafting from a ready packet.
- `wewrite-review`: revision advice; the source ledger remains authoritative.
- `wewrite-visual`: only on explicit user request and approved provider/local-output choice; record rights.
- `wewrite-stats`: only for actual user-provided or authorised account metrics.
- `wewrite-style` and `wewrite-learn`: only after explicit consent to persist preferences, using the user's own approved revisions.

Never run the root `wewrite` end-to-end pipeline, `wewrite-publish`, or XHS-oriented rewrite/image-post routes in 1.0. Tool-private state never replaces the project record.

## Select exactly one final HTML lane

Read [publishing lanes](references/publishing-lanes.md), then record the selection in the publication handoff.

1. **`md2wechat` automation:** inspect → optional temporary layout validation → local preview → convert. It is the only lane that may upload or create a WeChat draft, and only with explicit current-task approval and a ready target.
2. **`gzh-design`:** generate from locked Markdown, finish the upstream validator with zero errors and warnings, then let a human paste the output. Do not send its HTML to another renderer.
3. **Doocs/MD:** open, deploy, or edit only when explicitly requested. A human chooses and pastes the result.
4. **`dbs-wechat-html` fallback:** use only when `md2wechat` is unavailable and no external action is requested. It remains the sole formatter.

`wechat-svg` may create a checked static asset only when explicitly requested. It is an asset, not a second HTML lane.

## Short-video production

Create `content/video-handoffs/YYYY-MM-DD-slug.json` from the same packet, not by truncating the article. Include lane, hook, core tension, claims and evidence, scenes, captions, visual assets, rights, duration, human review, and output path.

- Confirm template fit: content changes but scene structure repeats, and text, screenshots, cards, UI, charts, or simple motion carry the message. Use a manual editor for one-off footage-first work.
- For a new lane, make 1–3 HyperFrames briefs with different hooks or scene rhythms. Promote only a clear, repeatable winner.
- For a stable lane, use `codex-remotion-daily-video`. Keep theme, components, caption rules, cover rules, render commands, and acceptance checks in the video project; keep daily variation in JSON.
- Before full render, check title/caption fit, safe zones, overflow, asset paths and rights, contrast, timing, cover readability, output format, and duration. Render a key still frame first.
- At review, improve one reusable rule or component instead of patching a one-off timeline.

## Review and learn

Before release, review source accuracy, originality, audience fit, voice, hook, asset rights, selected HTML lane, and the human publication decision. Record observed data only; never infer unobserved conversion or revenue.

At the weekly review, change one evidence-backed rule in the AIP brief, article structure, visual system, or video template. Link the decision to its packet and observed-data source.

## Definition of done

- AIP brief or explicit assumptions
- One complete evidence packet
- Article Markdown, or a documented blocker
- Video handoff, or a documented reason video is unsuitable
- Workflow Contract if the process repeats
- Selected final HTML lane and publication handoff
- Human review decision and next learning action

## Attribution

This original integration adapts architecture from `wechat-aip-architect` and coordinates upstream `dbskill`, `codex-workflow-builder`, `codex-remotion-daily-video`, `md2wechat`, `gzh-design`, Doocs/MD, and WeWrite. It does not copy their full instructions or component libraries. See [third-party notices](THIRD_PARTY_NOTICES.md) for licences and use boundaries.
