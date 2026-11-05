from __future__ import annotations

import csv
import json
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
RAW_DIR = BASE_DIR / "raw"
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_FILE = OUTPUT_DIR / "standardized-customers.json"


def iso_utc(value: str, source: str) -> str:
    """Convert supported source timestamp formats to ISO-8601 UTC."""
    value = value.strip()

    if source == "crm":
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    elif source == "marketing":
        dt = datetime.strptime(value, "%m/%d/%Y %I:%M %p").replace(
            tzinfo=timezone.utc
        )
    elif source == "support":
        dt = datetime.strptime(value, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    else:
        raise ValueError(f"Unsupported source: {source}")

    return dt.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def standard_record(
    customer_id: object,
    full_name: str,
    email: str | None,
    source_system: str,
    created_at: str,
) -> dict:
    record = {
        "customer_id": str(customer_id).strip(),
        "full_name": full_name.strip(),
        "email": email.strip() if isinstance(email, str) and email.strip() else None,
        "source_system": source_system,
        "created_at": iso_utc(created_at, source_system),
        "schema_version": "1.0",
    }

    if not record["customer_id"]:
        raise ValueError("customer_id is required")
    if not record["full_name"]:
        raise ValueError("full_name is required")

    return record


def load_crm() -> list[dict]:
    records = []
    with (RAW_DIR / "crm_customers.csv").open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            records.append(
                standard_record(
                    row["customer_id"],
                    row["name"],
                    row["email"],
                    "crm",
                    row["created_at"],
                )
            )
    return records


def load_marketing() -> list[dict]:
    records = []
    with (RAW_DIR / "marketing_customers.csv").open(
        newline="", encoding="utf-8"
    ) as f:
        for row in csv.DictReader(f):
            records.append(
                standard_record(
                    row["custID"],
                    row["full_name"],
                    row["email_address"],
                    "marketing",
                    row["date_created"],
                )
            )
    return records


def load_support() -> list[dict]:
    with (RAW_DIR / "support_customers.json").open(encoding="utf-8") as f:
        source_records = json.load(f)

    return [
        standard_record(
            row["id"],
            row["customerName"],
            row.get("contactEmail"),
            "support",
            row["created"],
        )
        for row in source_records
    ]


def main() -> None:
    records = load_crm() + load_marketing() + load_support()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    with OUTPUT_FILE.open("w", encoding="utf-8") as f:
        json.dump(records, f, indent=2)

    print(f"Standardized {len(records)} records.")
    print(f"Output: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
