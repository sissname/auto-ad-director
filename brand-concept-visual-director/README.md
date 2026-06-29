# 品牌方向稿视觉导演（Brand Concept Visual Director）

品牌方向稿 AI 视觉导演 skill，用于把品牌定位、参考图、偏好和禁区转成 3-5 个可比较的 AI 方向稿 prompt，并附创意总监评审和下一轮迭代问题。

## 适合谁

- 正在做品牌早期视觉探索的个人创作者、设计师、品牌顾问和小团队。
- 手上已经有品牌定位、参考图、SVG 草图或竞品截图，但还不该直接承诺最终 logo 的项目。
- 想先用 AI 方向图筛选视觉路线，再进入专业平面或品牌设计流程的人。

## 解决什么问题

- 把抽象的品牌定位翻译成 3-5 个差异明确的视觉方向。
- 明确参考图哪些元素可以借鉴，哪些不能照抄。
- 在输出 prompt 的同时附上创意总监评审和下一轮问题，帮助团队做选择。
- 避免把 SVG 示意、AI 草图或假文字当成最终专业 logo 交付。

## 能做什么

- 从品牌定位生成 3-5 个视觉方向。
- 把参考图转成可迁移的品牌视觉线索。
- 处理用户偏好、禁区、竞品规避和文字/logo 风险。
- 输出方向 prompt、负面风险、下一轮问题。
- 附创意总监评审表，帮助用户选择方向。
- 明确 AI 方向图不是最终 logo，避免把 SVG 或草图当成专业标志交付。

## 操作步骤

### 1. 安装

复制本目录到 Codex skills 目录：

```powershell
Copy-Item -Recurse -Force . "$env:USERPROFILE\.codex\skills\brand-concept-visual-director"
```

### 2. 在 Codex 中调用

使用：

```text
Use $brand-concept-visual-director to turn this brand positioning, references, and constraints into 3-5 visual direction prompts with creative review notes.
```

中文示例：

```text
用 brand-concept-visual-director 帮我把这个阅读陪伴品牌定位做成 3 个 AI 方向稿 prompt，并附创意总监评审。
```

### 3. 运行验证

进入技能目录后执行：

```powershell
$env:PYTHONUTF8='1'
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" .
python .\scripts\smoke_tests.py
python .\scripts\validate_v1_readiness.py
```

预期输出：

```text
Skill is valid!
冒烟测试通过。
v1 就绪检查通过。
```

### 4. 再开始真实项目

- 先用测试品牌或虚拟 brief 试跑一轮。
- 如果你要喂参考图、SVG 或 logo 草图，先确认它们只是方向线索。
- 真正进入品牌交付前，再补矢量设计、字体、网格、小尺寸识别和商标检索。

## 目录结构

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

## 常见坑

- 方向只有气质词，没有可执行 prompt：这会让 AI 出图不可控。
- 参考图借得太满：容易直接变成竞品翻版或侵权风险。
- 把 SVG / 草图当最终 logo：这个 skill 只负责前期方向探索，不负责最终品牌标志交付。
- 让模型硬生生生成精确品牌名、字体和字标：这通常会得到假文字或低质量结果。
- 方向太多：超过 5 个通常只会稀释判断质量。

## 设计原则

- 方向稿用于帮助选择视觉方向，不承诺最终 logo。
- 参考图只转译光影、构图、材质和气质，不复制原图、竞品或官方素材。
- 文字、logo、品牌名默认后期在设计软件中处理。
- 每个方向都必须包含风险和下一轮问题。

## 原始来源

- 路线要求：`J:\005-Auto-Ad-Director-Skill-发布归档\00-总览索引\NEXT-SKILL-ROADMAP.md`
- 归档记录：`J:\005-Auto-Ad-Director-Skill-发布归档\00-总览索引\README.md`
- 现有发布工作树：`J:\005-Auto-Ad-Director-Skill-发布归档\04-源码与配置副本\auto-ad-director-brand-concept-upload-worktree\`

## 许可证

MIT
