# Auto Ad Director

汽车广告 AI 视觉导演 skill，用于生成、诊断、迭代和交付汽车广告 AI 生图提示词。

Auto Ad Director is a Codex skill for automotive advertising prompt direction: campaign prompt bibles, brand visual systems, shot lists, platform prompt adaptation, image review, and repair workflows.

## 能做什么

- 从一句 brief 生成汽车广告 Campaign 提示词包
- 生成单张主视觉、6/9/12 格 contact sheet、社媒海报和客户提案素材
- 拆解参考图的光影、构图、镜头、材质和品牌风格
- 适配 Midjourney、Nano Banana、即梦、可灵、Seedream 和通用中文图像模型
- 诊断失败图：车轮错乱、车身变形、车标乱码、反射错误、人车融合、廉价棚拍感
- 进行提示词工程：参数实验、模块化 prompt、A/B 测试、版本记录
- 输出商业交付：Prompt Bible、Shot List、Art Director Review、Handoff Package

## 适用场景

- 汽车广告 AI 生图
- EV 新车发布视觉探索
- 汽车品牌 Campaign moodboard
- 参考图复刻与风格迁移
- 汽车广告提示词工程
- 出图后评分、修复和迭代
- 面向客户或团队的提示词交付包

## 安装

将本仓库复制到 Codex skills 目录：

```powershell
Copy-Item -Recurse -Force . "$env:USERPROFILE\.codex\skills\auto-ad-director"
```

然后在 Codex 中使用：

```text
Use $auto-ad-director to create a cinematic automotive campaign prompt package from this brief: ...
```

中文也可以直接描述需求，例如：

```text
用 auto-ad-director 帮我为小米 SU7 做一组上海雨夜汽车广告提示词。
```

## 结构

```text
auto-ad-director/
├─ SKILL.md
├─ agents/
│  └─ openai.yaml
└─ references/
   ├─ automotive-visual-framework.md
   ├─ benchmark-suite.md
   ├─ brand-archetypes.md
   ├─ brand-visual-library.md
   ├─ campaign-research-bank.md
   ├─ delivery-templates.md
   ├─ examples.md
   ├─ image-review-scorecard.md
   ├─ iteration-playbook.md
   ├─ platform-adapters.md
   ├─ prompt-engineering-system.md
   ├─ quality-review.md
   └─ shot-language-library.md
```

## 设计原则

- 参考资料是工具，不是限制。
- 先保证车辆真实度，再追求视觉风格。
- 不要求图像模型生成精确车标、广告语或车牌文字。
- 品牌视觉库是 prompt 导演启发，不是官方品牌手册。
- 不包含、下载或分发任何官方图片、PDF、品牌素材。

## English Summary

This skill helps Codex act as an automotive advertising prompt director. It supports research-backed brand tone, automotive shot language, prompt engineering, multi-platform prompt adaptation, campaign delivery templates, and image review/repair scorecards.

It does not include official brand assets and is not an official brand guideline for any automaker.

## License

MIT
