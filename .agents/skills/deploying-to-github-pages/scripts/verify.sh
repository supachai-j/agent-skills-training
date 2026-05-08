#!/usr/bin/env bash
# verify.sh — HTTP smoke test for a GitHub Pages site.
# Usage: ./verify.sh <org> <repo> [path1 path2 ...]
# If no paths given, checks "/" only.

set -euo pipefail

ORG="${1:?org/user is required}"
REPO="${2:?repo name is required}"
shift 2

PATHS=("$@")
[ ${#PATHS[@]} -eq 0 ] && PATHS=("/")

BASE="https://$ORG.github.io/$REPO"
[ "$REPO" = "$ORG.github.io" ] && BASE="https://$ORG.github.io"

echo "Checking $BASE"
fail=0
for p in "${PATHS[@]}"; do
  [[ "$p" != /* ]] && p="/$p"
  printf "  %-44s " "$p"
  code=$(curl -sIL "$BASE$p" -o /dev/null -w '%{http_code}')
  if [ "$code" = "200" ]; then
    echo "✓ 200"
  else
    echo "✗ $code"
    fail=1
  fi
done

[ "$fail" = "1" ] && exit 1 || echo "All paths return 200."
