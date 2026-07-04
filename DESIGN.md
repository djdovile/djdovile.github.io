---
name: "dj_hugo"
description: "A credible, clear, expert public academic profile and archive for Dovilė Jakniūnaitė."
colors:
  seminar-red: "#B72818"
  seminar-red-deep: "#761A0F"
  seminar-red-soft: "#F7E9E7"
  wayfinding-accent: "#506A52"
  wayfinding-deep: "#334536"
  warm-paper: "#FFFAF5"
  study-ink: "#3B2313"
  soft-shelf: "#F5EFE9"
  quiet-border: "#E4E2E1"
  muted-voice: "#6C6561"
  dark-room: "#2B262B"
  dark-ink: "#E0CAB6"
  white: "#FFFFFF"
typography:
  display:
    fontFamily: "Source Serif 4, ui-serif, Georgia, serif"
    fontSize: "clamp(2.2rem, 1.45rem + 3vw, 4rem)"
    fontWeight: 650
    lineHeight: 1.04
    letterSpacing: "-0.018em"
  headline:
    fontFamily: "Source Serif 4, ui-serif, Georgia, serif"
    fontSize: "clamp(1.55rem, 1.28rem + 0.9vw, 2.15rem)"
    fontWeight: 600
    lineHeight: 1.14
    letterSpacing: "-0.012em"
  title:
    fontFamily: "Source Serif 4, ui-serif, Georgia, serif"
    fontSize: "1.18rem"
    fontWeight: 600
    lineHeight: 1.34
    letterSpacing: "-0.004em"
  body:
    fontFamily: "Source Serif 4, ui-serif, Georgia, serif"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.72
    letterSpacing: "0"
  label:
    fontFamily: "ui-sans-serif, system-ui, sans-serif"
    fontSize: "0.92rem"
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: "0"
rounded:
  sm: "4px"
  md: "8px"
  card: "16px"
  pill: "999px"
spacing:
  xs: "4px"
  sm: "8px"
  md: "16px"
  lg: "24px"
  xl: "32px"
  section: "64px"
components:
  button-primary:
    backgroundColor: "{colors.seminar-red}"
    textColor: "{colors.white}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
  chip-filter:
    backgroundColor: "transparent"
    textColor: "{colors.muted-voice}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
    padding: "4px 12px"
  chip-filter-active:
    backgroundColor: "{colors.seminar-red}"
    textColor: "{colors.white}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
    padding: "4px 12px"
  card:
    backgroundColor: "{colors.white}"
    textColor: "{colors.study-ink}"
    rounded: "{rounded.card}"
    padding: "32px"
  nav-link:
    backgroundColor: "transparent"
    textColor: "{colors.study-ink}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
    padding: "8px 10px"
---

# Design System: dj_hugo

## 1. Overview

**Creative North Star: "The Public Seminar Room"**

This site should feel like a public academic room where a visitor can quickly understand the scholar, the archive, and the next route forward. The tone is credible, clear, and expert: calm enough for long-form reading, structured enough for research discovery, and confident without becoming promotional.

The current Hugo Blox system is the baseline, not the destination. Its warm coffee palette, seminar typography, small-radius controls, and bilingual navigation already support a readable academic home base. Its heavier card grids and template-like surfaces should be simplified over time so the archive feels intentionally organized rather than packaged.

The system explicitly rejects startup/portfolio flashiness, generic Hugo Blox template feel, decorative academic cliches, overdesigned personal-brand aesthetics, gratuitous cards, loud hero theatrics, and visual treatments that make scholarship look like marketing copy.

**Key Characteristics:**
- Public, institutional, and navigable rather than performative.
- Warm reading surface with strong ink contrast.
- Restrained accent use, with red as emphasis and a quiet green as wayfinding.
- Lithuanian-first clarity, with English parity handled deliberately.
- Archive-first layouts that help visitors find publications, posts, courses, projects, and contact paths.

## 2. Colors

