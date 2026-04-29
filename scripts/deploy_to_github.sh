#!/bin/bash
# Deploy: commit and push all changes to GitHub from project root
# Usage: bash scripts/deploy_to_github.sh [commit-message]
# Example: bash scripts/deploy_to_github.sh "Update methods section"

set -e

COMMIT_MSG="${1:-Deploy: $(date +%Y-%m-%d)}"

cd "$(dirname "$0")/.."

echo "=== Deploying to GitHub ==="
echo "Commit: $COMMIT_MSG"
echo ""

# Check remote exists
if ! git remote get-url origin >/dev/null 2>&1; then
    echo "ERROR: No 'origin' remote configured"
    exit 1
fi

REPO_URL=$(git remote get-url origin)
echo "Repo:   $REPO_URL"

# Stage all changes (new, modified, deleted)
git add -A

# Check if there are changes to commit
if git diff --cached --quiet; then
    echo ""
    echo "No changes detected. Working tree is clean."
    echo "=== Nothing to deploy ==="
    exit 0
fi

# Set identity
export GIT_AUTHOR_NAME="Raktim"
export GIT_AUTHOR_EMAIL="raktim.live@gmail.com"
export GIT_COMMITTER_NAME="Raktim"
export GIT_COMMITTER_EMAIL="raktim.live@gmail.com"

# Create commit using plumbing commands (avoids git commit alias/trailer issues)
TREE_HASH=$(git write-tree)
EPOCH=$(date +%s)
COMMIT_OBJ=$(printf 'tree %s\nauthor Raktim <raktim.live@gmail.com> %s +0000\ncommitter Raktim <raktim.live@gmail.com> %s +0000\n\n%s' \
    "$TREE_HASH" "$EPOCH" "$EPOCH" "$COMMIT_MSG" | git hash-object -t commit -w --stdin)

git update-ref HEAD "$COMMIT_OBJ"

echo "Created commit: $COMMIT_OBJ"

# Setup gh auth for git (enables token-based auth for push)
gh auth setup-git 2>/dev/null || true

# Push to GitHub
git push origin main

echo ""
echo "=== Deployment Complete ==="
echo "Repo: $REPO_URL"

# Extract repo URL for display
REPO_NAME=$(echo "$REPO_URL" | sed 's|\.git$||' | sed 's|.*github.com/||')
echo "View: https://github.com/$REPO_NAME"
