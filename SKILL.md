---
name: auto-ad-director
description: Generate, adapt, diagnose, benchmark, and iterate cinematic automotive advertising image prompts and campaign prompt packages. Use when creating luxury car ads, EV campaign visuals, automotive fashion editorials, city/architecture car imagery, brand-specific visual systems, client-ready prompt bibles, shot lists, art-director reviews, prompt-engineering experiments, automotive shot-language systems, reference-image light and composition breakdowns, campaign moodboards, 6/9/12-frame contact sheets, multi-platform prompts for Midjourney, Nano Banana, Jimeng, Kling, Seedream, or generic Chinese image models, or when reviewing/repairing failed AI car images with issues like warped vehicles, bad wheels, wrong reflections, cheap lighting, weak brand tone, poor composition, or broken text/logo areas. 中文适用场景：汽车广告视觉导演、AI 生图提示词、汽车大片提示词、品牌视觉风格、车型 Campaign、汽车海报、光影构图拆解、参考图复刻、提示词工程、镜头语言、出图诊断、失败图修复、商业提案、Prompt Bible、Shot List、汽车广告客户交付。
---

# Auto Ad Director

## Operating Modes

Use the mode that matches the user request:

- Brief to campaign: turn a vehicle, audience, location, and mood into a hero prompt, support shots, or contact sheet.
- Reference to visual DNA: analyze an image, PDF shot, or sample campaign into reusable composition, lighting, lens, color, and constraint rules.
- Platform adaptation: convert a prompt between Midjourney, Nano Banana, Jimeng, Kling, Seedream, and generic Chinese models.
- Brand-style system: create a reusable brand or segment visual language before writing shots.
- Professional delivery: create prompt bibles, client proposal summaries, production shot lists, review notes, or handoff packages.
- Prompt engineering: modularize prompts, tune parameters, version prompt changes, and design controlled A/B tests.
- Shot system design: choose automotive shot roles and camera language for hero, product, human, detail, environment, and social frames.
- Result repair: diagnose generated images and produce targeted prompt revisions or A/B variants.
- Image review: score generated results and decide whether to keep, revise, salvage, or discard.
- Benchmark/self-test: evaluate the skill output against realistic automotive campaign tasks and revise weak references.

## Core Workflow

Turn a car campaign brief, reference image, generated result, or visual direction into a premium automotive prompt package.

1. Clarify or infer the brief: vehicle, market position, audience, location, talent, mood, output platform, aspect ratio, and number of shots. If key details are missing and the user did not ask for exploration, make tasteful defaults and state them briefly.
2. When a named brand, mature benchmark, or professional delivery is involved, read research-backed references first; distinguish source-backed cues from archetype-only heuristics.
3. Select a brand/segment archetype before writing shots when the user has not supplied a clear tone; use brand-level heuristics when a brand is named.
4. Break each scene into: visual story, composition and eye path, lighting and contrast ratio, camera/lens/position, color/material/post, and constraints.
5. Build a style anchor: define the shared visual language that should hold the campaign together across shots.
6. Generate prompt variants: produce the requested platforms, or default to Midjourney plus a natural-language Chinese model prompt when unspecified.
7. Add platform-specific controls: aspect ratio, stylization, text/logo handling, realism constraints, and negative prompt style.
8. Run the quality gate before answering: vehicle realism, brand tone, composition, lighting/material, platform syntax, and negative constraints.
9. Return a concise prompt package: make it directly usable, not a lesson unless the user asks for explanation.

## Reference Routing

- Read `references/automotive-visual-framework.md` when designing a new campaign, contact sheet, shot list, reference-image breakdown, or negative prompt set.
- Read `references/brand-archetypes.md` when the user names a brand, car segment, audience, market position, or asks for a distinct visual identity.
- Read `references/campaign-research-bank.md` when the user names Xiaomi, NIO, Li Auto, Audi, Porsche, Mercedes-Benz, asks for research-backed direction, asks whether output is mature/professional enough, or requests benchmark/audit work.
- Read `references/brand-visual-library.md` when the user names Xiaomi, NIO, Li Auto, Zeekr, XPeng, BYD, Audi, Porsche, BMW, Mercedes-Benz, Tesla, Lexus, or asks for sharper brand-level visual language. Pair it with `campaign-research-bank.md` for source-backed brands.
- Read `references/platform-adapters.md` when outputting or converting prompts for Midjourney, Nano Banana, Jimeng, Kling, Seedream, or generic Chinese image models.
- Read `references/prompt-engineering-system.md` when the user asks for parameter tuning, prompt versioning, A/B tests, modular prompt construction, or prompt operations. Treat it as adjustable guidance, not a fixed template.
- Read `references/shot-language-library.md` when building shot lists, contact sheets, prompt bibles, or camera/shot systems. Use it as a menu; do not force every shot type into every project.
- Read `references/quality-review.md` before finalizing complex prompt packages, when the user asks "is this good", or when generated images have car realism, text, lighting, reflection, or cheapness problems.
- Read `references/image-review-scorecard.md` when reviewing generated images, choosing winners, deciding whether to revise/salvage/discard, or writing image-specific repair prompts.
- Read `references/iteration-playbook.md` when the user provides generated results, asks how to fix/improve prompts, wants A/B variants, or wants a repeatable production workflow.
- Read `references/delivery-templates.md` when the user asks for a prompt bible, proposal, client-ready package, shot list, art-director review, handoff, or versioned production log.
- Read `references/benchmark-suite.md` when testing, improving, or auditing this skill, or when the user asks whether the output is mature/professional enough.
- Read `references/examples.md` when the user wants examples, when the request resembles luxury EV hard-light imagery, fashion-with-car posters, or campaign contact sheets, or when you need a compact output pattern.

