---
name: brand-visual-research-builder
description: 基于品牌官方页面、新闻稿、媒体中心、产品页和用户提供链接，构建可追溯的品牌视觉研究库，并把观察结论翻译成镜头、光线、材质、颜色、场景、人物语气与 failure risks。Use when Codex needs source-backed brand visual research, official-page reading, compact research bank creation, brand-inspired prompt direction, campaign visual territory mapping, or compliance-aware prompt translation without保存原图、without claiming official authorization。中文适用：品牌视觉研究、官方页面拆解、来源留档、品牌气质转 prompt 规则、只做研究不出图、研究库压缩交付。
---

# Brand Visual Research Builder

## 核心工作流

把用户给出的品牌名、产品线、品牌方向稿需求或官方链接，整理成“有来源、可复用、能落到 prompt”的品牌视觉研究库。

1. 先判断研究范围：单品牌研究、单产品研究、品牌对标、品牌方向稿前置研究，还是只做研究不写 prompt。
2. 优先读取官方来源：品牌官网首页、产品页、新闻稿、媒体中心、Lookbook、店铺/空间页面、品牌故事页。只在用户明确要求时再补第三方媒体。
3. 用 `references/research-framework.md` 记录来源链接、页面类型、观察结论、可迁移的视觉变量和不应照抄的元素。
4. 用 `references/source-intake-and-compliance.md` 约束边界：不下载原图、不保留官方素材副本、不声称官方授权、不把“品牌启发”写成“官方标准”。
5. 用 `references/prompt-translation-rules.md` 把研究结果翻译成镜头、光线、构图、材质、色彩、场景、人物状态、版式留白和 negative risks。
6. 需要快速交付时，直接输出 `compact research bank`；需要稳态交付时，再补品牌摘要、source log、prompt rules、avoid list。
7. 用户明确要求“只做研究”时，不输出平台 prompt，只给研究结论与后续方向。
8. 用户要求“官方一致”“严格品牌合规”时，明确说明仍需真实 brand guideline、授权素材或用户提供的官方包，不能用公开页面替代正式规范。

## 任务接收清单

- 品牌名是否明确；如果只给集团名，优先锁定具体品牌或产品线。
- 用户要的是研究库、方向稿前置、prompt 规则，还是只做风险排查。
- 是否已经给了官方链接、品牌 PDF、发布页、媒体中心页或产品页。
- 目标输出面向什么：海报、包装、广告主视觉、空间效果图、社媒图、产品 hero、提案摘要。
- 是否需要多品牌对比，还是只做单品牌深挖。
- 是否存在敏感项：logo、字体、包装文案、独特插画角色、摄影签名风格、店装结构。

## Reference Routing

- 每次做品牌视觉研究，都先读 `references/research-framework.md`。
- 只要涉及来源留档、官方页面优先级、不可保存原图、授权边界，就读 `references/source-intake-and-compliance.md`。
- 只要需要把观察结论翻译成 prompt 变量、镜头规则或避免项，就读 `references/prompt-translation-rules.md`。
- 用户要示例输出、交付模板或“给我看一份长什么样”时，读 `references/examples.md`。
- 用户要快速套用已有品牌样本，或需要从公开案例里找视觉抓手时，读 `references/compact-research-bank.md`。
- 用户要把研究结果做成提案级、交付级或更稳的专业版本时，读 `references/professional-quality-gate.md`。
- 用户的问题和已知案例接近，或者你想用成熟研究模式复用结构时，读 `references/case-library.md`。
- 做本 skill 自测、回归检查或验收时，读 `references/benchmark-suite.md`。

## 输出模式

### Compact Research Bank

默认输出：

```text
品牌研究库：
- 品牌 / 产品线：
- 研究范围：
- 证据等级：官方页面 / 官方新闻 / 官方媒体中心 / 用户提供材料 / 推断
- 一句话视觉结论：

来源记录：
1. [链接] - 页面类型 - 为什么有用
2. [链接] - 页面类型 - 为什么有用

观察结论：
- 视觉领地：
- 构图与镜头：
- 光线与材质：
- 颜色与环境：
- 人物 / 叙事气质：

Prompt translation rules：
- 保留：
- 转译：
- 可控变量：
- 留白与文字策略：

Failure risks：
- 不能照抄的元素：
- 容易做俗的方向：
- 容易做偏的方向：
```

