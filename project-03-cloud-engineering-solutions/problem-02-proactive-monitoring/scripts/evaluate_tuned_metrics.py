import csv
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
METRICS_FILE = BASE_DIR / "examples" / "sample-metrics.csv"
RULES_FILE = BASE_DIR / "config" / "alert-rules.json"
REPORT_FILE = BASE_DIR / "tuned-monitoring-report.json"


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

    with METRICS_FILE.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    alerts = []
    last_status = {metric: "OK" for metric in rules}
    consecutive = {metric: 0 for metric in rules}
    previous_raw = {metric: "OK" for metric in rules}

    for row in rows:
        timestamp = row["timestamp"]

        for metric, rule in rules.items():
            value = float(row[metric])
            raw_status = classify(value, rule)

            if raw_status == previous_raw[metric] and raw_status != "OK":
                consecutive[metric] += 1
            elif raw_status != "OK":
                consecutive[metric] = 1
            else:
                consecutive[metric] = 0
                last_status[metric] = "OK"

            previous_raw[metric] = raw_status

            if (
                raw_status != "OK"
                and consecutive[metric] >= 2
                and raw_status != last_status[metric]
            ):
                alerts.append(
                    {
                        "timestamp": timestamp,
                        "metric": metric,
                        "value": value,
                        "status": raw_status,
                        "reason": "two consecutive samples at the same severity",
                    }
                )
                last_status[metric] = raw_status

    warning = sum(1 for alert in alerts if alert["status"] == "WARNING")
    critical = sum(1 for alert in alerts if alert["status"] == "CRITICAL")

    report = {
        "rows_checked": len(rows),
        "warning_alerts": warning,
        "critical_alerts": critical,
        "total_alerts": len(alerts),
        "alerts": alerts,
    }

    with REPORT_FILE.open("w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    print(f"Metric rows checked: {len(rows)}")
    print(f"Warning alerts:      {warning}")
    print(f"Critical alerts:     {critical}")
    print(f"Total tuned alerts:  {len(alerts)}")
    print(f"Report:              {REPORT_FILE}")

    if alerts:
        print("\nTuned alerts:")
        for alert in alerts:
            print(
                f"- {alert['timestamp']} | {alert['metric']} = "
                f"{alert['value']} | {alert['status']}"
            )


if __name__ == "__main__":
    main()
