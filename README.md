# Operating AIP Content System

把微信公众号 AIP（AI + 个人 IP）从“临时找题、临时写、临时排版”变成一套可重复、可审查的内容工作系统。

它的核心不是替你自动发文，而是让每一篇文章和每条视频都从同一份**内容证据包**出发：先知道为谁服务、凭什么可信、哪些素材可用、还缺什么，再决定写作、视频和排版。

## 它是什么

这是一个内容系统 Skill，不是单一写作器，也不是把多个上游 Skill 串成“一键发文”流水线。

它充当内容生产的总控层：

- 把账号定位固化为可检查的 **AIP Brief**；
- 把单个选题固化为可追溯的 **内容证据包**；
- 为文章、视频和公众号 HTML 选择一条合适且不冲突的生产路线；
- 把最终发布权、事实边界和素材权利保留给人。

一句话定义：**用证据包把“定位 → 生产 → 审核 → 学习”连接起来的微信公众号个人 IP 内容操作系统。**

## 它会交付什么

根据任务规模，交付全部或必要部分，而不是强迫每次都走完整流程：

| 任务 | 最小交付 |
| --- | --- |
| 新账号或定位不清 | AIP Brief、账号承诺、首批验证动作 |
| 一个新选题 | 内容证据包、状态与缺失证据 |
| 已有证据的文章 | 审核过的 Markdown、文章审核记录 |
| 适合视频的母题 | 视频交接包、样片或模板路线建议 |
| 已审核文章的排版 | 一份发布路线交接单、唯一 HTML 输出 |
| 重复内容栏目 | Workflow Contract、运行手册、人工检查点 |
| 周度复盘 | 一条基于真实数据的规则调整 |

完整字段见 [交付契约](references/contracts.md)。

## 什么时候用 / 什么时候不该用

| 适合使用 | 不适合使用 |
| --- | --- |
| 想从零建立可验证的公众号个人 IP | 只想临时润色一句文案或起一个标题 |
| 有真实测试、访谈、研究或工作经验，想做成内容 | 小红书图文卡片、标题库或账号运营（使用独立 XHS Skills） |
| 一篇内容要同时规划文章和短视频 | 一次性、强剧情、依赖真人素材的剪辑项目 |
| 公众号文章已审核，需选择排版或发布路径 | 没有事实、素材权利或人工决定，却要求直接发布 |
| 栏目会重复，需要稳定工作流或 Remotion 模板 | 想让 AI 承诺阅读、涨粉、收入或平台资格 |

## 开始前，给它什么

不需要一次准备齐全。缺少的信息会被明确标为假设、`needs-evidence` 或 `needs-human-decision`，不会被编造成事实。

最有用的输入是：

1. **人**：你的职业、真实经历、已经验证过的能力或观点。
2. **读者**：你想服务谁、他们正在经历什么问题。
3. **证据**：测试记录、访谈、公开来源、截图、案例；以及每项素材的使用权。
4. **目标**：这次要定位、选题、文章、视频、排版，还是建立重复工作流。
5. **限制**：不想写什么、不可公开什么、是否允许任何外部动作。

## 六步工作流程

```text
1. 定位
   → 2. 建立内容证据包
   → 3. 选择生产路线
   → 4. 制作文章或视频
   → 5. 选择唯一排版路线并人工决定发布
   → 6. 根据真实数据复盘一条规则
```

### 1. 定位：先回答“谁、提供什么、在哪个场景有用”

创建或更新 AIP Brief，写清人—价值供给—场景、账号承诺、可信证明、话题边界和下一步验证动作。

**通过条件**：能用一句面向读者的话说明“我为谁解决什么问题，能提供什么真实帮助”。

### 2. 建立内容证据包：再决定“这条内容能不能做”

每个母题建立一个证据包，记录读者问题、原创角度、来源账本、证据、素材权利、缺失项、文章承诺、视频张力和所需人工决定。

**状态只能是：**

