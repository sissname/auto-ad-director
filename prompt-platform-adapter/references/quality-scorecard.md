# Quality Scorecard

Use this before returning professional cross-platform packages, audits, failed prompt repairs, prompt bible conversions, A/B tests, or benchmark responses.

Score each category from 1 to 5. Revise any category below 4 before final output.

## Score Categories

### Intent Preservation

5 means the platform outputs preserve the same subject, visual story, composition, lighting, camera, material, and constraints.  
1 means the platform rewrite changes the creative idea or drops essential visual logic.

### Platform Fit

5 means each platform uses native syntax, detail density, and phrasing.  
1 means the same prompt is copied across platforms or unsupported syntax is reused.

### Parameter Discipline

5 means parameters appear only where useful and supported, with clear reasons for using or avoiding them.  
1 means parameters are copied blindly or omitted when they are necessary for the output.

### Risk Handling

5 means text/logo, brand, likeness, reference image, realism, and safety risks are explicitly controlled.  
1 means risks are ignored or handled with generic disclaimers.

### Visual Specificity

5 means prompts include concrete subject hierarchy, composition, light, camera, material, color, and post-processing.  
1 means prompts rely on vague terms such as premium, cinematic, high-end, beautiful, or futuristic.

### Negative Prompt Usefulness

5 means negative prompts are scene-specific and platform-appropriate.  
1 means negative prompts are generic word piles or appear in unsupported formats.

### Iteration Value

5 means the answer tells the user what to preserve, what to test next, and what risk to watch.  
1 means it stops at final prompts with no learning loop.

## Output Pattern

```text
Quality score:
- Intent preservation: 5/5
- Platform fit: 4/5
- Parameter discipline: 4/5
- Risk handling: 5/5
- Visual specificity: 4/5
- Negative prompt usefulness: 4/5
- Iteration value: 4/5

Revision note:
[weakest risk or next improvement]
```

## Revision Rules

- If intent preservation is weak, rebuild a platform-neutral intent lock before converting.
- If platform fit is weak, rewrite each platform prompt separately.
- If parameter discipline is weak, remove unsupported flags and add a parameter policy.
- If risk handling is weak, add text/logo, reference, realism, and negative controls.
- If visual specificity is weak, replace adjectives with composition, light, camera, and material.
- If negative prompt usefulness is weak, make negatives scene-specific.
- If iteration value is weak, add preserve/test/watch notes.
