# AI Dynamic Web Lab Generation for Core CSS Concepts

## Overview
Two single-file interactive HTML/CSS/JS tools generated using Gemini
(Canvas feature) to visualize core CSS concepts: the box model with
display-type interaction, and Flexbox/Grid layout behavior.

## Tool Used
Gemini, Canvas feature (single-file HTML/CSS/JS generation)

## Files
- `box-model-initial.html` — Initial Box Model & Display Property
  visualizer. Two boxes, sliders for padding/margin/border-width/width,
  a display-type dropdown (block/inline-block/inline), and
  background-clip-based coloring to distinguish content/padding/margin
  regions.
- `box-model-refined.html` — Refined version adding independent
  top/right/bottom/left sliders for margin, padding, and border, plus
  a corner-radius (border-radius) slider.
- `flexbox-grid-playground.html` — Flexbox & Grid playground. A
  container with 5 items, dropdowns for display (block/flex/grid),
  flex-direction, justify-content, align-items, and
  grid-template-columns.

## Prompts Used
See the accompanying Google Doc submission for the full text of all
three prompts (Initial Box Model, Refinement, and Flexbox/Grid) and
the reflection on the sequential-prompting workflow.

## How to View
Open any of the HTML files directly in a browser — each is fully
self-contained (HTML, CSS, and JS in one file), no build step or
server required.
