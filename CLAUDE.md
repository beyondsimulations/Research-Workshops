# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A Quarto website for university seminar preparation materials (University of Hamburg). Authored by Dr. Tobias Vlcek. The site hosts four workshops and curated literature/resources for Bachelor and Master students in operations research.

## Build Commands

- **Preview site locally:** `quarto preview`
- **Render full site:** `quarto render`
- **Render single page:** `quarto render workshops/large-language-models.qmd`
- **Python venv:** `.venv/` exists with Python 3.12; activate with `source .venv/bin/activate`

## Architecture

Quarto website project (`project: type: website` in `_quarto.yml`).

- `_quarto.yml` — central config: site metadata, sidebar navigation, format options, freeze settings
- `_brand.yml` — brand color palette and typography (Gelasio headings, Reddit Sans body, Google Sans Code monospace)
- `styles.scss` — custom theme built on `_brand.yml` variables; defines CSS utility classes (`.highlight`, `.task`, `.question`, `.flow`, `.loud-slide`, `.invert-font`)
- `index.qmd` — landing page with workshop overview table
- `workshops/` — workshop slide decks (revealjs + html dual output):
  - `large-language-models.qmd` — AI programming, LLM fundamentals, models/apps/harnesses framework, coding tools
  - `prompting.qmd` — RBTF prompting framework for researchers
  - `quarto-academic-writing.qmd` — Quarto for academic papers, citations, cross-references
  - `literature-research.qmd` — structured literature research, databases, AI tools, Zotero
  - `*-exercises.md` — future interactive exercise concepts for 90-min session expansion
- `templates/` — paper templates for students:
  - `seminar-paper-en.qmd` — English Typst/PDF template
  - `seminar-paper-de.qmd` — German Typst/PDF template
  - `references.bib` — sample bibliography
- `general/` — shared resources: `literature.qmd` (curated reading list), `header.html` (analytics)
- `_site/` — rendered output (gitignored)

## Content Conventions

- Pages must be listed in both `_quarto.yml` `project.render` and `website.sidebar.contents`
- Workshop slides use revealjs format with dual output (`revealjs` + `html`)
- Slide styling follows `lec_02_copilot_intro.qmd` patterns:
  - Section titles: `# [Title]{.flow} {.title}`
  - Emphasis: `[text]{.highlight}`, `[Question]{.question}`, `[Task]{.task}`
  - Incremental reveals: `. . .` between content blocks
  - Callouts: `:::{.callout-tip}`, `:::{.callout-warning}`, `:::{.callout-note}`, `:::{.callout-important}`
  - Columns: `::::{.columns} :::{.column width="50%"}`
- Footer pattern: `{{< meta title >}} | {{< meta author >}} | [Home](../index.qmd)`
- Paper templates use `format: typst` for PDF output (no LaTeX distribution needed)
- `execute: freeze: auto` — computations cached; only re-run when source changes
