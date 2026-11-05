import csv
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
METRICS_FILE = BASE_DIR / "examples" / "sample-metrics.csv"
RULES_FILE = BASE_DIR / "config" / "alert-rules.json"
REPORT_FILE = BASE_DIR / "monitoring-report.json"


def classify(value: float, rule: dict) -> str:
    warning = float(rule["warning"])
    critical = float(rule["critical"])
    direction = rule["direction"]

    if direction == "above":
        if value >= critical:
            return "CRITICAL"
        if value >= warning:
            return "WARNING"
    elif direction == "below":
        if value <= critical:
            return "CRITICAL"
        if value <= warning:
            return "WARNING"

    return "OK"


def main() -> None:
    with RULES_FILE.open(encoding="utf-8") as f:
        rules = json.load(f)

    alerts = []
    rows_checked = 0

    with METRICS_FILE.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            rows_checked += 1
            timestamp = row["timestamp"]

            for metric, rule in rules.items():
                value = float(row[metric])
                status = classify(value, rule)

                if status != "OK":
                    alerts.append(
                        {
                            "timestamp": timestamp,
                            "metric": metric,
                            "value": value,
                            "status": status,
                        }
                    )

    critical = sum(1 for alert in alerts if alert["status"] == "CRITICAL")
    warning = sum(1 for alert in alerts if alert["status"] == "WARNING")

    report = {
        "rows_checked": rows_checked,
        "alerts_generated": len(alerts),
        "warning_alerts": warning,
        "critical_alerts": critical,
        "alerts": alerts,
    }

    with REPORT_FILE.open("w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    print(f"Metric rows checked: {rows_checked}")
    print(f"Warning alerts:      {warning}")
    print(f"Critical alerts:     {critical}")
    print(f"Total alerts:        {len(alerts)}")
    print(f"Report:              {REPORT_FILE}")

    if critical:
        print("\nCritical conditions detected:")
        for alert in alerts:
            if alert["status"] == "CRITICAL":
                print(
                    f"- {alert['timestamp']} | {alert['metric']} = "
                    f"{alert['value']} | {alert['status']}"
                )


if __name__ == "__main__":
    main()
