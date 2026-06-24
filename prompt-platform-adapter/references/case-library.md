# Case Library

Use these text-only cases as v1 adaptation patterns. They are examples of prompt conversion logic, not official platform guidance or stored source imagery.

## Case 1: Perfume Product Hero

Input: frosted glass perfume bottle on wet black stone, low-key side light, silver-blue reflection, clean luxury poster, vertical 4:5.  
Goal: six-platform product hero package.

Conversion logic:

- Keep bottle hierarchy, wet stone, side light, silver-blue reflection, vertical poster.
- Midjourney uses `--ar 4:5`, `--style raw`, moderate stylize, and short `--no`.
- Chinese platforms use natural art direction, fake-label constraints, and glass geometry controls.
- Risk policy: no exact label text, no fake logo, avoid generic black-gold luxury.

## Case 2: Fashion Editorial

Input: model in matte red coat under hard winter sunlight, urban concrete wall, editorial crop, strong shadow, no readable text.  
Goal: adapt to MJ, Jimeng, Seedream, and generic Chinese.

Conversion logic:

- Keep color blocking, hard sunlight, concrete texture, editorial crop.
- Add hand/face/limb realism where people appear.
- Avoid magazine masthead, brand typography, and exact designer logos.
- Kling may include wind or coat movement only if the user wants motion-ready stills.

## Case 3: Spatial Skincare Pop-Up

Input: skincare pop-up tunnel with translucent ribs, aqua light, reflective floor, visitor path, product plinth, photo point.  
Goal: all-platform conversion with reference mood-only policy.

Conversion logic:

- Preserve tunnel rhythm, visitor path, reflective floor, product display, soft aqua light.
- State that reference controls mood/composition/light only.
- Avoid copying original signage, brand graphics, floor plan, or exact installation geometry.
- Spatial negatives: impossible structure, overexposed light ribs, unreadable signage, unsafe crowd clutter.

## Case 4: Automotive Reflection to Running Shoes

Input: MJ prompt about sports car on rain-wet asphalt with blue rim light and long reflection.  
Goal: convert to Chinese platforms and change subject to running shoes.

Conversion logic:

- Remove MJ flags from Chinese outputs.
- Preserve low-angle wet reflection and blue rim light.
- Replace vehicle geometry with outsole contact, shoe-pair alignment, mesh/rubber material.
- Negative controls: fake logo, warped soles, duplicated shoes, broken reflection, random text.

## Case 5: Failed Prompt Repair

Input: "luxury watch black gold cinematic ultra detailed logo text 8k" produced fake logo, plastic metal, unreadable text, and generic luxury look.  
Goal: audit and repair for MJ and generic Chinese model.

Conversion logic:

- Identify vague luxury language and exact logo/text request as likely causes.
- Replace with material-specific watch geometry, brushed steel, sapphire glass, controlled macro light.
- Move logo/text to clean blank dial or post-production note.
- Negative controls: fake logo, warped hands, melted dial markers, plastic metal, excessive black-gold smoke.
