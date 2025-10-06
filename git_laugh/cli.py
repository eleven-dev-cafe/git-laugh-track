"""
cli.py
-------
Defines the CLI tool `git-laugh` using the Click library.
"""

import os
import click
import shutil
from pathlib import Path
from .player import play_random_sound


@click.group()
def cli():
    """🎶 Git Laugh Track CLI — Play sounds on Git commits and pushes."""
    pass


@cli.command()
def play():
    """Play a random sound immediately (for testing)."""
    play_random_sound()


@cli.command()
def install():
    """Install Git hooks and sounds."""
    HOOKS_DIR = Path.home() / ".git-laugh-hooks"
    SOUNDS_DIR = Path.home() / ".git-laugh-sounds"

    # 1️⃣ Ensure target dirs exist
    HOOKS_DIR.mkdir(parents=True, exist_ok=True)
    SOUNDS_DIR.mkdir(parents=True, exist_ok=True)

    # 2️⃣ Copy hooks
    repo_hooks = Path.cwd() / "hooks"
    if not repo_hooks.exists():
        click.echo(f"⚠️ No 'hooks/' directory found at {repo_hooks}")
    else:
        for hook in ["post-commit", "post-push"]:
            src = repo_hooks / hook
            dst = HOOKS_DIR / hook
            if src.exists():
                shutil.copy2(src, dst)
                click.echo(f"✅ Installed hook: {hook}")
            else:
                click.echo(f"⚠️ Missing hook: {src}")

    # 3️⃣ Set global hooks path
    os.system(f'git config --global core.hooksPath "{HOOKS_DIR}"')

    # 4️⃣ Copy sounds
    project_sounds = Path.cwd() / "sounds"
    if not project_sounds.exists():
        project_sounds.mkdir(exist_ok=True)
        click.echo(f"📁 Created empty sounds folder: {project_sounds}")
    else:
        mp3_files = list(project_sounds.glob("*.mp3"))
        if mp3_files:
            for file in mp3_files:
                shutil.copy2(file, SOUNDS_DIR / file.name)
                click.echo(f"🎵 Copied sound: {file.name}")
        else:
            click.echo(f"⚠️ No .mp3 files found in {project_sounds}")

    # ✅ Summary
    click.echo("\n🎉 Installation Complete!")
    click.echo(f"Hooks path : {HOOKS_DIR}")
    click.echo(f"Sounds path: {SOUNDS_DIR}")


@cli.command()
def uninstall():
    """Uninstall global Git hooks and sounds."""
    hooks_dir = Path.home() / ".git-laugh-hooks"
    sounds_dir = Path.home() / ".git-laugh-sounds"

    if hooks_dir.exists():
        shutil.rmtree(hooks_dir)
        click.echo(f"✅ Removed hooks from {hooks_dir}")
    else:
        click.echo("⚠️ No hooks to remove.")

    if sounds_dir.exists():
        shutil.rmtree(sounds_dir)
        click.echo(f"✅ Removed sounds from {sounds_dir}")
    else:
        click.echo("⚠️ No sounds to remove.")
