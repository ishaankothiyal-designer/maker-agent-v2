# Theme 07 — Digital Composition & Templates
> Vision-verified 2026-05-31 — entries below reflect the actual section images.

Typography note for this section: **Care Sans is logo-only** (the "Cars24" wordmark). Headlines and campaign titles use **Arapey serif** (the "Luxe Cars, Real Prices." title is an italic serif, not Care Sans). CTA button labels use a sans-serif. Composite/template backgrounds use a single brand-blue/purple hue with a subtle gradient/glow (not flat fill).

---

## 01 — Logo Placement (Social Media | Posts)

Left rail title: "Logo Placement / Social media | posts". Two artboards on a light lavender card: a square post and a vertical story/reel, each with a translucent blue "SAFE AREA" region and the Cars24 wordmark placed top-left and top-right.

### Purpose (as written on slide)
The logo should always be placed in a way that: maintains visibility and clarity; supports the content, not compete with it; ensures consistency across all touchpoints.

### Standard Placement Rules
- **Top Left** — Preferred for most creatives.
- **Center** — Only for logo-focused / Story / announcement creatives.
- **Avoid:** random placement; center-bottom (unless intentional campaign style); placing over busy areas.

### Square Post — 1080 × 1080 (label: "Post safe area - 1080 x 1080")
Logo shown top-left and top-right of the artboard.

| Element | Rule |
|---|---|
| Placement | Top left / Top right |
| Padding | Padding |
| Logo size | 260 px width |
| Clear space | Height of our logo mark |
| Safe area | Center + Inner frame |

### Story / Reel — 1080 × 1920 (label: "Post safe area - 1080 x 1920")
Annotated dimension callouts on the artboard: **TOP UI UNSAFE ZONE 220 PX** (red tag "220"), an inner "1080" width marker, a "300" tag near the logo, a left "1280" marker, and **BOTTOM UI UNSAFE ZONE 420 PX** (red tag "420"). Safe area is the central inset block (note the bottom-right notch where the unsafe UI sits).

| Element | Rule |
|---|---|
| Top Unsafe | 225 px - height |
| Placement | Top left, Center, Top Right |
| Logo Size | 300 px width |
| Bottom Unsafe | 420 px - height |
| Safe Area | Center + Inner frame |

> Note: the on-canvas annotation reads "220 PX" for the top unsafe zone while the spec table reads "225 px"; treat ~220–225 px as the top reserved band and 420 px as the bottom reserved band.

---

## 02 — Video / Reels Guidelines (Safe Zones)

Left rail title: "Video/Reels Guidelines". Three vertical panels: Instagram Reel Safe Area, Text placement, Reference (a real Reels screenshot with orange annotation tags).

### Safe Area Definition (as written)
- A central safe area is defined within the vertical canvas (1080 × 1920).
- All key elements must be placed inside this safe area.
- The top and bottom sections are restricted zones due to UI overlap.

### UI Restricted Zones

| Zone | Approx. size | Contains (platform UI) | Do NOT place |
|---|---|---|---|
| Top UI Zone | ~200 px | Back button, "Reels" label, Camera icon | Logo, Headlines, Important visuals |
| Bottom UI Zone | ~200–250 px | Caption, Likes / comments / share icons | Text, CTA, Branding elements |

### Safe Area Usage
- The middle section is the only reliable content zone.
- All critical elements must stay within this area.

### Text placement panel — 3-zone grid (labels visible on panel)
- **1/3** (upper third)
- **2/3** (middle)
- **3/3 - Lower Third** (bottom)

### Reference screenshot annotations (orange tags)
- "All major elements to lie in the safe area."
- "Any text to be bottom aligned with the lower third or top aligned with the upper third of the safe area."

---

## 03 — Video Introductory Frames

Left rail title: "Video Guidelines". Header: "Video Introductory Frames". Three vertical blue artboards: Intro frame template, Intro frame reference, Reference with guides. All show: "Cars24" wordmark top, italic-serif title "Luxe Cars, / Real Prices.", an "Under 100K AED" offer lockup on a tilted card, and a row of cars rising from the bottom. Background is a single blue/purple hue with a subtle glow (not flat), with small accent stars.

