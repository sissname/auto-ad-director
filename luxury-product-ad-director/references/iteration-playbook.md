# Iteration Playbook

## 何时只做诊断

优先只做诊断，不直接重写整包 prompt 的情况：

- 用户已经有一轮能用图，只是某几个部位翻车。
- 用户要在多张图中选最值得修的方案。
- 用户没有给参考图，只描述“总觉得不够贵”。

此时先用 `quality-scorecard.md` 给出 `质量分`，再决定修法。

## 最小修复优先级

1. 主体结构
2. 材质真实度
3. 光影纪律
4. 品类正确性
5. 身体关系
6. 品牌气质
7. 装饰和氛围

## 常见修复动作

### 香水

- 如果瓶体脏：减少环境元素，强调 precise silhouette、clean glass edge、controlled liquid transparency。
- 如果太像电商图：补充空气、倒影、表面材质和 light falloff，而不是只加“cinematic”。
- 如果花香过俗：删掉花瓣，用湿度、色温、距离感表达香气。

### 腕表

- 如果金属太塑料：把材质拆成 brushed / polished 两类分别写。
- 如果表盘像贴图：强调 dial depth、applied markers、hands axis、clean crystal reflection band。
- 如果佩戴不可信：改成更静的腕部动作，减少大幅运动。

### 珠宝

- 如果宝石假：减少 sparkle，强调 cut planes、internal light、setting precision。
- 如果皮肤假：改成局部构图，限制美颜感和磨皮感。
- 如果婚庆感太重：删掉暖色布景和夸张 pose。

### 包袋

- 如果包型塌：强调 structured silhouette、defined edges、believable weight。
- 如果皮革假：增加 grain、waxed sheen、edge paint、crease logic。
- 如果人体抢戏：降低服装和表情存在感，让包袋重新成为主角。

## 下一轮写法

每次只允许 1-2 个主改动，格式如下：

```text
下一轮策略：
- 保留：上一轮最成立的 2 件事
- 主改动：本轮只改的 1-2 个问题
- 风险观察：最容易被新修改带坏的地方
```
