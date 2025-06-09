import json
import os

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "lists.json")

def load_lists():
    with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)
