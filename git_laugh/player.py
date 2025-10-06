"""
player.py
----------
Responsible for selecting and playing a random sound.
"""

import random
from pathlib import Path
from playsound import playsound


def play_random_sound(custom_path: Path | None = None):
    """
    Play a random sound from ~/.git-laugh-sounds (or a given path).

    Steps:
    1️ Ensure sound directory exists
    2️ List available .mp3/.wav/.ogg files
    3️ Choose one randomly
    4️ Play using playsound()
    """
    sound_dir = custom_path or (Path.home() / ".git-laugh-sounds")
    AUDIO_EXTS = (".mp3", ".wav", ".ogg")

    # 1️⃣ Check folder existence
    if not sound_dir.exists():
        print(f"⚠️ Sounds folder not found at {sound_dir}")
        return

    # 2️⃣ List audio files
    files = [f for f in sound_dir.iterdir() if f.suffix.lower() in AUDIO_EXTS]
    if not files:
        print(f"⚠️ No audio files found in {sound_dir}")
        return

    # 3️⃣ Pick random file
    sound_file = random.choice(files)
    print(f"🎧 Now playing: {sound_file.name}")

    # 4️⃣ Play sound
    try:
        playsound(str(sound_file))
    except Exception as e:
        print(f"⚠️ Could not play sound '{sound_file.name}': {e}")
