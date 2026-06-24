# Risk Controls

Use this file when prompts include text, logos, brands, people, realism, negative prompts, or reference images.

## Text and Logo

Do:

- Ask for clean negative space, blank label area, or post-production typography area.
- Use "no readable text, no fake logo, no watermark" for image models.
- Recommend adding final typography in design software.

Avoid:

- Asking models to render exact slogans, legal copy, package microtext, license plates, UI labels, or brand marks.
- Treating brand names as a guarantee of accurate logos.

## Realism

Do:

- Specify physical contact, scale, material response, shadows, and reflections.
- Use realistic geometry constraints for products, vehicles, architecture, hands, faces, and packaging.
- Reduce style intensity when product accuracy matters.

Avoid:

- Overloading prompts with surreal style when commercial realism is required.
- Mixing incompatible lens, scale, and material instructions.

## Negative Prompts

Good negatives are scene-specific:

- Product: warped geometry, fake label text, plastic surface, duplicated product, broken reflections.
- Fashion/person: extra fingers, distorted hands, melted facial features, merged limbs, fake text.
- Spatial: impossible structure, overexposed light strips, unsafe crowd clutter, distorted columns.
- Automotive: warped vehicle body, floating wheels, wrong reflections, random plate text.

Avoid generic negative piles that do not relate to the scene.

## Reference Image Weight

Do:

- Say what the reference controls: mood, lighting, composition, color palette, material response.
- Say what must change: subject, logos, text, exact artwork, faces, proprietary layout.
- Use "reference for visual DNA only" when copying risk exists.

Avoid:

- High reference dependence when the user wants a new subject.
- Exact style imitation of living artists, identifiable campaigns, or protected artwork.

## Conversion Note Checklist

Each cross-platform answer should explain:

- Why MJ uses or avoids parameters.
- Why Chinese prompts are written as natural directions.
- How text/logo risks are handled.
- How realism constraints are preserved.
- How negative prompts differ by platform.
