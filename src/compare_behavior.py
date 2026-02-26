import csv
import os
import ast

FILE_PATH = "behavior.csv"
THRESHOLD = 0.35

def compare_pattern(username, new_pattern):

    if not os.path.exists(FILE_PATH):
        return False

    old_patterns = []

    with open(FILE_PATH, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["username"] == username:
                old_patterns.append(ast.literal_eval(row["pattern"]))

    if not old_patterns:
        return False

    baseline_avg = sum([sum(p)/len(p) for p in old_patterns]) / len(old_patterns)
    new_avg = sum(new_pattern) / len(new_pattern)

    deviation = abs(new_avg - baseline_avg) / baseline_avg

    return deviation > THRESHOLD
