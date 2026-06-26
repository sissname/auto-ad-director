---
name: campaign-contact-sheet-director
description: 为广告系列生成统一风格的 6/9/12/16 格 contact sheet，建立 style anchor，按广告、产品、时尚、空间场景拆出 shot taxonomy、逐格 shot logic 和平台 prompts。Use when the user asks for a multi-frame campaign, pitch-deck contact sheet, launch visual sequence, lookbook grid, retail/spatial proposal board, or wants one brief expanded into a coherent series instead of random single images.
---

# Campaign Contact Sheet Director

## 核心工作流
把 brief、参考图描述、品牌方向、场地条件或单张英雄图需求，转成同一 campaign 世界观下的多格 contact sheet。
1. 先识别任务模式：从零生成、基于已有 brief 扩格、已有 hero 图延展、只做结构策划、不写平台 prompt。
2. 先写 style anchor 六件套：品牌承诺、情绪温度、主色/材质、光线逻辑、镜头气质、不可破坏约束。
3. 再决定格数：6 格适合快提案，9 格适合标准 campaign，12 格适合渠道覆盖，16 格适合大提案或空间项目。
4. 读取 `references/contact-sheet-framework.md`，用对应格数配方拆出 narrative spine，而不是平均分配画面。
5. 读取 `references/shot-taxonomy.md`，为每一格指定明确 shot role，避免每格都像 hero 图。
6. 读取 `references/platform-prompt-formats.md`，为每一格输出平台 prompt；默认给主平台版本，用户要求时再补全全部平台。
7. 输出时必须包含：style anchor、grid plan、逐格 shot logic、platform prompts、negative risks、统一性检查。
8. 如果用户只要结构，不要假装已经生成图片；如果用户只给文字，不要假装看过参考图。

## 任务接收清单

- 输入 brief 是否说清楚：卖什么、卖给谁、在什么场景说服对方。
- 是否已有固定主体：产品、人物、空间、装置、包装、服装系列。
- 是否已有 style anchor：品牌气质、关键词、禁区、参考方向、季节或地域信息。
- 是否明确输出格数：6 / 9 / 12 / 16。
- 是否明确场景类型：广告、产品、时尚、空间。
- 是否需要平台 prompt：Midjourney、即梦、通用中文模型，或只做 shot plan。
- 是否需要社媒裁切、安全留白、标题区、logo 区、横竖版兼容。
- 如果信息不全，先补最影响统一性的部分：主体、情绪、光线、场景。

## Reference Routing

- 只要开始做 contact sheet，先读 `references/contact-sheet-framework.md`。
- 需要给每一格安排 shot role、避免重复镜头时，读 `references/shot-taxonomy.md`。
- 需要落成可复制的平台 prompts 时，读 `references/platform-prompt-formats.md`。
- 用户要看完整示例、参考输出口径或不同场景写法时，读 `references/examples.md`。
- 用户要做专业评审、给客户讲为什么这组图成立时，读 `references/quality-scorecard.md`。
- 当前 brief 与历史难题高度相似，或你需要更稳的修正路径时，读 `references/case-library.md`。
- 做自测、比较版本成熟度或检查是否达标时，读 `references/benchmark-suite.md`。

## 输出模式

### 标准交付

```text
Contact Sheet Brief：
- 场景类型：
- 格数：
- 主平台：
- 目标用途：

Style Anchor：
- 品牌承诺：
- 情绪温度：
- 主色 / 材质：
- 光线逻辑：
- 镜头气质：
- 不可破坏约束：

Grid Plan：
- Frame 01：
- Frame 02：
- Frame 03：
- ...

逐格 Shot Logic：
- Frame 01
  Role：
  为什么在这一格：
  主体与动作：
  镜头与构图：
  光线与材质：
  连续性钩子：
  平台 Prompt：

统一性检查：
- 必须重复出现的 anchor：
- 可变化的变量：
- Negative risks：
```

### 只做结构策划

```text
Campaign Spine：
- 这组图在卖什么：
- 这组图的观看顺序：
- 哪几格负责吸引：
- 哪几格负责解释：
- 哪几格负责转化或裁切：

建议格数：
- 推荐：
- 为什么不是更少：
- 为什么不是更多：

Shot Map：
- Frame 01：
- Frame 02：
- ...
```

### 从已有 Hero 图扩格

```text
已有 Hero 图保留项：
- 必须保留的风格信号：
- 必须保留的光线逻辑：
- 必须保留的材质或颜色：

扩格原则：
- 新增镜头负责补什么：
- 哪些镜头只做信息补充：
- 哪些镜头承担社媒或裁切任务：

新增 Frame 列表：
- Frame 02：
- Frame 03：
- ...
```

### 专业提案版输出

```text
提案摘要：
- 这组图的核心承诺：
- 推荐格数与理由：
- 推荐主平台：

Style Anchor Audit：
- 必须锁定的锚点：
- 可以变化的变量：
- 最容易跑偏的点：

Frame Matrix：
- Frame 01：Role / 价值 / Prompt
- Frame 02：Role / 价值 / Prompt
- ...

客户要听懂的结论：
- 为什么这些格子不是随机拼图：
- 哪几格负责吸引：
- 哪几格负责证明：
- 哪几格负责传播：

执行提醒：
- 先出哪几格验证方向：
- 哪几格最值得做 A/B：
- 哪些内容建议后期补字：
```

## 案例复盘

当 brief 与已知场景高度接近，先去 `references/case-library.md` 找最近案例，再决定：
- 哪些 anchor 可以直接迁移
- 哪些镜头结构可以复用
- 哪些风险要提前规避
- 哪些平台提示需要收紧

不要把案例文本整段复述给用户；只提炼“可迁移逻辑”和“当前项目要改的部分”。

## v1 专业质量门

- 不能只有“好看”的形容词，必须给出逐格 role。
- 不能只有 hero 图，必须有证明材质、说明关系、承担裁切的格子。
- 不能只说统一，要明确哪些 anchor 固定、哪些变量变化。
- 不能只给 prompt，不解释为什么这样分格。
- 不能忽略平台差异；至少说明主平台和一个备用平台。
- 不能忽略社媒、标题区、横竖版中的至少一种交付限制。
- 如果用户明确要提案级输出，结尾必须给“先做哪几格验证方向”和“最容易翻车的风险”。

## 默认策略

- 用户没指定格数时：标准 campaign 默认 9 格，产品发布默认 6 或 9 格，时尚 lookbook 默认 12 格，空间提案默认 16 格。
- 用户没指定平台时：先输出通用中文版本，再补 Midjourney 简版。
- 不要把每一格都写成高饱和 hero 图；至少要有建立世界、解释材质、推进动作、交代环境、预留裁切的分工。
- 如果用户要求“统一但不要重复”，优先固定光线、材质、色温、镜头家族，再变化景别、动作、视角和构图密度。
- 对广告和产品场景，优先保证主体可辨识；对时尚场景，优先保证姿态、造型关系和版面节奏；对空间场景，优先保证动线、入口、节点和拍照点关系。
- 遇到文字、logo、UI、包装小字，优先建议留空位后期补字，不承诺模型稳定生成精确文案。
