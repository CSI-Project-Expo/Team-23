import json
import os

DATA_FILE = "data/patterns.json"

def store_pattern(username, pattern):
    if not os.path.exists("data"):
        os.makedirs("data")

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
    else:
        data = {}

    data[username] = pattern

    with open(DATA_FILE, "w") as f:
        json.dump(data, f)
