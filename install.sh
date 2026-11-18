#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

for TARGET in "$HOME/.claude/skills/linkedin-profile-optimizer" "$HOME/.gemini/config/skills/linkedin-profile-optimizer"; do
    mkdir -p "$TARGET"
    cp -f "$REPO_ROOT/SKILL.md" "$TARGET/"
    cp -rf "$REPO_ROOT/references" "$TARGET/"
    cp -rf "$REPO_ROOT/scripts" "$TARGET/"
    echo "Installed linkedin-profile-optimizer to: $TARGET"
done
