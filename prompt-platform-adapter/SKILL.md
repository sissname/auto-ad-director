---
name: prompt-platform-adapter
description: Convert visual briefs, reference-derived visual DNA, or existing image prompts across Midjourney, Jimeng, Kling, Nano Banana, Seedream, and generic Chinese image models. Use when adapting one prompt or creative brief into platform-specific prompts, explaining conversion choices, deciding when to use or avoid parameters, handling text/logo/realism/negative prompt/reference image weight risks, or producing cross-platform prompt packages for AI image generation. 中文适用：多平台提示词适配、MJ/即梦/可灵/Nano Banana/Seedream/通用中文模型转换、提示词翻译优化、参数取舍、负面词、文字 logo 风险、参考图权重控制。
---

# Prompt Platform Adapter

## Core Workflow

Turn one visual brief, reference-image breakdown, or existing prompt into platform-specific prompt outputs.

1. Preserve the creative intent before changing syntax. Identify subject, visual story, composition, light, camera, material, color, post-processing, and constraints.
2. Decide target platforms. Default to Midjourney, Jimeng, Kling, Nano Banana, Seedream, and generic Chinese model when the user asks for "all platforms" or does not specify.
3. Classify the source with the Platform Intake Checklist before converting.
4. Read `references/platform-rules.md` and `references/platform-matrix.md` before writing platform prompts.
5. Read `references/risk-controls.md` when the prompt includes text, logo, brand marks, people, realism requirements, reference images, or negative prompts.
6. Read `references/quality-scorecard.md` before returning professional packages, audits, repairs, A/B conversions, or benchmark work.
7. Convert by platform behavior, not by direct translation. Adjust prompt density, sentence style, parameters, negatives, reference-image language, and iteration notes.
8. Add conversion notes explaining what changed and why.
9. Run the Professional Conversion Gate before returning.

## Platform Intake Checklist

Classify the input before adapting:

- Brief: extract subject, output type, aspect ratio, visual story, composition, lighting, camera, material, and constraints. Fill missing fields with conservative defaults and state them.
- Existing Midjourney prompt: preserve core visual intent, remove MJ flags for non-MJ platforms, translate `--no` into scene-specific Chinese constraints, and decide whether MJ parameters should be kept, reduced, or removed.
- Existing Chinese prompt: identify whether it is natural art direction or a keyword pile; convert to MJ with concise visual nouns and parameters only when useful.
- Reference-derived visual DNA: preserve style anchor, light, composition, material logic, and do-not-copy notes; do not imply reference-weight exact copying.
- Failed prompt or failed image description: audit likely prompt causes first, then write a repair conversion with the smallest useful changes.
- Prompt bible: keep style anchor and shared rules stable while adapting platform prompt blocks and negative prompt base.

## Reference Routing

- Read `references/platform-rules.md` for every conversion task.
- Read `references/platform-matrix.md` when deciding platform fit, parameter policy, forbidden patterns, or failure modes.
- Read `references/risk-controls.md` for text/logo, realism, brand, reference-image weight, negative prompt, or safety-sensitive adaptation.
- Read `references/quality-scorecard.md` before returning professional output, A/B conversion, repaired prompts, prompt bible conversion, or v1 benchmark work.
- Read `references/case-library.md` when the task resembles product hero, fashion editorial, spatial installation, automotive reflection, or mood-only reference adaptation.
- Read `references/examples.md` when the user asks for examples or the task resembles product, fashion, spatial, automotive, or campaign prompt adaptation.
- Read `references/benchmark-suite.md` when testing, improving, or auditing the skill.

## Output Formats

### Full Cross-Platform Package

Return:

```text
Intent lock:
- Subject:
- Visual story:
- Composition:
- Lighting:
- Camera/lens:
- Material/color/post:
- Constraints:

Conversion notes:
- What stays consistent:
- What changes by platform:
- Parameter policy:
- Text/logo policy:
- Reference image policy:

Prompt - Midjourney:
[prompt]

Prompt - Jimeng:
[prompt]

Prompt - Kling:
[prompt]

Prompt - Nano Banana:
[prompt]

Prompt - Seedream:
[prompt]

Prompt - Generic Chinese model:
[prompt]

Negative/risk controls:
[platform-aware risks]

Quality score:
[compact score from quality-scorecard when professional output is requested]

Iteration note:
- Preserve:
- Test next:
- Watch:
```

### Single Platform Conversion

When the user names one target platform, return:

```text
Intent preserved:
[brief summary]

Target platform:
[platform]

Converted prompt:
[ready-to-use prompt]

Conversion note:
[why wording, parameters, negatives, or reference controls changed]

Risks:
[specific risks and fixes]
```

### Prompt Audit Before Conversion

When the input prompt is weak, unsafe, or overloaded, audit before converting:

```text
Prompt audit:
- Missing visual information:
- Platform mismatch:
- Text/logo risk:
- Realism risk:
- Negative prompt risk:

Clean intent:
[rewritten platform-neutral brief]

Then convert:
[requested platform outputs]
```

### Failed Prompt Repair

When a prompt or generated result failed, return:

```text
Failure audit:
- What failed:
- Likely prompt cause:
- Platform mismatch:
- Risk level:

Repair strategy:
- Keep:
- Change:
- Remove:

Repaired platform prompt:
[target prompt]

Iteration note:
[what to test next]
```

### Prompt Bible Conversion

When adapting a prompt bible, return:

```text
Style anchor preserved:
[shared visual language]

Shared rules:
- Composition:
- Lighting:
- Camera:
- Material/color:
- Text/logo policy:
- Negative prompt base:

Platform prompt blocks:
- Midjourney:
- Jimeng:
- Kling:
- Nano Banana:
- Seedream:
- Generic Chinese model:

Conversion notes:
[platform differences and parameter policy]
```

### A/B Test Conversion

When the user wants variants, return:

```text
A/B test intent:
- Constant variables:
- Variable under test:

Variant A:
[conservative platform prompt]

Variant B:
[stronger platform prompt]

Decision metric:
[what result difference to compare]
```

## Professional Conversion Gate

Before finalizing, check:

- The intent lock captures the original concept before syntax changes.
- Each platform prompt has a distinct structure or wording appropriate to that platform.
- Midjourney parameters appear only in the Midjourney prompt.
- Chinese platforms use natural Chinese directions, not translated keyword piles.
- Text/logo requests are converted into clean areas or post-production notes, not exact rendered typography.
- Reference image weight is described cautiously and does not imply exact copying.
- Negative prompts target actual failure modes rather than generic lists.
- Conversion notes explain tradeoffs, not just "translated to Chinese".
- Professional packages include a quality score and iteration note.

If any item fails, revise once before answering.

## Default Policies

- If aspect ratio is missing, choose 4:5 for posters/product/social, 16:9 for cinematic/spatial, and 1:1 for square contact-sheet cells.
- If the user asks for exact brand text or logo generation, recommend leaving a clean area for later design layout.
- If the user provides a reference image, adapt mood, light, composition, and material logic; avoid copying original artwork, layout, logo, face, or distinctive product design.
- If platform support is uncertain, label the output as practical guidance instead of official platform syntax.
