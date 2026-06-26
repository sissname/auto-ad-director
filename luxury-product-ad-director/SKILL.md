---
name: luxury-product-ad-director
description: Build luxury product advertising prompt packages for perfume, watches, jewelry, and bags. Use when Codex needs category-specific hero still life, macro detail, reflection/refraction control, material rendering, or fashion hand/body relation prompts for high-end product imagery, campaign key visuals, prompt bibles, or generation repair. 中文适用：香水、腕表、珠宝、包袋广告图提示词；hero still life、微距、反射/折射、材质表现、手部/身体关系、campaign prompt bible，以及避免 generic black-gold luxury 的高端产品视觉方向。
---

# Luxury Product Ad Director

## Core Workflow

把用户 brief、参考图描述、失败图问题或 campaign 方向，翻译成适合高端产品广告生图的可执行 prompt package。

1. 先判断品类：香水、腕表、珠宝、包袋；不要混用材质逻辑。
2. 再判断画面模式：`Hero Still Life`、`Macro / Material Detail`、`Reflection / Refraction Study`、`Hand / Body Relation`。
3. 把输入拆成商业约束：产品卖点、价格带、品牌气质、投放场景、是否允许人体、是否需要后期补字。
4. 建立 style anchor，不要直接写“黑金奢华”“高级感拉满”这种空词。
5. 依据品类决定镜头、光线、表面、景深、背景和容易翻车的部位。
6. 输出时至少给出：画面目标、镜头逻辑、材质逻辑、主 prompt、负面约束、下一轮测试点。
7. 如果用户要求 `Prompt Bible`，追加 hero、macro、body relation 三类 shot 的成套语言。
8. 如果用户给的是失败图描述，先指出失败类型，再给最小修复动作，不要直接整套重写。
9. 交付前跑一次反套路检查，确认结果没有滑向 generic black-gold luxury。

## 任务接收清单

- 产品是什么：香水、腕表、珠宝、包袋中的哪一类。
- 输出模式是什么：单张 hero、微距材质、手 / 身体关系、完整 Prompt Bible。
- 想卖的不是“贵”，而是哪种贵：冷静工艺、感性诱惑、收藏价值、手工温度、都市权力、旅行自由、稀有宝石光学等。
- 是否有必须保护的细节：表盘刻度、宝石切面、皮革纹理、液体颜色、金属硬件、缝线、扣具、链条、瓶盖结构。
- 是否允许人体出镜；如果允许，是手、腕、耳颈、锁骨、肩背还是半身局部。
- 是否需要控制可后期补字区域；默认不要让模型硬写品牌文案。

## Reference Routing

- 每次都读 `references/luxury-visual-framework.md`，它负责把“高端产品广告”拆成可操作的镜头和布光语言。
- 只要涉及具体品类，就读 `references/category-material-camera-logic.md`，不要把香水的玻璃逻辑套给包袋，也不要把珠宝的 sparkle 逻辑套给腕表。
- 用户要看示例或我需要一个安全的输出骨架时，读 `references/examples.md`。
- 用户要求成套交付、campaign 包或主副镜头体系时，读 `references/prompt-bible-examples.md`。
- 需要正式评分、选图、给客户评审意见时，读 `references/quality-scorecard.md`。
- 用户要求“参考一个已有成功 / 失败案例”或我需要更稳的迁移逻辑时，读 `references/case-library.md`。
- 用户已经出过图，需要只做诊断、最小修复或下一轮策略时，读 `references/iteration-playbook.md`。
- 做自测、验收、回归检查时，读 `references/benchmark-suite.md`。

## 输出模式

### Hero Still Life

返回：

```text
项目目标：
- 品类：
- 卖点：
- 画面模式：

Style anchor：
[一段可复用的高端产品视觉系统]

镜头与场景逻辑：
- 镜头：
- 光线：
- 材质反应：
- 背景 / 台面：
- 留白 / 文案位：

主 Prompt：
[可执行 prompt]

负面约束：
[要压制的失败]
```

