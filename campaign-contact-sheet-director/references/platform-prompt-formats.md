# Platform Prompt Formats

## 适合谁

- 需要把逐格 shot logic 落成可复制 prompt 的人
- 同一组图要交给不同平台出图的人

## 解决什么问题

- 让 contact sheet 不止有构图说明，还有可执行 prompt
- 在 Midjourney、即梦、通用中文模型之间保持统一锚点

## 通用写法顺序

先写固定锚点，再写本格变量：
1. 主体
2. 场景
3. 动作或叙事目的
4. 镜头与构图
5. 光线与材质
6. 风格锚点
7. 输出约束

## Midjourney

适合：结构短、镜头明确、需要快速出多版。

```text
[主体], [场景], [动作或关系], [镜头与构图], [光线与材质], [style anchor], campaign contact sheet frame [编号], no extra products, no broken anatomy, no random text --ar [比例] --stylize [数值]
```

写法提醒：
- 保持短句和逗号节奏
- 把 frame role 写进 prompt，例如 `frame 03 detail proof`
- 需要统一时，把 style anchor 原词重复

## 即梦

适合：中文描述更完整、需要把画面意图说清楚。

```text
为同一组 campaign contact sheet 的第 [编号] 格生成画面。
主体是：[主体]。
这格负责：[role]。
画面场景：[场景]。
镜头与构图：[镜头与构图]。
光线与材质：[光线与材质]。
必须延续的统一锚点：[style anchor]。
避免：[negative risks]。
```

写法提醒：
- 用“这格负责什么”明确 role
- 中文描述不要空泛，多给材质和光线信息

## 通用中文模型

适合：平台不明确、要交给不同工具手动改写、或让新手直接复制。

```text
同一组品牌 campaign contact sheet，第 [编号] 格。
保持统一的 [情绪温度]、[主色与材质]、[光线逻辑]、[镜头气质]。
本格重点表现 [role]： [主体与动作]。
采用 [构图]，强调 [材质 / 空间 / 人物关系]。
保留 [连续性钩子]，避免 [negative risks]。
```

## 逐格交付建议

- 默认只给主平台 prompt，避免一次性 16 格 x 3 平台造成噪音
- 用户说“全部平台都要”时，再按同一 frame 顺序补齐
- 每格 prompt 后面都附一行 `为什么这样写`

## 常见坑

- 只复制同一个 prompt 换编号，没有逐格差异
- 负面约束只写一次，后面全丢
- 场景变了，但 style anchor 没重复，导致整组漂移
- 社媒裁切格仍然沿用横版构图

## 原始来源

- 路线要求：`J:\005-Auto-Ad-Director-Skill-发布归档\00-总览索引\NEXT-SKILL-ROADMAP.md`
