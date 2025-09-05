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
    1. Ensure ~/.git-laugh-sounds exists.
    2. List all .mp3 files inside.
    3. Pick a random file.
    4. Play it using playsound.
    """
    sound_dir = Path.home() / ".git-laugh-sounds"

    # Ensure the directory exists
    if not sound_dir.exists():
        print(f"❌ Sounds folder not found at {sound_dir}")
        return

    # Collect all mp3 files
    files = list(sound_dir.glob("*.mp3"))
    if not files:
        print(f"❌ No MP3 files found in {sound_dir}")
        return

    # Pick a random sound
    sound_file = random.choice(files)

    # Play the file
    try:
        # playsound an audio
        playsound(str(sound_file))

    except Exception as e:
        print(f"⚠️ Could not play sound: {e}")
