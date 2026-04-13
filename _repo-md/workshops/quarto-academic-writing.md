---
title: Quarto for Academic Writing
subtitle: Write in Markdown, render to PDF with citations and cross-references
author: Dr. Tobias Vlćek
---


# <span class="flow">Quarto for Academic Writing</span>

## What is Quarto and why use it?

Quarto is an <span class="highlight">open-source scientific publishing system</span> developed by Posit (formerly RStudio). Write in **Markdown**, render to multiple formats:

- PDF (via Typst or LaTeX)
- HTML pages and websites
- Presentation slides
- Word documents

> **Tip**
>
> Think of Quarto as a **modern replacement for LaTeX** that is simpler to learn and just as capable for academic writing.

**LaTeX**

- Steep learning curve
- Complex syntax for simple tasks
- Difficult to debug errors
- Large installation (several GB)
- Output mainly PDF

**Quarto**

- <span class="highlight">Simple Markdown syntax</span>
- Easy to read and write
- Clear error messages
- Lightweight installation
- PDF, HTML, Word, slides, websites

> **Note**
>
> Quarto produces **publication-quality** PDFs via Typst with no need to install a full TeX distribution!

**LaTeX**

``` latex
\textbf{bold} and \textit{italic}

\begin{itemize}
  \item First item
  \item Second item
\end{itemize}

\section{Introduction}

\parencite{smith2023}
```

**Quarto**

``` markdown
**bold** and *italic*

- First item
- Second item

## Introduction

[@smith2023]
```

Same output quality, <span class="highlight">much less typing</span>!

# <span class="flow">Getting Started</span>

## Installation by platform

**macOS**

``` bash
brew install quarto
```

