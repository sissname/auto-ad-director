# Examples

Use these as output patterns, not fixed templates.

## Example 1: Fashion Editorial Reference to New Subject

Request: "Analyze this moody fashion photo, but make it for a perfume bottle."

Output pattern:

```text
Reference read:
- Visual story: A solitary premium object/person emerging from shadow.
- Subject hierarchy: Original person is primary; transferable hierarchy is one sculptural subject against a dark soft background.
- Composition: Center-weighted vertical frame, large shadow field, narrow highlight on face/product side.
- Lighting and ratio: Low-key side light, estimated 4:1 or stronger contrast, soft falloff.
- Camera/lens estimate: Portrait-length compression, shallow focus.
- Material/color: Black, charcoal, pale skin/highlight accent; satin shadows.
- Post-processing: Soft filmic contrast, restrained grain.
- Transferable visual DNA: single subject, shadow-dominant frame, one controlled highlight, minimal props.
- Do-not-copy / risk notes: Do not copy model likeness, clothing, exact pose, or editorial layout.

Style anchor:
A low-key editorial still life with one sculptural subject isolated in a shadow-heavy vertical frame, a single soft side highlight defining form, restrained charcoal palette, shallow depth, and polished filmic contrast.
```

## Example 2: Interior Reference, Analysis Only

Request: "Only analyze this hotel lobby reference."

Output pattern:

```text
Reference analysis only:
- Visual story: Calm arrival space, premium but not flashy.
- Composition: Wide symmetrical frame, low seating forms create horizontal stability, ceiling lights lead eye inward.
- Lighting: Warm practical pools balanced with soft ambient fill; low contrast, hospitality mood.
- Camera/lens: Wide but not distorted, eye-level, deep focus.
- Color/material/post: Stone, warm wood, brushed metal, muted beige/green accents, clean architectural retouching.
- Transferable rules: Use symmetry, warm pools of practical light, layered depth, tactile natural materials.
- Non-transferable details: Do not copy furniture designs, artwork, hotel branding, or exact floor pattern.
- Failure risks: Generic beige lobby, overexposed ceiling, distorted wide-angle columns, cluttered decor.
```

## Example 3: Product Reference to Social Poster

Request: "Keep the wet reflection mood, change subject to running shoes."

Output pattern:

```text
Kept from reference:
- Light: hard rim light reflected on wet ground.
- Composition: low angle, subject occupying lower center, long reflection leading toward viewer.
- Camera: ground-level wide feel.
- Color/material: black surface with electric blue highlight.
- Mood: night launch energy, premium performance.

Changed for new subject:
- Subject logic: shoe pair grounded on wet track/asphalt, not floating.
- Setting logic: minimal night sports surface, no car/product from reference.
- Material interaction: outsole and mesh catch rim light; reflection below shoes stays physically aligned.
- Risk controls: avoid fake logos, warped soles, random text, excessive neon smoke.
```

## Example 4: Three Platform Prompt Block

```text
Prompt - Midjourney:
premium running shoes on rain-wet black asphalt, low-angle hero composition, long reflection leading toward camera, hard blue rim light from rear left, soft black negative space above, textured mesh and rubber catching precise highlights, cinematic product launch still, clean commercial retouching --ar 4:5 --style raw --v 6 --no text, logo, watermark, warped sole, extra shoe

Prompt - Jimeng:
画面主体是一双高端跑鞋，放置在雨后黑色沥青地面上。低机位英雄构图，鞋子位于画面下方中心，地面的长反射把视线引向主体，上方保留干净的暗色留白。光线来自后左侧的冷蓝色硬边缘光，鞋面织物和橡胶外底出现清晰但克制的高光。整体是夜间产品发布大片质感，商业修图干净。避免可读文字、乱码 logo、水印、鞋底变形、重复鞋子和过度霓虹烟雾。

Prompt - Generic Chinese model:
生成一张 4:5 产品广告图：一双高端跑鞋放在雨后的黑色沥青地面上，低机位构图，主体位于画面下方中心，湿地反射形成通向镜头的视觉引导。后左侧有冷蓝色硬边缘光，鞋面织物和橡胶材质被高光勾勒，上方保留干净暗色留白用于后期排版。画面应有克制的夜间发布大片质感，避免可读文字、乱码 logo、水印、鞋底畸变、重复主体、廉价 HDR 和过度霓虹效果。
```

## Example 5: V1 Quality Score Block

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
The strongest risk is reflection realism, so the next generation should keep the wet-ground setup simple and avoid adding extra props near the shoes.
```
