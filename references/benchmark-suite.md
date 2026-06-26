# Benchmark Suite

Use this reference to self-test the skill or to create realistic practice tasks. Mature output should include research-backed style cues, a style anchor, shot logic, platform-aware prompts, negative risks, and iteration guidance.

## Scoring Rubric

Score each response from 1-5:

- Brief fit: answers the actual vehicle, brand, platform, and deliverable.
- Research use: uses `campaign-research-bank.md` or clearly states when a brand is only archetype-backed.
- Visual specificity: has location, light, lens, material, and composition.
- Automotive realism: protects wheels, proportions, reflections, logo/text areas.
- Brand maturity: tone fits the brand/segment, not generic luxury.
- Platform execution: syntax and language match target platforms.
- Iteration usefulness: includes risks, repair path, or test variants when appropriate.

Professional threshold: average 4.2+, with Automotive realism and Brand maturity both at least 4.

## Benchmark Tasks

### 1. Xiaomi SU7 Shanghai Rain Night

Task: Create a 6-shot campaign prompt bible for Xiaomi SU7 in Shanghai rainy blue-hour streets, output Midjourney and Nano Banana.

Expected qualities:

- Tech-lifestyle performance, not old luxury.
- Wet asphalt, glass reflections, clean speed, phone-like polish.
- No random Chinese text or warped wheels.

### 2. Xiaomi YU7 Bright Tech Launch

Task: Create a social-first launch contact sheet for a Xiaomi YU7-style SUV using bright product colors and clean modern roads.

Expected qualities:

- Consumer-electronics polish, precise geometry, fresh color accents.
- SUV confidence without family-MPV softness.
- Clean typography areas only, no generated slogans.

### 3. NIO ET9 Executive Smart Luxury

Task: Produce a client-ready prompt bible for a NIO ET9-style executive EV.

Expected qualities:

- Executive smart luxury, quiet CBD arrival, refined cabin comfort.
- Warm premium technology rather than cold sci-fi.
- Clear shot system: hero, interior, detail, human, social crop.

### 4. NIO Interior Comfort Support Shot

Task: Write one generic Chinese prompt for a NIO-style rear-cabin executive comfort image.

Expected qualities:

- Spacious cabin, soft ambient light, composed professional user.
- No random UI text; readable luxury materials.
- Protect hands, reflections, seat geometry.

### 5. Li Auto L9 Family Flagship

Task: Create a hero and interior support shot for Li Auto L9-style family flagship comfort.

Expected qualities:

- Family premium, safe weekend context, warm light.
- Cabin readability and six-seat spaciousness.
- No racing cues or lonely fashion editorial mood.

### 6. Audi A6 e-tron Light Design

Task: Create 4 prompts around Audi-like premium lighting: hero exterior, light-bar macro, urban reflection, social crop.

Expected qualities:

- Progressive precision, illuminated rings/light-bar logic, cool architecture.
- Macro detail treats lighting as technology jewelry.
- Avoid fake logo generation and overdone neon.

### 7. Audi Architecture Contact Sheet

Task: Build a 12-frame contact sheet for a cold-tech Audi-like EV campaign.

Expected qualities:

- Glass, black/silver paint, crisp hard shadows, disciplined composition.
- Mix hero, macro, talent, reflection, interior, and environment.
- Clean borders, no captions.

### 8. Porsche 911 Mountain Performance

Task: Convert a generic "red sports car cinematic" prompt into a Porsche-like mountain performance campaign without exact badges.

Expected qualities:

- Sculpted motion, road grip, low raking light, asphalt texture.
- Clean emblem area rather than fake badge.
- Performance desire without hiding body geometry.

### 9. Porsche Platform Adaptation

Task: Convert a Porsche-like performance prompt into Midjourney and Jimeng/即梦.

Expected qualities:

- MJ uses compact English and valid parameters.
- Jimeng uses fluent Chinese visual direction.
- Both include no-fake-logo and grounded-wheel constraints.

### 10. Mercedes-Benz S-Class Executive Proposal

Task: Create a client proposal summary plus shot list for a Mercedes-Benz S-Class-style executive luxury campaign.

Expected qualities:

- Refined detail, comfort, status, silence.
- Hotel/museum/polished-stone settings, soft highlights, warm cabin.
- Mature human tone, no noisy youth styling.

### 11. Mercedes-Maybach Comfort Detail

Task: Write a premium interior detail prompt for a Maybach-like rear cabin.

Expected qualities:

- Crafted comfort, quiet luxury, soft material tactility.
- No cramped cabin or random UI text.
- Warm interior spill, chrome/wood/leather restraint.

### 12. Failed Generation Repair: Wheels and Floating Car

Task: The generated image has a beautiful rainy street, but the car floats and the wheels are broken. Repair the prompt and provide A/B variants.

Expected qualities:

- Diagnosis identifies ground contact and wheel geometry.
- A keeps concept; B strengthens staging.
- Minimal rewrite, targeted constraints.

### 13. Failed Generation Repair: Logo/Text and Reflection

Task: The car looks good, but the grille text is gibberish and wet-ground reflections create a duplicate vehicle. Repair the prompt.

Expected qualities:

- Replaces exact text request with clean logo/text area.
- Clarifies real car versus reflection.
- Adds "no duplicate real vehicle" and reflection logic.

### 14. Reference Image Breakdown

Task: Given a described reference shot with a low-angle EV beside glass architecture and a model at the door, extract reusable visual DNA and produce MJ + Chinese model prompts.

Expected qualities:

- Separates subject hierarchy, composition, light, lens, material, risks.
- Does not invent exact camera metadata.
- Converts reference into reusable prompt rules.

### 15. Commercial Handoff Package

Task: Produce a handoff package for another designer to continue a premium Chinese EV campaign.

Expected qualities:

- Locked decisions, final prompts, do-not-change list, open tests.
- Clear brand territory and negative risks.
- Useful enough for another agent/designer without extra context.

## Self-Test Procedure

1. Pick one benchmark task.
2. Load only the references needed for that task.
3. Draft the response.
4. Score with the rubric.
5. Revise once if any category is below 4 or if average is below 4.2.
6. Record what the skill failed to make easy, then update the relevant reference if needed.

## Common Maturity Failures

- The answer is only a prompt, with no style anchor or shot logic.
- Brand tone is generic and could fit any car.
- Research-backed brands are treated the same as archetype-only brands.
- Negative prompt is pasted without scene-specific risks.
- Platform syntax is mixed up.
- The response ignores output role: hero, support, detail, contact sheet, prompt bible, or handoff.
- It overuses "cinematic" but under-specifies light, lens, material, and location.
