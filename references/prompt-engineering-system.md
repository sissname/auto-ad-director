# Prompt Engineering System

Use this reference when the user wants more controlled prompt engineering, parameter experiments, prompt versioning, or reusable prompt modules. Treat everything here as an adjustable system, not a rigid recipe.

## Flexibility Principle

- Start with the user's intent, not with a fixed template.
- Use modules as building blocks; remove any module that makes the prompt too long or too constrained.
- Prefer a clear prompt with 5 strong decisions over a bloated prompt with 20 weak adjectives.
- Treat platform parameters as experiment knobs. Record what changed; do not present any value as universally best.

## Modular Prompt Blocks

Build prompts from only the blocks needed for the task:

```text
vehicle_block: [brand/model/body type/color/stance/geometry constraints]
brand_block: [brand territory, audience, tone]
scene_block: [location, weather, time, architecture, ground material]
composition_block: [subject hierarchy, camera angle, foreground/background, eye path]
lighting_block: [source direction, softness, contrast ratio, highlight/shadow behavior]
camera_block: [lens estimate, distance, depth of field, crop/aspect]
material_block: [paint, glass, chrome, wet road, fabric, interior surfaces]
human_block: [talent role, pose, wardrobe, emotion, relation to car]
platform_block: [aspect ratio, stylization, platform-specific syntax]
negative_block: [scene-specific risks, not a generic dump]
iteration_block: [what to preserve, what to test, expected effect]
```

Minimum good automotive prompt:

```text
vehicle_block + scene_block + composition_block + lighting_block + material_block + negative_block
```

Add `brand_block` for campaign work, `human_block` for fashion/lifestyle, and `iteration_block` when revising results.

## Parameter Experiment Heuristics

### Midjourney

Use these as starting ranges:

- `--style raw`: prefer for realism and car geometry.
- `--stylize 50-90`: product accuracy and controlled realism.
- `--stylize 100-160`: campaign polish with moderate interpretation.
- `--chaos 2-4`: stable hero images and product geometry.
- `--chaos 5-8`: contact sheets, moodboards, exploratory variation.

Experiment rule:

```text
Only change one variable per version when diagnosing a failure.
```

Example:

```text
V1: --stylize 140 --chaos 6
Issue: car body too interpretive.
V2: --stylize 80 --chaos 3
Expected effect: cleaner product geometry, less campaign abstraction.
```

### Chinese Natural-Language Models

Prompt length is a control surface:

- Short prompt: good for simple product scenes; may under-specify brand tone.
- Medium prompt: best default for automotive ads; clear sections without overload.
- Long prompt: useful for contact sheets or precise story worlds; may cause detail drift.

Use section labels when the scene has many constraints:

```text
主题：
画面：
构图：
光线：
镜头：
材质：
负面约束：
```

### Video-Capable Image/Video Models

If the task is still image, say "static advertising image" or "single poster image." If the task is video, shift to motion:

```text
camera_move:
vehicle_motion:
human_motion:
duration:
first_frame:
last_frame:
```

## Version Control

Use this format when doing serious prompt operations:

```text
Version:
Prompt change:
Changed variable:
Reason:
Expected effect:
Observed result:
Score:
Next action:
```

Useful changed variables:

- vehicle description
- camera/lens
- lighting
- location
- material contrast
- platform parameter
- negative constraint
- human pose
- prompt length

## Controlled A/B Testing

Good A/B tests change one meaningful creative variable:

- A: hard sunlight vs B: blue-hour rain
- A: low 35mm hero vs B: long-lens executive arrival
- A: clean architecture vs B: wet street reflection
- A: no human vs B: distant owner gesture

Weak A/B tests only add vague adjectives:

- A: cinematic vs B: very cinematic
- A: premium vs B: ultra premium

## Prompt Compression

When a prompt feels too heavy, compress in this order:

1. Remove repeated adjectives.
2. Merge color and material into one phrase.
3. Keep only one location family.
4. Keep one camera strategy.
5. Move quality warnings into negative prompt.

Do not remove:

- vehicle realism constraints
- ground contact
- logo/text safety
- main light direction
- subject hierarchy

## Non-Restrictive Defaults

These are defaults, not limits:

- Use 16:9 for hero and contact sheet; change for social, poster, or user request.
- Use 4:5 for fashion/product poster; change for platform needs.
- Use 35-50mm for realism; use wider lenses for architecture or more drama.
- Use restrained color grading for premium work; break this for youth, motorsport, or experimental briefs.
