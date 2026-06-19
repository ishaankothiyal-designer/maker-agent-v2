# Cars24 Maker Agent Exports

This file is the source of truth for export structure, serial handling, and export provenance notes. Do not create per-run generation manifests unless the user explicitly asks for them; add durable run notes here instead.

## Canonical Structure

Every new exported creative must use three levels:

```text
4_exports/{serial}_{brief}_{DD-Mon}/
  v1/
    {brief}-image1.[ext]
    {brief}-image2.[ext]
  v2/
    {brief}-image1.[ext]
```

- `{serial}` is a zero-padded counter. Before creating a new project folder, scan existing numbered folders and choose the next unused serial after the highest existing serial.
- `{brief}` is a kebab-case short slug of the brief, max 30 characters.
- `{DD-Mon}` is the run date, for example `18-Jun`.
- `vN/` is one version folder per generation run.
- Image filenames include the same short brief slug: `{brief}-imageN.[ext]`.

## Export Fidelity

The exported file is the source of truth for final Maker runs.

- Codex runs use Codex ImageGen / `image_gen`; Claude and non-Codex CLI runs use Higgsfield with GPT Image 2 (`gpt_image_2`) by default.
- Every final output must be saved under `4_exports/{serial}_{brief}_{DD-Mon}/vN/`.
- Chat previews should display those exact saved files with absolute Markdown image paths whenever the file exists. The preview and the export must be the same bitmap.
- Export means copy, rename, or explicitly requested resize of the same generated bitmap. Export must never mean "run the prompt again."
- Do not crop by default. Cropping is a separate post-production choice and requires an explicit user request.
- If a Codex `image_gen` result is visible but no exact local/exportable bitmap can be verified, stop and ask before any regeneration, provider switch, or fallback.

## Current Serial State

Historical exports contain duplicate and missing serials. Preserve them as history; do not renumber old folders.

- Existing highest serial observed after the v2.17 export-fidelity update: `025`.
- Next new brief should start at `026`, unless a later folder already exists.
- Known historical duplicates: `001`, `021`.
- Known historical gaps: `003`, `004`, `005`, `006`, `007`.

## Canonical Learning Rule

Do not use `4_exports/` as canonical reference-learning input. Exports are output history and audit evidence only. Brand/reference truth lives in:

- `3_Skills/Global Skills/master-rules.md`
- `1_References/CREATIVE-DIRECTION.md`
- `1_References/HIGGSFIELD-CONTEXT-PACKAGE.md`
- `1_References/reference-index.json`
- `1_References/reference-tags/`
- `1_References/REFERENCE-ATLAS.md`
- `1_References/REFERENCE-SKILL-MAP.md`

## Run Notes

### 021 Introducing Cars24 Labs Style-Purity Test

Former source: `4_exports/021_introducing-cars24-labs_18-Jun/v1/run-manifest.md`

- Source row: `5_BATCH_EXPORT/cars24-batch-processing-template.xlsx` -> `Example rows` -> item 1.
- Title: `Introducing Cars24 Labs: our $20 million bet on AI`
- Context: Cars24 announces Labs, a `$20M` AI bet to build, partner with, and invest in AI-native companies.
- Canvas: `1000 x 650 px`
- Theme: dark
- Logo: none
- Generated style explorations: photography, abstract pattern/form, infographic/icon, illustration.
- Style-purity audits were captured for each exploration:
  - Photography: focused Cars24 product team reviewing one prototype decision; rejected illustration overlays, icon clusters, infographic arrows, 3D platform blocks, network maps, dashboard clutter, and sci-fi robot cliches.
  - Abstract pattern/form: one central AI Labs signal attracting build, partner, and invest paths; rejected people, cars, UI cards, icons, labels, dashboards, 3D blocks, and sci-fi robot cliches.
  - Infographic/icon: build, partner, invest as three icon pillars with minimal connector path; rejected people, photo scenes, 3D platform blocks, network maps, UI clutter, and decorative illustration vignettes.
  - Illustration: Autonaut builders shaping one AI-native product idea; rejected infographic icon clusters, flowcharts, SaaS dashboards, 3D platform blocks, network maps, realistic photo treatment, and robot cliches.
- Export note from that run: four Codex ImageGen outputs were generated in-thread, but Codex ImageGen did not expose local filesystem image handles for saving into that folder during the run.

### 025 One Year AI Journey

- Source row: `5_BATCH_EXPORT/cars24-batch-processing-template.xlsx` -> `Example rows` -> item 15.
- Title: `One year into our AI journey`
- Requested matrix: illustration, photo, infographic, and abstract styles in both dark and light themes.
- Export note: the first built-in Codex ImageGen pass produced better chat-visible previews but did not expose local file handles in the current Codex tool surface. A second file-writing generation pass was used to populate `4_exports/025_one-year-ai-journey_18-Jun/v1/`, which caused visual drift. This run is the reason for the export fidelity rule. As of v2.24, Codex uses `image_gen`; if the exact generated bitmap cannot be verified/copied into `4_exports/`, stop and ask before any regeneration, provider switch, or fallback.

## Hygiene

`.DS_Store` files are macOS Finder metadata. They are not source or export truth. Ignore them in git; delete them only as workspace cleanup, not as part of brand/version history.
