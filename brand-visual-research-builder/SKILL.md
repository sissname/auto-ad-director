---
name: brand-visual-research-builder
description: Build compact brand visual research banks from official pages, press or newsroom pages, media-center pages, product pages, and other official brand surfaces. Use when Codex needs to整理官网视觉研究、保留原始来源链接、提炼视觉观察、沉淀 Prompt Translation Rules、列出 Failure Risks、做品牌调性对比、把研究转成可执行提示词方向，并且明确不保存原图、不宣称官方授权、不把研究结论写成官方品牌规范。
---

# Brand Visual Research Builder

## 核心工作流

把品牌官网信息整理成可复用的视觉研究库，而不是整理成“好看但不可执行”的灵感摘抄。

1. 先确认研究目标：单品牌研究、多个品牌对比、某一产品线视觉拆解，还是给后续 prompt director 做前置研究。
2. 只优先读取官方来源：官网首页、品牌故事页、新闻 / newsroom、媒体中心、产品页、店铺 / 空间页、投资者页面、发布会回放页。
3. 为每个页面保留原始链接、页面类型、为什么读它、从中观察到的视觉证据。
4. 把观察拆成可控变量：构图、景别、镜头高度、光线方向、色温、材质、表面处理、空间语气、人物状态、文字 / logo 策略。
5. 明确区分“可转译的视觉规律”和“不能照抄的具体元素”，尤其是商标、版式、标语、包装文字、门店装置、受保护图案和人物肖像。
6. 输出 `Compact Research Bank`，其中必须包含来源链接、观察结论、`Prompt Translation Rules`、`Failure Risks` 和安全措辞。
7. 如果用户要继续出图，只把研究结果转成方向，不把研究库伪装成官方授权手册。
8. 在专业交付前运行一次“专业质量门”，检查来源覆盖、证据纪律、可转译性和非官方措辞是否到位。

## 来源优先级

默认按下面顺序取证：

1. 产品页：最能说明材质、结构、光线、色彩和近景细节。
2. 新闻 / Newsroom：最能说明发布语气、品牌要强调的世界观和主叙事。
3. 媒体中心 / Press / Image bank：最能说明官方愿意公开展示的角度、构图和视觉控制方式。
4. 官网首页 / 品牌页：最能说明整体调性、页面留白、文字密度和视觉节奏。
5. 官方空间 / 门店 / 展陈页：用于补足空间语言、道具密度、动线和材质氛围。

如果某品牌没有公开 newsroom 或 media center，不要硬编；改为补读其官方 about、空间、产品分类页，并在输出里说明来源结构有限。

## Reference Routing

- 每次做品牌研究，先读 `references/research-workflow.md`。
- 涉及来源可信度、页面类型取舍、链接保留方式时，读 `references/official-source-rules.md`。
- 需要把研究转成 prompt 变量时，读 `references/prompt-translation-rules.md`。
- 需要现成品牌样例、研究库格式或对照写法时，读 `references/compact-research-bank.md`。
- 需要示例输出节奏时，读 `references/examples.md`。
- 需要验证这个 skill 是否成熟时，读 `references/benchmark-suite.md`。
- 做专业版交付、自查或验收时，读 `references/quality-scorecard.md` 和 `references/case-library.md`。

## 输出模式

### 单品牌研究卡

适合先把一个品牌研究明白，再决定是否进入 prompt 生成。

```text
研究任务：
- 品牌 / 产品线：
- 研究目标：
- 证据状态：直接读取官方页面 / 基于用户提供链接 / 基于描述推断

来源台账：
- 页面类型：
  链接：
  读取理由：
  视觉证据：

核心观察：
- 品牌视觉领域：
- 构图与景别：
- 光线与色温：
- 材质与表面：
- 颜色纪律：
- 空间 / 场景语气：
- 人物 / 叙事气质：

Prompt Translation Rules：
- 镜头：
- 光线：
- 材质：
- 颜色：
- 场景：
- 文案 / logo 处理：

Failure Risks：
- 容易跑偏成什么：
- 不要照抄什么：
- 生成时最脆弱的部位：

安全措辞：
- 推荐写法：
- 避免写法：
```

### Compact Research Bank

适合给后续 skill、团队成员或自己留一个紧凑研究库。

```text
Brand:
Research angle:
Source links:
- [official page]
- [newsroom / media / product]

Observation summary:
- [3-5 条核心视觉规律]

Prompt Translation Rules:
- Camera:
- Light:
- Material:
- Color:
- Space / talent:
- Typography / logo policy:

Failure Risks:
- [3-5 条最容易翻车的问题]

Safe wording:
- “受该品牌公开页面启发的视觉方向”
- “基于官方公开页面提炼的非官方研究结论”
```

### 多品牌对比

适合给提案、方向筛选或 prompt platform adapter 做前置判断。

```text
对比结论：
- 品牌 A：
  核心视觉领域：
  Prompt Translation Rules：
  Failure Risks：
- 品牌 B：
  核心视觉领域：
  Prompt Translation Rules：
  Failure Risks：

最关键差异：
- 光线：
- 材质：
- 场景：
- 情绪：
- 是否适合混用：
```

### 研究转 Prompt Brief

只有在用户明确要继续生成时再给这一层。

```text
研究转译 Brief：
- Style anchor：
- Camera：
- Light：
- Material：
- Color：
- Space：
- Talent / object behavior：
- Text / logo policy：
- Negative constraints：
```

## 质量规则

- 不保存原图，只保存链接、页面名称、观察结论和转译规则。
- 不宣称“官方授权”“官方风格复刻”“官方品牌规范”；除非用户真的提供了授权文件。
- 不把具体版式、标语、包装文字、门店图形系统当成可直接照抄的 prompt 内容。
- 如果只读到了产品页，没有读到 newsroom / media，就明确写“来源覆盖偏产品侧”。
- 如果用户只给了品牌名，没有给链接，也没有要求联网，优先写出需要补的官方页面类型。
- 如果观察只能从文字页面推断，标记为“推断项”，不要假装看到了图像细节。
- 把每一条观察都转成控制指令，避免停留在“高级、极简、未来感”这类空词上。

## 专业质量门

在输出 v1 级研究库前，逐项检查：

- 是否至少覆盖了 3 类官方来源。
- 是否每个来源都保留了原始链接。
- 是否把观察拆成可执行变量，而不是审美形容词。
- 是否写明了 `Prompt Translation Rules` 和 `Failure Risks`。
- 是否至少点出 1 条“不应照抄”的元素。
- 是否使用了非官方、安全的归纳措辞。
- 是否能直接被后续 prompt director 或提案文档接走。

如果有任一项缺失，先补齐再交付。
