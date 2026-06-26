# Brand Visual Research Builder

Brand Visual Research Builder 是一个把品牌公开官方页面研究，转成可追溯视觉研究库与 prompt 规则的 Codex skill。

它不负责冒充“官方品牌规范”，而是帮助我们从官网、产品页、新闻稿、媒体中心和设计页面里，抽取真正有用的视觉变量：镜头、构图、光线、材质、颜色、场景和 failure risks。

## 适合什么任务

- 品牌视觉研究
- 方向稿前置研究
- 品牌公开页面拆解
- 研究后再写 AI 出图 prompt
- 品牌对标
- 只做研究不出图

## 当前包含

```text
brand-visual-research-builder/
├─ SKILL.md
├─ README.md
├─ agents/
│  └─ openai.yaml
├─ references/
│  ├─ benchmark-suite.md
│  ├─ case-library.md
│  ├─ compact-research-bank.md
│  ├─ examples.md
│  ├─ professional-quality-gate.md
│  ├─ prompt-translation-rules.md
│  ├─ research-framework.md
│  └─ source-intake-and-compliance.md
└─ scripts/
   ├─ smoke_tests.py
   └─ validate_v1_readiness.py
```

## 交付原则

- 只保留来源链接、观察结论、prompt translation rules 和 failure risks
- 不保存官方原图或媒体素材副本
- 不宣称官方授权
- 不把公开页面观察冒充成正式 brand guideline
- 需要精确品牌合规时，仍要用户提供正式官方资料

## 本地验证

```powershell
$env:PYTHONUTF8='1'
python C:\Users\windows\.codex\skills\.system\skill-creator\scripts\quick_validate.py C:\Users\windows\.codex\skills\brand-visual-research-builder
python C:\Users\windows\.codex\skills\brand-visual-research-builder\scripts\smoke_tests.py
python C:\Users\windows\.codex\skills\brand-visual-research-builder\scripts\validate_v1_readiness.py
```

## English Summary

This skill helps Codex research a brand from official public pages and convert the findings into source-backed prompt translation rules. It preserves links and observations, but does not store official images or claim any official authorization.
