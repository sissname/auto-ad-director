# 示例

以下示例用于展示输出节奏，不要机械照抄内容。

## 示例 1：产品主视觉漂浮

用户请求：

```text
用 $ai-image-quality-director 看一下这张 AI 生成的耳机广告图。产品悬在半空，背景是蓝色渐变，感觉有点假，帮我判断值不值得修。
```

输出模式：

```text
图像审查：
- 任务类型：单图评分
- 证据来源：基于描述推断
- 一句话总评：产品概念可用，但接地感和材质真实度不足，适合小修后继续。

评分卡：
- 结构与主体完整性：4/5
- 真实感与物理逻辑：2/5
- 构图与视觉层级：4/5
- 光线与材质表现：3/5
- 品牌气质与风格一致性：4/5
- 商业可用性：3/5
- 文字 / logo 风险：4/5
- 可修复性：4/5

决策：
- 结论：小修
- 最高优先级问题：缺少接触逻辑，耳机像抠图贴上去
- 最小修复动作：加入明确支撑关系、接触阴影和材质边缘高光
- 下一轮观察点：是否仍然有塑料感
```

## 示例 2：人物手部翻车

用户请求：

```text
这张 AI 时尚海报手很怪，脸还行。先别改图，只告诉我问题在哪。
```

输出模式：

```text
诊断结论：
- 核心问题：手部解剖错误，手指长度和弯曲关系异常
- 次级问题：手与服装边缘融合，前景分离不清
- 最可能的失败原因：近景手势复杂，但 prompt 没有约束手部姿态
- 哪些是生成模型常见问题：手部、首饰、布料边缘
- 哪些是 brief 或 prompt 造成的：动作描述太模糊
- 如果继续修，第一刀该改哪里：先简化手势，再加强手部与身体分离
```

## 示例 3：包装文案乱码

用户请求：

```text
这张护肤品包装图整体挺高级，但瓶身标签全是乱码。直接给我下一版修复 prompt。
```

输出模式：

```text
保留：
- 干净的瓶身轮廓
- 柔和高端的漫射光

修复：
- 必改问题：不要让模型生成具体标签文字
- 删除或收紧的描述：删除 exact label copy、precise typography
- 新增的物理/结构/光线约束：clean label area, blank packaging panel, crisp glass edge highlight

修复 Prompt：
premium skincare bottle hero shot, translucent frosted bottle on pale stone plinth, soft diffused top light, controlled edge highlights, clean front label area left blank for later design, no random text, no fake logo, realistic glass thickness, subtle contact shadow, minimal warm-beige luxury palette

Iteration note：
- Preserve：柔和高级光感
- Test next：标签区域是否足够干净
- Watch：玻璃边缘不要因为留白而变得太假
```
