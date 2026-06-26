# Benchmark Suite

用这些基准检查本 skill 是否真的能把官方页面研究转成可执行视觉规则，而不是只会写品牌摘要。

## 验收基准 1：Apple 消费电子海报前置研究

输入：

```text
Use $brand-visual-research-builder. 研究 Apple iPhone 的官方公开页面，给我一个 compact research bank，后面我要做消费电子海报方向。
```

期望输出：

- 至少 3 个 Apple 官方链接
- 一句话视觉结论
- 能落到轮廓、材质、背景、留白、风险

Fail if：

- 没有链接
- 只写“高级、简洁、科技感”
- 没有 failure risks

## 验收基准 2：Nike 鞋类主视觉规则

输入：

```text
Use $brand-visual-research-builder. 研究 Nike Air Max Dn8 的公开页面，把结论翻成鞋类主视觉的镜头、光线、材质和避免项。
```

期望输出：

- 来源含 Nike Newsroom 和产品页
- 镜头规则明确
- 风险里指出俗套速度特效和失真鞋底

Fail if：

- 只给品牌故事，不给可控变量
- 不区分运动能量和奢侈品棚拍

## 验收基准 3：Porsche 只做研究不出 Prompt

输入：

```text
Use $brand-visual-research-builder. 先研究 Porsche 911 的官方页面，告诉我适合迁移的视觉领地和不能照抄的元素，不要写 prompt。
```

期望输出：

- 明确是研究模式
- 有来源链接
- 说出道路接触、曲线高光、黄昏张力等变量
- 说出 badge、具体构图、 campaign 版式不能照抄

Fail if：

- 仍然输出平台 prompt
- 没说版权/识别性风险

## 验收基准 4：Dyson 产品演示图规则

输入：

```text
Use $brand-visual-research-builder. 研究 Dyson Airwrap i.d. 的官方页面，帮我总结适合做产品演示图的视觉规则。
```

期望输出：

- 同时抓到产品页和新闻页
- 写清楚器具结构、手势、发丝、气流逻辑
- 风险里点名手部错误和廉价电商感

Fail if：

- 只写“高级美容科技”
- 完全忽略使用动作

## 验收基准 5：Aesop 空间与产品混合研究

输入：

```text
Use $brand-visual-research-builder. 研究 Aesop 的产品页、设计哲学和空间页面，给我一个能转成空间效果图与产品静物图的 research bank。
```

期望输出：

- 有产品页、设计哲学页、空间页
- 可迁移元素包括材质、光线、秩序和建筑感
- 不照抄标签与店铺布局

Fail if：

- 把 Aesop 讲成普通香水品牌
- 没指出店铺与标签的高风险复制问题

## 验收基准 6：Apple 与 Aesop 品牌对标

输入：

```text
Use $brand-visual-research-builder. 对比 Apple 和 Aesop 的公开页面视觉差异，我想知道一个更偏工业精密，一个更偏建筑触感时，后续 prompt 变量该怎么分开。
```

期望输出：

- 有双方官方来源
- 明确镜头、材质、色彩和留白差异
- 说清两个品牌不能共用一套“高级极简”模板

Fail if：

- 只说一个更科技，一个更文艺
- 没有具体变量差异

## 验收基准 7：严格品牌合规需求

输入：

```text
Use $brand-visual-research-builder. 我需要一份严格符合某品牌官方规范的提案，请直接按官网研究替我生成完整规则。
```

期望输出：

- 明确说明公开页面研究不能替代正式 brand guideline
- 仍给可用的公开研究方向
- 提醒需要用户提供正式官方资料

Fail if：

- 直接声称能输出官方规范
- 完全不提授权边界

## 验收基准 8：只给官方链接

输入：

```text
Use $brand-visual-research-builder. 我只给你这几个官方链接，请不要自己去找第三方资料，帮我整理品牌视觉研究库。
```

期望输出：

- 只基于提供链接
- 如果证据不足，会明确标注
- 保持来源 log 清晰

Fail if：

- 擅自引入第三方页面
- 假装证据已经充分

## 验收基准 9：研究后迁移到新主体

输入：

```text
Use $brand-visual-research-builder. 研究 Porsche 911 的公开页面，但我后面不是做车，是做受它启发的机械腕表方向。请提前告诉我哪些只能借气质，哪些绝对不能照抄。
```

期望输出：

- 说明可借的是道路张力、金属高光、黄昏氛围
- 明确不能照抄轮廓、徽章、车型识别元素
- 转译方向指向腕表材质和结构，而不是赛车语言

Fail if：

- 仍然输出汽车生成策略
- 没分清“借气质”和“借形体”

## 验收基准 10：证据不足时的保守输出

输入：

```text
Use $brand-visual-research-builder. 这个品牌只有一页很薄的官方故事页，没有产品页和新闻页。帮我做研究，但不要过度推断。
```

期望输出：

- 明确证据等级不足
- 结论保守，不装作品牌视觉已被充分证明
- 把后续建议写成“下一步应补什么官方来源”

Fail if：

- 仍然写出很确定的品牌视觉规则
- 不说明证据缺口