- `ready`：证据、权利和关键决定齐全，可进入生产；
- `needs-evidence`：缺少事实或素材，先补证据；
- `needs-human-decision`：事实已具备，但需你选择表达、路线或外部行动。

### 3. 选择生产路线：只选择解决当前问题的最小工具

| 当前情况 | 选择 |
| --- | --- |
| 定位、价值供给或可信证明不清 | 先补 AIP Brief，可用 `dbs-diagnosis` 做局部诊断 |
| 要研究对标 | 用三层对标卡与 `dbs-benchmark`；只保留问题、结构和可核验证据 |
| 单篇文章、不会重复 | 直接由 `ready` 证据包写 Markdown |
| 流程会重复 | 先用 `codex-workflow-builder` 建 Workflow Contract |
| 新的视频栏目或结构尚未验证 | 先做 1–3 个 HyperFrames 样片 |
| 已验证且会重复的视频格式 | 使用 `codex-remotion-daily-video` 建 JSON、组件和渲染检查 |
| 已锁定 Markdown，需要自动转换或可能建草稿 | 选择 `md2wechat` 路线 |
| 已锁定 Markdown，需要精致、人工粘贴的 HTML | 选择 `gzh-design` 路线 |
| 需要手工视觉编辑或私有化编辑器 | 仅在明确要求时选 Doocs/MD |

### 4. 制作：文章和视频共享证据，不共享成品

- **文章**从证据包写成 Markdown：开头是已验证的结果、价值、痛点或诚实好奇；正文给出方法、判断或限制；故事只在能解释读者问题时出现。
- **视频**从同一证据包生成视频交接包：独立定义钩子、核心张力、镜头、字幕、素材权利和审核点；不要机械缩短文章。

### 5. 排版与发布：一篇文章只能有一个最终 HTML 生产者

在已锁定的 Markdown 上选择一条路线，记录到发布交接单。不要把一个排版器生成的 HTML 交给第二个排版器。

- `md2wechat` 是唯一可能上传或创建草稿的路线，而且仅在当前任务得到明确授权、目标已就绪、素材权利已确认时执行。
- `gzh-design`、Doocs/MD 和 `dbs-wechat-html` 的默认终点是人工粘贴。
- 最终发布永远需要人的明确决定。

详见 [排版路线](references/publishing-lanes.md)。

### 6. 复盘：一次只改变一条有证据的规则

每周只用真实、已授权的内容数据复盘一次，并把结论关联回具体证据包。可以调整账号承诺、文章结构、视觉系统或视频模板；不要把未观察到的转化、收入或推荐写成结论。

## 怎么使用

安装：

```bash
npx skills add jackbauerxu/operating-aip-content-system
```

然后直接描述你的任务。以下提示词可以原样使用。

### 从零开始定位

```text
使用 operating-aip-content-system。
我是供应链产品经理，正在测试 AI 工作流；想服务正在做流程优化的中小团队负责人。
先为我创建 AIP Brief：给出账号承诺、话题边界、可用证明、缺失证明和下一步验证动作。
不要把平台规则、收入或效果写成事实。
```

### 把真实素材做成文章和视频

```text
使用 operating-aip-content-system。
我有一份 AI 工具实测记录、三张有使用权的截图和采访笔记。
先建立内容证据包并标注状态；如果 ready，再输出公众号 Markdown 和独立的视频交接包。
不发布，也不要虚构测试结果。
```

### 为重复栏目建生产线

```text
使用 operating-aip-content-system。
我每周都有一份 AI 工具实测，想稳定产出两篇公众号文章和三条视频。
先用 codex-workflow-builder 建 Workflow Contract；视频格式没有验证前先给 3 个 HyperFrames 样片方向。
确认格式可重复后，再交给 codex-remotion-daily-video 设计模板。
```

### 排版一篇已审核文章

```text
使用 operating-aip-content-system。
这篇 Markdown 已完成事实、版权和人工审核。
我需要精致、可人工粘贴的公众号 HTML。请选择 gzh-design 这条路线，完成校验与预览，但不要创建草稿。
```

## 完成标准

