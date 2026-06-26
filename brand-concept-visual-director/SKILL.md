---
name: brand-concept-visual-director
description: Generate, compare, review, and iterate AI visual direction drafts for early-stage brand concept exploration. Use when turning brand positioning, audience, references, preferences, forbidden zones, mood words, or rough logo/sketch ideas into 3-5 visual direction prompts, creative director review forms, next-round questions, brand moodboards, image-generation prompt packages, or when avoiding premature final-logo claims and SVG sketch overconfidence. 中文适用：品牌方向稿、品牌视觉探索、AI 方向图、品牌定位转视觉 prompt、参考图转方向、创意总监评审、3-5 个方向方案、logo 探索前期草案、禁止把 SVG 示意当最终专业 logo。
---

# 品牌方向稿视觉导演（Brand Concept Visual Director）

## 核心工作流

把品牌定位、参考图、用户偏好和禁区，转成可用于 AI 生图的 3-5 个视觉方向稿 prompt，并附上创意总监式评审和下一轮迭代问题。

1. 先锁定输入：品牌定位、目标用户、品类、语气、参考图角色、必须避免项、输出平台、方向数量。
2. 如果信息不足，给出保守默认并明确写出假设；不要编造品牌事实。
3. 读取 `references/brand-concept-framework.md` 建立方向拆解。
4. 涉及参考图、草图、SVG、logo 探索时，读取 `references/reference-and-logo-boundaries.md`。
5. 需要多方向输出、评审、迭代时，读取 `references/creative-review-scorecard.md`。
6. 输出 3-5 个方向，每个方向必须有：方向命名、适用判断、视觉系统、prompt、风险、下一轮问题。
7. 最后给出创意总监评审表，帮助用户选择方向，而不是承诺最终 logo 或最终品牌系统。

## 输入检查清单

- 品牌定位：一句话说明品牌是谁、服务谁、解决什么问题。
- 用户感受：希望用户感到安心、兴奋、专业、亲密、实验、奢华、轻松，还是别的。
- 参考图角色：只借光影/构图/气质，还是借材质、色彩、空间、图形节奏。
- 禁区：不要像哪些品牌、不要哪些颜色、不要哪些图形、不要哪些情绪。
- 输出目标：方向稿、moodboard prompt、社媒视觉、包装方向、空间方向、logo 前期探索。
- 文字/logo 策略：默认不要求图像模型生成精确文字或最终 logo。

## 参考资料路由

- 读 `references/brand-concept-framework.md`：所有方向稿任务都要读。
- 读 `references/reference-and-logo-boundaries.md`：有参考图、logo、SVG、草图、品牌资产、不可照抄项时读。
- 读 `references/creative-review-scorecard.md`：输出评审表、方向比较、成熟度判断、下一轮迭代时读。
- 读 `references/case-library.md`：任务接近阅读品牌、咖啡、护肤、AI 工具、生活方式品牌时读。
- 读 `references/examples.md`：用户要示例或需要紧凑输出样式时读。
- 读 `references/benchmark-suite.md`：测试、审计、升级 skill 时读。

## 输出格式

### 品牌方向稿交付包

```text
输入理解：
- 品牌定位：
- 目标用户：
- 关键词：
- 参考图角色：
- 禁区：
- 默认假设：

方向 1：[名称]
- 核心气质：
- 适合原因：
- 视觉系统：
- Prompt：
- 负面/风险：
- 下一轮问题：

方向 2：[名称]
...

创意总监评审：
| 方向 | 品牌贴合 | 识别性 | 延展性 | 生成可控性 | 风险 | 建议 |
| --- | --- | --- | --- | --- | --- | --- |

推荐下一步：
[建议保留/合并/淘汰哪些方向，以及下一轮怎么测]
```

### 只做方向审查

```text
方向审查：
- 最强方向：
- 最弱方向：
- 品牌偏移：
- 参考图误读：
- logo/文字风险：
- 下一轮要问的问题：
```

### Logo 前期探索安全输出

```text
Logo/符号探索说明：
- 这不是最终 logo：
- 可探索的视觉母题：
- 不应承诺的内容：
- 生图 prompt：
- 后续专业设计动作：
```

## 专业质量门

返回前检查：

- 是否输出了 3-5 个彼此有差异的方向，而不是同一个风格换词。
- 每个方向是否能转成可执行 prompt。
- 是否明确参考图只借鉴哪些要素、哪些不能复制。
- 是否避免把 SVG、AI 图、草图当成最终专业 logo。
- 是否有创意总监评审表和下一轮问题。
- 是否能帮助用户选择方向，而不是只给漂亮形容词。

不达标时，先修订一次再回答。
