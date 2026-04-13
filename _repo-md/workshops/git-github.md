---
title: Git and GitHub
subtitle: Version control and project organization for your thesis
author: Dr. Tobias Vlćek
---


# <span class="flow">Why Version Control?</span>

## Welcome

This workshop covers <span class="highlight">Git and GitHub</span>. By the end, you will be able to track changes to your files with Git, use Zed's built-in Git integration to stage and commit, push your work to GitHub as a backup, and understand the terminal commands behind what Zed does visually.

> **Tip**
>
> Version control is not just for programmers. It protects every document you write: thesis drafts, code, and data analysis scripts.

## The problem and the solution

**What usually happens:**

    essay_final.docx
    essay_final_v2.docx
    essay_final_REALLY_FINAL.docx
    essay_final_REALLY_FINAL_revised.docx

**What version control gives you:**

- A complete history of every change you made, so you can see what your project looked like at any point in time
- The ability to undo any mistake, even weeks later
- A backup in the cloud through GitHub, so your work survives a lost or broken laptop
- A way to work with others without overwriting each other's changes

> **Warning**
>
> If your laptop dies tomorrow, is your thesis safe? Git and GitHub make sure the answer is yes.

## Git vs GitHub

|                | Git                       | GitHub                            |
|---------------|-----------------------------|-----------------------------|
| **What**       | Software on your computer | A website that hosts repositories |
| **Purpose**    | Tracks changes to files   | Sharing, collaboration, backup    |
| **Connection** | Works entirely offline    | Requires internet                 |
| **Cost**       | Free and open-source      | Free tier available               |

> **Note**
>
> Git is the engine. GitHub is one of several online platforms (others include GitLab and Bitbucket) where you store your Git repositories.

# <span class="flow">Setting Up Git</span>

## Installing and configuring Git

**macOS** (via Homebrew, which you installed in the earlier workshop):

``` bash
brew install git
```

**Windows:**

``` bash
winget install Git.Git
```

**Linux:**

``` bash
sudo apt install git
```

Verify it works with `git --version`.

Once installed, open <span class="highlight">Zed's integrated terminal</span> and tell Git who you are:

``` bash
git config --global user.name "Your Name"
git config --global user.email "your.email@uni-hamburg.de"
```

This labels your commits with your name and email. You only need to do this once.

> **Important**
>
> Use the same email you will register on GitHub. This links your commits to your GitHub account.

# <span class="flow">The Core Git Workflow</span>

## How Git works

Git organizes your work into <span class="highlight">three zones</span>:

1.  **Working directory:** your files as you edit them
2.  **Staging area:** changes you have selected for the next snapshot
3.  **Repository:** permanent saved snapshots (commits)

Think of it like writing an email: you draft the text (working directory), you review what to include (staging), you hit send (commit). The command `git add` moves changes to staging, and `git commit` saves the snapshot. This two-step process lets you choose exactly what goes into each commit.

You can interact with Git in two ways. **Zed's Git panel** lets you click to stage, commit, and view diffs visually, which is enough for most daily work. **Terminal commands** give you full control over every operation and work in any environment, not just Zed. We will teach both: start with Zed's visual tools for comfort, then learn the terminal commands so you understand what is happening underneath.

Zed has <span class="highlight">built-in Git support</span>: the **source control panel** shows all changed files at a glance, you can **check the box** next to a file to stage it, **type a commit message** and commit without leaving the editor, and the **diff view** shows exactly which lines changed inline. Colored **gutter markers** in the margin indicate added, modified, and deleted lines.

> **Tip**
>
> For daily work, Zed's Git panel is all you need. The terminal commands in the following sections show you what is happening behind the scenes and become useful when you need more control or when something goes wrong.

## Starting a new project

In Zed's terminal, navigate to where you want your project and run:

``` bash
mkdir my-project
cd my-project
git init
```

You should see: `Initialized empty Git repository in .../my-project/.git/`

Now create a file and check the status:

``` bash
echo "# My First Project" > README.md
git status
```

