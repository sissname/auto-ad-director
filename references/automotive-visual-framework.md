# Automotive Visual Framework

Use this reference to design premium car campaign prompts with consistent visual language.

## Global Style Anchor Pattern

Create a short paragraph that locks the campaign world:

```text
Shared visual language: [brand tier] automotive advertising + [fashion/product/editorial tone] + [city/landscape/architecture] + [light signature]. Core objects: [vehicle], [talent/props], [materials]. Talent emotion: [cool/distant/confident/etc.]. Product rules: [proportions, logo/text areas, reflections]. Avoid: [style-breaking defects].
```

Strong anchors usually specify:

- Vehicle: body color, segment, body type, clean logo area, grounded wheels.
- Human presence: age/style only when useful, gesture, wardrobe, emotional distance.
- Location: city, architecture, ground material, skyline, wet street, rooftop, showroom.
- Light: hard sun, blue-hour rain, golden side light, soft showroom daylight, macro flare.
- Materials: metallic paint, glass, mirror wall, wet pavement, red brick, black trim, fabric/sequence highlights.
- Campaign restraint: low saturation, high contrast, real reflection logic, no random typography.

## Shot Taxonomy

Use these shot types to build variety without losing coherence.

### Hero Exterior

- Product-first wide or three-quarter shot.
- Use architectural lines and ground reflections to lead toward the car.
- Good defaults: 24-35mm, low or architectural eye-level, small aperture feel, 16:9.

### Automotive Fashion Portrait

- Talent and car share the frame; gesture creates narrative.
- Use door edge, roofline, hood, or mirror as a compositional line.
- Good defaults: 35-50mm, low or slightly high angle, hard side light, 4:5.

### Macro Detail

- Brand letters, light bar, wheel, paint reflection, sensor detail, interior surface.
- Treat the car like luxury jewelry or technology.
- Good defaults: 85-100mm macro, shallow depth, bloom or prism flare only if controlled.

### Reflection / Mirror

- Glass wall, mirrored building, wet pavement, car paint, window reflection.
- State whether repeated people are reflections, not extra real subjects.
- Include "accurate reflection logic" and "do not create duplicate real talent."

### Rainy City Wide

- Wet street, glass towers, small human figure, blue-gray air, warm window accents.
- Keep it cinematic, not neon cyberpunk unless requested.
- Good defaults: 28-35mm, atmospheric perspective, restrained contrast.

### Rooftop Architectural

- Vehicle as a design object inside a city-stage composition.
- Use skyline, geometric floor, facade color, mirror wall, long sunlight.
- Good defaults: 24-28mm, clean commercial photography, realistic scale.

### Showroom Catalog

- Cleaner, brighter, more controlled than street work.
- Use white/neutral architecture, diffuse daylight, restrained wardrobe.
- Good defaults: 35-50mm, full body or product three-quarter, low saturation.

### Contact Sheet

- 6/9/12-frame grid with one vehicle, one campaign world, varied shot types.
- The prompt should say "clean borders, no captions" unless the user asks for labels.
- Keep recurring characters consistent without asking for impossible identity precision.

## Scene Field Template

Use this template before writing prompts:

```text
Visual story: What moment is this? Why does the image exist?
Composition: Subject hierarchy, lines, foreground/background layers, eye path.
Lighting: Source direction, softness, contrast ratio estimate, highlight/shadow behavior.
Camera/lens: Angle, distance, focal length estimate, depth of field.
Color/material/post: Palette, car paint, glass/wet/brick/metal/fabric, grain/HDR/bloom.
Constraints: Vehicle realism, clean text/logo areas, no duplicates, no geometry errors.
```

Lighting ratio guide:

- 2:1 or 3:1: clean catalog, soft daylight, readable product.
- 4:1 or 5:1: hard editorial advertising, deep shadows with retained detail.
- 8:1+: dramatic silhouette; use carefully to avoid dead black product loss.

## Premium Automotive Negative Prompt Library

Use as a base and trim to fit the platform:

```text
extra people, duplicate face, distorted limbs, deformed hands, floating wheels, broken wheel geometry, warped car body, incorrect vehicle proportions, plastic paint, melted architecture, impossible reflections, random watermark, gibberish logo, incorrect brand text, extra license plate text, cheap studio look, cartoon style, over-smoothed skin, excessive HDR, blown-out sky, crushed black shadows without detail, low-resolution noise
```

Chinese version:

```text
不要生成多余人物、重复脸、肢体变形、手部错误、漂浮轮胎、错乱车轮、车身比例错误、塑料质感车漆、建筑融化、反射逻辑错误、随机水印、乱码车标、错误品牌文字、额外车牌文字、廉价棚拍、卡通感、过度磨皮、过度 HDR、天空过曝、死黑无细节、低清噪点
```