### 单品牌深挖

当用户要“把这个品牌研究透，再给视觉规则”时，返回：

```text
品牌视觉研究：
- 品牌 / 产品：
- 研究目标：
- 研究结论：

Source log：
- 官方首页：
- 产品页：
- 新闻 / Press：
- 媒体 / Store / Story：

Evidence-backed visual territory：
- 1 句话定义：
- 3 个最强证据：

Prompt translation：
- 镜头：
- 构图：
- 光线：
- 材质：
- 色彩：
- 场景：
- 人物状态：
- Negative risks：
```

### 只做研究不写 Prompt

用户说“先别写 prompt，只做研究”时，返回：

```text
研究结论：
- 核心视觉领地：
- 关键证据：
- 可迁移元素：
- 不应照抄元素：
- 视觉风险：
- 如果下一步要出图，最适合先锁定的变量：
```

### 品牌对标

用户要比较两个品牌时，返回：

```text
品牌对标：
- 品牌 A 视觉结论：
- 品牌 B 视觉结论：

差异：
- 构图：
- 光线：
- 材质：
- 场景：
- 人物状态：

转译建议：
- 更像 A 时该加什么：
- 更像 B 时该加什么：
- 两边都该避免什么：
```

### 专业研究包

用户要“给团队过会”“写进提案”“做成可复用研究条目”时，返回：

```text
专业研究包：
- 品牌 / 产品：
- 研究目标：
- 证据等级：A / B / C / D
- 一句话结论：

Source log：
1. URL - 页面类型 - 证据
2. URL - 页面类型 - 证据

Visual territory：
- 构图与镜头：
- 光线：
- 材质：
- 色彩：
- 场景：
- 人物 / 叙事：

Prompt translation：
- Preserve：
- Translate：
- Control variables：
- Negative risks：

结论：
- 适合做什么：
- 不适合做什么：
- 还缺什么正式资料：
```

### 案例复用

用户要“参考一个类似品牌研究方式”时，先读 `references/case-library.md`，再返回：

```text
案例匹配：
- 最接近的案例：
- 为什么像：

可直接复用：
- 来源抓法：
- 观察结构：
- Prompt 转译结构：

针对本次任务的调整：
- 要保留：
- 要替换：
- 要额外提醒的风险：
```

## v1 专业质量门

- 至少给出 2 个可回查的官方来源链接；如果不足，明确写“证据不足”。
- 研究结论必须能落到镜头、光线、材质、色彩、场景中的至少 5 项。
- 至少指出 1 类“不能照抄的元素”和 2 类 failure risks。
- 不能把公开页面观察写成“官方规范”或“授权风格”。
- 只做研究模式下，不要偷偷补平台 prompt。
- 如果用户要求严格品牌合规，必须提醒还需要正式 brand guideline 或授权素材。
- 对标任务必须说明品牌差异，而不是把两个品牌都翻译成同一套“高级感”。
- 结尾必须说明“适合做什么 / 不适合做什么 / 还缺什么资料”。

如果以上任一项缺失，先自我修订一轮再输出。

## 默认策略

- 用户没给链接时，优先从公开可见的官方页面建立最小研究库，不要求先补齐所有材料。
- 研究阶段默认只保存文字化结论与来源链接，不保存官方图片、副本或截图。
- 不把公开页面观察写成“官方 brand guideline”；一律用“品牌启发”“官方页面可见视觉领地”“公开证据显示”这类措辞。
- 遇到 logo、排版、插画角色、包装正面、品牌签名字体、店装平面这类高版权/高识别元素时，只总结原则，不要求模型复刻。
- 如果官方页面信息不足，明确标注“证据不充分”，再补充保守推断，不要装作看到了不存在的内容。
- 做提案级交付时，优先按 `专业研究包` 输出，而不是只给一段紧凑摘要。
