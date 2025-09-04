"""
player.py
----------
Responsible for selecting and playing a random sound.
"""

import random
from pathlib import Path
from playsound import playsound

def play_random_sound():
    """
    Plays a random .mp3 file from ~/.git-laugh-sounds.

    Steps:
    1. Check if ~/.git-laugh-sounds exists.
    2. List all .mp3 files inside.
    3. Pick a random file.
    4. Play the file using playsound.
    """
    sound_dir = Path.home() / ".git-laugh-sounds"

    # Ensure the sound directory exists
    if not sound_dir.exists():
        return

    # Collect all mp3 files
    files = list(sound_dir.glob("*.mp3"))
    if not files:
        return

    # Pick a random sound
    sound_file = random.choice(files)

    try:
        playsound(str(sound_file))
    except Exception as e:
        print(f"⚠️ Could not play sound: {e}")
