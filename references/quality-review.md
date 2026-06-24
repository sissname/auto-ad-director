# Quality Review

Use this reference as the gate before returning high-stakes prompt packages or when diagnosing weak results.

## Prompt Scorecard

Score mentally from 1-5. Revise any category below 4 before final output.

```text
Vehicle realism: wheels grounded, proportions plausible, body not warped.
Brand tone: visual language matches segment, audience, and price tier.
Composition: subject hierarchy is clear; eye path leads to car or campaign moment.
Lighting: source direction, contrast, and shadow detail are explicit.
Material fidelity: paint, glass, wet ground, fabric, and architecture are named.
Platform fit: syntax matches target platform; unsupported flags removed.
Text/logo risk: no demand for exact generated typography; clean placement areas specified.
Negative constraints: targeted to likely failures, not a generic word pile.
```

## Failure Pattern to Repair Map

### Warped Car Body

Likely cause: too many scene elements, extreme lens, vague vehicle description.

Repair:

- Add "realistic vehicle proportions, production-car geometry, grounded wheels."
- Reduce surreal style words and remove conflicting body descriptors.
- Use 35-50mm instead of ultra-wide unless architecture is the subject.

### Broken Wheels or Floating Tires

Likely cause: weak ground relationship or overemphasis on reflections.

Repair:

- Add "tires firmly touching [ground material], correct wheel alignment."
- Specify visible ground plane and shadow contact.
- Avoid "floating", "dreamlike", "zero gravity", or abstract floor language.

### Bad Logos or Random Text

Likely cause: asking the image model to render exact brand typography.

Repair:

- Replace exact text requests with "clean logo area" or "blank typography space."
- Add "no random text, no gibberish logo, no license plate text."
- Plan to add final copy in design software after generation.

### Cheap Studio Look

Likely cause: generic "luxury product photography" without location, light, or material.

Repair:

- Anchor in a specific location, weather, ground, and architecture.
- Add real light direction and contrast ratio.
- Use restrained color grading and fewer props.

### Person and Car Merge

Likely cause: unclear foreground/background relationship.

Repair:

- State exact body position: "standing beside the front fender", "leaning on the open door edge."
- Add "do not merge body with car, visible separation between subject and vehicle."
- Reduce complex reflections around limbs.

### Reflection Logic Fails

Likely cause: mirror/wet/glass scene does not distinguish real subject from reflection.

Repair:

- State which subject is real and which is reflected.
- Add "accurate reflection logic, no duplicate real person."
- Simplify to one reflective surface.

### Image Feels Generic

Likely cause: no style anchor or brand archetype.

Repair:

- Add archetype, location specificity, light signature, material signature, and emotional distance.
- Replace "beautiful car ad" with a campaign world: city, architecture, weather, wardrobe, lens.

## Final Gate

Before finalizing, check:

- Does the prompt say what the car is doing in the frame?
- Is the camera position clear enough to stage the shot?
- Is the light physically plausible?
- Is there a named material contrast, such as silver paint against wet black asphalt?
- Are typography and logo requests safe?
- Is the negative prompt specific to this scene?

If not, revise once before answering.