The palette is a warm civic reading palette: paper, ink, shelves, and restrained accent marks. It should support reading and orientation before identity display.

### Primary
- **Seminar Red**: The project-configured primary accent. Use it for selected filters, key calls to action, active states, and rare emphasis. It should feel like a marker in a seminar handout, not a decorative brand wash.
- **Deep Seminar Red**: The darker hover and emphasis companion for Seminar Red. Use it where primary red needs stronger contrast or a pressed state.
- **Soft Seminar Red**: A quiet tint for selected backgrounds, callouts, and subtle grouping when white is too bare.

### Secondary
- **Quiet Wayfinding Accent**: The secondary accent for functional links and navigation. It should read as institutional orientation, not as product-blue decoration.
- **Deep Wayfinding Accent**: The stronger companion for visited, hover, or high-contrast wayfinding states.

### Neutral
- **Warm Paper**: The main light background. It gives the site a reading-room temperature without becoming decorative parchment.
- **Study Ink**: The main foreground and heading color. This is the default text authority.
- **Soft Shelf**: Header, footer, and quiet section surface. It separates navigation and metadata from page content without creating another card.
- **Quiet Border**: Dividers, filter borders, and subtle containment. It should clarify structure, not decorate it.
- **Muted Voice**: Secondary text and metadata. Keep contrast high enough for publication records and older archive material.
- **Dark Room** and **Dark Ink**: The system-mode dark palette. Use it for OS dark mode only, keeping the same restrained hierarchy.

### Named Rules
**The Accent Rarity Rule.** Seminar Red should stay under roughly 10 percent of any screen. Its authority depends on scarcity.

**The Wayfinding Is Functional Rule.** The wayfinding accent is a working link color, not a brand personality. Do not expand it into hero backgrounds, gradients, or decorative panels.

## 3. Typography

**Display Font:** Source Serif 4, with system serif fallback.
**Body Font:** Source Serif 4, with system serif fallback.
**Interface Font:** System sans for navigation, metadata, chips, and compact controls.
**Label/Mono Font:** JetBrains Mono is available for code only, not as a general brand voice.

**Character:** The typography should feel like a precise public seminar handout: serious, readable, and quietly institutional. The serif is for scholarship, prose, and archive titles; the sans is for wayfinding and interface work. Avoid decorative academic costume.

### Hierarchy
- **Display** (650, fluid 2.2-4rem, 1.04 line-height): Page-level identity and major section openings. Use sparingly and keep line breaks calm.
- **Headline** (600, fluid 1.55-2.15rem, 1.14 line-height): Section titles such as publications, books, teaching, and writing.
- **Title** (600, 1.18rem, 1.34 line-height): Publication titles, card titles, and list group labels.
- **Body** (400, 1.0625rem, 1.72 line-height): Biography, summaries, article text, and explanatory copy. Keep prose measure near 65-75 characters when possible.
- **Label** (500, 0.92rem, 1.4 line-height): Navigation, filter chips, metadata, and compact controls. Do not use all-caps tracked labels as repeated section grammar.

### Named Rules
**The Reading First Rule.** Type exists to make expertise easy to scan and read. Increase clarity through hierarchy and measure before adding decorative type treatments.

**The No Academic Costume Rule.** Do not use serif flourishes, fake manuscript cues, decorative initials, or scholarly ornaments to signal seriousness.

**The Interface Sans Rule.** Use the system sans for wayfinding, metadata, and controls so the serif does not make every piece of UI feel like prose.

## 4. Elevation

The current site uses Hugo Blox cards with rounded corners and visible shadow on repeated item grids. Treat that as a transitional baseline. The desired direction is flatter and more archival: structure should come from spacing, type hierarchy, dividers, and tonal surfaces, with shadows reserved for true interactive lift or repeated item cards that need separation.

