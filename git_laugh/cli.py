"""
cli.py
-------
Defines the CLI tool `git-laugh` using the Click library.
"""

import click
from pathlib import Path
import shutil
from .player import play_random_sound

@click.group()
def cli():
    """
    🎶 Git Laugh Track CLI
    Play random sounds on git commit & push.
    """
    pass

@cli.command()
def play():
    """
    Play a random sound immediately.
    Useful for testing that your setup works.
    """
    play_random_sound()

@cli.command()
def install():
    """
    Install Git hooks globally.

    - Creates ~/.git-laugh-hooks directory.
    - Copies post-commit and post-push hooks.
    - Users must also set `core.hooksPath` via global-install.sh.
    """
    hooks_dir = Path.home() / ".git-laugh-hooks"
    hooks_dir.mkdir(parents=True, exist_ok=True)

    # Repo's hooks folder (relative to package location)
    repo_hooks = Path(__file__).resolve().parent.parent / "hooks"

    for hook in ["post-commit", "post-push"]:
        shutil.copy(repo_hooks / hook, hooks_dir / hook)

    print(f"✅ Hooks installed in {hooks_dir}")

@cli.command()
def uninstall():
    """
    Uninstall global Git hooks.

    - Removes ~/.git-laugh-hooks if it exists.
    """
    hooks_dir = Path.home() / ".git-laugh-hooks"
    if hooks_dir.exists():
        shutil.rmtree(hooks_dir)
        print("❌ Hooks removed")
    else:
        print("⚠️ No hooks found")
