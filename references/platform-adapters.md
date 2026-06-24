# Platform Adapters

Use this reference when adapting automotive campaign prompts across image platforms. Treat platform support as practical prompt writing guidance, not a guarantee of exact parameter availability.

## Midjourney

Best for compact English keyword prompts with parameters.

Pattern:

```text
[subject and scene], [composition], [lighting], [camera/lens], [materials], [campaign style], [realism constraints] --ar [ratio] --style raw --stylize [number] --chaos [number] --quality 1 --no [negative prompt]
```

Guidance:

- Use `--ar 16:9` for wide hero/contact sheets, `--ar 4:5` for fashion posters, `--ar 1:1` for square social.
- Use `--style raw` for realism.
- Use `--stylize 80-150` for premium campaign polish; reduce for exact product realism.
- Use `--chaos 3-6` for controlled variation.
- Put negative constraints after `--no`; keep them short enough to remain useful.
- For logos/text, prefer "clean minimal brand typography area" or "clean logo area"; avoid relying on exact generated lettering.

## Nano Banana

Best for fluent natural-language prompts. Use Chinese if the user is Chinese; English is fine when requested.

Pattern:

```text
生成一张[画幅/比例][广告类型]：[subject/location/action]。构图[composition]。光线[lighting]。镜头[camera/lens]。色彩与材质[color/material]。要求[realism constraints]。负面约束：[negative prompt]。
```

Guidance:

- State aspect ratio in natural language: "横向 16:9", "竖版 4:5".
- Describe exact visual relationships: who is foreground, where the car sits, what is reflected.
- Include "不要生成随机文字/乱码车标" for brand areas.
- Do not include Midjourney parameters.

## Jimeng / 即梦

Best for detailed Chinese visual direction with clear scene order.

Guidance:

- Write a single fluent Chinese paragraph or short labeled sections.
- Put the most important subject first: vehicle, location, talent, action.
- Use concrete camera language: "低机位 35mm", "高位俯拍", "100mm 微距".
- Use separate "负面提示词" if the interface supports it; otherwise append "避免..." constraints.
- Avoid asking for complex exact typography; request "留出干净文字区域".

## Kling Image / 可灵

Best for cinematic Chinese prompts that may later extend into video concepts.

Guidance:

- Emphasize motion-ready scene logic: wind in hair, wet reflections, door opening, moving light, camera angle.
- Keep physical relationships explicit so the model does not merge person and car.
- For still images, state "单张广告海报/静态摄影".
- Avoid excessive parameter syntax; use natural language constraints.

## Seedream / Seedance-Style Image Prompts

Use for visually rich Chinese or bilingual prompts. If the user specifically requests Seedance for video, switch to shot motion, camera move, and duration language.

Guidance:

- For image prompts, specify "静态图像" to avoid accidental video language.
- Use high-level cinematic language plus exact composition.
- Keep negative prompt separate when possible.
- For car campaigns, specify "真实车辆比例、轮胎贴地、车漆反射真实".

## Generic Chinese Image Model

Use when the platform is unknown or the user wants a universal prompt.

Pattern:

```text
主题：[one sentence]
画面：[subject, setting, action]
构图：[composition]
光线：[lighting]
镜头：[camera/lens]
色彩材质：[palette/materials]
风格：[campaign style]
负面约束：[negative prompt]
```

Guidance:

- Prefer clear Chinese sentences over keyword piles.
- Avoid platform flags such as `--ar`.
- Include aspect ratio in plain language.
- Use "可预留文字区域" rather than generating exact ad copy inside the image.

## Conversion Rules

- Preserve intent before syntax: do not lose composition, light, lens, or product constraints.
- Translate English MJ keywords into fluent Chinese for Chinese models.
- Remove unsupported flags when moving away from MJ.
- Keep negative prompts platform-appropriate: terse for MJ, explicit sentence constraints for Chinese models.
- When platform behavior is uncertain, say "平台通用版" and provide a clean natural-language prompt.
