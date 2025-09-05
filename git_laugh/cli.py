"""
cli.py
-------
Defines the CLI tool `git-laugh` using the Click library.
"""

import os
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
    """Install Git hooks and copy sounds."""
    HOOKS_DIR = Path.home() / ".git-laugh-hooks"
    SOUNDS_DIR = Path.home() / ".git-laugh-sounds"

    # 1. Ensure hooks dir exists
    HOOKS_DIR.mkdir(parents=True, exist_ok=True)

    # 2. Copy hook scripts
    repo_hooks = Path(__file__).resolve().parent.parent / "hooks"
    for hook in ["post-commit", "post-push"]:
        src = repo_hooks / hook
        dst = HOOKS_DIR / hook
        if src.exists():
            shutil.copy2(src, dst)
            print(f"Hook with name {hook} Installed")

        else:
            click.echo("hooks does not exist")

    # 3. Configure git to use this hooks path
    os.system(f'git config --global core.hooksPath "{HOOKS_DIR}"')

    # 4. Ensure sounds dir exists
    SOUNDS_DIR.mkdir(parents=True, exist_ok=True)

    # 5. Copy sounds from project `sounds/` folder
    project_sounds = Path(__file__).resolve().parent.parent / "sounds"
    if project_sounds.exists():
        mp3_files = list(project_sounds.glob("*.mp3"))
        for file in mp3_files:
            shutil.copy2(file, SOUNDS_DIR / file.name)
            print(f"Sound added at {file}")

    else:
        print("❌ Project sound does not exist")

    click.echo(f"✅ Required Hooks installed in {HOOKS_DIR}")
    click.echo(f"✅ All Sounds installed in {SOUNDS_DIR}")
    

@cli.command()
def uninstall():
    """
    Uninstall global Git hooks.

    - Removes ~/.git-laugh-hooks if it exists.
    """
    hooks_dir = Path.home() / ".git-laugh-hooks"
    if hooks_dir.exists():
        shutil.rmtree(hooks_dir)
        print(f"✅ All Hooks uninstalled from {hooks_dir}")
    else:
        print("⚠️ No hooks found")

    sound_dir = Path.home() / ".git-laugh-sounds"
    if sound_dir.exists():
        shutil.rmtree(sound_dir)
        print("✅ All Sounds uninstalled from {sound_dir}")
    else:
        print("⚠️ No sound present")
        