Git will tell you `README.md` is an <span class="highlight">untracked file</span>. It exists, but Git is not watching it yet. Zed shows this directly in the file tree: untracked and modified files are marked automatically once you run `git init`.

## Staging and committing

**Stage** a file to tell Git you want to include it in the next snapshot:

``` bash
git add README.md
```

**Commit** to save the snapshot with a message:

``` bash
git commit -m "Add initial README file"
```

That is your first commit. Now edit the file and repeat:

``` bash
echo "This project is for learning Git." >> README.md
git add README.md
git commit -m "Add project description to README"
```

> **Note**
>
> `git add .` stages all changed files at once. Use it when you want to commit everything, but be careful not to include files you did not intend to track.

## Commit messages and history

**Unhelpful messages:**

- "fixed stuff"
- "update"
- "final version"
- "asdf"

**Descriptive messages:**

- "Add methodology section"
- "Fix citation format in literature review"
- "Update results table with revised data"
- "Remove unused figures from images folder"

> **Warning**
>
> Write messages that describe <span class="highlight">what changed and why</span>. Six months from now, "update" tells you nothing. "Fix broken cross-reference in chapter 3" tells you everything.

To see all your commits in a compact view, run `git log --oneline`. Each line shows a short identifier (the commit hash) and your message, forming the timeline of your project. To see what changed since your last commit, run `git diff`. Zed's source control panel shows diffs visually, so you can see exactly which lines were added, changed, or removed without memorizing the command.

## Ignoring files you do not need

Some files should <span class="highlight">not be tracked</span>, such as compiled output, system files, and large data. Create a `.gitignore` file:

    _site/
    _freeze/
    .DS_Store
    *.pdf

For a Quarto project, this means you track your `.qmd` source files but not the rendered output. The output can always be regenerated.

> **Note**
>
> Add `.gitignore` early in your project. It is much easier to ignore files from the start than to remove them from Git history later.

# <span class="flow">Connecting to GitHub</span>

## Setting up GitHub

