# Platform Output Formats

Use this file when turning visual DNA into prompts. Platform adaptation must preserve intent while changing syntax, detail density, and risk controls. Treat platform guidance as practical prompt-writing advice, not as an official guarantee of feature support.

## Platform Selection

- Midjourney: compact visual language, strong composition, mood, and style anchors.
- Jimeng / 即梦: detailed Chinese visual direction with clear subject hierarchy and scene order.
- Kling / 可灵: cinematic stills that may later become motion concepts; useful for spatial, fashion, and action-ready scenes.
- Seedream: visually rich Chinese or bilingual image prompts with polished commercial rendering.
- Nano Banana: fluent natural-language prompts; useful for broad Chinese prompt compatibility and direct scene explanation.
- Generic Chinese model: safest fallback when the target platform is unknown.

## Midjourney

Best for compact visual language, composition, style anchors, and parameterized variations.

Template:

```text
[subject and action], [composition and camera], [lighting], [material/color], [environment], [post-processing], [safe translation note], [commercial realism constraints] --ar [ratio] --style raw --stylize [number] --chaos [number] --v 6 --no [short negatives]
```

Use:

- Put subject and composition first.
- Use `--style raw` for controllability when the brief needs realism.
- Use `--stylize 60-150` for polished commercial mood; reduce for strict product realism.
- Use `--chaos 3-8` for controlled variations, not for exact product work.

Avoid:

- Long prose explanations inside the prompt.
- Exact text, logo, slogan, UI, celebrity, or campaign imitation requests.
- Overloaded moodboards that merge incompatible references.

Failure modes:

- Generic cinematic look when material and light behavior are vague.
- Text/logo gibberish when the prompt asks for exact typography.
- Composition drift when too many subjects are equal priority.

## Jimeng / 即梦

Best for fluent Chinese scene descriptions with explicit subject hierarchy, atmosphere, and material behavior.

Template:

```text
画面主体：[primary subject]。
构图：[framing, eye path, negative space]。
光影：[direction, contrast, ratio estimate, material response]。
镜头：[camera height, lens feel, focus]。
色彩与质感：[palette, surfaces, post-processing]。
参考转译：[what to preserve from reference and what not to copy]。
限制：[avoid failures, text/logo safety, anatomy/geometry/reflection controls]。
```

Use:

- Write natural Chinese, not keyword fragments.
- Put the most important subject in the first sentence.
- Describe exact visual relationships: where light hits, what remains in shadow, what surface reflects.

Avoid:

- Midjourney flags.
- Asking for exact typography or brand marks.
- Too many disconnected style adjectives.

Failure modes:

- Over-literal copying if the reference role is not explained.
- Weak hierarchy when every visual element is listed with equal weight.

## Kling / 可灵

Best for cinematic still-image prompts with motion-ready physical logic.

Template:

```text
单张静态广告图：[primary subject and setting]。[composition and camera]。[light and atmosphere]。[material and physical interaction]。画面具有可延展为视频镜头的真实动作/动线逻辑，但当前只生成静态画面。避免[risks]。
```

Use:

- Emphasize motion-ready scene logic: wind, reflection, entrance path, body gesture, light movement.
- State "单张静态广告图" when the user wants an image, not video.
- Keep foreground/background separation explicit.

Avoid:

- Duration, shot cuts, or multi-shot video language for still images.
- Abstract motion that breaks product geometry.

Failure modes:

- Subject/environment merge when movement language is vague.
- Cinematic excess that hides product or spatial structure.

## Seedream

Best for polished commercial visuals with rich Chinese or bilingual descriptions.

Template:

```text
静态图像，[image type and aspect]。[primary subject] in/at [setting]，采用[composition]。[lighting] creates [material response]。[palette and post]。参考图仅用于[transferable DNA]，不复制[non-transferable details]。Negative: [risks].
```

Use:

- Combine high-level art direction with exact composition and material rules.
- Specify "静态图像" to avoid accidental video phrasing.
- Keep negative prompt separate when the interface supports it.

Avoid:

- Generic "luxury black gold" unless it is genuinely the brief.
- Dense lists of props without hierarchy.

Failure modes:

- Over-polished plastic surfaces if material texture is underspecified.
- Brand-like text artifacts if text/logo policy is missing.

## Nano Banana

Best for fluent natural-language prompts, especially Chinese prompts that should read like direct art direction.

Template:

```text
生成一张[画幅/比例][图像类型]：[subject/location/action]。构图[composition and eye path]。光线[direction, ratio, mood]。镜头[camera/lens/focus]。色彩与材质[color/material/post]。参考图只借鉴[transferable elements]，不要复制[protected details]。负面约束：[negative prompt]。
```

Use:

- State aspect ratio in natural language: "横向 16:9", "竖版 4:5".
- Use complete sentences.
- Spell out what is borrowed from the reference and what is replaced.

Avoid:

- Platform flags.
- Exact lettering, logo, or UI reproduction.

Failure modes:

- Prompt becomes a caption if no image type or composition is stated.
- Generic output if the reference transfer rule is too broad.

## Generic Chinese Image Model

Best for broad compatibility. Use simple, complete Chinese sentences and strong hierarchy.

Template:

```text
生成一张[format/aspect]的[image type]：[primary subject]位于[composition]，[secondary elements]辅助形成[visual story]。光线来自[direction]，形成[contrast/ratio]，[materials]呈现[surface response]。镜头为[camera/lens estimate]，[post-processing]。参考图仅用于[light/composition/mood transfer]，不复制[non-transferable details]。请保持[constraints]，避免[negative risks]。
```

Use:

- Make the prompt self-contained.
- Prefer "留出干净文字区域" over asking the model to render exact text.
- Spell out realism, geometry, surface, and lighting constraints.

Avoid:

- Unsupported parameter syntax.
- Relying on brand names as visual shorthand when the task is reference translation.

Failure modes:

- Descriptive but not generative wording when subject action and frame are missing.
- Broken text/logo areas without explicit constraints.

## Default Aspect Ratio Choices

- Product hero: 4:5 or 3:4.
- Cinematic wide: 16:9 or 21:9.
- Social poster: 4:5.
- Square moodboard/contact sheet cell: 1:1.
- Spatial/environment: 16:9.

## Conversion Rules

- Preserve intent before syntax: do not lose composition, light, lens, material, or constraints.
- Translate terse English visual keywords into fluent Chinese for Chinese models.
- Remove unsupported flags outside Midjourney.
- Keep negative prompts platform-appropriate: terse for Midjourney, explicit sentence constraints for Chinese models.
- When platform behavior is uncertain, say "platform-generic" or "平台通用版" and provide a clean natural-language prompt.
