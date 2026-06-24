---
name: visual-reference-prompt-director
description: Analyze reference images, screenshots, moodboard frames, or described visuals into reusable visual DNA and prompt packages. Use when turning an image reference into prompt-ready structure, recreating the mood while changing the subject, producing Midjourney/Jimeng/generic Chinese model prompts, doing analysis-only reference breakdowns, or identifying visual risks, non-copyable elements, composition, lighting ratio, camera/lens, material, color, post-processing, and negative constraints. 中文适用：参考图拆解、光影构图分析、参考图转提示词、复刻气质但更换主体、只分析不生成 prompt、找出不可照抄项和失败风险。
---

# Visual Reference Prompt Director

## Core Workflow

Turn a reference image, screenshot, PDF frame, moodboard sample, or user-described visual into a reusable visual system and platform-ready prompts.

1. Identify the user mode: analysis only, prompt generation, subject swap, risk review, or benchmark/self-test.
2. Inspect the reference as visual evidence. If the actual image is not available, label all observations as inferred from the user's description.
3. Break the visual into: visual story, subject hierarchy, composition, light ratio, camera/lens, material/color, post-processing, and constraints.
4. Separate transferable mood from non-copyable specifics. Preserve atmosphere, structure, light behavior, and camera logic; avoid copying protected artwork, logos, exact layouts, faces, text, or distinctive proprietary design.
5. Build a style anchor: one compact paragraph that describes the reusable visual DNA without tying it to the original subject.
6. If the user asks to change subject, rewrite the visual DNA around the new subject before generating prompts.
7. Choose the delivery mode: single reference breakdown, subject swap, analysis-only, risk review, prompt bible, or case replay.
8. Output Midjourney, Jimeng, Kling, Seedream, Nano Banana, and generic Chinese model prompts when the user wants a full v1 prompt package; otherwise output only requested platforms.
9. Run the professional quality gate before finalizing. Revise once if the result is mostly description, lacks transfer rules, or misses risk controls.

## Reference Intake Checklist

Use the source type to decide how cautious the analysis should be:

- Real image attachment: inspect visible evidence directly; mark camera, lens, and light ratio as estimates unless metadata is supplied.
- Screenshot or social post: analyze the image content, crop, overlays, and compression artifacts; avoid copying UI, captions, account marks, or visible logos.
- Text-only reference description: state "inferred from description" and avoid pretending to see details that were not provided.
- PDF or deck frame: treat it as a selected visual frame; separate image content from layout, typography, annotations, page furniture, and client branding.
- Moodboard with multiple images: identify common visual DNA across references first, then note outlier elements that should not be merged into one overloaded prompt.

## Reference Routing

- Read `references/visual-breakdown-framework.md` for every image/reference analysis task.
- Read `references/platform-output-formats.md` when generating or adapting prompts for Midjourney, Jimeng, or generic Chinese image models.
- Read `references/risk-and-constraints.md` when the user asks what cannot be copied, when a real brand/person/artwork is involved, or when the prompt may create text/logo/style imitation risks.
- Read `references/quality-scorecard.md` before finalizing professional output, v1 benchmark work, prompt bibles, or any answer where maturity/professional quality matters.
- Read `references/case-library.md` when the user asks for examples, case replay, or when a task resembles automotive night reflections, perfume/product still life, fashion portrait translation, interior/spatial reference, or illustrated poster risk review.
- Read `references/examples.md` when the user wants examples or when you need a compact output pattern.
- Read `references/benchmark-suite.md` when testing this skill, evaluating its maturity, or running smoke prompts.

## Output Formats

### Reference Breakdown With Prompts

Return:

```text
Reference read:
- Visual story:
- Subject hierarchy:
- Composition:
- Lighting and ratio:
- Camera/lens estimate:
- Material/color:
- Post-processing:
- Transferable visual DNA:
- Do-not-copy / risk notes:

Style anchor:
[reusable visual system]

Prompt - Midjourney:
[ready-to-use prompt]

Prompt - Jimeng:
[ready-to-use Chinese prompt]

Prompt - Generic Chinese model:
[ready-to-use Chinese prompt]

Negative constraints:
[risks to suppress]
```

### Subject Swap

When the user wants to "keep the mood but change the subject", return:

```text
Kept from reference:
- Light:
- Composition:
- Camera:
- Color/material:
- Mood:

Changed for new subject:
- Subject logic:
- Setting logic:
- Material interaction:
- Risk controls:

Platform prompts:
[requested platforms]
```

### Analysis Only

When the user asks for analysis only, do not generate prompts. Return:

```text
Reference analysis only:
- Visual story:
- Composition:
- Lighting:
- Camera/lens:
- Color/material/post:
- Transferable rules:
- Non-transferable details:
- Failure risks:
```

### Risk Review

When the task is to identify failure risks or non-copyable elements, return:

```text
Risk map:
- Copying/IP risk:
- Brand/logo/text risk:
- Person/likeness risk:
- Platform generation risk:
- Composition failure risk:
- Material/lighting failure risk:

Safer translation:
[how to preserve the intent without copying the reference]
```

### Prompt Bible

When the user wants a reusable professional package, return:

```text
Project:
Reference role:

Style anchor:
[shared visual DNA]

Transfer rules:
- Composition:
- Lighting:
- Camera:
- Material/color:
- Post:
- Safe substitutions:

Platform prompts:
- Midjourney:
- Jimeng:
- Kling:
- Seedream:
- Nano Banana:
- Generic Chinese model:

Negative prompt base:
[scene-specific constraints]

Quality score:
[short 1-5 score summary from quality-scorecard]

Iteration notes:
- Preserve:
- Test next:
- Watch risks:
```

### Case Replay

When using a case from `references/case-library.md`, return:

```text
Case match:
- Closest case:
- What transfers:
- What changes:

Reference breakdown:
[task-specific analysis]

Prompt package or risk review:
[mode-specific output]
```

## Quality Rules

- Do not claim EXIF metadata, exact lens, focal length, lighting setup, or production facts unless supplied. Mark lens, light ratio, and camera height as visual estimates.
- Do not merely describe the image. Convert each observation into an instruction that can guide a new generation.
- Preserve mood through relationships: light direction, contrast, depth, eye path, material response, color discipline, and subject hierarchy.
- Avoid "in the style of [living artist/brand/campaign]" as the main instruction. Translate style into visual components.
- Keep text/logo requests safe. Prefer clean negative space for later typography over asking image models to render exact words.
- For subject swaps, rebuild physical interactions around the new subject; do not paste the old composition mechanically when scale, material, or movement changes.
- Always include constraints for fragile areas: hands/faces, reflections, readable text, logos, geometry, water/glass/metal, repeated patterns, and crowd details when relevant.
- If the reference is unavailable, ask for the image only when essential. Otherwise work from the description and clearly label uncertainty.

## Professional Quality Gate

Before returning a v1-level answer, check:

- The output separates observation from prompt translation.
- The style anchor can be reused with a different subject.
- Composition, light, camera, material, post, and constraints are all operational.
- The answer names at least one non-transferable or do-not-copy element when a reference is involved.
- Platform prompts differ by platform behavior, not only language.
- The negative constraints target likely failures in this scene.
- The next iteration note says what to preserve, what to test, and what risk to watch.

If any item fails, revise once before answering.
