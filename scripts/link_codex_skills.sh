#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET="${1:-$HOME/.agents/skills}"

mkdir -p "$TARGET"

for skill in "$ROOT"/skills/*; do
  [[ -d "$skill" ]] || continue
  name="$(basename "$skill")"
  dest="$TARGET/$name"
  if [[ -e "$dest" || -L "$dest" ]]; then
    echo "skip: $dest already exists"
  else
    ln -s "$skill" "$dest"
    echo "linked: $dest -> $skill"
  fi
done
