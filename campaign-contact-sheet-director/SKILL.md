---
name: campaign-contact-sheet-director
description: 将品牌、广告、产品、时尚或空间 brief 转成 6/9/12/16 格 campaign contact sheet 的统一风格策划、镜头分配、逐格 shot logic 与多平台 prompts。Use when the user needs a coherent multi-frame campaign board, launch visual system, shot list, proposal deck image plan, or cross-platform prompt package where every frame must share a style anchor while still having a distinct frame purpose.
---

# Campaign Contact Sheet Director

## 核心工作流

把用户给出的 brief、方向词、参考图分析结论或既有 campaign 概念，重组为“统一锚点下的多格系列画面”而不是一串彼此无关的单图 prompt。
1. 先判断任务模式：新建 6/9/12/16 格方案、已有方案扩格、只做 shot plan、只做平台 prompts、或做 review and repair。
2. 必先读取 `references/contact-sheet-framework.md`，建立 style anchor：品牌气质、叙事阶段、镜头系统、光线系统、色温、材质处理、版式留白、裁切纪律。
3. 必先读取 `references/shot-taxonomy.md`，决定每格属于 hero、detail、lifestyle、motion、environment、macro、portrait、social crop 中的哪一类，不允许所有格子都写成 hero 图。
4. 根据需求场景读取 `references/scenario-playbooks.md`，在 advertising、product、fashion、spatial 四类里选择最接近的打法。
5. 根据格数完成镜头配比，保证“封面图、信息补位图、节奏变化图、收口图”都存在。
6. 每一格都写清楚 shot logic：画面目的、主体、镜头距离、镜头高度、构图、动作、背景、光线、与锚点的连续关系、失败风险。
7. 需要落地生成时，再读取 `references/platform-prompt-matrix.md`，输出 master anchor prompt 和逐格平台 prompts。
8. 如果用户要求专业提案级输出或二次修订，追加读取 `references/quality-scorecard.md` 与 `references/case-library.md` 做质量把关和案例复盘。

## 任务接收清单

先补齐以下信息；缺什么就基于现有信息合理假设并显式写出假设。

- 任务目标：提案、投放、风格探索、拍摄前置、AI 生图出图、社媒连发、空间效果图。
- 主场景：advertising、product、fashion、spatial。
- 交付格数：6 / 9 / 12 / 16。
- 主体对象：车、产品、模特、空间、装置、包装、多人或混合主体。
- 统一锚点：品牌关键词、情绪、色彩、材质、时间段、地点、镜头语言。
- 非复制约束：不能照搬的参考元素、logo/文字风险、版权敏感对象、禁用风格。
- 平台范围：Midjourney、即梦、可灵、Nano Banana、Seedream、通用中文模型。
- 输出深度：只要 shot list、要 prompt package、还是要 review and repair。

## Frame Count Decision

优先按叙事密度而不是“越多越好”来选格数。

- `6 格`：适合单一主线 campaign，强调 1 个 hero + 2 个支撑镜头 + 2 个变化镜头 + 1 个收口镜头。
- `9 格`：适合标准提案页或内容矩阵，能同时兼顾英雄图、细节、人物/动作、环境和社媒裁切。
- `12 格`：适合中等复杂项目，能够覆盖横版/竖版需求、两轮节奏变化和更完整的叙事弧线。
- `16 格`：适合大型 campaign system、品牌发布、完整空间提案或多平台联动，需要显式分成 4 个小章节。

如果用户没指定格数：

- 需求偏提案或需要“看起来像一套完整 campaign”时，默认 `9 格`。
- 需求偏高端发布、品类丰富、要兼顾横竖版时，默认 `12 格`。
- 只想快速看方向是否成立时，默认 `6 格`。
- 需要覆盖多个子场景、多个裁切和多个触点时，默认 `16 格`。

## Reference Routing

