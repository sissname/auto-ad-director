# Brand Concept Visual Director

品牌方向稿 AI 视觉导演 skill，用于把品牌定位、参考图、偏好和禁区转成 3-5 个可比较的 AI 方向稿 prompt，并附创意总监评审和下一轮迭代问题。

## 能做什么

- 从品牌定位生成 3-5 个视觉方向。
- 把参考图转成可迁移的品牌视觉线索。
- 处理用户偏好、禁区、竞品规避和文字/logo 风险。
- 输出方向 prompt、负面风险、下一轮问题。
- 附创意总监评审表，帮助用户选择方向。
- 明确 AI 方向图不是最终 logo，避免把 SVG 或草图当成专业标志交付。

## 安装

复制本目录到 Codex skills 目录：

```powershell
Copy-Item -Recurse -Force . "$env:USERPROFILE\.codex\skills\brand-concept-visual-director"
```

使用：

```text
Use $brand-concept-visual-director to turn this brand positioning, references, and constraints into 3-5 visual direction prompts with creative review notes.
```

中文示例：

```text
用 brand-concept-visual-director 帮我把这个阅读陪伴品牌定位做成 3 个 AI 方向稿 prompt，并附创意总监评审。
```

## 结构

```text
brand-concept-visual-director/
├─ SKILL.md
├─ agents/
│  └─ openai.yaml
├─ references/
│  ├─ benchmark-suite.md
│  ├─ brand-concept-framework.md
│  ├─ case-library.md
│  ├─ creative-review-scorecard.md
│  ├─ examples.md
│  └─ reference-and-logo-boundaries.md
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

预期：

```text
Skill is valid!
Smoke tests passed.
v1 readiness passed.
```

## 设计原则

- 方向稿用于选择视觉方向，不承诺最终 logo。
- 参考图只转译光影、构图、材质和气质，不复制原图、竞品或官方素材。
- 文字、logo、品牌名默认后期在设计软件中处理。
- 每个方向都必须包含风险和下一轮问题。

## License

MIT
