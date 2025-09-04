#!/bin/bash
# global-install.sh
# ------------------
# Installs Git Laugh Track hooks globally.
# This sets `core.hooksPath` to ~/.git-laugh-hooks
# so every Git repo on your machine uses the hooks.

set -e

# Ensure git-laugh CLI is available
if ! command -v git-laugh &>/dev/null; then
    echo "❌ git-laugh not installed. Run: pip install ."
    exit 1
fi

# Configure Git to use the global hooks path
git config --global core.hooksPath "$HOME/.git-laugh-hooks"

# Run CLI install command (copies hooks)
git-laugh install

echo "✅ Global hooks enabled! (Located in ~/.git-laugh-hooks)"