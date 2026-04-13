---
title: Literature and Resources
subtitle: Tools and references from the workshops
author: Dr. Tobias Vlćek
---


This page collects the tools, databases, and references mentioned across the workshops. Use it as a quick-reference when you need a link or want to explore a topic further.

# AI Models and Apps

## Hosted LLMs

These are LLMs hosted by companies, which you can access through their websites or APIs. Free tiers are available for most of them; paid tiers unlock more capable models and higher usage limits.

- [OpenAI (ChatGPT)](https://chatgpt.com): The creators of ChatGPT, currently on GPT-5.4. General-purpose models with text, image, and voice capabilities. The free tier uses a weaker model; paid plans give access to the latest version.
- [Anthropic (Claude)](https://claude.ai): Strong at reasoning, coding, and handling long documents. Claude Opus and Sonnet are the main models, with a limited free tier.
- [Google (Gemini)](https://gemini.google.com): Google's LLM with tight integration into Google services (Docs, Sheets, Gmail) and multimodal capabilities including image and video understanding.
- [Mistral (Le Chat)](https://chat.mistral.ai/): A European provider based in France. Offers an affordable student tier and access to Mistral Vibe, and their models run well for both English and European languages.
- [NotebookLM](https://notebooklm.google/): Google's Gemini that can be fed with files, images, and YouTube videos to generate text based on the content. Great for understanding and summarizing content from lectures or to create podcasts from papers.

## Local LLMs and tools

These tools let you run open-source models on your own machine. Running locally gives you more privacy and control, but requires a decent GPU for larger models.

- [Ollama](https://ollama.com/): Free and open-source tool to run large language models locally. Supports a wide range of models including Llama, Mistral, and Gemma. Smaller models (under 8B parameters) can often run on a CPU with enough RAM, though responses will be slower than hosted alternatives.
- [Hugging Face](https://huggingface.co/): The largest open repository of AI models, datasets, and community fine-tunes. You can browse models by task (text generation, translation, summarization), download them, and run them locally through Ollama or the Hugging Face Transformers library.
- [LM Studio](https://lmstudio.ai/): A desktop application for discovering, downloading, and running LLMs locally. Offers both a chat UI and an OpenAI-compatible local server, which means tools that work with the OpenAI API can connect to your local model instead. *Better than Ollama for most users.*

# AI Coding Tools

These are the tools covered in the [Working with AI](../workshops/large-language-models.qmd) workshop. They range from full editors with built-in AI to terminal-based agents that can work autonomously.

- [Zed](https://zed.dev/): A modern, fast code editor built in Rust with built-in AI assistant support. Recommended for this course. Offers a [free student tier](https://zed.dev/education) with unlimited edit predictions and \$10/month in API credits for one year when you sign up with a GitHub account and university email.
- [GitHub Copilot](https://github.com/features/copilot): AI pair programmer that provides inline code suggestions as you type. Integrates into VS Code, Zed, and JetBrains. Free for students via the [GitHub Student Developer Pack](https://education.github.com/pack).
- [OpenCode](https://opencode.ai): Open-source terminal-based AI coding assistant. Lightweight and fast, supports multiple AI providers with your own API keys. Good for quick file edits and terminal tasks.
- [Claude Code](https://claude.ai/code): Anthropic's CLI coding agent for autonomous multi-step tasks. Reads your entire codebase for context, runs terminal commands, and iterates on errors. Requires a Claude subscription or Anthropic API key.
- [Mistral Vibe](https://github.com/mistralai/mistral-vibe): Mistral's open-source CLI coding agent. It scans your project's file structure and Git status, supports natural language commands, and can modify and execute changes across multiple files. Included in the [Mistral Student subscription](https://help.mistral.ai/en/articles/347553-as-a-student-am-i-eligible-for-a-discount-on-le-chat-pro).

# Literature Research

## Academic databases

These databases index peer-reviewed journals, conference proceedings, and working papers. Most require a university login, which you can set up through the [University of Hamburg library](https://www.sub.uni-hamburg.de/) or VPN.

- [Google Scholar](https://scholar.google.com/): Free and broadly accessible across most disciplines. A good starting point with "Cited by" and "Related articles" features for snowballing, though it includes non-peer-reviewed work and metadata can be incomplete.
- [Scopus](https://www.scopus.com/): Comprehensive coverage with strong citation analysis tools. Useful for tracking how a paper has been cited over time and for finding the most-cited papers in a field. Access via university login.
- [Web of Science](https://www.webofscience.com/): Focuses on high-quality journals with rigorous indexing criteria. If a journal is indexed here, it has passed a quality threshold. Access via university login.
- [IEEE Xplore](https://ieeexplore.ieee.org/): Specializes in engineering and computer science, covering IEEE and IET journals and conference proceedings. Access via university login.
- [SSRN](https://www.ssrn.com/): A preprint server for working papers in business, economics, law, and social sciences. Free access, but papers are not peer-reviewed.
- [EBSCOhost](https://search.ebscohost.com/): Multi-disciplinary database aggregator available through the university library. Covers a wide range of subjects beyond STEM.
- [University of Hamburg Library](https://www.sub.uni-hamburg.de/): The portal for accessing most of the databases above. Set up VPN access early so you can search from home.

## AI discovery tools

These tools use AI to surface papers you might miss through keyword search alone. They are good for exploring how papers connect and for getting a quick overview of a research field, but always verify what they find by reading the actual papers.

- [Semantic Scholar](https://www.semanticscholar.org/): AI-powered academic search engine that finds related papers and surfaces connections across disciplines. Also provides TLDR summaries and citation context for many papers.
- [Connected Papers](https://www.connectedpapers.com/): Builds a visual graph of related papers from a seed paper. The graph shows similarity (not citation direction), so you can see clusters of related work at a glance.
- [Elicit](https://elicit.com/): AI research assistant that extracts findings from papers and helps with systematic reviews. You can ask it a research question and it will pull relevant results from the literature.
- [Research Rabbit](https://www.researchrabbit.ai/): Discovers related work from seed papers you provide. Works like a recommendation engine for academic literature: add papers you know, and it suggests what to read next.
- [Consensus](https://consensus.app/): AI search engine that returns research findings rather than web pages. Useful when you want to know "what does the evidence say about X" rather than finding individual papers.
- [Perplexity](https://www.perplexity.ai/): AI search with support for academic sources. Useful for quick overviews of a topic with inline citations, though you should always check the original sources.

## Reference management

A reference manager keeps your papers organized, generates citations automatically, and prevents the chaos of managing `.bib` files by hand.

- [Zotero](https://www.zotero.org/): Free, open-source reference manager recommended for this course. Includes a browser connector for saving papers with one click, PDF storage and annotation, collections and tags for organizing your library, and sync across devices.
- [Better BibTeX for Zotero](https://retorque.re/zotero-better-bibtex/): A plugin that auto-exports your Zotero library to a `.bib` file whenever you add or change a reference. This keeps your citations in sync with your Quarto project without manual steps.

# Scientific Writing

These resources cover the principles of academic writing, from structuring your argument to meeting university requirements. See also the [Scientific Writing](scientific-writing.qmd) guide on this site.

- [Wie schreibe ich wissenschaftlich?](https://studienperspektiven.check.uni-hamburg.de/wie-schreibe-ich-wissenschaftlich/) (University of Hamburg, StudienPerspektivTage): an introduction to academic writing principles, with links to writing center workshops and individual consultations at UHH.
- [APA Style](https://apastyle.apa.org/): the citation and formatting standard used in the course templates. The website covers in-text citations, reference lists, and formatting rules.

# Optimization

If your thesis involves implementing optimization models, the following resources will help you get started.

- [Optimization with Julia](https://beyondsimulations.github.io/Optimization-with-Julia/): A full course on mathematical optimization with Julia, covering linear programming, mixed-integer programming, and heuristics. Includes hands-on exercises and solver integration. This is the recommended programming course at the institute.
- [Gurobi](https://www.gurobi.com/): Commercial optimization solver with a [free academic license](https://www.gurobi.com/academia/academic-program-and-licenses/). One of the fastest solvers available for LP, MIP, and QP. Install via the website after obtaining your academic license.
- [HiGHs](https://highs.dev/): Open-source solver for linear and mixed-integer programming. No license required, easy to install (`pip install highspy` or via Julia's package manager). A good default if you don't need Gurobi's speed.

# Academic Writing Tools

These tools are covered in the [Quarto for Academic Writing](../workshops/quarto-academic-writing.qmd) workshop. Together they replace LaTeX for most academic writing tasks.

- [Quarto](https://quarto.org): Open-source scientific publishing system by Posit. Write in Markdown, render to PDF, HTML, Word, or slides. Handles citations, cross-references, and numbering automatically. Used to create this website and the course templates.
- [Typst](https://typst.app/): A modern typesetting system that Quarto uses for PDF output. Compiles in milliseconds (not seconds like LaTeX), produces clean PDFs, and does not require installing a multi-gigabyte TeX distribution.

# Version Control

These tools are covered in the [Git & GitHub](../workshops/git-github.qmd) workshop. Git protects your work from accidental loss and makes collaboration straightforward.

- [Git](https://git-scm.com/): Free, open-source version control system. Tracks every change you make to your files, lets you undo mistakes at any point, view a complete history of your project, and work with others without overwriting each other's changes.
- [GitHub](https://github.com): The largest hosting platform for Git repositories. Offers free accounts and a [Student Developer Pack](https://education.github.com/pack) with extra features including GitHub Copilot and private repositories.
- [Pro Git (free book)](https://git-scm.com/book/en/v2): The standard reference for Git by Scott Chacon and Ben Straub, freely available online. Chapters 1-3 cover everything you need for thesis work; the rest is useful if you work in larger teams.
- [Learn Git Branching](https://learngitbranching.js.org/): An interactive, visual tutorial that lets you practice Git branching in a sandbox. Good for building intuition about how branches and merges work before you use them on real projects.

# Understanding AI

These resources go deeper into how AI works and how to use it effectively. They complement the [Working with AI](../workshops/large-language-models.qmd) and [AI Prompting](../workshops/prompting.qmd) workshops.

- [One Useful Thing](https://www.oneusefulthing.org/): Ethan Mollick's blog on practical AI use. His [Guide to Which AI to Use](https://www.oneusefulthing.org/p/a-guide-to-which-ai-to-use-in-the) explains the models, apps, and harnesses framework used in the first workshop and is updated regularly as new models appear.
- [3Blue1Brown](https://www.youtube.com/channel/UCYO_jab_esuFRV4b17AJtAw): Visual explanations of how LLMs and neural networks work, by Grant Sanderson. The videos on attention and transformers are particularly useful for understanding the concepts from the first workshop.
- [Prompt Engineering Guide](https://www.promptingguide.ai/): A community-maintained collection of prompting techniques and strategies. Covers zero-shot, few-shot, chain-of-thought, and other approaches beyond the RBTF framework taught in the prompting workshop.
- [AI Assistance and Coding Skills](https://www.anthropic.com/research/AI-assistance-coding-skills): A 2025 Anthropic study that ran a randomized trial with 52 developers. Those using AI scored 17% lower on comprehension tests, with the biggest gap in debugging. However, developers who asked for explanations rather than just code performed nearly as well as those coding by hand.
- [The Many Masks LLMs Wear](https://www.understandingai.org/p/the-many-masks-that-llms-wear): Kai Williams at Understanding AI on how LLMs shift personas mid-conversation, how fine-tuning on one task can trigger unexpected behavior elsewhere, and what that means for trusting model output.
- [Effective Harnesses for Long-Running Agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents): Justin Young at Anthropic Engineering on building agent systems that work across multiple sessions. Covers a two-agent architecture with progress tracking and automated testing, offering a concrete example of why the harness matters more than the model.

# Further Reading

These are general resources for staying current with AI developments, rather than tools you will use directly in your thesis work.

- [Daily Dose of Data Science](https://www.dailydoseofds.com): A website and newsletter with short, visual explanations of data science and machine learning concepts. Good for building general fluency with the field.
- [Alpha Signal](https://alphasignal.ai/): A newsletter that curates the most-discussed AI research papers and industry developments each week. Useful if you want to follow what is happening without reading every preprint yourself.
