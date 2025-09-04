#!/bin/bash
# uninstall.sh
# -------------
# Removes Git Laugh Track hooks globally.
# Unsets `core.hooksPath` and deletes ~/.git-laugh-hooks.

set -e

# Remove Git config
git config --global --unset core.hooksPath || true

# Run CLI uninstall
git-laugh uninstall

echo "❌ Global hooks disabled!"
