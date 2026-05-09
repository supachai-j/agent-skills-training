---
name: deploying-to-github-pages
description: Deploys a static site repo to GitHub Pages end-to-end — gitignore, .nojekyll, gh repo create, push, enable Pages via API, wait for build, HTTP smoke test. Use when the user wants to publish a site, deploy to GitHub Pages, ship to github.io, make a static site live, or asks "how do I make this live" — including for project pages, user pages, and template repos.
license: Apache-2.0
compatibility: Requires git, gh (GitHub CLI authenticated), curl. Works on macOS/Linux/WSL.
metadata:
  author: supachai-j
  version: "1.0"
  needs_auth: gh
allowed-tools: Bash(git:*) Bash(gh:*) Bash(curl:*) Bash(touch:*) Bash(echo:*) Bash(sleep:*) Read Write
---

# Deploying to GitHub Pages

End-to-end deploy pipeline distilled from shipping
[agent-skills-training](https://supachai-j.github.io/agent-skills-training/),
[supachai-j.github.io](https://supachai-j.github.io/), and
[course-portal-template](https://supachai-j.github.io/course-portal-template/).

## When to use

Trigger when the user wants:
- Static site published (HTML/CSS/JS only, no build step)
- "Deploy to GitHub Pages" / "publish on github.io" / "make this live"
- Bootstrap a fresh repo + Pages from a local folder
- Project pages (`<user>.github.io/<repo>`) or user pages (`<user>.github.io`)

Do **not** use for:
- Sites needing a build step (use Actions-based deploy instead)
- Private/enterprise hosting
- Static-site generators that need their own deploy flow (Hugo, Jekyll, etc.)

## Pre-flight checklist

Before running the deploy script, confirm:

- [ ] `gh auth status` shows you're logged in
- [ ] Project root has `index.html` (or a redirect HTML if entrypoint is elsewhere)
- [ ] Project root has `.nojekyll` (critical — see Gotchas)
- [ ] Project has `.gitignore` excluding `.DS_Store`, IDE configs, `node_modules/`
- [ ] No secrets in any file: scan with `grep -rE 'api[_-]?key|token|password|secret' --include='*.html'`

## One-shot deploy

```bash
${CLAUDE_SKILL_DIR}/scripts/deploy.sh <github-org> <repo-name> [--private]
```

Or step-by-step manually:

```bash
# 1. Pre-flight files
[ -f .nojekyll ] || touch .nojekyll
[ -f .gitignore ] || cat > .gitignore <<'EOF'
.DS_Store
.obsidian/
*.swp
.idea/
.vscode/
node_modules/
EOF

# 2. Init git
git init -b main
git add .
git commit -m "Initial: <project name>"

# 3. Create + push to GitHub
gh repo create <org>/<repo> --public --source=. --remote=origin --push \
  --description "<one-sentence description>"

# 4. Enable Pages (legacy build, source main / root)
gh api -X POST /repos/<org>/<repo>/pages \
  -f "build_type=legacy" \
  -f "source[branch]=main" \
  -f "source[path]=/"

# 5. Wait for first build, then smoke test
${CLAUDE_SKILL_DIR}/scripts/verify.sh <org> <repo>
```

## User pages vs project pages

| Type | Repo name | URL | Special |
|---|---|---|---|
| User pages | `<username>.github.io` | `https://<username>.github.io/` | Pages auto-enables on first push |
| Project pages | any repo name | `https://<username>.github.io/<repo>/` | Must enable Pages explicitly |
| Template repo | any name | `https://<username>.github.io/<repo>/` | Use `gh api -X PATCH ... -f is_template=true` to add "Use this template" button |

## Gotchas (the things that bit us)

### `.nojekyll` is non-negotiable

Without it, GitHub Pages tries to run Jekyll over your files. Jekyll **chokes**
on filenames containing colons (`concept:skill-md.md`) and underscores
(`_TEMPLATE.md`). The build silently drops those files.

Always `touch .nojekyll` before pushing.

### "It worked, why is the URL 404?"

First build takes ~30-90 seconds. Use the `verify.sh` script to poll until
`status: built`, then HTTP-check.

### Browser cached old redirect

If you change `/index.html` from a redirect to a direct page, browsers may
keep the cached 301. Tell users to **hard-refresh** (`Cmd+Shift+R` /
`Ctrl+F5`) or open in incognito. Cache-Control on Pages is `max-age=600`
(10 minutes).

### File names with colons

Pages serves them fine over HTTP, but some CDN edges normalise URL-encoded
colons differently. Test the live URL, not just `localhost`.

### Absolute paths break on project pages

A project page lives at `https://<user>.github.io/<repo>/`. An `href="/foo.html"`
in your HTML resolves to `https://<user>.github.io/foo.html` — **outside your
repo**, so you get a 404.

The classic culprit is `404.html`, where authors instinctively write absolute
links back to the home page:

```html
<!-- ❌ Breaks on project pages -->
<a href="/">← Home</a>
<a href="/course-en.html">Course</a>

<!-- ✅ Use repo-prefixed absolute paths -->
<a href="/<repo>/">← Home</a>
<a href="/<repo>/course-en.html">Course</a>

<!-- ✅ Or relative paths (works for entry-level pages, fragile from deep URLs) -->
<a href="./">← Home</a>
<a href="course-en.html">Course</a>
```

**Lint with**:

```bash
# Find absolute paths that don't include the repo slug
grep -nE 'href="/[^/]' *.html
```

**User pages don't have this problem** — they live at `<user>.github.io/` so `/`
is the right root.

### The `--source=.` shorthand

Skips the manual `git remote add` + `git push -u origin main`. The
`gh repo create … --source=. --push` command does all of it in one shot.

## Updating an already-deployed site

```bash
# Just commit + push. Pages rebuilds automatically (~30s).
git add .
git commit -m "Update: <what changed>"
git push
# Optionally watch the rebuild:
gh api /repos/<org>/<repo>/pages/builds/latest --jq '.status'
```

## Custom domain (optional)

If the user wants `their-domain.com` instead of `<user>.github.io/<repo>`:

```bash
echo "their-domain.com" > CNAME
git add CNAME && git commit -m "Add custom domain" && git push
# Then in their DNS:
#   - A records pointing to GitHub's IPs (185.199.108.153, 154, 155, 156)
#   - Or CNAME pointing to <user>.github.io
gh api -X PUT /repos/<org>/<repo>/pages \
  -f "cname=their-domain.com" \
  -f "https_enforced=true"
```

DNS propagation: 10 minutes to 24 hours.

## Final checklist

After deploy:

- [ ] `gh api /repos/<org>/<repo>/pages` shows `status: built`
- [ ] HTTP `curl -I <live-url>` returns `200`
- [ ] All entry-point paths return `200` (use `verify.sh`)
- [ ] Test on a fresh browser session (cache miss)
- [ ] Mobile viewport renders correctly
- [ ] Repo description + topics filled in
- [ ] README has the live URL prominently linked

## Related skills

- [`scaffolding-course-portal`](../scaffolding-course-portal/SKILL.md) — calls this in Phase 10
- [`adding-theme-toggle`](../adding-theme-toggle/SKILL.md) — should be done before deploy

## References

- [scripts/deploy.sh](scripts/deploy.sh) — the full bash pipeline
- [scripts/verify.sh](scripts/verify.sh) — HTTP smoke test
- [references/PAGES-GOTCHAS.md](references/PAGES-GOTCHAS.md) — lessons from incidents
