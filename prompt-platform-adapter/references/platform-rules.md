# Platform Rules

Use this file for every platform adaptation. The goal is to make each output behave like a native prompt for that platform.

## Midjourney

Use for compact visual keywords, composition, style anchors, and parameters.

Pattern:

```text
[subject], [composition], [lighting], [camera/lens], [material/color], [environment], [post-processing], [realism constraints] --ar [ratio] --style raw --stylize [value] --chaos [value] --v 6 --no [short negatives]
```

Parameter policy:

- Use `--ar` when aspect ratio matters.
- Use `--style raw` for controllable realism.
- Use `--stylize 50-150` for commercial polish; reduce for product fidelity.
- Use `--chaos 3-8` for controlled exploration; avoid for strict product matching.
- Keep `--no` short and targeted.

Avoid:

- Long paragraph prompts.
- Exact rendered text, slogans, logos, or UI.
- Chinese-model negative phrasing inside MJ syntax.

Failure modes:

- Generic cinematic look if light/material details are vague.
- Text/logo gibberish if exact typography is requested.
- Subject drift if too many style anchors compete.

## Jimeng / 即梦

Use for detailed Chinese visual direction with ordered scene logic.

Pattern:

```text
画面主体：[subject]。
构图：[composition and eye path]。
光影：[light direction, contrast, material response]。
镜头：[camera height, lens feel, focus]。
色彩与质感：[palette, material, post]。
限制：[text/logo, anatomy, geometry, reflection, realism constraints]。
```

Parameter policy:

- Prefer natural-language aspect ratio such as "竖版 4:5" or "横向 16:9".
- Avoid MJ flags.
- Use separate negative prompt only if the interface supports it; otherwise append "避免..." constraints.

Avoid:

- Keyword piles translated from English.
- Asking for exact words, logos, or tiny package labels.

Failure modes:

- Overliteral reference copying if the reference role is not explained.
- Weak hierarchy if every noun is listed equally.

## Kling / 可灵

Use for cinematic stills and image prompts that may later become motion concepts.

Pattern:

```text
单张静态广告图：[subject and action]，[setting]。[composition/camera]。[motion-ready physical detail]。[lighting and atmosphere]。[material and realism constraints]。避免[risks]。
```

Parameter policy:

- State "单张静态广告图" for still-image output.
- Mention motion-ready physical details only when they help: wind, light sweep, visitor path, fabric movement, water reflection.
- Avoid duration or shot-cut language unless the user asks for video.

Avoid:

- Multi-shot storyboard language for one image.
- Motion words that break product geometry.

Failure modes:

- Product gets hidden by cinematic atmosphere.
- Person/object merges with background when movement relationships are vague.

## Nano Banana

Use for clear natural-language prompts, especially fluent Chinese art direction.

Pattern:

```text
生成一张[ratio/type]：[subject]位于[setting]，[composition]。光线[lighting]，镜头[camera]，色彩与材质[materials/post]。请保持[realism/brand/geometry constraints]，避免[negative risks]。
```

Parameter policy:

- Use plain language for aspect ratio.
- Avoid platform flags.
- Put constraints in full sentences.

Avoid:

- Dense English keyword strings.
- Overly abstract style descriptions without staging.

Failure modes:

- Output becomes a caption if no image type, composition, or subject action is stated.
- Generic results if material and light are not tied to the subject.

## Seedream

Use for polished commercial visuals with rich Chinese or bilingual descriptions.

Pattern:

```text
静态图像，[image type and ratio]。[primary subject] in/at [setting]，采用[composition]。[lighting] creates [material response]。[palette/post]。Negative: [risks].
```

Parameter policy:

- Say "静态图像" for still images.
- Use bilingual phrasing only when the user works bilingually or wants an English/MJ bridge.
- Keep negatives separate when useful.

Avoid:

- Generic black-gold luxury without product-specific material logic.
- Brand/text exactness.

Failure modes:

- Over-polished plastic look.
- Decorative but weak product hierarchy.

## Generic Chinese Image Model

Use as the safest fallback when platform is unknown.

Pattern:

```text
生成一张[ratio/type]：[subject]在[scene]中，[composition]，[visual story]。光线来自[direction]，形成[contrast]，[materials]呈现[response]。镜头为[camera/lens estimate]，[post-processing]。避免[negative risks]。
```

Parameter policy:

- No platform flags.
- Use complete Chinese sentences.
- Use direct constraints rather than abstract tags.

Avoid:

- Assuming support for weights, seeds, or style flags.
- Exact logo/text rendering.

Failure modes:

- Vague "高级感" output if there is no physical staging.
- Broken typography without text policy.

## Conversion Rule

Always convert in this order:

1. Lock the neutral intent.
2. Remove unsupported syntax.
3. Rewrite hierarchy for the target platform.
4. Add platform-specific parameter or no-parameter policy.
5. Add platform-specific risk controls.
6. Explain the conversion.
