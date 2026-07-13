# Publishing Lanes

## Rule: exactly one final HTML producer

Start with locked, human-reviewed Markdown. Choose the smallest lane that fulfils the request and record it in the publishing-lane handoff. Never pass final HTML or inline styles from one lane through another lane.

| Lane | Use when | Required checks | Endpoint |
| --- | --- | --- | --- |
| `md2wechat` automation | Repeatable conversion, local preview, or an explicitly requested WeChat draft | `inspect`, relevant readiness target, validation of any temporary layout copy, local preview | HTML; upload/draft only after explicit current-task approval |
| `gzh-design` | Agent-designed visual layout is the priority | Upstream checker has zero errors and warnings; human preview | Copy-paste HTML, pasted by a human |
| Doocs/MD | A human wants visual editing or private editor deployment | Explicit request to open/deploy; human visual review | Human-selected pasteable HTML |
| `dbs-wechat-html` fallback | `md2wechat` is unavailable and only pasteable HTML is needed | Locked copy; no external action requested | Human-selected pasteable HTML |

`wechat-svg` is an optional checked static visual asset, not a renderer. Use it only on explicit request, then insert it through the selected lane after compatibility and rights checks pass.

## md2wechat automation lane

1. Run `inspect <article.md> --json` and read article-specific readiness targets and blockers.
2. If enhanced layout is needed, preserve the source Markdown; make a temporary formatted copy, use only truthful modules, and validate it.
3. Preview locally. Preview must not upload, create a draft, or alter source Markdown.
4. Convert only when its target is ready.
5. Upload assets or create a draft only after explicit user instruction, asset/cover rights confirmation, and a ready target.

If credentials or required readiness are missing, report the blocker. Do not silently switch mode, publish, or downgrade the approved argument.

## gzh-design lane

Use only after source Markdown and article review are locked. Follow the installed skill's current design and validator instructions. The output must have zero validation errors and warnings, be previewed by a human, and end as deliberate human paste—not an automatic upload or draft.

## Doocs/MD editor lane

Doocs/MD is a visual-editing or self-hosting option, not an autonomous publication command. Start the editor or deployment only on explicit request. Preserve the Markdown source and article review beside the manually selected result. Do not start a server just to inspect an article.

## Prohibited combinations

- Do not run WeWrite's root pipeline and then publish automatically.
- Do not feed `gzh-design` HTML through Doocs/MD or `md2wechat`.
- Do not use one lane's output to override another lane's design.
- Do not turn a pasteable-HTML fallback into a hidden WeChat draft path.
