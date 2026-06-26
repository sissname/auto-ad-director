---
name: spatial-installation-prompt-director
description: Turn mall displays, pop-ups, exhibitions, immersive corridors, site photos, or text briefs into spatial-installation prompt packages. Use when Codex needs entrance, installation device, lighting, floor graphic, traffic flow, photo point prompts, proposal summaries, or commercial-space effect-image direction. 中文适用：商场美陈、快闪店、展陈空间、沉浸通道、现场照片分析、活动空间效果图、空间提案摘要、入口门头、主装置、灯光、地贴、动线与拍照点提示词。
---

# Spatial Installation Prompt Director

## Core Workflow

把用户给的场地照片、平面描述、活动 brief 或失败效果图，翻译成能直接用于空间提案与 AI 效果图生成的 prompt package。

1. 先判断场景类型：`Mall Display`、`Pop-up`、`Exhibition`、`Immersive Corridor`。
2. 再判断输入类型：现场照片、场地平面 / 描述、已有方向稿、失败效果图。
3. 把需求拆成六个固定交付区：入口、主装置、灯光、地贴、动线、拍照点。
4. 建立统一 style anchor，避免每个区各说各话。
5. 把空间语言转成可执行 prompt，同时保留提案摘要与风险提示。
6. 如果用户给的是失败图或弱方向，先指出最小修复动作，再改 prompt。
7. 输出前检查：尺度是否可信、动线是否可走、灯光是否服务主题、拍照点是否有传播价值。

## 任务接收清单

- 项目类型：商场中庭、品牌快闪、品牌展陈、沉浸通道中的哪一种。
- 活动主题：新品发布、节点营销、IP 联名、品牌周年、艺术展、互动体验等。
- 场地约束：层高、柱网、入口朝向、消防边界、设备点位、是否可吊挂、是否能封顶。
- 目标人群：亲子、年轻潮流、轻奢消费、商务人群、旅游客流等。
- 交付目标：单张效果图、整套方向包、提案摘要、失败修复。
- 品牌限制：主色、logo 位、不能碰的符号、预算感、是否允许大面积屏幕。
- 传播目标：打卡传播、导流进店、停留时长、事件感、夜间可见性。

## Site Intake Decision

### 现场照片输入

优先识别：

- 真实入口在哪里，第一视线看到什么。
- 天花、立柱、扶梯、店招、玻璃幕墙是否会抢主视觉。
- 人流主要从哪个方向切入，停留点和回头点在哪。
- 是否已经有不能移动的设备、广告位、服务台或围挡。

### 文字 brief 输入

至少补齐：

- 空间类型与大致尺度。
- 活动主题和品牌气质。
- 想优先做强的区：入口、装置、灯光、地贴、动线还是拍照点。
- 需要偏“销售导流”还是偏“事件体验”。

### 失败效果图输入

先判断失败属于哪一类：

- 只剩概念，没有空间构成。
- 装置很大，但入口识别弱。
- 灯光漂亮，但人流走不进去。
- 拍照点有趣，但与主装置脱节。
- 视觉很满，但像廉价临展，不像品牌提案。

## Reference Routing

- 每次都读 `references/spatial-installation-framework.md`，它负责把空间项目拆成统一交付结构。
- 只要涉及具体场景，就读 `references/scenario-playbooks.md`，不要把展陈空间的逻辑硬套给快闪店。
- 输入里出现现场照片、原始场地描述、扶梯中庭、入口视线、人流组织时，读 `references/site-intake-and-traffic-flow.md`。
- 用户要求完整交付包、Prompt Bible、提案结构或多区成套输出时，读 `references/prompt-bible-examples.md`。
- 用户要把视觉方向翻成客户能读懂的提案摘要、过会摘要或执行摘要时，读 `references/proposal-summary-playbook.md`。
- 用户要参考现成格式，或我需要一个安全的中文输出骨架时，读 `references/examples.md`。
- 用户要求判断“能不能提案”“哪一张能留”“哪里要修”时，读 `references/quality-scorecard.md`。
- 用户要求复用历史空间逻辑、迁移类似案例，或我需要更稳的修正路径时，读 `references/case-library.md`。
- 做自测、验收、回归时，读 `references/benchmark-suite.md`。

## 输出模式

### 单区方向包

适合用户只要入口、主装置或拍照点其中一类。

返回：