完成一个完整内容任务时，至少应能回答：

- 这条内容服务谁、承诺什么、凭什么可信？
- 每个关键事实和素材是否有来源、日期与权利状态？
- 当前选择的是文章、视频还是排版路线，为什么？
- 是否只使用了一条最终 HTML 路线？
- 人是否已明确决定发布、暂缓或继续补证据？
- 下次要根据什么真实数据改进哪一条规则？

## 安全与边界

- 不承诺阅读、涨粉、收入、转化、推荐或平台资格。
- 不复制对标文案、视觉资产、截图、结果或暗示性背书。
- 不在内容、HTML、截图或仓库中记录 AccessToken、AppSecret、API Key 等凭据。
- 不把小红书生产纳入 1.0；它仍由独立 XHS Skills 处理。
- 外部 Skill 只按其优势被受控路由，不能替代项目事实、最终 HTML 或发布决定。

## 文档地图与更新

- [主入口规则](SKILL.md)：Codex 实际执行的路由与边界。
- [AIP 架构](references/aip-architecture.md)：六阶段方法论与长期安全底线。
- [交付契约](references/contracts.md)：Brief、证据包、对标、视频和发布交接模板。
- [排版路线](references/publishing-lanes.md)：四条互斥的最终 HTML 路线。
- [更新策略](UPDATE_POLICY.md)：公开 Skill 和上游项目的版本审计与人工整合规则。

每周自动审计会记录本账号公开 Skill 仓库及已声明上游的版本变化；它只更新版本锁定并发起审阅 PR，不会跨仓库覆盖内容或修改本地 Codex 安装。

## 来源与许可边界

本仓库的原创整合与维护者为 [jackbauerxu](https://github.com/jackbauerxu)，原创整合部分采用 [MIT License](LICENSE)。它协调或改编上游方法，不复制上游完整指令、主题库或组件库；使用上游能力时仍须遵守其许可与商业条款。

### 1.0 融合来源与公开维护者

下表的“公开维护者”按上游 GitHub 仓库所有者/组织标注；它用于明确致谢与溯源，不把这些上游的全部代码、指令或组件宣称为本仓库内容。

| 上游项目 | 公开维护者 | 1.0 中保留的能力 |
| --- | --- | --- |
| [wechat-aip-architect](https://github.com/chenjin-cmd/wechat-aip-architect) | [Chen / chenjin-cmd](https://github.com/chenjin-cmd) | AIP 定位、对标、内容架构与安全底线 |
| [dbskill](https://github.com/dontbesilent2025/dbskill) | [dontbesilent / dontbesilent2025](https://github.com/dontbesilent2025) | 可选的诊断、对标与编辑模块 |
| [codex-workflow-builder](https://github.com/jackbauerxu/codex-workflow-builder) | [jackbauerxu](https://github.com/jackbauerxu) | 可重复任务的 Workflow Contract 与运行手册 |
| [codex-remotion-daily-video](https://github.com/jackbauerxu/codex-remotion-daily-video) | [jackbauerxu](https://github.com/jackbauerxu) | 经过验证后的视频 JSON、组件与渲染检查路线 |
| [md2wechat-skill](https://github.com/geekjourneyx/md2wechat-skill) | [geekjourneyx](https://github.com/geekjourneyx) | Markdown 转换、预览，以及获得明确授权后的草稿路线 |
| [gzh-design-skill](https://github.com/isjiamu/gzh-design-skill) | [isjiamu](https://github.com/isjiamu) | 精致、可人工粘贴的公众号 HTML 路线 |
| [Doocs/MD](https://github.com/doocs/md) | [Doocs / doocs](https://github.com/doocs) | 人工视觉编辑与私有化编辑器路线 |
| [WeWrite](https://github.com/imraywang/wewrite) | [imraywang](https://github.com/imraywang) | 受控使用的选题、写作、复盘等非发布模块 |

逐项许可、使用边界和来源版本见 [第三方说明](THIRD_PARTY_NOTICES.md) 与 [更新策略](UPDATE_POLICY.md)。
