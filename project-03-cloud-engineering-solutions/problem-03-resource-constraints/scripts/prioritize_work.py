import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
INPUT_FILE = BASE_DIR / "examples" / "team-workload.csv"


def priority_label(score: int) -> str:
    if score >= 23:
        return "P1"
    if score >= 16:
        return "P2"
    if score >= 9:
        return "P3"
    return "P4"


def main() -> None:
    tasks = []

    with INPUT_FILE.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            impact = int(row["impact"])
            urgency = int(row["urgency"])
            score = impact * urgency

            row["score"] = score
            row["priority"] = priority_label(score)
            tasks.append(row)

    tasks.sort(key=lambda task: task["score"], reverse=True)

    print("Prioritized team workload:\n")
    for task in tasks:
        print(
            f"{task['priority']} | score={task['score']:>2} | "
            f"{task['task']} | owner={task['owner']} | "
            f"{task['estimated_minutes']} min"
        )


if __name__ == "__main__":
    main()
