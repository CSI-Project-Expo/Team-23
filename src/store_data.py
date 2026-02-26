import csv
import os

FILE_PATH = "behavior.csv"

def store_pattern(username, pattern):
    file_exists = os.path.isfile(FILE_PATH)

    with open(FILE_PATH, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["username", "pattern"])

        writer.writerow([username, pattern])