```text
项目目标：
- 场景类型：
- 优先区：
- 传播目标：

Style anchor：
[统一空间气质]

空间构成：
- 体块：
- 材质：
- 灯光：
- 视线焦点：

Prompt：
[可执行 prompt]

风险提醒：
[最容易翻车的地方]
```

### Zone Prompt Package

适合用户要完整提案方向或多区效果图。

返回：

```text
Project：
Scenario：

Style anchor：
[统一视觉 DNA]

Zone plan：
- Entrance：
- Installation Device：
- Lighting：
- Floor Graphic：
- Traffic Flow：
- Photo Point：

Prompt stack：
- Entrance Prompt：
- Device Prompt：
- Lighting Prompt：
- Floor Graphic Prompt：
- Traffic Flow Prompt：
- Photo Point Prompt：

Negative risks：
[跨区共用的失败约束]
```

### Proposal Summary

当用户需要把空间方向翻成提案摘要时，返回：

```text
提案摘要：
- 核心概念：
- 空间主叙事：
- 入口吸引动作：
- 主装置价值：
- 动线组织：
- 拍照传播机制：
- 执行风险：
```

### Review and Repair

当用户提供失败效果图描述或觉得“方案不成立”时，返回：

```text
问题诊断：
- 失败点：
- 根本原因：
- 风险级别：

最小修复动作：
- 保留：
- 先改：
- 暂不改：

修复 Prompt：
[改过的 prompt]
```

### 专业评审包

当用户要判断“这套空间方向能不能提案”“哪一张效果图能留”“下一轮应该修什么”时，返回：

```text
专业评审包：
- 场景类型：
- 评审目标：

质量分：
- 场地适配度：
- 入口识别度：
- 主装置记忆点：
- 动线可走性：
- 拍照传播性：
- 材质落地感：
- 品牌匹配度：
- 商业成熟度：

结论：
- 保留 / 小修 / 大修 / 重做

最小修复动作：
- 保留什么：
- 先改什么：
- 暂不改什么：
```

### Case Replay

当用户要求“参考类似成功经验”“把已有项目逻辑迁到新场地”时，返回：

```text
案例复盘：
- 最接近的案例：
- 能迁移什么：
- 不能照搬什么：

本次应用：
- 保留：
- 替换：
- 风险：

下一轮策略：
- 主改动：
- 验证点：
```

## 不能妥协的规则

- 不要只写“未来感、艺术感、沉浸感”这类概念词，必须翻成体块、尺度、材质、灯光和视线逻辑。
- 不要让入口、主装置、灯光、地贴、动线、拍照点彼此断裂；必须共享同一套 style anchor。
- 不要假设模型能稳定生成品牌 logo、可读长文案或精确导视；默认留后期补字区。
- 不要把所有空间都做成“弧形灯带通道 + 镜面地面 + 漂浮球体”的通用模板。
- 动线相关输出必须能解释“人从哪来、在哪里停、如何走向下一区”。
- 拍照点不是单独雕塑；它必须服务入口识别、品牌传播或店铺导流中的至少一个目标。

## v1 专业质量门

交付前检查：

- 有没有把入口、主装置、灯光、地贴、动线、拍照点的分工说清楚。
- 有没有说明场地的真实限制，而不是把任何地方都当白盒空间。
- 有没有给出可执行 prompt，而不是纯概念描述。
- 如果用户要提案摘要，是否已经把空间主叙事、传播动作和执行风险写清楚。
- 如果用户要评审或修图，`质量分` 是否能转成最小修复动作。
- 如果参考了案例，是否明确说出哪些可迁移、哪些不能照搬。
- 有没有主动避开通用灯带隧道、廉价乐园风、无动线雕塑岛、假 logo 导视。

任一项答不上来，就不要当作专业版交付。

## 默认策略

- 用户没指定场景类型时，优先按 `Mall Display` 处理商场中庭，按 `Pop-up` 处理店前区或短期活动，按 `Exhibition` 处理内容型展陈，按 `Immersive Corridor` 处理线性通道。
- 用户没给平台时，先输出通用中文 prompt，再补一个 Midjourney 简版，避免把平台参数当成空间逻辑本身。
- 用户只给一句主题时，先补齐空间类型、主要人群、入口记忆点和导流目标，再开始写六区方案。
- 用户只要漂亮效果图时，也要最少交代入口、主装置和动线三者关系，否则不算可提案方向。
- 真实品牌、logo、长文案、导视文字默认建议后期补字，不承诺模型直接稳定生成。
