# Luxury Product Ad Director

Luxury Product Ad Director 是一个面向高端产品广告生图的 Codex skill，专门处理香水、腕表、珠宝、包袋四类品类的 prompt direction。

它的目标不是输出一段泛泛的“奢华产品提示词”，而是把品类差异、材质行为、镜头逻辑、反射 / 折射控制、hero still life、macro 细节和 hand / body relation 全部拆成可执行交付。

## 适合谁

- 在做高端产品广告图、campaign KV、社媒主视觉、提案 moodboard 的团队
- 想把香水、腕表、珠宝、包袋的生图逻辑分开处理，而不是共用一套“黑金奢华”模板的人
- 需要输出 Prompt Bible、评审包、修复策略、下一轮测试点的使用者

## 能解决什么问题

- 从 brief 生成品类正确的高端产品广告 prompt
- 处理 hero still life、macro / material detail、reflection / refraction、hand / body relation
- 针对香水、腕表、珠宝、包袋分别给出材质与镜头逻辑
- 输出 Prompt Bible，而不是几段互相无关的 prompt
- 对已有生成结果做专业评审：打分、定位失败、给出最小修复动作
- 避免 generic black-gold luxury、过量 sparkle、廉价棚拍感

## 目录结构

```text
luxury-product-ad-director/
├─ SKILL.md
├─ agents/
│  └─ openai.yaml
├─ references/
│  ├─ benchmark-suite.md
│  ├─ case-library.md
│  ├─ category-material-camera-logic.md
│  ├─ examples.md
│  ├─ iteration-playbook.md
│  ├─ luxury-visual-framework.md
│  ├─ prompt-bible-examples.md
│  └─ quality-scorecard.md
└─ scripts/
   ├─ smoke_tests.py
   └─ validate_v1_readiness.py
```

## 安装

复制到 Codex skills 目录：

```powershell
Copy-Item -Recurse -Force . "$env:USERPROFILE\.codex\skills\luxury-product-ad-director"
```

然后在 Codex 里使用：

```text
Use $luxury-product-ad-director to build a luxury product campaign prompt package for perfume, watch, jewelry, or bag imagery.
```

中文也可以直接用：

```text
用 luxury-product-ad-director 帮我做一套高端香水广告 Prompt Bible，要包含 hero、微距和手部关系镜头，并避免黑金俗套。
```

## 交付原则

- 高端感必须建立在材质、镜头、光线和身体关系上，不建立在空泛形容词上
- 香水、腕表、珠宝、包袋必须使用不同的视觉逻辑
- 人体只在能增强价值时出现；一旦出现，就必须约束比例、姿态和接触关系
- logo、长文案、精细刻字默认留给后期，不把模型文字能力当成交付核心
- 遇到失败图时，优先输出专业评审包和最小修复动作

## 本地验证

```powershell
$env:PYTHONUTF8='1'
python C:\Users\windows\.codex\skills\.system\skill-creator\scripts\quick_validate.py C:\Users\windows\.codex\skills\luxury-product-ad-director
python C:\Users\windows\.codex\skills\luxury-product-ad-director\scripts\smoke_tests.py
python C:\Users\windows\.codex\skills\luxury-product-ad-director\scripts\validate_v1_readiness.py
```

预期结果：

```text
Skill is valid!
Smoke tests passed.
v1 readiness passed.
```

## English Summary

This skill helps Codex act as a luxury product ad director for perfume, watches, jewelry, and handbags. It focuses on category-specific material response, camera logic, still life systems, body relation, professional review, and prompt bible delivery rather than generic luxury wording.

## License

MIT
