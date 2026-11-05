import json
import re
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
INPUT_FILE = BASE_DIR / "output" / "standardized-customers.json"
REPORT_FILE = BASE_DIR / "output" / "data-quality-report.json"

EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
REQUIRED_FIELDS = {
    "customer_id",
    "full_name",
    "email",
    "source_system",
    "created_at",
    "schema_version",
}
VALID_SOURCES = {"crm", "marketing", "support"}


def is_iso_utc(value: str) -> bool:
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
        return value.endswith("Z")
    except (TypeError, ValueError):
        return False


def validate_record(record: dict, index: int) -> list[str]:
    errors = []

    missing = REQUIRED_FIELDS - record.keys()
    if missing:
        errors.append(f"record {index}: missing fields: {sorted(missing)}")
        return errors

    if not isinstance(record["customer_id"], str) or not record["customer_id"].strip():
        errors.append(f"record {index}: customer_id must be a non-empty string")

    if not isinstance(record["full_name"], str) or not record["full_name"].strip():
        errors.append(f"record {index}: full_name must be a non-empty string")

    email = record["email"]
    if email is not None and (not isinstance(email, str) or not EMAIL_PATTERN.match(email)):
        errors.append(f"record {index}: invalid email format")

    if record["source_system"] not in VALID_SOURCES:
        errors.append(f"record {index}: invalid source_system")

    if not is_iso_utc(record["created_at"]):
        errors.append(f"record {index}: created_at must be ISO-8601 UTC ending in Z")

    if record["schema_version"] != "1.0":
        errors.append(f"record {index}: schema_version must equal 1.0")

    extra = record.keys() - REQUIRED_FIELDS
    if extra:
        errors.append(f"record {index}: unexpected fields: {sorted(extra)}")

    return errors


def main() -> None:
    with INPUT_FILE.open(encoding="utf-8") as f:
        records = json.load(f)

    all_errors = []
    seen_ids = set()
    duplicate_ids = []

    for index, record in enumerate(records, start=1):
        all_errors.extend(validate_record(record, index))

        customer_id = record.get("customer_id")
        if customer_id in seen_ids:
            duplicate_ids.append(customer_id)
        seen_ids.add(customer_id)

    if duplicate_ids:
        all_errors.append(f"duplicate customer_id values: {sorted(set(duplicate_ids))}")

    valid_count = len(records) if not all_errors else len(records) - len(
        {int(e.split()[1].rstrip(":")) for e in all_errors if e.startswith("record ")}
    )

    report = {
        "records_checked": len(records),
        "valid_records": valid_count,
        "invalid_records": len(records) - valid_count,
        "duplicate_ids": sorted(set(duplicate_ids)),
        "errors": all_errors,
        "status": "PASS" if not all_errors else "FAIL",
    }

    with REPORT_FILE.open("w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    print(f"Records checked: {report['records_checked']}")
    print(f"Valid records:   {report['valid_records']}")
    print(f"Invalid records: {report['invalid_records']}")
    print(f"Status:          {report['status']}")
    print(f"Report:          {REPORT_FILE}")

    if all_errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
