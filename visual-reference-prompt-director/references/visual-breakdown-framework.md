# Visual Breakdown Framework

Use this file for every reference-image task. The goal is not to name what is visible, but to extract prompt-controllable rules.

## Breakdown Fields

### Visual Story

Define the image's narrative job in one sentence:

- What is the viewer meant to notice first?
- What emotional state does the image sell?
- Is the image editorial, commercial, cinematic, documentary, product-led, spatial, fashion-led, or abstract?

Prompt translation: make the story active, such as "a quiet premium product reveal after rain" instead of "nice night photo".

### Subject Hierarchy

Map primary, secondary, and atmospheric elements:

- Primary subject: the object, person, space, or action that must remain legible.
- Secondary subject: environment, props, gesture, surface, or supporting figure.
- Atmosphere: haze, reflections, weather, texture, negative space, crowd, shadow.

Prompt translation: name hierarchy directly. Models fail when every object is treated as equally important.

### Composition

Describe both geometry and eye path:

- Framing: close-up, medium, wide, hero, macro, cropped, symmetrical, diagonal, layered.
- Placement: center-weighted, rule of thirds, low horizon, high horizon, foreground occlusion, deep corridor.
- Eye path: where the viewer enters, what leads the eye, where it rests.
- Negative space: where text or brand overlay could go, if relevant.

Prompt translation: convert into "low-angle three-quarter composition with foreground shadow framing and clean upper-left negative space".

### Lighting and Ratio

Estimate visible light behavior:

- Direction: side, back, top, rim, soft frontal, window, practical, reflected, underlit.
- Contrast: low key, high key, hard shadow, soft gradient, high ratio, flat daylight.
- Function: reveal form, create silhouette, make material glossy, hide background, separate subject.
- Ratio estimate: use plain language such as "strong 4:1 side light" only as an estimate.

Prompt translation: include light source and material response, not just "cinematic lighting".

### Camera and Lens

Infer only visible camera language:

- Camera height: eye-level, low, high, tabletop, ground, drone-like.
- Lens feel: wide-angle spatial depth, normal editorial realism, telephoto compression, macro detail.
- Focus: shallow depth of field, deep focus, motion blur, selective focus.
- Movement implication: static product still, handheld realism, tracking motion, frozen action.

Prompt translation: use estimates like "telephoto-compressed feel" rather than fake metadata.

### Material, Color, and Texture

Name color discipline and material behavior:

- Palette: restrained neutrals, saturated accent, monochrome, complementary contrast, warm/cool split.
- Material response: matte, satin, chrome, glass, wet asphalt, velvet, skin, plastic, paper, stone.
- Texture scale: macro grain, smooth gradients, visible fabrication, environmental patina.

Prompt translation: tie color to surface, such as "cold blue reflections on wet black stone, warm amber skin highlights".

### Post-Processing

Identify visible finishing:

- Contrast curve: soft filmic roll-off, crisp commercial contrast, crushed blacks, lifted shadows.
- Grain/noise: clean digital, film grain, editorial texture.
- Color grade: teal-orange, warm natural, silver-cool, muted luxury, high saturation.
- Retouching: polished product, documentary skin, surreal composite, raw flash.

Prompt translation: include finishing only after core scene instructions.

## Transferable Visual DNA

Write the reusable DNA as rules:

- Keep: mood, light behavior, composition logic, lens feel, palette logic, material response.
- Change: exact subject, protected brand assets, copyable artwork, exact text, unique layout, identifiable people.
- Rebuild: scale, physics, surface contact, and environment around the new subject.

## Analysis Discipline

Do not output generic adjectives without operational meaning. Replace weak phrases:

- "high-end" -> "restrained palette, precise highlight control, clean negative space, minimal props"
- "cinematic" -> "wide frame, motivated side/back light, layered depth, controlled contrast"
- "moody" -> "low-key exposure, shadow-dominant frame, single rim highlight, muted color"
- "futuristic" -> "smooth material transitions, integrated light strips, minimal seams, cool reflective surfaces"

