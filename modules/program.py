import subprocess
from config.lists_loader import load_lists

_favs = load_lists()
_programs = _favs.get("programs", {})

def open_program(app_key: str) -> bool:
    exe = _programs.get(app_key.lower())
    if exe:
        try:
            subprocess.Popen([exe], shell=True)
            return True
        except Exception as e:
            print(f"[program] Error opening {exe}: {e}")
    return False
