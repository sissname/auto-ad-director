# Iteration Playbook

Use this reference when improving generated images, creating A/B prompt variants, or building a repeatable campaign workflow.

## Result Audit

Ask the user for the generated image when possible. If only a description is available, audit from that description.

```text
Keep: [what already works]
Fix: [one to three highest-impact failures]
Protect: [elements that must not drift]
Next prompt move: [smallest effective edit]
```

Prioritize fixes in this order:

1. Vehicle geometry and wheel contact.
2. Main composition and subject hierarchy.
3. Lighting and material realism.
4. Brand tone.
5. Styling details and background richness.

## Prompt Revision Ladder

Use the lowest rung that solves the issue:

1. Constraint patch: add or tighten a negative prompt.
2. Staging patch: clarify who/what is where.
3. Lens/light patch: change camera angle, focal length, or light direction.
4. World patch: change location, weather, ground material, or architecture.
5. Concept reset: rebuild the style anchor and shot from scratch.

## A/B Variant Strategy

When asked for variants, produce purposeful differences:

- A: faithful repair. Same composition, tighter realism constraints.
- B: stronger campaign version. Same idea, more decisive light/location/pose.
- C: exploratory if requested. Different shot type or mood, still same brand world.

Do not create variants that differ only by adjectives like "more cinematic" or "more premium." Change controllable visual variables.

## Production Workflow

For real campaign work, use this loop:

1. Style anchor: lock brand archetype, palette, location family, light signature.
2. Shot system: define hero, support, detail, human, environment, and social crop.
3. Generation batch: produce 3-5 prompt variants per key shot.
4. Selection: choose based on car realism first, then brand impact.
5. Repair: apply the revision ladder.
6. Lock winners: record final prompt, seed/reference settings if the platform supports them, and what changed.

## Prompt Change Log Format

Use this when the user is iterating:

```text
Version:
Changed:
Reason:
Expected effect:
Risk:
```

Example:

```text
Version: V2
Changed: Replaced "ultra-wide futuristic plaza" with "35mm low eye-level wet Shanghai street, tires firmly on black asphalt."
Reason: V1 warped the wheelbase and made the car float.
Expected effect: More believable stance and clearer ground contact.
Risk: Less architectural drama.
```

## When to Stop

Stop expanding prompts when the next edit would only add style noise. A good automotive prompt usually has:

- One vehicle.
- One main location.
- One light signature.
- One camera strategy.
- One material contrast.
- One clear human action, if talent is included.
