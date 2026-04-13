---
title: Structured Literature Research
subtitle: Finding, evaluating, and organizing academic sources
author: Dr. Tobias Vlćek
---


# <span class="flow">Why Structured Research?</span>

## Welcome

This workshop covers <span class="highlight">structured literature research</span>, a core skill for any Bachelor or Master thesis. You will learn how to formulate a clear research question, build effective search strategies, use AI tools for discovery, organize references with Zotero, and evaluate sources critically.

> **Tip**
>
> Finding the right literature early saves you weeks of work later.

## Common mistakes

Most students start by <span class="highlight">Googling randomly</span> and hoping for the best. Other common pitfalls include reading only what is cited in one paper, stopping after the first five results, not keeping track of what you have already read, and relying on a single database or search engine.

> **Warning**
>
> These mistakes lead to incomplete reviews, missed papers, and wasted time.

## A structured approach

A systematic process <span class="highlight">saves time and produces better results</span>. The goal is to find, evaluate, and organize relevant literature. The process at a glance:

1.  **Formulate** a clear research question
2.  **Search** systematically across databases
3.  **Snowball** forwards and backwards
4.  **Organize** references in a manager
5.  **Evaluate** sources critically
6.  **Write** your literature review

# <span class="flow">Formulating Your Research Question</span>

## Start broad, then narrow down

Begin with your <span class="highlight">general topic area</span>, ask yourself what specifically you want to investigate, and narrow down step by step.

**Too broad:**

"Vehicle routing problems"

**Focused:**

"How do metaheuristics compare to exact methods for vehicle routing problems with time windows?"

## Use a framework to structure your question

The <span class="highlight">PICO framework</span> helps you define your question clearly:

| Element | Meaning | Example |
|------------|----------------------|---------------------------------------|
| **P**opulation | What problem or domain? | Vehicle routing with time windows |
| **I**ntervention | What approach or method? | Metaheuristic algorithms |
| **C**omparison | Compared to what? | Exact methods (branch-and-bound) |
| **O**utcome | What do you measure? | Solution quality, computation time |

> **Note**
>
> Not every research question fits PICO perfectly. Use it as a guide, not a strict rule.

A <span class="highlight">well-defined question</span> determines which databases to search, which keywords to use, which papers are relevant, and when you have covered enough ground.

> **Important**
>
> Write down your research question before you start searching. Revisit and refine it as you learn more about the field.

# <span class="flow">Search Strategy</span>

## Google Scholar

