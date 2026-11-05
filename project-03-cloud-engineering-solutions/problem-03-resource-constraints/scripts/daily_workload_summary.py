import csv
from collections import defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
INPUT_FILE = BASE_DIR / "examples" / "team-workload.csv"


def main() -> None:
    totals = defaultdict(int)
    counts = defaultdict(int)

    with INPUT_FILE.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            owner = row["owner"]
            totals[owner] += int(row["estimated_minutes"])
            counts[owner] += 1

    print("Daily workload summary:\n")

    for owner in sorted(totals):
        minutes = totals[owner]
        hours = minutes / 60
        status = "OVERLOADED" if minutes > 120 else "OK"

        print(
            f"{owner}: {counts[owner]} tasks | "
            f"{minutes} min ({hours:.1f} hr) | {status}"
        )


if __name__ == "__main__":
    main()
