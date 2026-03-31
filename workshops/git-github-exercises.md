# Git & GitHub — Interactive Exercise Concepts

## For Future 90-Minute Session Expansion

These exercises are designed to be added when workshops expand from 30 to 90 minutes.

### Exercise 1: First Repository (15 min)
- Create a folder called `git-practice` and initialize it as a Git repository
- Create a file `notes.txt`, write a few lines about what you learned today
- Stage and commit with a meaningful message
- Edit the file, add more lines, stage and commit again
- Run `git log --oneline` to confirm both commits appear
- Discuss: what makes a good commit message?

### Exercise 2: The .gitignore File (10 min)
- In the same repository, create a few files: `draft.pdf`, `notes.txt`, `.DS_Store`
- Create a `.gitignore` that excludes `*.pdf` and `.DS_Store`
- Run `git status` -- verify only unignored files appear
- Stage and commit the `.gitignore` itself
- Discuss: what files should you typically ignore in a Quarto project?

### Exercise 3: Push to GitHub (15 min)
- Create a new repository on GitHub (no README, no .gitignore)
- Link your local `git-practice` repo with `git remote add origin`
- Push with `git push -u origin main`
- Visit the GitHub page and verify your files and commit history appear
- Make another local change, commit, push, and refresh the GitHub page

### Exercise 4: Branching and Merging (15 min)
- Create a branch called `draft` with `git checkout -b draft`
- Make a change and commit it on the branch
- Switch back to `main` with `git checkout main` -- notice the change is gone
- Merge the branch with `git merge draft`
- Verify the change is now on `main`
- Discuss: when would branching be useful in your thesis work?

### Exercise 5: Pair Exercise — Clone and Explore (15 min)
- Pair up with another student
- Share the URL of your GitHub repository
- Clone your partner's repo with `git clone <url>`
- Read their commit history with `git log --oneline`
- Discuss: can you tell what they did from their commit messages alone?
- Reflect on what makes a repository easy to understand for others
