# Reference Tags — v2.0

The reference-tagging layer turns the Cars24 reference library into a queryable system for selecting image-generation references.

## Source of truth

- Project version: `3_Skills/Global Skills/master-rules.md` → `sync-metadata.version`
- Machine-readable index: `1_References/reference-index.json`
- Human ontology: `1_References/reference-tags/ontology.md`
- Query recipes: `1_References/reference-tags/query-recipes.md`

## Included sources

Only canonical reference inputs are tagged:

- `1_References/1_Brand Guidelines/`
- `1_References/2_Image References/`
- `1_References/3_Illustrations References/`
- `1_References/4_Infographic Icon References/`
- `1_References/5_Photography References/`

## Excluded sources

Do not tag or learn from:

- `4_exports/`
- temporary generations
- failed or exploratory variants
- output audits, unless explicitly promoted into `master-rules.md` by the user

Exports are output history. They are useful for audit, comparison, and feedback, but they are not brand truth.

## Core principle

References should not only say what an image contains. They must say what the agent is allowed to learn from the image.

Every attachable reference should answer:

- What role does this reference play?
- What should the model copy?
- What should the model ignore?
- Is it safe to attach, or should it only inform prompt text?

## Marble/statue guard

The dark and light theme cards may contain marble/statue subjects. These are historical layout placeholders only.

When using those cards:

- Copy layout structure.
- Copy subject scale and placement.
- Copy negative-space balance.
- Copy text hierarchy.
- Copy pattern placement.
- Ignore marble material.
- Ignore statue identity.
- Ignore classical sculpture texture.
- Do not generate marble/statue photo heroes.

For photo creatives, the hero must be a real human, real car, real hub, or real Cars24 service moment.

## Required reference map fields

When presenting the Stage 7 reference map, include:

| Field | Meaning |
|---|---|
| File | Exact path |
| Role | Layout, subject style, pattern texture, photo style, logo context, etc. |
| Attachability | Attachable, attach with caution, rules only, do not attach |
| Copy from reference | What the model should take |
| Ignore from reference | What the model must not take |
| Reason | Why this is the right reference for this slide |