### Annotated rules (from "Intro frame reference")
| Layer | Rule (verbatim) |
|---|---|
| Brand logo always on top | Top aligned with the upper third of safe area |
| Title text | Preferably in the upper third of safe area (for intros with more content) or within first 2/3rds of the safe area |
| All major content | Within lower 2/3rds of the safe area |
| Centrally Aligned | All text and elements to be centrally aligned to the entire frame (not safe area) |

### "Reference with guides" panel
Same composition overlaid with the 3-zone grid: **1/3**, **2/3**, **3/3 - Lower Third**.

Composition order top→bottom: Cars24 wordmark → "Luxe Cars, Real Prices." (italic serif) → "Under 100K AED" tilted offer card → car lineup.

---

## 04 — Digital Assets / Templates

Left rail title: "Digital Assets". Body copy (verbatim): "Our digital assets are designed to maintain a consistent and engaging brand experience across all digital platforms. The use of brand colors, shapes, and visual elements should be clear, vibrant, and adaptable to different screen sizes and formats. Primary colors should be used to drive recognition, while supporting tones help create hierarchy and balance. Brand shapes and graphic elements should be used thoughtfully to enhance layouts, guide user attention, and create a cohesive visual identity across websites, apps, and digital campaigns." A blue "Templates" button/link sits below.

### "Templates" row (two landscape examples)
- Both are landscape banners with the Cars24 wordmark top-left, a green **"30 DAY RETURN GUARANTEE"** badge/stamp, and the line "Now buy pre-owned cars, worry-free."
- Left: lifestyle photo (people seated outdoors on/near a car) under a light sky.
- Right: lifestyle photo (people in the open boot/hatch of a red car).

### "Social Media Templates" row (two square examples)
- Left: brand-blue square, white headline "Take your time. / Make it yours.", the green "30 DAY RETURN GUARANTEE" stamp lower-center, Cars24 wordmark top-left, small accent stars.
- Right: brand-blue→purple gradient square (single hue, subtle glow), centered text "Australia's First / 30-Day Return / Guarantee", small supporting line above, Cars24 wordmark top-left.

Observed template language: full-bleed brand blue (single hue with subtle gradient/glow), bold white headline, green "30 Day Return" badge as the offer callout, accent stars, logo top-left, photography bleeding for lifestyle banners.

---

## 05 — CTA Button Guidelines

Left rail title: "CTA Button Guidelines". Intro (verbatim): "To maintain visual consistency and balance across all CTA buttons, Cars24 follows a proportional scaling system based on a single unit value." Two grey mock artboards (1080×1080 and 1080×1920) each show the headline "Sell your car with ease" with a small purple/blue "Primary Button" pill beneath it.

### Formula (verbatim)
Let X = Base padding unit (vertical padding):
| Property | Value |
|---|---|
| Top / Bottom Padding | X |
| Left / Right Padding | 2X |
| Corner radius | X |
| Font Size | 3X |

### Worked Example (verbatim, "If X = 10 px")
| Property | Value |
|---|---|
| Corner Radius | 10 px |
| Top / Bottom Padding | 20 px |
| Left / Right Padding | 20 px |
| Font Size | 30 px |

> Note: the slide's worked example lists Left/Right Padding as **20 px** at X=10 (whereas the formula states 2X = 20 px — consistent here; if X changes, Left/Right = 2X). Both top/bottom and left/right resolve to 20 px in this specific example.

Caption: "This creates a CTA that feels visually stable and well-spaced."

### Button states / variants shown
- **Filled (primary):** solid purple/blue pill, white label "Primary Button".
- **Outline:** white/transparent fill, purple/blue 1px border, purple/blue label "Primary Button".
- (Used for contrast: filled pill on light backgrounds; outline used as the secondary treatment.)

### How It Works (verbatim)
Ensures: text remains legible and prominent; buttons maintain balanced proportions; CTA scales consistently across formats and sizes.

### Do / Don't (verbatim)
- **Do:** Keep it short and clear; Maintain spacing and alignment; Use high contrast.
- **Don't:** Avoid multiple CTAs; Avoid long sentences; Avoid visual effects communications.

---

## Creative Direction Insight
Cars24's digital compositions are architecturally driven — everything is placed with mathematical intention (safe zones, the X-based CTA formula, the 1/3 grid for video). Build to the safe area first, then layer the brand. Eye order should land on the car or the offer first, then the brand. Keep backgrounds a single brand-blue/purple hue with a subtle gradient/glow (never flat), reserve Care Sans for the logo only, and set headlines/campaign titles in Arapey serif.
