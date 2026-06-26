# Spatial Installation Prompt Director

Spatial Installation Prompt Director 是一个面向商业空间提案与 AI 效果图生成的 Codex skill，专门处理商场美陈、快闪店、展陈空间和沉浸通道的 prompt direction。

它的目标不是输出几句“空间感提示词”，而是把场地照片、文字 brief、失败效果图或已有方向，拆成入口、主装置、灯光、地贴、动线、拍照点六区联动的可执行交付。

## 适合谁

- 在做商场中庭美陈、品牌快闪、展陈提案、沉浸式通道方向的人
- 需要把现场照片或文字 brief 快速转成效果图 prompt 和提案摘要的团队
- 想要专业评审包、案例迁移、下一轮修复策略，而不是只要一句 prompt 的使用者

## 能解决什么问题

- 从商场美陈、快闪、展陈、沉浸通道 brief 生成可执行 prompt package
- 兼容现场照片 intake 和文字 brief intake
- 输出入口、主装置、灯光、地贴、动线、拍照点六区 prompt
- 生成 Proposal Summary，支持客户提案摘要
- 对弱方向或失败效果图做专业评审和最小修复动作
- 避免 generic 灯带隧道、廉价乐园风、无动线雕塑岛

## 目录结构

```text
spatial-installation-prompt-director/
├─ SKILL.md
├─ agents/
│  └─ openai.yaml
├─ references/
│  ├─ benchmark-suite.md
│  ├─ case-library.md
│  ├─ examples.md
│  ├─ prompt-bible-examples.md
│  ├─ quality-scorecard.md
│  ├─ scenario-playbooks.md
│  ├─ site-intake-and-traffic-flow.md
│  └─ spatial-installation-framework.md
└─ scripts/
   ├─ smoke_tests.py
   └─ validate_v1_readiness.py
```

## 安装

复制到 Codex skills 目录：

```powershell
Copy-Item -Recurse -Force . "$env:USERPROFILE\\.codex\\skills\\spatial-installation-prompt-director"
```

然后在 Codex 里使用：

```text
Use $spatial-installation-prompt-director to turn a mall, pop-up, exhibition, or immersive corridor brief into spatial prompts and proposal-ready summaries.
```

中文也可以直接用：

```text
用 spatial-installation-prompt-director 帮我把这张商场中庭现场照片做成一套入口、主装置、灯光、地贴、动线和拍照点的提案级效果图 prompt。
```

## 交付原则

- 必须先处理真实场地限制，再谈概念气质
- 入口、主装置、灯光、地贴、动线、拍照点必须共享同一套 style anchor
- 拍照点必须服务传播、入口识别或导流中的至少一个目标
- logo、精细导视、长文案默认留后期，不把模型文字能力当成交付核心
- 发现失败图时，优先输出专业评审包和最小修复动作

## 本地验证

```powershell
$env:PYTHONUTF8='1'
python C:\Users\windows\.codex\skills\.system\skill-creator\scripts\quick_validate.py C:\Users\windows\.codex\skills\spatial-installation-prompt-director
python C:\Users\windows\.codex\skills\spatial-installation-prompt-director\scripts\smoke_tests.py
python C:\Users\windows\.codex\skills\spatial-installation-prompt-director\scripts\validate_v1_readiness.py
```

预期结果：

```text
Skill is valid!
Smoke tests passed.
v1 readiness passed.
```

## English Summary

This skill helps Codex act as a spatial-installation prompt director for mall displays, pop-ups, exhibitions, and immersive corridors. It turns site photos or text briefs into entrance, installation, lighting, floor-graphic, traffic-flow, photo-point prompts, proposal summaries, review packages, and repair strategies.

## License

MIT
