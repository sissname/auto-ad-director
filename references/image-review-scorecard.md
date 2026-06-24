# Image Review Scorecard

Use this reference when the user provides generated images, asks which image to keep, asks whether an output is usable, or wants a repair plan. Score to decide what to do next; do not use the score to over-police creative experiments.

## Score Categories

Score 1-5:

```text
Vehicle realism:
Brand fit:
Composition:
Lighting/material:
Human quality:
Text/logo safety:
Commercial usability:
Fixability:
```

Decision guide:

- 4.5-5 average: candidate/winner; minor retouch or prompt lock.
- 3.8-4.4 average: revise; keep concept, patch weaknesses.
- 3.0-3.7 average: salvage only if one element is very strong.
- Below 3.0: discard or concept reset.

Never approve an automotive ad image if vehicle realism is below 3, unless it is explicitly experimental art.

## Category Guidance

### Vehicle Realism

Look for:

- wheels aligned and grounded
- plausible body proportions
- clean glass and panel lines
- realistic paint reflections
- no melted architecture attached to car

Common fix:

```text
Add correct vehicle proportions, grounded wheels, visible contact shadow, realistic panel geometry.
```

### Brand Fit

Look for:

- brand/segment tone matches research or archetype
- location and human tone support the brand
- color/material language is coherent

Common fix:

```text
Re-anchor the image with brand territory, location family, light signature, and material contrast.
```

### Composition

Look for:

- one clear hero subject
- readable car silhouette
- foreground/background separation
- no accidental crop destroying the car

Common fix:

```text
Clarify subject hierarchy, camera position, crop, and eye path.
```

### Lighting and Material

Look for:

- believable light source
- shadows with detail
- metallic paint reads as metal, not plastic
- wet/glass reflections obey scene logic

Common fix:

```text
Specify source direction, contrast ratio, reflective surfaces, and restrained post-processing.
```

### Human Quality

Look for:

- hands/limbs plausible
- talent separated from vehicle
- expression fits campaign tone
- wardrobe supports brand

Common fix:

```text
Simplify pose, state exact relation to the car, reduce reflection complexity near limbs.
```

### Text and Logo Safety

Look for:

- no gibberish badges
- no random plate text
- typography area can be edited later

Common fix:

```text
Use clean logo area, blank typography space, no random text, no generated license plate characters.
```

### Commercial Usability

Look for:

- can this become a poster, social crop, moodboard, or pitch image?
- does it have negative space if copy is needed?
- is the product readable at thumbnail size?

Common fix:

```text
Add clean negative space, simpler background, stronger product scale, or social crop guidance.
```

### Fixability

Look for:

- if only one or two issues fail, revise.
- if car geometry, brand tone, and composition all fail, reset.

Common fix:

```text
Choose repair, salvage, or reset before writing a new prompt.
```

## Review Output Format

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

Next version:
[revised prompt or exact change list]
```

## Avoid Over-Limiting

- Do not reject unusual color, crop, or styling if it serves the brief and vehicle realism holds.
- Do not force luxury restraint on youth, motorsport, concept, or experimental art briefs.
- Do not require every image to be client-ready; some images are useful as exploration frames.
