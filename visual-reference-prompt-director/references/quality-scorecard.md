# Quality Scorecard

Use this scorecard before returning professional output, prompt bibles, v1 benchmark responses, or any answer where the user asks whether the work is mature.

Score each category from 1 to 5. Revise any category below 4 before final output.

## Score Categories

### Visual Specificity

5 means the output names concrete visual relationships: subject hierarchy, frame, eye path, light direction, material response, and post-processing.  
1 means it relies on generic terms such as cinematic, premium, beautiful, high-end, or futuristic without operational detail.

### Transferability

5 means the output clearly separates reusable visual DNA from original subject, exact layout, logos, text, faces, artwork, and brand-specific material.  
1 means it effectively copies the reference or cannot work with a new subject.

### Composition Logic

5 means the prompt can stage the frame: camera height, subject placement, foreground/background, negative space, and viewer eye path are clear.  
1 means the prompt only lists objects.

### Lighting Control

5 means the light source, direction, contrast, ratio estimate, shadow behavior, and material response are clear.  
1 means it says only "good lighting", "cinematic lighting", or "soft light".

### Platform Fit

5 means each platform prompt uses an appropriate syntax, detail density, and negative constraint style.  
1 means the same prompt is copied across platforms or uses unsupported flags.

### Risk Handling

5 means the answer flags do-not-copy elements, text/logo risks, likeness or artwork risks, and likely generation failures.  
1 means no risks are named.

### Iteration Usefulness

5 means the answer tells the user what to preserve, what to test next, and what risk to watch in the next generation round.  
1 means it stops at a single final prompt.

## Output Pattern

Use this compact form when scoring:

```text
Quality score:
- Visual specificity: 4/5
- Transferability: 5/5
- Composition logic: 4/5
- Lighting control: 4/5
- Platform fit: 4/5
- Risk handling: 5/5
- Iteration usefulness: 4/5

Revision note:
[one sentence describing the weakest remaining risk]
```

## Revision Rules

- If visual specificity is weak, replace adjectives with frame, light, material, and camera details.
- If transferability is weak, rewrite the style anchor without protected names, exact layouts, or original subject identity.
- If composition logic is weak, add camera height, subject placement, eye path, and negative space.
- If lighting control is weak, add direction, contrast, shadow, highlight, and material response.
- If platform fit is weak, rewrite platform prompts separately rather than translating one prompt.
- If risk handling is weak, add do-not-copy and generation failure notes.
- If iteration usefulness is weak, add preserve/test/watch notes.
