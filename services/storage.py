# services/storage.py
import json, os
from typing import Any

def load_json(path: str, default: Any) -> Any:
    if not os.path.exists(path):
        save_json(path, default)
        return default
    with open(path, "r") as f:
        return json.load(f)

def save_json(path: str, data: Any):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
