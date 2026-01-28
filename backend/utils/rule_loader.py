import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def load_rule(filename: str):
    path = BASE_DIR / "rules" / filename
    with open(path, "r") as f:
        return json.load(f)