[Google Scholar](https://scholar.google.com/) is the most accessible starting point: free, broad coverage, and easy to use.

**Pros:**

- Free and always available
- Covers most disciplines
- "Cited by" feature for snowballing
- Full-text search across papers

**Cons:**

- Quality varies widely
- No advanced filtering options
- Includes non-peer-reviewed work
- Metadata can be incomplete

Useful search techniques: use <span class="highlight">quotes for exact phrases</span> like `"vehicle routing problem"`, the `author:` operator (e.g. `author:taillard`) to find a specific researcher's work, and date ranges to focus on recent publications. The "Cited by" link under each result lets you find newer papers that reference a given work, and "Related articles" surfaces similar papers.

> **Tip**
>
> Create a Google Scholar profile and set up **alerts** for your search terms. You will be notified when new papers match your query.

## Specialized databases

Beyond Google Scholar, use <span class="highlight">specialized databases</span> for more thorough coverage:

| Database | Strength | Access |
|----------------------|--------------------------------|-------------------|
| [Scopus](https://www.scopus.com/) | Comprehensive, citation analysis | University login |
| [Web of Science](https://www.webofscience.com/) | High-quality journals | University login |
| [IEEE Xplore](https://ieeexplore.ieee.org/) | Engineering and CS | University login |
| [SSRN](https://www.ssrn.com/) | Working papers, business/economics | Free |
| [EBSCOhost](https://search.ebscohost.com/) | Multi-disciplinary | University library |

> **Note**
>
> Access most of these through the [University of Hamburg library](https://www.sub.uni-hamburg.de/) or VPN.

## Building search strings

Use <span class="highlight">Boolean operators</span> to combine search terms:

- **AND** --- both terms must appear: `"vehicle routing" AND "metaheuristic"`
- **OR** --- either term can appear: `"genetic algorithm" OR "simulated annealing"`
- **NOT** --- exclude a term: `"optimization" NOT "continuous"`
- **Wildcards** --- match variations: `optimi*` matches optimize, optimization, optimizing

A complete search string for our example:

    ("vehicle routing" OR "VRP") AND
    ("metaheuristic" OR "genetic algorithm" OR
    "simulated annealing") AND "optimization"

<span class="highlight">Start broad</span>, then narrow with additional terms. Document your search strings so you can reproduce and refine them, and track how many results each search returns.

> **Tip**
>
> Keep a search log: record the database, search string, date, and number of results for each search you run.

## Snowballing

Snowballing is <span class="highlight">how you find papers that keyword search misses</span>.

**Forward citation tracking:**

- Who cited this paper?
- Use Google Scholar "Cited by"
- Finds newer work that builds on a given paper
- Good for finding the latest developments

**Backward citation tracking:**

- What does this paper cite?
- Check the reference list
- Finds foundational and seminal papers
- Helps you understand the research lineage

> **Important**
>
> Combine both directions. Forward snowballing finds new work; backward snowballing finds the foundations. Together, they fill the gaps that keyword search leaves.

# <span class="flow">AI Tools for Literature Research</span>

## AI discovery tools

Several tools now use AI to <span class="highlight">help you find papers faster</span>. They complement traditional database searches --- they are good at surfacing papers you would not discover through keyword search alone, at showing how papers relate to each other, and at giving you a quick overview of a research field.

| Tool | What It Does |
|----------------------|--------------------------------------------------|
| [Semantic Scholar](https://www.semanticscholar.org/) | AI-powered academic search, finds related papers |
| [Connected Papers](https://www.connectedpapers.com/) | Visual graph of related papers |
| [Elicit](https://elicit.com/) | AI research assistant, extracts findings |
| [Research Rabbit](https://www.researchrabbit.ai/) | Discovers related work from seed papers |
| [Consensus](https://consensus.app/) | AI search engine for research findings |
| [Perplexity](https://www.perplexity.ai/) | AI search with academic sources |

## Using AI tools effectively

Start with a <span class="highlight">seed paper</span> you know is relevant, then use Connected Papers to visualize how papers connect, Semantic Scholar to find semantically similar work, and Elicit to quickly extract findings across many papers.

<span class="highlight">No single tool is sufficient</span> on its own. Use a layered approach:

1.  **Start** with Google Scholar and database searches
2.  **Expand** with AI tools (Semantic Scholar, Connected Papers)
3.  **Snowball** forwards and backwards from relevant papers
4.  **Verify** everything you find by reading the actual papers

> **Warning**
>
> AI tools are helpful for **discovery**, but always verify: check the actual paper, read abstracts yourself, and do not trust AI summaries blindly. AI can hallucinate references that do not exist.

# <span class="flow">Reference Management with Zotero</span>

## Why use a reference manager?

You will read <span class="highlight">dozens to hundreds of papers</span>. Without a system, you will lose track of what you have read, waste time reformatting citations, and miss papers when writing your bibliography. A reference manager lets you organize papers by topic, cite correctly in any format, collaborate with others, and sync across devices.

## Zotero and the workflow

[Zotero](https://www.zotero.org/) is free, open-source, and works on Windows, Mac, and Linux. It comes with a **browser connector** for saving papers with one click, **PDF storage** for attaching and annotating papers directly, **collections** and **tags** for organizing your library, **groups** for collaborative projects, and **sync** for accessing everything from any device.

> **Important**
>
> **Always import via DOI** when possible. This gives you the most accurate and complete metadata. After importing, always check that the data is correct.

The workflow for your seminar or thesis:

1.  **Find** a paper via Google Scholar, Scopus, or an AI tool
2.  **Save** it with the Zotero browser connector or import via DOI
3.  **Organize** it into a collection for your project
4.  **Export** a `.bib` file from Zotero
5.  **Cite** in Quarto using `[@citationkey]`

**In your `.qmd` file:**

``` markdown
Recent work by [@taillard1993]
shows that...
```

**Rendered output:**

Recent work by Taillard (1993) shows that...

# <span class="flow">Evaluating Sources</span>

## Source types and quality indicators

Not all sources <span class="highlight">carry the same weight</span>:

| Source Type           | Reliability   | Peer-Reviewed?   |
|-----------------------|---------------|------------------|
| Journal articles      | High          | Yes              |
| Conference papers     | Medium--High  | Usually          |
| Preprints (arXiv)     | Variable      | No               |
| Textbooks             | High          | Editorial review |
| Working papers (SSRN) | Variable      | No               |
| Blog posts, websites  | Low--Variable | No               |

> **Warning**
>
> Prefer peer-reviewed journal articles and reputable conference proceedings. Use preprints and working papers with caution.

When evaluating a paper, consider: **journal reputation** (is it recognized in the field?), **author credentials** (are they established researchers?), **methodology** (is the approach rigorous and well-described?), **recency** (has it been superseded?), and **citation count** (has it been cited by others, and how often?).

> **Note**
>
> For operations research specifically: check the **benchmark instances** used, the **computational setup**, and whether the results are **reproducible**.

## Reading papers efficiently

You don't need to read every paper from start to finish. For most papers, start with the abstract and conclusion to decide whether it is relevant. If it is, read the introduction for context, then the methodology and results. Save a deep read for the papers that are closest to your own work.

Annotate as you read. In Zotero, you can highlight and comment directly on PDFs. For each paper, note the research question, the method used, the main findings, and any limitations. This makes writing your literature review much faster because you won't need to re-read papers later.

## Reading critically

Do not accept results at face value. Ask yourself whether the <span class="highlight">sample size</span> is sufficient, whether the **assumptions** are reasonable, whether the **conclusions** follow from the results, whether the findings can be **generalized** to other contexts, and whether there are **limitations** the authors do not discuss.

> **Tip**
>
> A good literature review is not about reading everything. It is about finding and connecting the right papers. For guidance on how to write the review itself, see the [Scientific Writing](../general/scientific-writing.qmd) guide.

# <span class="flow">Wrap-up</span>

## Summary and resources

The full process:

1.  **Question** --- Define a clear, focused research question
2.  **Search** --- Use databases, Boolean operators, and search strings
3.  **Snowball** --- Follow citations forwards and backwards
4.  **Discover** --- Use AI tools to find related work
5.  **Organize** --- Store everything in Zotero and export to `.bib`
6.  **Evaluate** --- Assess quality, relevance, and reliability
7.  **Write** --- Synthesize findings into a coherent review

> **Important**
>
> Start your literature research **early**. It is an iterative process that improves as you learn more about your topic.

| Resource         | Link                                                    |
|----------------------|--------------------------------------------------|
| Google Scholar   | [scholar.google.com](https://scholar.google.com/)       |
| Semantic Scholar | [semanticscholar.org](https://www.semanticscholar.org/) |
| Connected Papers | [connectedpapers.com](https://www.connectedpapers.com/) |
| Elicit           | [elicit.com](https://elicit.com/)                       |
| Zotero           | [zotero.org](https://www.zotero.org/)                   |
| UHH Library      | [sub.uni-hamburg.de](https://www.sub.uni-hamburg.de/)   |