Or download the installer from [quarto.org](https://quarto.org/docs/get-started/)

**Windows**

``` bash
winget install Posit.Quarto
```

Or download the installer from [quarto.org](https://quarto.org/docs/get-started/)

**Linux**

Download the `.deb` or `.rpm` package from [quarto.org](https://quarto.org/docs/get-started/)

``` bash
# Debian/Ubuntu
sudo dpkg -i quarto-*.deb
```

## PDF output with Typst

Quarto uses <span class="highlight">Typst</span> for PDF rendering. It is **built in**, so there is no need to install a full TeX distribution (saves several GB). Simply set `format: typst` in your YAML frontmatter.

``` yaml
---
title: "My Paper"
format:
  typst:
    toc: true
    number-sections: true
---
```

> **Tip**
>
> Typst is fast and produces clean PDFs. It compiles in milliseconds rather than seconds.

## Recommended editors

- **Zed:** A fast, modern editor with Quarto support available through a [community extension](https://zed.dev/extensions?query=quarto). Install it from the extensions panel and you are ready to write `.qmd` files.
- **VS Code:** With the [Quarto extension](https://marketplace.visualstudio.com/items?itemName=quarto.quarto) installed, you get syntax highlighting, an integrated live preview, and autocompletion for YAML options and cross-references.
- **RStudio:** Has native Quarto support built in, making it a natural choice if you already use R for data analysis or are familiar with the RStudio interface.

> **Note**
>
> Any text editor works with Quarto files since they are just plain text (`.qmd` files). The editors above simply provide extra convenience features like live preview and autocompletion.

# <span class="flow">Quarto Basics</span>

## YAML frontmatter

Every Quarto document starts with a <span class="highlight">YAML header</span> between `---` markers. This header controls the title, author, format, and options.

``` yaml
---
title: "My Seminar Paper"
author: "Jane Doe"
date: today
bibliography: references.bib
format:
  typst:
    toc: true
    number-sections: true
---
```

> **Tip**
>
> YAML uses indentation (spaces, not tabs!) to define structure. Be careful with alignment.

## Markdown syntax essentials

**Syntax**

``` markdown
# Heading 1
## Heading 2
### Heading 3

**bold text**
*italic text*

- Bullet list
- Another item
  - Nested item

1. Numbered list
2. Second item

[Link text](https://example.com)
```

**Result**

### Heading 3

**bold text** and *italic text*

- Bullet list
- Another item
  - Nested item

1.  Numbered list
2.  Second item

[Link text](https://example.com)

## Figures, tables, and equations

Include images with captions and <span class="highlight">cross-reference labels</span>:

``` markdown
![Caption text](images/figure.png){#fig-example width="80%"}
```

Reference in text: `@fig-example` renders as "Figure 1".

> **Warning**
>
> The label **must** start with `#fig-` for Quarto to recognize it as a figure cross-reference.

Use pipe tables for simple data presentation:

``` markdown
| Method | Objective | Time (s) |
|--------|----------:|:--------:|
| Exact  |   142.5   |   3.21   |
| Greedy |   138.7   |   0.05   |

: Comparison of solution methods {#tbl-results}
```

Reference in text: `@tbl-results` renders as "Table 1". The label must start with `#tbl-` for table cross-references.

- Inline math: `$x^2 + y^2 = z^2$` renders as $x^2 + y^2 = z^2$
- Display math with cross-reference:

``` markdown
$$
\min \sum_{i \in \mathcal{I}} \sum_{j \in \mathcal{J}} c_{ij} \cdot x_{ij}
$$ {#eq-objective}
```

<span id="eq-objective">
$$\min \sum_{i \in \mathcal{I}} \sum_{j \in \mathcal{J}} c_{ij} \cdot x_{ij}
 \qquad(1)$$</span>

- Reference in text: `@eq-objective` renders as "Equation 1"

# <span class="flow">Academic Features</span>

## Citations with BibTeX

Store references in a `.bib` file and set `bibliography: references.bib` in YAML. Then use the `[@key]` syntax to cite:

| Syntax                     | Output                     |
|----------------------------|----------------------------|
| `[@smith2023]`             | (Smith, 2023)              |
| `@smith2023`               | Smith (2023)               |
| `[@smith2023; @jones2024]` | (Smith, 2023; Jones, 2024) |
| `[@smith2023, p. 42]`      | (Smith, 2023, p. 42)       |

> **Tip**
>
> For Typst output, use `bibliographystyle: apa` in your YAML. This uses Typst's built-in APA style, so no extra `.csl` file is needed.

## Cross-references overview

Quarto has a <span class="highlight">unified cross-referencing system</span>:

| Element  | Label Prefix | Reference Syntax |
|----------|:------------:|:----------------:|
| Figure   |   `#fig-`    |   `@fig-label`   |
| Table    |   `#tbl-`    |   `@tbl-label`   |
| Equation |    `#eq-`    |   `@eq-label`    |
| Section  |   `#sec-`    |   `@sec-label`   |

> **Note**
>
> All cross-references are **automatically numbered** and updated when you add or remove elements. No more manual numbering!

## Cross-references in practice

``` markdown
![The metro system in Mecca, Saudi Arabia.
](images/metro.png){#fig-metro width="80%"}

As shown in @fig-metro, the system connects ...
```

- The label `#fig-metro` makes the figure referenceable
- `@fig-metro` in text becomes "Figure 1" automatically
- Works with PNG, JPG, SVG, and PDF images

``` markdown
| Instance | Optimal | Heuristic | Gap (%) |
|----------|--------:|----------:|--------:|
| Small    |   245   |    248    |   1.2   |
| Medium   |  1,340  |   1,382   |   3.1   |
| Large    | 12,450  |  13,102   |   5.2   |

: Computational results {#tbl-computation}

The results in @tbl-computation show that ...
```

- The caption goes **below** the table with `: Caption text {#tbl-label}`

``` markdown
$$
\sum_{j \in \mathcal{J}} a_{ij} \cdot x_{ij}
  \leq b_i \quad \forall i \in \mathcal{I}
$$ {#eq-capacity}

The capacity constraint in @eq-capacity ensures ...
```

<span id="eq-capacity">
$$\sum_{j \in \mathcal{J}} a_{ij} \cdot x_{ij} \leq b_i \quad \forall i \in \mathcal{I}
 \qquad(2)$$</span>

- The label `{#eq-label}` goes right after the closing `$$`

# <span class="flow">Advanced Formatting with Typst</span>

## Embedding raw Typst

The Quarto templates use <span class="highlight">Typst</span> (not LaTeX) to produce the PDF. For most writing, you only need Markdown. But for advanced formatting, you can embed raw Typst code in a fenced block:

```` markdown
```{=typst}
#v(1cm)                          // vertical space
#text(fill: red)[important]      // colored text
#align(center)[centered text]    // alignment
#line(length: 100%)              // horizontal line
#set text(size: 9pt)             // change font size locally
```
````

> **Note**
>
> Typst is much simpler than LaTeX. See the [Typst documentation](https://typst.app/docs) for the full reference.

## Footnotes and special characters

``` markdown
This claim needs a source^[See Smith (2023) for details.].
```

- En-dash for ranges: `5--10` renders as 5--10
- Em-dash for parenthetical remarks: `---` renders as ---
- Non-breaking space: `16\ GB` keeps the number and unit together

# <span class="flow">Workflow Tips</span>

## Reference management with Zotero

Use [Zotero](https://www.zotero.org/) (free) to manage your references. Export your collection as a `.bib` file via *File → Export Library* (or right-click a collection → *Export Collection*) and select **BibTeX** as the format. The workflow becomes: save a paper to Zotero, export to `.bib`, cite in Quarto with `[@key]`. See the [Literature Research](../workshops/literature-research.qmd) workshop for detailed setup instructions.

## Writing best practices

- **Keep figures in an `images/` folder.** A dedicated folder prevents clutter in your project root and makes it straightforward to locate and update graphics later.
- **Use `quarto preview` for <span class="highlight">live preview</span> while writing.** Seeing your rendered output update in real time helps you catch formatting issues early, before they pile up.
- **Write one sentence per line.** This makes version control diffs much cleaner, because a change to one sentence shows up as a single changed line rather than a reflow of an entire paragraph.
- **Use `<!-- comments -->` to leave notes for yourself.** HTML comments are invisible in the rendered output, so you can mark sections that need revision or leave reminders without affecting the final document.

For guidance on academic language, paragraph structure, and precision in scientific writing, see the [Scientific Writing](../general/scientific-writing.qmd) guide.

## Templates

Ready-to-use templates for seminar papers, bachelor theses, and master theses are available on the [Templates](../general/templates.qmd) page. Download them there, then come back to this workshop for the formatting syntax.

> **Takeaway**
>
> Quarto lets you **focus on content, not formatting**. Write your ideas in simple Markdown, and Quarto handles the rest: citations, cross-references, numbering, and clean PDF output.
