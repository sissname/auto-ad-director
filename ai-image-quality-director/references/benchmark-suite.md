# Benchmark Suite

用这些基准测试本 skill 是否真的能给出评分、定位问题、输出修复动作和下一轮建议，而不是只会泛泛点评。

## 验收基准 1：人物手指数量错误

输入：

```text
Use $ai-image-quality-director. 这张 AI 时尚大片里模特左手有六根手指，脸和服装都不错。请评分、定位问题、给修复 prompt 和下一轮 note。
```

期望输出：

- 明确手部解剖是最高优先级问题
- 评分里结构与主体完整性明显低分
- 修复动作优先简化手势和分离边界
- 有 `Preserve / Test next / Watch`

Fail if：

- 只说“手有点怪”却没有具体修复动作
- 一上来就重做整个画面

## 验收基准 2：产品漂浮没有接触阴影

输入：

```text
Use $ai-image-quality-director. 一张耳机广告图主体悬在空中，没有接触阴影，背景和构图还不错。帮我判断值不值得修。
```

期望输出：

- 指出接地感失败
- 结论应是“小修”或“可修”
- 修复 Prompt 里包含 contact shadow 或 grounded placement

Fail if：

- 把问题归因为“缺少高级感”
- 没有说明为什么仍值得修

## 验收基准 3：瓶身标签乱码

输入：

```text
Use $ai-image-quality-director. 这张护肤品主视觉玻璃瓶很漂亮，但标签全是乱码。给我可直接使用的下一版 prompt。
```

期望输出：

- 指出文字 / logo 风险
- 建议 clean label area 或 blank typography space
- 不能继续要求模型生成精确文案

Fail if：

- 让模型“重新写对标签”
- 完全忽略瓶身材质表现

## 验收基准 4：汽车轮胎漂浮

输入：

```text
Use $ai-image-quality-director. 夜景汽车广告图氛围很好，但车轮像飘起来了。请给评分、失败原因和最小修复动作。
```

期望输出：

- 真实感与物理逻辑低分
- 最高优先级是 grounded wheels / contact shadow / wheel alignment
- 保留夜景氛围，不要整套推翻

Fail if：

- 只建议“更真实一些”
- 把夜景氛围也一起删掉

## 验收基准 5：高端香水做成廉价电商图

输入：

```text
Use $ai-image-quality-director. 这张香水图主体没坏，但太像普通电商白底，不像高端品牌。请做诊断并给下一轮策略。
```

期望输出：

- 品牌气质与风格一致性低分
- 指出是品牌语境、光线、材质和空间语汇的问题
- 下一轮策略不是只加“luxury”

Fail if：

- 只堆高级形容词
- 没有说清楚要改哪些具体变量

## 验收基准 6：空间效果图比例失真

输入：

```text
Use $ai-image-quality-director. 商场快闪店效果图入口做得很炫，但人和装置比例失真，像小人国。请先只做诊断。
```

期望输出：

- 使用“只做诊断”模式
- 点出尺度系统和透视关系错误
- 不输出修复 prompt

Fail if：

- 直接开始写 prompt
- 没有说明 visitor scale 的问题

## 验收基准 7：海报裁切不可用

输入：

```text
Use $ai-image-quality-director. 这张 4:5 海报主视觉挺帅，但人物头顶太满，品牌标题没地方放。给我商业可用性的判断和修复建议。
```

期望输出：

- 商业可用性低分
- 明确标题区、留白和裁切问题
- 修复动作包含 negative space 或 crop planning

Fail if：

- 只谈审美，不谈版式落地
- 没有提标题区冲突

## 验收基准 8：镜面反射里多出一个假人

输入：

```text
Use $ai-image-quality-director. 时尚大片里镜子反射出了第二个像实体一样的人，主模特本身还不错。请给我修复方案。
```

期望输出：

- 点出 reflection logic failure
- 修复动作强调一个主要反射面、real subject vs reflection
- 保留主模特的优点

Fail if：

- 把问题当作双人构图
- 没有针对反射逻辑给约束

## 验收基准 9：AI 脸部过度蜡像感

输入：

```text
Use $ai-image-quality-director. 这张人像广告脸部很像蜡像，皮肤过度磨平。帮我判断是修还是重做，并给原因。
```

期望输出：

- 指出材质和真实感失败
- 根据其他信息判断修或重做
- 修复建议包含 controlled skin texture 或降低过度磨皮

Fail if：

- 只说“不自然”
- 没有给决策依据

## 验收基准 10：风格堆词导致画面失焦

输入：

```text
Use $ai-image-quality-director. 这个 prompt 生成的图满是 cinematic、epic、premium，但画面很乱。请帮我定位问题并给出更好的下一版方向。
```

期望输出：

- 识别“风格堆词但没有画面逻辑”
- 建议用机位、光线、材质、留白替换空泛形容词
- 输出结构化下一轮计划

Fail if：

- 继续追加更多形容词
- 不指出 prompt 层面的根本问题

## 通过标准

这 10 条里，每一条都必须至少产出：

- 明确评分或优先级判断
- 问题定位
- 修复动作或明确说明只诊断
- 下一轮观察点或迭代说明
