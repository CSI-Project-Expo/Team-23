import json
import os

DATA_FILE = "data/patterns.json"

def compare_pattern(username, new_pattern):
    if not os.path.exists(DATA_FILE):
        return False

    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    if username not in data:
        return False

    old_pattern = data[username]
    if not old_pattern or not new_pattern:
        return False

    diff = sum(abs(o - n) for o, n in zip(old_pattern, new_pattern))
    avg_diff = diff / len(new_pattern)

    # threshold for suspicious behavior
    return avg_diff > 0.5
