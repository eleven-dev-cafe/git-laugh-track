"""
player.py
----------
Responsible for selecting and playing a random sound.
"""

import random
import os
from pathlib import Path
from playsound import playsound

def play_random_sound():
    """
    Plays a random .mp3 file from either:
    1. Project 'sounds/' folder (relative to this script)
    2. User's home '.git-laugh-sounds' folder

    Steps:
    1. Check project sounds folder first.
    2. If empty, check ~/.git-laugh-sounds.
    3. Pick a random file.
    4. Play it using playsound.
    """
    # 1. Project sounds folder (relative to this script)
    base_dir = Path(__file__).parent
    project_sounds = base_dir.parent / "sounds"

    # 2. User home sounds folder
    home_sounds = Path.home() / ".git-laugh-sounds"

    # Prefer project sounds if available
    if project_sounds.exists() and any(project_sounds.glob("*.mp3")):
        sound_dir = project_sounds
    else:
        sound_dir = home_sounds

    # Ensure the directory exists
    if not sound_dir.exists():
        print(f"❌ No sounds folder found at {sound_dir}")
        return

    # Collect all mp3 files
    files = list(sound_dir.glob("*.mp3"))
    if not files:
        print(f"❌ No MP3 files found in {sound_dir}")
        return

    # Pick a random sound
    sound_file = random.choice(files)
    print(f"▶ Playing: {sound_file.name}")

    # Play the file
    try:
        playsound(str(sound_file))
    except Exception as e:
        print(f"⚠️ Could not play sound: {e}")
