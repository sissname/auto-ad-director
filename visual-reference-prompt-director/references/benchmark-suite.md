# Benchmark Suite

Use these v1 acceptance benchmarks to test whether the skill produces prompt-ready structure, safe transfer rules, and platform-aware output rather than generic image description.

## Acceptance Benchmark 1: Automotive Night Mood to Running Shoes

Input:

```text
Use $visual-reference-prompt-director. I have a rainy blue night sports car ad reference: low camera, wet asphalt, long reflection, dark upper negative space, hard blue rim light. Keep the mood but change the subject to running shoes. Output a full v1 prompt package.
```

Expected output:

- Reference read with visual story, hierarchy, composition, lighting, camera, material/color, post, transferable DNA, and do-not-copy notes.
- Subject swap logic that rebuilds shoe geometry, outsole contact, mesh/rubber highlights, and aligned reflection.
- Platform prompts for Midjourney, Jimeng, Kling, Seedream, Nano Banana, and generic Chinese model.
- Quality score and iteration notes.

Fail if:

- It copies car brand, vehicle shape, license plate, exact campaign layout, or car-specific language.
- It ignores reflection physics or shoe-specific material constraints.

## Acceptance Benchmark 2: Black-and-White Fashion Portrait to Perfume Bottle

Input:

```text
Use $visual-reference-prompt-director. Reference: low-key black-and-white fashion portrait, one side-lit model, deep shadow, shallow focus, soft grain. Change the subject to a perfume bottle and output prompts.
```

Expected output:

- Separates portrait mood from model likeness, pose, clothing, and exact crop.
- Rebuilds glass bottle silhouette, edge highlights, label/text safety, tabletop or plinth contact, and simple reflection.
- Includes negative constraints for fake label text, warped bottle, noisy glass, copied likeness, and generic black-gold luxury.

Fail if:

- The output still reads like a portrait prompt.
- It asks the model to render exact label typography.

## Acceptance Benchmark 3: Warm Hotel Lobby, Analysis Only

Input:

```text
Use $visual-reference-prompt-director to analyze a warm hotel lobby reference: symmetrical wide frame, practical lights, stone floor, wood panels, soft seating. Only analyze it; do not generate prompts.
```

Expected output:

- Uses Analysis Only format.
- Includes visual story, composition, lighting, camera/lens, color/material/post, transferable rules, non-transferable details, and failure risks.
- Does not output platform prompts.

Fail if:

- It generates Midjourney/Jimeng prompts.
- It misses non-transferable furniture/art/logo/layout details.

## Acceptance Benchmark 4: Mall Light Tunnel to Skincare Pop-Up

Input:

```text
Use $visual-reference-prompt-director. Reference: mall pop-up with tunnel-like light ribs, reflective floor, entrance threshold, photo point at the end. Translate the visual DNA into a skincare brand pop-up effect image.
```

Expected output:

- Extracts entrance, light rhythm, visitor path, reflective floor, product/plinth logic, and photo point.
- Rebuilds brand expression around skincare materials: translucent, watery, soft diffusion, clean product display.
- Includes platform prompts and installation-specific failure risks.

Fail if:

- It becomes a generic sci-fi tunnel.
- It misses visitor scale, entrance logic, or product display.

## Acceptance Benchmark 5: Illustrated Poster Risk Review

Input:

```text
Use $visual-reference-prompt-director to tell me what I can and cannot copy from a distinctive illustrated poster reference before making an AI image prompt. It has a recognizable character, hand-lettered title, bold limited palette, and unusual layout.
```

Expected output:

- Uses Risk Review format.
- Clearly separates transferable mood/color/composition from non-copyable character, lettering, layout, symbols, and artist-identifying expression.
- Provides safer translation before any prompt.

Fail if:

- It suggests copying the exact character, lettering, layout, or named style.
- It gives only legal disclaimers without usable visual translation.

## Acceptance Decision

The skill is v1-ready only if all five benchmarks produce:

- Structured breakdown or mode-specific output.
- Transferable visual DNA.
- Do-not-copy or risk notes.
- Platform-aware prompts when prompts are requested.
- Scene-specific negative constraints.
- Quality score or iteration notes for prompt packages.
