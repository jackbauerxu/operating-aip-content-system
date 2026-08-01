# 微信公众号发布前审融合设计

## 目标

将 `yuwen-cool/yuwen-publish-precheck` 的可迁移方法接入 `operating-aip-content-system`，让公众号文章在进入 HTML 排版或外部发布路线前，完成“候选扫描 → 语义复核 → 保意修复 → 改后复检”。

## 范围

- 检查内容证据包、标题/摘要、正文、图片文字、引用、素材权利、商业关系和行动引导。
- 输出 `ready-to-publish / needs-revision / hold`，并区分必须改、建议改、待人工决定。
- 保留原有 `ready`、`needs-evidence`、`needs-human-decision` 状态和“唯一 HTML 路线”闸门。
- 来源仓库只提供方法转译；其平台专属规则不被宣称为微信公众号官方规则。

## 验收标准

1. 主 Skill 明确候选命中不等于违规、零命中不等于安全。
2. 修复梯度为披露/声明 → 补证据 → 收窄断言 → 最小改写 → 删除或暂缓，且改写后必须复检。
3. 文章审核契约记录预审结论、风险分级、替换文本和复检结果。
4. 测试提示覆盖正常预审、缺证据阻断和绕审拒绝；JSON、frontmatter、来源审计和 git diff 校验通过。
