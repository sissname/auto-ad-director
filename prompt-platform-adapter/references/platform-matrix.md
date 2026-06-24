# Platform Matrix

Use this matrix to choose platform behavior, parameter policy, forbidden patterns, and adaptation focus.

## Midjourney

- Best for: mood exploration, strong composition, stylized commercial art direction, quick visual variation.
- Parameter strategy: use `--ar`; use `--style raw` for control; tune `--stylize` and `--chaos` only when the user wants variation or polish.
- Avoid: exact text, exact logos, UI reproduction, long Chinese paragraphs, unsupported negative sentences.
- Failure modes: generic cinematic polish, fake typography, subject drift, over-stylized materials.
- Adaptation focus: concise visual nouns, composition first, short `--no` negatives, controlled parameters.

## Jimeng / 即梦

- Best for: detailed Chinese art direction, product or poster prompts, clear subject hierarchy.
- Parameter strategy: use natural-language ratios; avoid MJ flags; use separate negatives only if the interface supports them.
- Avoid: direct English keyword translation, exact brand text/logo, overly dense style stacks.
- Failure modes: weak hierarchy, overliteral reference copying, fake text, decorative clutter.
- Adaptation focus: ordered Chinese sections for subject, composition, light, camera, material, and constraints.

## Kling / 可灵

- Best for: cinematic stills, motion-ready scenes, fashion, spatial installations, action-oriented product moments.
- Parameter strategy: state still image vs video; use motion-ready physical details only when helpful.
- Avoid: duration/shot-cut language for stills, vague movement, effects that hide product structure.
- Failure modes: product hidden by atmosphere, subject/background merge, cinematic excess.
- Adaptation focus: physical relationships, visitor path or body motion, light movement, clear still-image instruction.

## Nano Banana

- Best for: fluent natural-language prompts, broad Chinese compatibility, direct art-direction style prompts.
- Parameter strategy: plain-language ratio and constraints; no flags.
- Avoid: dense English keyword strings, abstract style without staging, exact text/logo rendering.
- Failure modes: caption-like output, generic aesthetic, weak material logic.
- Adaptation focus: complete Chinese sentences, strong hierarchy, explicit realism and risk controls.

## Seedream

- Best for: polished commercial visuals, bilingual art direction, rich product/spatial/fashion prompts.
- Parameter strategy: specify static image and ratio in natural language; keep negatives separate when useful.
- Avoid: generic black-gold luxury, brand/text exactness, too many props.
- Failure modes: over-polished plastic surfaces, weak product hierarchy, decorative instead of commercial output.
- Adaptation focus: commercial polish plus exact material behavior and clean negative prompt.

## Generic Chinese Model

- Best for: unknown platform, universal fallback, handoff to users who may paste into different tools.
- Parameter strategy: no flags, no unsupported weights, use plain ratios and full sentences.
- Avoid: platform-specific syntax, exact logo/text generation, vague style shorthand.
- Failure modes: generic output, broken typography, missing camera/composition.
- Adaptation focus: self-contained prompt with subject, scene, composition, light, camera, material, post, and negatives.
