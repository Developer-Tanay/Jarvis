import webbrowser
from config.lists_loader import load_lists

_lists  = load_lists()
_websites = _lists.get("websites", {})

def open_website(key: str) -> bool:
    url = _websites.get(key.lower())
    if url:
        webbrowser.open(url)
        return True
    return False
