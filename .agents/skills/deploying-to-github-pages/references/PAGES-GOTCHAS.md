# GitHub Pages — gotchas

Lessons from incidents on real deploys.

## 1. Missing `.nojekyll` silently drops files

**Symptom:** Some files don't appear at expected URLs even though they're in the repo.

**Cause:** GitHub Pages defaults to running Jekyll, which:
- Skips files/folders starting with `_`
- Chokes on filenames containing `:`
- Tries to interpret `.md` as Liquid templates

**Fix:** `touch .nojekyll` at repo root before pushing. Pages will then serve files verbatim.

## 2. Browser cache holds stale redirect

**Symptom:** After flattening URL structure, users still land on 404 from old `<meta refresh>` redirect.

**Cause:** GitHub Pages sends `Cache-Control: max-age=600` (10 min). Browsers cache the redirect HTML for that long.

**Fix:**
- For users hitting the issue: hard refresh (`Cmd+Shift+R`) or open in incognito
- For author: wait 10 min after deploy, or version the redirect file path

## 3. First Pages build delay

**Symptom:** `gh api .../pages` returns `status: building` for 30-90 seconds after push.

**Fix:** Don't HTTP-test immediately. Poll the build status first:

```bash
for i in $(seq 1 24); do
  st=$(gh api /repos/$ORG/$REPO/pages/builds/latest \
        | sed -n 's/.*"status":"\([^"]*\)".*/\1/p' | head -1)
  [ "$st" = "built" ] && break
  sleep 5
done
```

## 4. Custom 404 not picked up

**Symptom:** Random 404s show GitHub's default page even though `404.html` exists.

**Cause:** Pages reads `custom_404` from the build. If build hasn't completed since `404.html` was added, the flag stays `false`.

**Fix:** After adding `404.html`, push and wait for rebuild. Verify with:

```bash
gh api /repos/$ORG/$REPO/pages --jq '.custom_404'   # should be: true
```

## 5. Markdown files served as `text/markdown`, not rendered

**Symptom:** Linking to `wiki-index.md` shows raw text, not rendered HTML.

**Cause:** Pages with `.nojekyll` doesn't process `.md` to HTML — it serves them with `Content-Type: text/markdown; charset=utf-8`.

**Fix (if you want HTML rendering):**
- Convert `.md` to `.html` at build time
- OR use a static-site generator (Hugo, Eleventy) — but that needs a different deploy flow
- OR live with raw markdown rendered by browser (acceptable for wiki-style content)

## 6. User pages vs project pages confusion

**User pages** (`<user>.github.io`): repo MUST be named exactly `<username>.github.io`. Pages is auto-enabled on first push.

**Project pages** (`<user>.github.io/<repo>`): any repo name. Pages must be enabled explicitly:

```bash
gh api -X POST /repos/<org>/<repo>/pages \
  -f "build_type=legacy" -f "source[branch]=main" -f "source[path]=/"
```

Forgetting the explicit enable for project pages → "Pages is not enabled" 404.

## 7. Deploying private repo without Pro

**Symptom:** `gh repo create --private` succeeds, but Pages enable returns 422.

**Cause:** Free GitHub accounts can only enable Pages on public repos. Private requires Pro/Team.

**Fix:** Either upgrade, or use `--public`. The site is public anyway once Pages is on, so privacy of the source is the only diff.

## 8. Fork doesn't enable Pages by default

**Symptom:** Forked a repo, pushed changes, expected Pages to work — but it's off.

**Cause:** Pages settings are not inherited on fork. Each new repo (including forks) needs explicit enable.

**Fix:** Enable Pages on the fork after first push.

## 9. Trailing slash matters for project pages

`https://user.github.io/repo` (no slash) → some browsers send `?` or hit a redirect.
`https://user.github.io/repo/` (with slash) → clean.

Always link with trailing slash from external sites.

## 10. CNAME file is replaced on push

**Symptom:** Pushed and the custom domain stopped working.

**Cause:** A `CNAME` file at repo root persists across pushes IF you committed it. If you set the domain via Settings UI but didn't commit the CNAME, the next push removes it.

**Fix:** Always commit `CNAME` containing your domain:

```bash
echo "your-domain.com" > CNAME
git add CNAME && git commit -m "Lock custom domain"
```
