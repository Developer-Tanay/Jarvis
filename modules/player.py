# modules/player.py
import os
import webbrowser
from playsound3 import playsound
from config.lists_loader import load_lists

_lists = load_lists()
_songs = _lists["songs"]

def play_song(key: str) -> bool:
    item = _songs.get(key.lower())
    if not item:
        print(f"[player] Song '{key}' not found in list.")
        return False

    if item.startswith("http://") or item.startswith("https://"):
        webbrowser.open(item)
        return True

    path = os.path.expandvars(item)
    if not os.path.exists(path):
        print(f"[player] File not found: {path}")
        return False

    try:
        playsound(path, block=False)
        return True
    except Exception as e:
        print(f"[player] Playback error for {path}: {e}")
        return False
