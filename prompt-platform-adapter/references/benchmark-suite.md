# Benchmark Suite

Use these v1 acceptance benchmarks to validate mature cross-platform adaptation. Passing requires platform-specific conversion, risk policy, quality scoring, and useful iteration notes.

## Acceptance Benchmark 1: Perfume Product Hero Across Six Platforms

Input:

```text
Use $prompt-platform-adapter to convert this brief to MJ, 即梦, 可灵, Nano Banana, Seedream, and generic Chinese model: frosted perfume bottle on wet black stone, low-key side light, silver-blue reflection, vertical 4:5, clean luxury poster.
```

Expected output:

- Intent lock with subject, story, composition, lighting, camera, material/color/post, and constraints.
- Six platform prompts with clear platform differences.
- Text/logo and fake label risks.
- Quality score and iteration note.

Fail if:

- Prompts are direct translations.
- MJ parameters appear in Chinese platforms.
- It asks models to render exact label text.

## Acceptance Benchmark 2: MJ Running Shoes Prompt to Chinese Platforms

Input:

```text
Use $prompt-platform-adapter to convert this Midjourney prompt to 即梦, 可灵, Seedream, and generic Chinese model: premium running shoes on rain-wet black asphalt, low-angle hero composition, blue rim light, long reflection, commercial product launch still --ar 4:5 --style raw --no logo text watermark warped sole.
```

Expected output:

- Removes MJ flags from Chinese platforms.
- Preserves low-angle reflection logic.
- Adds shoe-specific geometry, outsole contact, material, and logo/text risks.
- Explains conversion choices.

Fail if:

- MJ flags remain in Chinese prompts.
- Reflection and low camera are lost.
- Negative prompt becomes generic.

## Acceptance Benchmark 3: Spatial Mood-Only Reference

Input:

```text
Use $prompt-platform-adapter. I have a reference image for mood only. Convert my brief across all platforms: skincare pop-up tunnel with soft aqua light, reflective floor, translucent product plinth, visitor photo point. Explain reference image weight and what not to copy.
```

Expected output:

- Explains reference image policy.
- Does not imply exact copying.
- Includes spatial structure, visitor path, product plinth, and photo point.
- Names overexposure, signage, crowd, structure, and generic sci-fi risks.

Fail if:

- It treats the reference as exact layout to copy.
- It misses installation-specific failure risks.

## Acceptance Benchmark 4: Failed Prompt Repair

Input:

```text
Use $prompt-platform-adapter to repair this failed prompt for MJ and generic Chinese model: luxury watch black gold cinematic ultra detailed logo text 8k. The result had fake logo text, plastic metal, distorted watch hands, and generic smoke.
```

Expected output:

- Failure audit before repaired prompts.
- Identifies vague luxury language, exact logo/text, and material under-specification as causes.
- Repairs with watch geometry, brushed metal, sapphire glass, macro light, and clean typography area.
- Includes quality score or iteration note.

Fail if:

- It only rewrites prettier prompts without diagnosing failure.
- It keeps exact logo/text generation.

## Acceptance Benchmark 5: Prompt Bible Cross-Platform Conversion

Input:

```text
Use $prompt-platform-adapter to convert this prompt bible across all platforms. Style anchor: quiet premium city night, wet ground, restrained blue highlights, low camera, product silhouette first. Shared rules: no readable text, clean logo area, realistic reflections, commercial poster crop.
```

Expected output:

- Preserves style anchor.
- Creates shared rules and platform prompt blocks.
- Differentiates parameter strategy across platforms.
- Keeps text/logo policy and reflection risk controls.

Fail if:

- It drops the style anchor.
- It treats the prompt bible as one single prompt.
- It omits platform parameter strategy.

## Acceptance Decision

The skill is v1-ready only if all five benchmarks produce:

- Intent lock or audit before conversion.
- Platform-specific prompts or blocks.
- Conversion notes.
- Risk controls for text/logo, realism, negative prompts, and references when relevant.
- Quality score or iteration note for professional outputs.