### Macro / Material Detail

返回：

```text
Detail target：
- 想强调的工艺：
- 不能坏的细节：

Macro logic：
- 焦段 / 机位：
- 光比：
- 反射 / 折射控制：
- 景深策略：

Detail Prompt：
[可执行 prompt]

Negative constraints：
[微距最容易翻车的地方]
```

### Hand / Body Relation

只在人体能增强商品价值时使用。返回：

```text
Body relation goal：
- 出现部位：
- 商品与身体的关系：
- 姿态限制：

Body-safe Prompt：
[可执行 prompt]

风险观察：
- 手指 / 指甲 / 关节：
- 皮肤质感：
- 产品比例：
- 配饰冲突：
```

### Prompt Bible

当用户要完整交付包时，至少包含：

```text
Project：
Category：

Style anchor：
[统一视觉 DNA]

Shot system：
- Hero：
- Macro：
- Reflection / Material：
- Hand / Body Relation：

Prompt stack：
- 主视觉 Prompt：
- 细节 Prompt：
- 人体关系 Prompt：

Negative base：
[跨 shot 通用负面约束]

Next test：
- 保留什么：
- 下一轮试什么：
- 最怕什么：
```

### 专业评审包

当用户需要“这张图到底能不能交”“几张图里选哪张”“下一轮怎么修”时，返回：

```text
专业评审包：
- 品类：
- 使用场景：
- 评审目标：

质量分：
- 主体结构：
- 材质真实度：
- 光影纪律：
- 品类正确性：
- 身体关系：
- 品牌气质：
- 商业可用性：
- 文字 / logo 风险：

结论：
- 保留 / 小修 / 大修 / 重做

最小修复动作：
- 保留什么：
- 先改什么：
- 暂时不要改什么：
```

### 案例复盘

当用户要求“参考之前的类似成功 / 失败经验”时，返回：

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

- 不要用 `generic black-gold luxury` 代替真正的品牌与材质判断。
- 不要让香水像电商白底修图，也不要让珠宝、腕表、包袋全部落进同一种棚拍模板。
- 不要要求模型稳定输出品牌 logo、精细排版或可读长文案；默认预留后期补字区域。
- 不要把 `bling`、`sparkle`、`diamond dust` 滥用到所有品类。
- 人体一旦出镜，必须把手部比例、皮肤质感、佩戴方式和产品受力关系写清楚。
- 失败修复优先级始终是：主体结构 > 材质真实度 > 光影逻辑 > 品牌气质 > 装饰氛围。

## 反套路检查

如果结果出现以下问题，先自改一轮再输出：

- 只有“高级、奢华、电影感、黑金”这类形容词，没有镜头和材质逻辑。
- 香水、腕表、珠宝、包袋的 prompt 互换后几乎也能成立。
- 光线只会写 rim light、sparkle、dramatic shadow，没有说明为什么适合这个材质。
- 人体出镜只是“拿着产品”，没有建立产品与身体的关系。
- 过度依赖漂浮烟雾、金粉、镜面地台、黑金渐变、假性 bokeh。

## v1 专业质量门

交付前检查：

- 有没有明确区分品类，而不是把同一套“贵感”复制到四类产品。
- 有没有把 Hero、Macro、Hand / Body Relation 的任务分工写清楚。
- 有没有说明最脆弱的材质部位和结构部位。
- 如果给了评分，`质量分` 是否能转成行动，而不是审美形容词。
- 如果涉及人体，是否明确写了比例、抓握、佩戴、皮肤与商品的关系。
- 如果用户要求修图或下一轮 prompt，是否提供了最小修复动作，而不是整包重写。
- 有没有主动避开 generic black-gold luxury、过量 sparkle、假性贵气滤镜。

任一项答不上来，就不要当作专业版交付。
