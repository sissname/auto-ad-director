# Campaign Contact Sheet Director

Campaign Contact Sheet Director 是一个面向广告提案、多格视觉规划和平台出图交付的 Codex skill。它的目标不是只写几条好看的 prompt，而是把一个 brief 拆成统一风格的 6 / 9 / 12 / 16 格 contact sheet，并且给出逐格 shot logic、平台 prompts、质量检查和提案口径。

## 适合谁

- 需要把单条 brief 扩成整组 campaign 画面的人
- 需要做广告提案、产品发布板、时尚 lookbook、空间提案板的人
- 已有 hero 图，但还缺系列延展和逐格逻辑的人

## 解决什么问题

- 同一组图看起来像同一 campaign，而不是随机拼图
- 能同时支持广告、产品、时尚、空间四种场景
- 支持 6 / 9 / 12 / 16 格 contact sheet 规划
- 给出统一的 style anchor、shot taxonomy、逐格 shot logic
- 输出 Midjourney、即梦、通用中文模型三类平台 prompts
- 自带 examples、benchmark suite、smoke tests 和 v1 readiness 校验

## 目录结构

```text
campaign-contact-sheet-director/
├─ SKILL.md
├─ agents/
│  └─ openai.yaml
├─ references/
│  ├─ benchmark-suite.md
│  ├─ case-library.md
│  ├─ contact-sheet-framework.md
│  ├─ examples.md
│  ├─ platform-prompt-formats.md
│  ├─ quality-scorecard.md
│  └─ shot-taxonomy.md
├─ scripts/
│  ├─ smoke_tests.py
│  └─ validate_v1_readiness.py
├─ LICENSE
└─ README.md
```

## 操作步骤

### 1. 安装到 Codex skills 目录

```powershell
Copy-Item -Recurse -Force . "$env:USERPROFILE\.codex\skills\campaign-contact-sheet-director"
```

### 2. 在 Codex 里直接调用

英文示例：

```text
Use $campaign-contact-sheet-director to turn this launch brief into a unified 9-frame campaign contact sheet with per-frame shot logic and Midjourney prompts.
```

中文示例：

```text
用 campaign-contact-sheet-director 帮我把这个护肤新品 brief 拆成 6 格产品发布板，保留统一 style anchor，并给每一格的即梦 prompt。
```

### 3. 需要更专业的输出时

可以直接要求：

- 给我提案级输出，不要只给 prompt
- 先只做结构策划，不写平台 prompt
- 基于这张 hero 图补出 12 格时尚系列
- 同时给 Midjourney 和即梦版本，并指出最容易翻车的格子

## 常见坑

- 每一格都写成 hero 图，缺少 detail、environment 和 social crop
- 只想统一，不写哪些 anchor 必须固定
- 有平台 prompt，但没有逐格职责
- 忘记预留标题区、社媒裁切位或竖版传播位
- 文字、logo、包装小字直接让模型硬生，导致交付不可用

## 本地验证

先建议在测试项目里跑，确认结构和脚本都正常，再用于正式归档或发布。

```powershell
$env:PYTHONUTF8='1'
python C:\Users\windows\.codex\skills\.system\skill-creator\scripts\quick_validate.py C:\Users\windows\.codex\skills\campaign-contact-sheet-director
python C:\Users\windows\.codex\skills\campaign-contact-sheet-director\scripts\smoke_tests.py
python C:\Users\windows\.codex\skills\campaign-contact-sheet-director\scripts\validate_v1_readiness.py
```

## 原始来源

- 技能路线图：`J:\005-Auto-Ad-Director-Skill-发布归档\00-总览索引\NEXT-SKILL-ROADMAP.md`
- 当前归档说明：`J:\005-Auto-Ad-Director-Skill-发布归档\00-总览索引\README.md`

## English Summary

This skill helps Codex turn one visual brief into a coherent 6/9/12/16-frame campaign contact sheet with unified style anchors, shot taxonomy, per-frame shot logic, platform-specific prompts, examples, benchmark cases, and professional readiness validation.

## License

MIT
