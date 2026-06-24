# Visual Reference Prompt Director

Reference-image prompt direction skill for Codex. It turns visual references, screenshots, PDF frames, moodboard samples, or text-described visuals into reusable visual DNA, safe transfer rules, platform-ready prompts, and quality review notes.

## What It Does

- Breaks a reference into visual story, subject hierarchy, composition, lighting ratio, camera/lens estimate, material/color, post-processing, and constraints.
- Supports analysis-only work when no prompt should be generated.
- Supports "keep the mood, change the subject" workflows.
- Flags do-not-copy elements, text/logo risks, likeness risks, artwork risks, and likely generation failures.
- Outputs platform-aware prompts for Midjourney, Jimeng, Kling, Seedream, Nano Banana, and generic Chinese image models.
- Includes a v1 quality scorecard, text-only case library, acceptance benchmark suite, and readiness validation script.

## Install

Copy this folder into your Codex skills directory:

```powershell
Copy-Item -Recurse -Force . "$env:USERPROFILE\.codex\skills\visual-reference-prompt-director"
```

Then invoke it in Codex:

```text
Use $visual-reference-prompt-director to analyze this reference image into visual DNA, risk notes, and platform-ready prompts.
```

Chinese usage also works:

```text
用 visual-reference-prompt-director 拆解这张参考图，保留光影和构图气质，但把主体换成香水瓶。
```

## Structure

```text
visual-reference-prompt-director/
├─ SKILL.md
├─ agents/
│  └─ openai.yaml
├─ references/
│  ├─ benchmark-suite.md
│  ├─ case-library.md
│  ├─ examples.md
│  ├─ platform-output-formats.md
│  ├─ quality-scorecard.md
│  ├─ risk-and-constraints.md
│  └─ visual-breakdown-framework.md
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

- Translate references into visual components instead of copying source material.
- Do not store or redistribute official images, brand assets, or copyrighted artwork.
- Treat lens, light ratio, and camera position as visual estimates unless metadata is supplied.
- Prefer controllability over spectacle: clear subject hierarchy, physical light, material response, and scene-specific constraints.
- Use platform guidance as practical prompt-writing advice, not an official guarantee of platform behavior.

## License

MIT
