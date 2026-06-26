# Campaign Contact Sheet Director

`campaign-contact-sheet-director` 是一个面向广告提案、品牌发布、产品 launch、时尚 campaign 和空间效果图规划的 Codex skill。

它的核心目标不是“多写几条 prompt”，而是把一个 brief 组织成 **6 / 9 / 12 / 16 格统一风格的 contact sheet**：先建立整套的 style anchor，再拆出逐格镜头角色、逐格 shot logic，以及面向不同平台的 prompt 包。

## 适合谁

- 需要把单张好图扩成整套 campaign 的团队
- 需要给客户、设计团队、运营或提案会展示多格分镜方案的人
- 想让 AI 生图从“散图试错”升级到“成套系统输出”的使用者
- 需要 advertising、product、fashion、spatial 四类场景统一方法论的人

## 能解决什么问题

- 把 brief 转成 6 / 9 / 12 / 16 格 contact sheet 结构
- 建立统一的 style anchor：品牌气质、镜头系统、光线系统、色彩、材质、裁切纪律
- 用 shot taxonomy 分配每格职责：hero、detail、lifestyle、motion、environment、macro、portrait、social crop
- 输出逐格 shot logic，而不是只给一串抽象气氛词
- 为 Midjourney、即梦、可灵、Nano Banana、Seedream、通用中文模型生成逐格平台 prompts
- 对现有 contact sheet 做 review and repair，指出保留项、替换项和重写项

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
│  ├─ platform-prompt-matrix.md
│  ├─ quality-scorecard.md
│  ├─ scenario-playbooks.md
│  └─ shot-taxonomy.md
└─ scripts/
   ├─ smoke_tests.py
   └─ validate_v1_readiness.py
```

## 安装

复制到 Codex skills 目录：

```powershell
Copy-Item -Recurse -Force . "$env:USERPROFILE\\.codex\\skills\\campaign-contact-sheet-director"
```

然后在 Codex 中调用：

```text
Use $campaign-contact-sheet-director to turn this campaign brief into a unified 9-frame contact sheet with per-frame shot logic and platform prompts.
```

中文也可以直接用：

```text
用 campaign-contact-sheet-director 把这个 brief 拆成一套统一风格的 12 格 contact sheet，并给我逐格平台提示词。
```

## v1 关键能力

- 支持 `6 / 9 / 12 / 16` 四种常用格数
- 支持 `advertising / product / fashion / spatial` 四类场景
- 强制先写 `Master Anchor Prompt` 再写逐格 prompts
- 每格都要求说明存在理由、连续性关系和失败风险
- 提供 `benchmark suite`、`quality scorecard`、`case library`
- 提供 `smoke tests` 和 `v1 readiness validation`

## 交付原则

- 先做整套锚点，再写单格 prompt
- 至少覆盖 4 种 shot type，避免整套画面过度重复
- 平台输出必须保留统一锚点，同时体现平台差异
- 涉及文字、包装或 logo 时，优先留出安全区和后期补字方案
- review and repair 必须说明保留项、替换项、重写项

## 本地验证

```powershell
$env:PYTHONUTF8='1'
python C:\Users\windows\.codex\skills\.system\skill-creator\scripts\quick_validate.py C:\Users\windows\.codex\skills\campaign-contact-sheet-director
python C:\Users\windows\.codex\skills\campaign-contact-sheet-director\scripts\smoke_tests.py
python C:\Users\windows\.codex\skills\campaign-contact-sheet-director\scripts\validate_v1_readiness.py
```

## English Summary

This skill turns a visual brief into a coherent multi-frame campaign contact sheet rather than a loose list of prompts. It builds a unified style anchor, assigns frame roles, writes per-frame shot logic, and adapts the output for multiple image-generation platforms.

## License

MIT