- 每次都先读 `references/contact-sheet-framework.md`。
- 每次都先读 `references/shot-taxonomy.md`。
- 涉及 advertising、product、fashion、spatial 任一场景时，读 `references/scenario-playbooks.md` 对应小节。
- 需要真正输出平台 prompts 时，读 `references/platform-prompt-matrix.md`。
- 用户要看格式示例、中文模板或示范任务时，读 `references/examples.md`。
- 做自测、验收或回归时，读 `references/benchmark-suite.md`。
- 用户要求“专业一点”“提案可交付”“帮我挑哪里还不够成熟”时，读 `references/quality-scorecard.md`。
- 用户的 brief 与既有成熟 pattern 接近，或你想减少重新发明结构的风险时，读 `references/case-library.md`。

## 输出模式

### Contact Sheet Blueprint

当用户要“先把这一套镜头搭出来”时，返回：

```text
项目定义：
- 场景类型：
- 格数：
- 目标用途：
- 核心主体：
- 已知约束：
- 关键假设：

统一 Style Anchor：
- 品牌/情绪：
- 光线系统：
- 镜头系统：
- 色彩与材质：
- 构图纪律：
- 后期与质感：
- 不能复制：

格子规划：
1. Frame 01 | [shot type] | 这格负责什么
2. Frame 02 | [shot type] | 这格负责什么
...

连续性规则：
- 必须重复出现的锚点：
- 可以变化的变量：
- 节奏推进方式：
- 裁切与版式留白：
```

### Per-frame Prompt Package

当用户要完整多平台 prompts 时，返回：

```text
Master Anchor Prompt：
[用于整套画面统一风格的总锚点]

Per-frame Prompt Package：
Frame 01
- Shot type：
- Shot logic：
- Continuity link：
- Midjourney：
- 即梦：
- 可灵：
- Nano Banana：
- Seedream：
- 通用中文模型：
- Negative risks：

Frame 02
...

Assembly Notes：
- 哪几格必须最先出图验证：
- 哪几格容易跑偏：
- 如果整套不统一，先锁哪个变量：
```

### Adapt Existing Direction

当用户已有部分镜头或已有一张 hero 图，要求“扩成一套 contact sheet”时，返回：

```text
现有锚点复述：
- 已经成立的部分：
- 需要补足的空位：

扩格策略：
- 保持不变：
- 新增镜头类型：
- 新增节奏段落：
- 需要避免的重复：

扩格清单：
Frame 01 ...
Frame 02 ...
```

### Review and Repair

当用户已经拿到一套 contact sheet，但怀疑“像拼贴而不是一套 campaign”时，返回：

```text
Review and Repair：
- 当前阶段：
- 最强锚点：
- 断裂点：
- 过度重复的镜头：
- 缺失的镜头功能：
- 优先修复顺序：

Repair actions：
1. 先统一什么
2. 再替换哪几格
3. 哪几格保留
4. 哪几格需要重写 prompt
```

## 默认约束

- 不要把 6/9/12/16 格当成“同一张 prompt 的不同裁切”；每格都必须有独立角色。
- 不要让所有格子都使用同一个镜头高度和同一个构图比例。
- 不要只会写气氛词；每格至少落到主体关系、镜头、光线或动作之一。
- 涉及文字、包装、屏幕界面、海报标题时，优先给留白和后期补字方案，不承诺模型稳定出字。
- 当用户只给抽象方向时，先帮他把 anchor 拆清楚，再写 frame prompts。
- 当用户给了参考图分析但没有原图时，可以继续工作，但必须标记“基于参考结论重建，而非直接识图”。

## v1 专业质量门

- 整套输出必须先有 `Master Anchor Prompt`，再有逐格 prompt；不能只有 9 条散 prompt。
- 至少覆盖 4 种 shot type；否则画面会像重复试拍而不是 campaign。
- 每一格都必须说明自己为何存在，不能只写“另一个角度的 hero 图”。
- 必须显式说明整套中哪些变量固定、哪些变量允许变化。
- 平台 prompts 必须体现各平台差异，而不是单纯翻译。
- 遇到 advertising、product、fashion、spatial 时，必须体现对应场景的物理和商业逻辑。
- 如果做 review and repair，必须指出“保留项 / 替换项 / 重写项”三类动作。
- 结束前自查：这套输出是否真的能被别人拿去按格出图、排版和提案；如果不能，先补全再输出。
