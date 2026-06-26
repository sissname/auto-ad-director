# Spatial Installation Prompt Director

`Spatial Installation Prompt Director` 是一个把商场美陈、快闪店、展陈空间、沉浸通道 brief，转成空间效果图 prompt 与提案摘要的 Codex skill。

它支持两类常见输入：

- 现场照片或场地条件
- 纯文字 brief、活动主题或方向描述

它默认把任务拆成六个核心交付区：

- 入口
- 主装置
- 灯光
- 地贴
- 动线
- 拍照点

## 适合谁

- 做商场美陈和中庭活动方向的人
- 做品牌快闪和展陈提案的人
- 需要把空间概念快速转成 AI 效果图 prompt 的人
- 需要把空间方向写成客户可读摘要的人

## 解决什么问题

- 把抽象空间概念翻成可执行 prompt
- 把现场照片里的入口、扶梯、柱网、人流限制纳入方案
- 避免只有“漂亮空间图”，没有入口识别、动线逻辑和传播点
- 帮用户同时拿到效果图方向和提案摘要

## 当前包含

```text
spatial-installation-prompt-director/
├─ .gitignore
├─ LICENSE
├─ README.md
├─ SKILL.md
├─ agents/
│  └─ openai.yaml
├─ references/
│  ├─ benchmark-suite.md
│  ├─ case-library.md
│  ├─ examples.md
│  ├─ proposal-summary-playbook.md
│  ├─ prompt-bible-examples.md
│  ├─ quality-scorecard.md
│  ├─ scenario-playbooks.md
│  ├─ site-intake-and-traffic-flow.md
│  └─ spatial-installation-framework.md
└─ scripts/
   ├─ smoke_tests.py
   └─ validate_v1_readiness.py
```

## 操作步骤

1. 明确场景类型：`Mall Display`、`Pop-up`、`Exhibition`、`Immersive Corridor`。
2. 明确输入类型：现场照片、文字 brief、已有方向稿，还是失败效果图。
3. 先锁定统一 style anchor，再拆六区输出。
4. 需要客户摘要时，按 `proposal-summary-playbook.md` 输出，不只给视觉形容词。
5. 提交前用 smoke tests 和 v1 readiness 做一次自检。

## 常见坑

- 只做漂亮主装置，不解释入口和动线。
- 把任何空间都画成通用灯带隧道。
- 假设模型能稳定生成 logo、导视文案和精确文字。
- 无视现场柱子、扶梯、吊挂和消防限制。

## 本地验证

```powershell
$env:PYTHONUTF8='1'
python C:\Users\windows\.codex\skills\spatial-installation-prompt-director\scripts\smoke_tests.py
python C:\Users\windows\.codex\skills\spatial-installation-prompt-director\scripts\validate_v1_readiness.py
```

如果要跑 `quick_validate.py`，当前环境需要可用的 `PyYAML`。

## 原始来源

- 技能路线图：`J:\005-Auto-Ad-Director-Skill-发布归档\00-总览索引\NEXT-SKILL-ROADMAP.md`
- 项目归档总览：`J:\005-Auto-Ad-Director-Skill-发布归档\00-总览索引\README.md`
- 相关候选记录：`J:\005-Auto-Ad-Director-Skill-发布归档\03-外部记录\skill-candidate-ideas.json`

## English Summary

This skill turns mall display, pop-up, exhibition, and immersive corridor briefs into spatial prompt packages and proposal-ready summaries. It supports both site-photo intake and text-only briefs, and it structures outputs around entrance, device, lighting, floor graphic, traffic flow, and photo point logic.
