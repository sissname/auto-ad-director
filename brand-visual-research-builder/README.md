# Brand Visual Research Builder

`brand-visual-research-builder` 是一个给 Codex 用的品牌视觉研究 skill。它的目标不是抓图搬运，而是把官网公开页面整理成可复用的研究库：保留来源链接、提炼视觉观察、沉淀 `Prompt Translation Rules`、列出 `Failure Risks`，并且始终明确“不保存原图、不宣称官方授权”。

## 能做什么

- 读取官网首页、新闻 / newsroom、媒体中心、产品页、空间页等官方来源
- 整理单品牌研究卡、`Compact Research Bank`、多品牌对比结论
- 把官网视觉证据转成镜头、光线、材质、颜色、空间、文字策略等控制变量
- 明确哪些内容只能“受启发”，不能直接照抄
- 产出可交给后续 prompt director 使用的研究转译 brief
- 提供 5 个品牌的紧凑研究库样例、示例输出、benchmark suite 和 v1 readiness 校验

## 适合谁

- 想先做品牌官网研究，再进入 AI 出图的人
- 需要把品牌调性整理成团队可复用研究库的人
- 做提案、方向筛选、竞品对比、品牌视觉拆解的人
- 想降低“看起来像某品牌但又很假”这类风险的人

## 安装

将本文件夹复制到 Codex skills 目录：

```powershell
Copy-Item -Recurse -Force . "$env:USERPROFILE\.codex\skills\brand-visual-research-builder"
```

然后在 Codex 中调用：

```text
用 $brand-visual-research-builder 为这个品牌整理官网研究库，保留来源链接、视觉观察、提示词转换规则和失败风险。
```

也可以这样说：

```text
用 brand-visual-research-builder 研究 Apple 官网视觉，后面我要给耳机主视觉做方向，不要保存原图。
```

## 结构

```text
brand-visual-research-builder/
├─ README.md
├─ LICENSE
├─ SKILL.md
├─ agents/
│  └─ openai.yaml
├─ references/
│  ├─ benchmark-suite.md
│  ├─ case-library.md
│  ├─ compact-research-bank.md
│  ├─ examples.md
│  ├─ official-source-rules.md
│  ├─ prompt-translation-rules.md
│  ├─ quality-scorecard.md
│  └─ research-workflow.md
└─ scripts/
   ├─ smoke_tests.py
   └─ validate_v1_readiness.py
```

## 验证

```powershell
$env:PYTHONUTF8='1'
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" .
python .\scripts\smoke_tests.py
python .\scripts\validate_v1_readiness.py
```

期望输出：

```text
Skill is valid!
Smoke tests passed.
v1 readiness passed.
```

## 研究边界

- 不下载、不另存、不分发官网原图。
- 只保留：原始链接、页面名称、你的中文摘要、观察结论和转译规则。
- 不把研究结论说成官方品牌规范或官方授权风格。
- 如果品牌没有公开 newsroom 或 media center，要在输出里说明来源结构有限，而不是硬编来源。

## 原始来源处理原则

- 优先读官方首页、产品页、新闻 / newsroom、媒体中心、空间 / about 页面。
- 每个页面都保留原始来源链接。
- 把观察写成控制变量，不停留在“高级、极简、未来感”之类空词。
- 把 `Failure Risks` 写清楚，尤其是商标、标语、版式、材质失真、文字乱码和调性跑偏。

## English Summary

This skill turns official brand surfaces into compact visual research banks for prompt direction. It preserves source URLs, summarizes visual evidence, extracts prompt-translation rules, and records failure risks without downloading original images or claiming official authorization.

## License

MIT
