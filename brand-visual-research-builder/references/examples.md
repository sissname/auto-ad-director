# Examples

## 示例 1：只做研究，不生成 Prompt

输入：

```text
Use $brand-visual-research-builder. 研究 Aesop 的公开页面视觉气质，保留来源链接，只告诉我哪些元素适合转成空间效果图，先别写 prompt。
```

期望输出重点：

- 给出 3-4 个官方链接
- 明确 Aesop 的视觉领地是“克制、触感、建筑感、温和知识性”
- 说清楚适合转成空间图的变量：材质、光线、表面、留白、秩序
- 明确不能照抄标签、店铺平面和品牌字体

## 示例 2：研究后直接转成 Prompt 规则

输入：

```text
Use $brand-visual-research-builder. 帮我研究 Nike Air Max Dn8 的官方页面，把结论翻译成我后面做鞋类主视觉会用到的镜头、光线、材质和 failure risks。
```

期望输出重点：

- 来源里同时有 Nike Newsroom 和产品页
- 结论不是“运动感很强”，而是能落到低机位、鞋底结构、切边构图、地面纹理
- Failure risks 要指出俗套火焰、赛博霓虹、失真鞋底
- 如果没有要求，先不给具体平台 prompt

## 示例 3：给方向稿前置研究

输入：

```text
Use $brand-visual-research-builder. 我想做一个受 Apple 公共页面启发的消费电子海报方向，请先做 compact research bank，并列出之后写 prompt 时必须保留和必须避免的东西。
```

期望输出重点：

- 用 Apple 官方新闻和产品页做证据
- 把“工业精密 + 纯净背景 + 受控边缘高光”写成一句话结论
- 保留：轮廓、极简背景、金属玻璃材质、留白
- 避免：假 logo、杂乱 UI、花哨科技滤镜

## 示例 4：品牌对标

输入：

```text
Use $brand-visual-research-builder. 对比 Porsche 911 和 Dyson Airwrap i.d. 的公开页面视觉差异，我想知道一个偏机械欲望，一个偏工程美容工具，它们的镜头和材质规则有什么根本不同。
```

期望输出重点：

- 先列各自官方来源
- 对比镜头：Porsche 更低、更有道路接触；Dyson 更近、更强调手势和结构
- 对比材质：Porsche 偏金属、漆面、路面反光；Dyson 偏塑料、金属、发丝与气流逻辑
- 对比风险：不能把两者都做成“同一种高级”
