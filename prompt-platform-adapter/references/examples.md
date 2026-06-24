# Examples

## Example 1: Product Hero Brief

Input:

```text
A frosted glass perfume bottle on wet black stone, low-key side light, silver-blue reflection, clean luxury poster, vertical 4:5.
```

Conversion note:

- Keep the bottle, wet stone, side light, blue-silver reflection, and vertical luxury poster intent.
- Midjourney uses compact keywords and parameters.
- Chinese platforms use full visual direction and text/logo safety.
- Risk policy: leave clean label/logo area for post-production, do not ask the model to render exact typography.

Midjourney:

```text
frosted glass perfume bottle on wet black stone, vertical luxury product poster, low-key side light from camera left, silver-blue reflection across stone surface, clean negative space above, shallow depth of field, restrained commercial retouching, accurate bottle geometry, premium material detail --ar 4:5 --style raw --stylize 90 --chaos 4 --v 6 --no text, logo, watermark, warped bottle, fake label
```

Jimeng:

```text
画面主体是一只磨砂玻璃香水瓶，放在雨后质感的黑色石材表面上，竖版 4:5 产品海报构图。瓶身位于画面下方中心，上方保留干净留白。光线从画面左侧进入，形成低调侧光和银蓝色反射，玻璃边缘清晰但不过曝。整体是克制的高端商业修图质感。避免可读文字、乱码 logo、水印、瓶身变形、假标签和过度黑金奢华感。
```

Generic Chinese model:

```text
生成一张竖版 4:5 产品广告图：一只磨砂玻璃香水瓶放在湿润的黑色石材表面上，主体位于画面下方中心，上方有干净留白。左侧低调侧光勾勒瓶身边缘，石材表面出现银蓝色反射，整体为克制的高端商业修图效果。请保持瓶身结构真实、玻璃质感清晰，避免可读文字、乱码 logo、水印、瓶身畸变、假标签和廉价黑金风格。
```

## Example 2: Spatial Installation Brief

Input:

```text
Skincare pop-up tunnel, translucent ribs, soft aqua light, reflective floor, visitor path to photo point, horizontal 16:9.
```

Conversion note:

- Kling receives motion-ready visitor-path language.
- MJ keeps visual density compact.
- Chinese generic prompt makes structure and safety constraints explicit.
- Reference policy: borrow tunnel rhythm, aqua light, reflective floor, and visitor path only; do not copy signage, graphics, or floor plan.

Midjourney:

```text
skincare pop-up tunnel installation, translucent ribbed light structure, soft aqua glow, reflective floor, clear visitor path leading to product plinth photo point, horizontal architectural effect image, clean commercial spatial rendering, realistic scale and safe structure --ar 16:9 --style raw --stylize 80 --chaos 4 --v 6 --no readable signage, logo, watermark, impossible structure, overcrowded people, blown-out lights
```

Generic Chinese model:

```text
生成一张横向 16:9 商业空间效果图：护肤品牌快闪通道由半透明肋骨状灯光结构组成，柔和水蓝色光线沿动线延伸，地面有干净反射，访客路径通向末端产品展台和拍照点。参考图只借鉴灯光节奏、通道构图和反射氛围，不复制原有品牌标识、图案、导视或平面结构。避免可读招牌、乱码 logo、结构不可能、灯带过曝、人群拥挤和泛科幻通道感。
```

## Example 3: Fashion Editorial Prompt

Input:

```text
Model in matte red coat under hard winter sunlight, urban concrete wall, editorial crop, strong shadow, no readable text.
```

Conversion note:

- Keep color blocking, hard sunlight, editorial crop, and concrete texture.
- Avoid exact magazine masthead or brand typography.
- Chinese platforms should specify hands/face realism and no random text.

Midjourney:

```text
fashion editorial portrait, model in matte red coat against urban concrete wall, hard winter sunlight casting strong graphic shadow, cropped magazine-style composition without text, realistic face and hands, muted concrete texture, crisp commercial editorial color --ar 4:5 --style raw --stylize 100 --chaos 5 --v 6 --no text, logo, watermark, distorted hands, melted face
```

Jimeng:

```text
画面主体是一位穿哑光红色大衣的模特，站在城市混凝土墙前，竖版 4:5 时尚编辑片构图。冬季硬阳光从侧上方照射，在墙面和服装上形成强烈几何阴影，红色大衣与灰色混凝土形成明确色块对比。镜头为中近景裁切，保留杂志感但不要生成任何可读文字或刊头。保持面部、手部和服装结构真实，避免乱码文字、品牌 logo、水印、手指畸变和面部融化。
```