### Shadow Vocabulary
- **Card Baseline** (`box-shadow: framework default shadow-lg`): Existing Hugo Blox collection cards. Keep only where repeated items genuinely need individual affordance.
- **Card Hover** (`box-shadow: framework default shadow-xl`): Existing hover state for item cards. Use only when the item is clickable and the lift communicates interactivity.

### Named Rules
**The Archive Surface Rule.** A list of publications is not a gallery by default. Prefer citation lists, tables, dividers, and compact records before card grids.

**The No Ghost Card Rule.** Do not pair a light border with a broad decorative shadow on static surfaces. Choose structure or lift, not both.

## 5. Components

### Buttons
- **Shape:** Small, controlled corners (4px) for primary actions and filter controls.
- **Primary:** Seminar Red background with white text, used for selected states and rare calls to action.
- **Hover / Focus:** Darken toward Deep Seminar Red and show a visible focus outline. The control should feel precise, not glossy.
- **Secondary / Ghost:** Transparent background, Study Ink or Muted Voice text, and Quiet Border when containment is needed.

### Chips
- **Style:** Publication filters are compact chips with 4px corners, 1px borders, and label-size text.
- **State:** Selected chips use Seminar Red and white text. Unselected chips should remain quiet and readable, with hover moving toward Seminar Red border.

### Cards / Containers
- **Corner Style:** Existing cards may use 16px corners, but new archival surfaces should start at 4-8px unless the repeated item pattern requires stronger separation.
- **Background:** White cards on Warm Paper; Soft Shelf for navigation and footer surfaces.
- **Shadow Strategy:** Keep existing Hugo Blox card shadows only for repeated clickable items. Avoid shadows on page sections.
- **Border:** Use Quiet Border for subtle structure and dividers.
- **Internal Padding:** Existing cards can hold 32px padding; dense archive records should use tighter 12-16px spacing.

### Inputs / Fields
- **Style:** White or Warm Paper background, Quiet Border stroke, 4px corner radius, Study Ink text.
- **Focus:** Seminar Red or Deep Wayfinding Accent outline with sufficient contrast.
- **Error / Disabled:** Error states should be explicit in text and color; disabled states must remain readable.

### Navigation
- **Style:** Sticky centered navbar with Study Ink text, Soft Shelf or Warm Paper surface, search enabled, language switcher visible, and no theme toggle.
- **Hover / Active:** Use underline, weight, or restrained accent color. Do not turn the nav into a campaign header.
- **Mobile:** Prioritize language switching, search, and archive paths. Navigation should remain utilitarian and compact.

### Publication Type Filters
Publication type filters are the clearest current custom pattern. They should stay compact, bilingual, and archive-oriented: Visos/All, Straipsniai/Articles, Knygos/Books, Knygų skyriai/Book chapters. Their job is orientation, not decoration.

## 6. Do's and Don'ts

### Do:
- **Do** make authorship, institutional context, publications, and project evidence easy to trust.
- **Do** use Seminar Red for selected states, primary calls to action, and rare emphasis only.
- **Do** keep publication and blog archives navigable through citation lists, filters, dates, and clear metadata.
- **Do** prioritize Lithuanian-first clarity while keeping English structure ready for deliberate parity.
- **Do** use Warm Paper, Study Ink, Soft Shelf, and Quiet Border to create hierarchy without visual noise.
- **Do** preserve keyboard accessibility, visible focus states, readable contrast, and clear link affordances.

### Don't:
- **Don't** create startup/portfolio flashiness.
- **Don't** preserve a generic Hugo Blox template feel when custom archive structure would be clearer.
- **Don't** use decorative academic cliches, manuscript effects, fake scholarly ornaments, or ornamental serif flourishes.
- **Don't** build an overdesigned personal-brand aesthetic.
- **Don't** add gratuitous cards. Cards are for repeated clickable items, not default page structure.
- **Don't** use loud hero theatrics or make scholarship look like marketing copy.
- **Don't** bury useful archive navigation under decorative design.
- **Don't** expand the wayfinding accent into brand panels, gradients, or generic product-site links.
