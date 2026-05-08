#!/usr/bin/env bash
# deploy.sh — one-shot deploy of the current directory to GitHub Pages.
#
# Usage:  ./deploy.sh <org> <repo> [--private] [--user-pages]
#
#   <org>           GitHub user or org (e.g. supachai-j)
#   <repo>          Repo name (e.g. my-course)
#   --private       Make the repo private (default: public)
#   --user-pages    Skip explicit Pages enable (auto-enabled for <user>.github.io)
#
# Pre-flight: must be run from the project root, with gh authenticated.

set -euo pipefail

ORG="${1:?org/user is required}"
REPO="${2:?repo name is required}"
shift 2 || true

VISIBILITY="--public"
SKIP_PAGES_ENABLE=0
for arg in "$@"; do
  case "$arg" in
    --private) VISIBILITY="--private" ;;
    --user-pages) SKIP_PAGES_ENABLE=1 ;;
    *) echo "Unknown arg: $arg" >&2; exit 1 ;;
  esac
done

cd "$(pwd)"

# 1. Auth check
gh auth status &>/dev/null || { echo "❌ gh not authenticated. Run: gh auth login"; exit 1; }

# 2. Pre-flight files
[ -f .nojekyll ] || { echo "+ creating .nojekyll"; touch .nojekyll; }
if [ ! -f .gitignore ]; then
  echo "+ creating .gitignore"
  cat > .gitignore <<'EOF'
.DS_Store
.obsidian/
*.swp
*.swo
.idea/
.vscode/
node_modules/
EOF
fi

# 3. Secret scan
if grep -rEi 'api[_-]?key|secret_token|password\s*=\s*["'\''][^"'\'']+' \
     --include='*.html' --include='*.md' --include='*.js' --exclude-dir=node_modules . 2>/dev/null; then
  echo "⚠️  Possible secrets detected above. Review before pushing."
  read -rp "Continue anyway? [y/N] " confirm
  case "$confirm" in y|Y) ;; *) exit 1 ;; esac
fi

# 4. Git init (idempotent)
if [ ! -d .git ]; then
  git init -b main
  git add .
  git commit -m "Initial: $REPO"
fi

# 5. Create + push
if ! gh repo view "$ORG/$REPO" &>/dev/null; then
  gh repo create "$ORG/$REPO" $VISIBILITY --source=. --remote=origin --push
else
  echo "+ repo $ORG/$REPO already exists; pushing..."
  git remote add origin "https://github.com/$ORG/$REPO.git" 2>/dev/null || true
  git push -u origin main
fi

# 6. Enable Pages
if [ "$SKIP_PAGES_ENABLE" -eq 0 ]; then
  echo "+ enabling Pages..."
  gh api -X POST "/repos/$ORG/$REPO/pages" \
    -f "build_type=legacy" \
    -f "source[branch]=main" \
    -f "source[path]=/" 2>&1 | grep -v 'already enabled' || true
fi

# 7. Wait for build
LIVE_URL="https://$ORG.github.io/$REPO/"
[ "$REPO" = "$ORG.github.io" ] && LIVE_URL="https://$ORG.github.io/"

echo
echo "+ waiting for first Pages build (~30-90s)..."
for i in $(seq 1 24); do
  st=$(gh api "/repos/$ORG/$REPO/pages/builds/latest" 2>/dev/null \
        | sed -n 's/.*"status":"\([^"]*\)".*/\1/p' | head -1)
  printf "  [%d] %s\n" "$i" "$st"
  [ "$st" = "built" ] && break
  sleep 5
done

# 8. HTTP smoke test
echo
echo "+ smoke test"
code=$(curl -sIL "$LIVE_URL" -o /dev/null -w '%{http_code}')
if [ "$code" = "200" ]; then
  echo "  ✓ $LIVE_URL → 200"
else
  echo "  ⚠ $LIVE_URL → $code (may still be propagating; retry in 30s)"
fi

echo
echo "═══════════════════════════════════════"
echo "  Deployed: $LIVE_URL"
echo "  Repo:     https://github.com/$ORG/$REPO"
echo "═══════════════════════════════════════"
