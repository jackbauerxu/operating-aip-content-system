# Operating AIP Content System

一个面向微信公众号 AIP（AI + Personal IP）的内容系统 Skill。它把账号定位、内容证据、对标学习、文章生产、短视频模板、排版和人工发布决策组织成同一条可追溯的工作流。

它不是“自动发文器”。它让创作者保留判断、真实经历、事实边界和最终发布权；AI 负责把重复工作做成可复用的流程。

## 定义

**AIP 内容系统**是从“定位—内容—信任—复盘”持续运作的生产体系：

```text
定位与账号承诺
  → 内容证据包
  → 选题 / 写作 / 视频交接
  → 选定一个最终排版路线
  → 人工发布决定
  → 基于真实数据的每周学习
```

唯一的事实源是每个选题的 **内容证据包**。平台格式、文章、视频和视觉素材都从它分支出来；没有证据、版权或人工决定的内容不能被工具升级成“已证实”。

## 安装

```bash
npx skills add jackbauerxu/operating-aip-content-system
```

安装后，在 Codex 中直接提出任务，或显式调用：

```text
使用 $operating-aip-content-system，帮我把一份 AI 工具实测做成公众号和短视频栏目。
```

## 适用场景

- 从零定位一个微信公众号 AIP，并建立可验证的信任路径。
- 研究对标账号或文章，但需要避免洗稿与不实结论。
- 将真实测试、访谈、研究或自有内容资产，变成公众号文章与视频选题。
- 将已经稳定的内容栏目转为可维护的 Remotion 生产线。
- 为审核通过的 Markdown 选择合适的公众号排版与发布路径。

不适用于小红书生产、图文卡片批量生产或一次性剪辑项目；这些范围留给独立的 XHS 和手工视频工作流。

## 能力归属与防冲突设计

| 层级 | 保留的最强能力 | 明确边界 |
| --- | --- | --- |
| AIP 总架构 | `wechat-aip-architect` 的六阶段闭环、人—货—场、真人 IP、对标、信任与合规商业化 | 所有生产工具必须在定位和证据之后工作。动态平台规则必须重新核验。 |
| 策略与诊断 | `dbs-diagnosis`、`dbs-benchmark`、`dbs-content`、`dbs-hook`、`dbs-resonate`、`dbs-spread` | 只能给出诊断与编辑建议，不能编造事实、发布或控制最终 HTML。 |
| 内容智能 | 小而明确的 `wewrite-*` 模块 | 只做受控选题、起草、审稿、素材或真实数据分析；不运行一键全流程或发布。 |
| 重复工作流 | `codex-workflow-builder` | 为重复任务建立项目契约和运行手册，不替代内容判断。 |
| 短视频 | `codex-remotion-daily-video` | 新格式先验证；稳定格式才进入 JSON、组件、静帧检查和渲染循环。 |
| 最终 HTML | `md2wechat`、`gzh-design`、Doocs/MD 或 `dbs-wechat-html` 兜底 | 一篇文章只选一条最终 HTML 生产线，禁止二次套样式或串联转换。 |

## 快速使用示例

### 新账号

```text
我是供应链产品经理，正在测试 AI 工作流。
使用这个 Skill：先按人—货—场给我做一个细分 AIP 定位、账号五要素、首批 10 个可验证选题和一份对标卡。
不要把平台门槛或收入写成事实。
```

### 稳定内容栏目

```text
我每周有一份 AI 工具实测笔记和三张可公开截图。
请建立一个“每周两篇公众号、三条视频”的工作流；先建立证据包和审核点。
视频格式稳定后再进入 Remotion，不要自动发布。
```

### 已审核文章的排版

```text
这篇 Markdown 已经通过事实、版权和人工审核。
我需要精致、可人工粘贴的公众号 HTML：请选择 gzh-design 这一条路线，完成校验和预览，但不要建草稿。
```

## 发布安全

- 只有 `md2wechat` 自动化路线可创建公众号草稿，且必须有当前任务中的明确授权、就绪目标和素材权利确认。
- `gzh-design` 与 Doocs/MD 的默认终点是人工粘贴，不会偷偷切换为草稿创建。
- 不把 AccessToken、AppSecret、API Key 或其他凭据写入 Markdown、截图、仓库或 HTML。
- 不承诺阅读、涨粉、收入、推荐、转化或平台资格；需要时以当前官方来源和账户真实数据为准。

## 仓库结构

```text
SKILL.md                         # 主入口与路由规则
references/aip-architecture.md   # AIP 六阶段架构与安全底线
references/contracts.md          # AIP brief、证据包、对标卡、发布交接模板
references/publishing-lanes.md   # 四条互斥的最终 HTML 路线
test-prompts.json                # 正向、拒绝与边界场景
THIRD_PARTY_NOTICES.md           # 上游项目与许可边界
```

## 来源与许可边界

本仓库的原创整合部分采用 [MIT License](LICENSE)。它只调度或改编上游方法，不复制上游完整指令、主题库或组件库。使用上游能力时，仍须遵守其各自许可与商业条款，详见 [第三方说明](THIRD_PARTY_NOTICES.md)。

主要来源包括：[wechat-aip-architect](https://github.com/chenjin-cmd/wechat-aip-architect)、[dbskill](https://github.com/dontbesilent2025/dbskill)、[codex-workflow-builder](https://github.com/jackbauerxu/codex-workflow-builder)、[codex-remotion-daily-video](https://github.com/jackbauerxu/codex-remotion-daily-video)、[md2wechat](https://github.com/geekjourneyx/md2wechat-skill)、[gzh-design-skill](https://github.com/isjiamu/gzh-design-skill)、[Doocs/MD](https://github.com/doocs/md) 与 [WeWrite](https://github.com/imraywang/wewrite)。