Go to [github.com](https://github.com) and sign up with your university email. Apply for the [GitHub Student Developer Pack](https://education.github.com/pack) for extra features. If you already set up GitHub for Copilot in the earlier workshop, you are ready to go.

To create your first remote repository, click the **+** icon in the top-right corner and select **"New repository"**. Name it `my-project` (matching your local folder), leave it **public** (or private if you prefer), and **do not** initialize with a README since you already have one locally. Click **"Create repository"** and GitHub will show you setup instructions.

## Pushing to GitHub

Back in Zed's terminal, connect your local repo to GitHub and push your commits:

``` bash
git remote add origin https://github.com/YOUR-USERNAME/my-project.git
git branch -M main
git push -u origin main
```

Refresh your GitHub page. Your files and commit history are now visible online.

> **Note**
>
> GitHub will ask you to log in the first time you push. If the login prompts become annoying, look into SSH keys or the GitHub CLI (`gh auth login`) for a smoother setup.

After the initial setup, the day-to-day cycle is simple. Both approaches (Zed's visual panel and the terminal) accomplish the same thing:

**In Zed's Git panel:**

1.  Edit your files
2.  Open the source control panel
3.  Check the boxes to stage changes
4.  Type a commit message and commit
5.  Push to GitHub

**In the terminal:**

1.  Edit your files
2.  `git add .`
3.  `git commit -m "message"`
4.  `git push`

> **Important**
>
> Commit and push at the end of every work session. This is your backup. If anything happens to your machine, your work is safe on GitHub.

# <span class="flow">Branching</span>

## Working with branches

Sometimes you want to try a new analysis approach but do not want to break what works. A <span class="highlight">branch</span> is an independent line of development that lets you experiment safely.

**Without branches:**

- You edit your only copy
- If it goes wrong, you have to undo manually
- Risky for larger changes

**With branches:**

- You create a separate copy to experiment
- Your main version stays untouched
- Merge back only if you are happy with the result

The commands:

``` bash
# Create and switch to a new branch
git checkout -b experiment

# Do your work, then add and commit as usual
git add .
git commit -m "Try a new approach to analysis"

# Switch back to main
git checkout main

# Merge the branch into main
git merge experiment
```

> **Note**
>
> Branching becomes more useful as your project grows. For now, just know it exists. In professional teams, developers create a branch for every new feature or fix, then merge it back after review through **pull requests**.

# <span class="flow">Project Organization</span>

## Folder structure

A clean folder structure makes your project easier to navigate, version-control, and share. Here is a recommended layout for a thesis project:

    my-thesis/
    ├── seminar-paper-en.qmd    # Your paper (or -de.qmd)
    ├── references.bib           # Bibliography
    ├── typst-show.typ           # Required Typst helper
    ├── images/                  # All figures
    │   ├── fig-results.png
    │   └── fig-network.pdf
    ├── code/                    # Scripts and implementation
    │   ├── model.py
    │   └── analysis.py
    └── data/                    # Input data and instances
        ├── instances/
        └── results/

> **Tip**
>
> Keep your project root clean. Put figures in `images/`, scripts in `code/`, and data in `data/`. This makes it easy to find files and write clean `.gitignore` rules.

## File naming conventions

- **No spaces** --- use hyphens or underscores: `fig-results.png`, not `fig results.png`
- **Lowercase** --- avoids cross-platform issues: `data/instances/`, not `Data/Instances/`
- **Be descriptive** --- `fig-gap-by-instance-size.png` is better than `plot1.png`
- **Date-prefix raw data** if versioned: `2026-03-15-survey-responses.csv`

## What to track (and what not to)

<div id="tbl-git-track">

| Track with Git      | Do NOT track                       |
|:--------------------|:-----------------------------------|
| `.qmd` source files | Generated PDFs (`_site/`, `*.pdf`) |
| `.bib` bibliography | Quarto cache (`_freeze/`)          |
| Code and scripts    | Large datasets (use cloud storage) |
| `.gitignore`        | System files (`.DS_Store`)         |
| `typst-show.typ`    | Editor settings (`.vscode/`)       |

Table 1: Version control decisions
</div>

A good `.gitignore` for a Quarto thesis project:

    _site/
    _freeze/
    *.pdf
    .DS_Store
    .quarto/

# <span class="flow">Wrap-up</span>

## Reference and resources

| Command                       | What it does                  |
|-------------------------------|-------------------------------|
| `git init`                    | Start tracking a folder       |
| `git status`                  | See what has changed          |
| `git add <file>`              | Stage a file for commit       |
| `git commit -m "..."`         | Save a snapshot               |
| `git log --oneline`           | View commit history           |
| `git remote add origin <url>` | Connect to GitHub             |
| `git push`                    | Send commits to GitHub        |
| `git pull`                    | Get updates from GitHub       |
| `git checkout -b <name>`      | Create and switch to a branch |

**Takeaways:**

1.  **Version control protects your work.** No more "final_v2_REALLY_FINAL.docx"
2.  **Zed's Git panel handles daily tasks.** Stage, commit, and diff without leaving your editor
3.  **Terminal commands give you full control.** Needed for setup, branching, and when things go wrong
4.  **Push to GitHub at the end of every session.** It is your backup

> **Important**
>
> Start using Git now, even for a single file. The safety net is worth the 30 seconds it takes to commit.

| Resource | Link |
|--------------------------|----------------------------------------------|
| Pro Git (free book) | [git-scm.com/book](https://git-scm.com/book/en/v2) |
| GitHub Docs | [docs.github.com](https://docs.github.com) |
| Learn Git Branching | [learngitbranching.js.org](https://learngitbranching.js.org/) |
| GitHub Student Pack | [education.github.com/pack](https://education.github.com/pack) |

> **Tip**
>
> Pro Git chapters 1-3 cover everything you need for your thesis work. The interactive tutorial at Learn Git Branching is a good way to practice.
