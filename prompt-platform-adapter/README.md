# Prompt Platform Adapter

Cross-platform prompt adaptation skill for Codex. It converts one visual brief, reference-derived visual DNA, existing Midjourney prompt, Chinese prompt, failed prompt, or prompt bible into platform-aware prompts with conversion notes, parameter discipline, risk controls, quality scoring, and iteration guidance.

## What It Does

- Converts visual prompts across Midjourney, Jimeng, Kling, Nano Banana, Seedream, and generic Chinese image models.
- Preserves intent before adapting syntax.
- Explains parameter usage and when to avoid parameters.
- Handles text/logo, realism, negative prompt, brand, and reference image weight risks.
- Supports prompt audit, failed prompt repair, prompt bible conversion, and A/B test conversion.
- Includes v1 quality scorecard, platform matrix, case library, acceptance benchmarks, and readiness validation.

## Install

Copy this folder into your Codex skills directory:

```powershell
Copy-Item -Recurse -Force . "$env:USERPROFILE\.codex\skills\prompt-platform-adapter"
```

Then invoke it in Codex:

```text
Use $prompt-platform-adapter to convert this visual brief into platform-ready prompts with conversion notes and risk controls.
```

Chinese usage:

```text
用 prompt-platform-adapter 把这个香水广告 brief 转成 MJ、即梦、可灵、Nano Banana、Seedream 和通用中文模型提示词，并说明参数和风险控制。
```

## Structure

```text
prompt-platform-adapter/
├─ SKILL.md
├─ agents/
│  └─ openai.yaml
├─ references/
│  ├─ benchmark-suite.md
│  ├─ case-library.md
│  ├─ examples.md
│  ├─ platform-matrix.md
│  ├─ platform-rules.md
│  ├─ quality-scorecard.md
│  └─ risk-controls.md
└─ scripts/
   ├─ smoke_tests.py
   └─ validate_v1_readiness.py
```

## Validation

Run:

```powershell
$env:PYTHONUTF8='1'
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" .
python .\scripts\smoke_tests.py
python .\scripts\validate_v1_readiness.py
```

Expected result:

```text
Skill is valid!
Smoke tests passed.
v1 readiness passed.
```

## Design Principles

- Preserve creative intent before adapting platform syntax.
- Do not copy unsupported flags into platforms that do not use them.
- Write Chinese platform prompts as natural art direction, not translated keyword piles.
- Treat platform rules as practical prompt-writing guidance, not official platform guarantees.
- Keep text/logo exactness out of generation; prefer clean layout areas and post-production.

## License

MIT