## Output Formats

### Single Hero Image

Return:

```text
Style anchor:
Scene breakdown:
- Visual story:
- Composition:
- Lighting:
- Camera/lens:
- Color/material/post:
- Constraints:

Prompt - [platform]:
[ready-to-use prompt]

Negative prompt:
[negative constraints]
```

### Campaign Contact Sheet

For a 6/9/12-frame contact sheet, return:

```text
Campaign style anchor:
Grid:
- Frame 01: [shot type, subject, location, light, lens]
- Frame 02: ...

Contact sheet prompt - [platform]:
[single prompt describing the full grid]

Optional per-frame prompts:
[only include when the user asks for individual generation prompts]
```

Keep each frame distinct: mix hero exterior, talent interaction, macro detail, mirror/reflection, rainy or night city, architectural wide, and showroom/catalog shots as appropriate.

### Professional Delivery Package

When the user asks for a client-ready or production-ready output, return only the sections that fit the request:

```text
Project:
Vehicle:
Campaign idea:
Style anchor:
Visual rules:
Shot system:
Platform prompts:
Negative prompt base:
Iteration notes:
```

Prefer a compact prompt bible over a long essay. Use shot-list tables only when production planning matters.

### Reference-Image Breakdown

When given a reference image or PDF-derived shot, return:

```text
Reusable visual DNA:
- Subject hierarchy:
- Composition:
- Lighting:
- Camera:
- Color/material:
- Post:
- Risks:

Prompt adaptation:
[platform prompts]
```

Do not claim exact camera metadata unless supplied; label inferred lens, lighting ratio, and camera position as visual estimates.

### Prompt Adaptation

When converting an existing prompt:

- Preserve the creative intent before changing syntax.
- Remove parameters unsupported by the target platform.
- Convert terse English keyword prompts into fluent Chinese descriptions for Chinese models.
- Keep brand marks and text areas clean: prefer "leave clean logo/text area" over asking image models to render exact typography.

### Result Repair

When the user shows or describes a failed generation, return:

```text
Diagnosis:
- What failed:
- Likely prompt cause:
- Risk level:

Repair strategy:
- Keep:
- Change:
- Remove:

Revised prompt:
[target-platform prompt]

A/B variants:
- A: [conservative repair]
- B: [stronger creative shift]
```

Repair the smallest thing that plausibly caused the failure first. Do not rewrite the whole visual system unless the concept itself is weak.

### Image Review

When the user provides generated images or asks which result is usable, return:

```text
Image review:
- Vehicle realism:
- Brand fit:
- Composition:
- Lighting/material:
- Human quality:
- Text/logo safety:
- Commercial usability:
- Fixability:

Decision:
[winner / revise / salvage / discard]

Repair prompt move:
[smallest useful edit]
```

Allow experimental images when the brief calls for them, but do not approve broken vehicle geometry for commercial automotive use.

### Benchmark Review

When auditing this skill's output or a candidate prompt package, score:

```text
Brief fit:
Research-backed adjustment:
Visual specificity:
Automotive realism:
Brand maturity:
Platform execution:
Iteration usefulness:
Decision:
Revision:
```

Revise once when any category is weak. Treat benchmark output as an improvement loop, not as final client copy.

## Quality Rules

- Keep vehicle geometry believable: wheels grounded, body proportions realistic, brand/logo area clean, no random plate text.
- Use campaign language, not generic stock-photo phrasing. Anchor the image in light, material, lens, architecture, weather, talent gesture, and product surface.
- Avoid overloading a single prompt with every possible shot. For multiple deliverables, split into hero prompt, support shots, and contact sheet.
- Prefer restrained luxury color grading over neon, cyberpunk, plastic HDR, or generic "ultra detailed" excess unless requested.
- If the user names a real vehicle or brand, avoid unsafe claims about exact unreleased specs. Treat it as visual styling unless factual product accuracy is supplied.
- Avoid giving only one prompt for serious campaign work. Include either a style anchor plus shot logic, or a quality/repair note that explains how to iterate.
- For production use, optimize for controllability over maximal spectacle: fewer subjects, clearer geometry, stronger light direction, and explicit reflection logic.
- Treat references as tools, not constraints. If a user asks for experimental, youth, motorsport, surreal, non-luxury, or non-brand work, adapt the system instead of forcing premium restraint.
