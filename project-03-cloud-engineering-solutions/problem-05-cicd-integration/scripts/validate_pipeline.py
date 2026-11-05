import json
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
APP_FILE = BASE_DIR / "app" / "health_check.py"
CONFIG_FILE = BASE_DIR / "config" / "deployment-config.json"


def validate_python() -> None:
    subprocess.run(
        [sys.executable, "-m", "py_compile", str(APP_FILE)],
        check=True,
    )
    print("Python syntax validation: PASS")


def validate_config() -> None:
    with CONFIG_FILE.open(encoding="utf-8") as f:
        config = json.load(f)

    required = {
        "application",
        "environment",
        "replicas",
        "health_check_path",
        "deployment_strategy",
        "rollback_enabled",
    }

    missing = required - config.keys()
    if missing:
        raise ValueError(f"Missing config fields: {sorted(missing)}")

    if config["replicas"] < 1:
        raise ValueError("replicas must be at least 1")

    if not config["health_check_path"].startswith("/"):
        raise ValueError("health_check_path must begin with /")

    if config["deployment_strategy"] not in {"rolling", "blue-green", "canary"}:
        raise ValueError("unsupported deployment_strategy")

    print("Deployment configuration validation: PASS")


def run_health_check() -> None:
    subprocess.run(
        [sys.executable, str(APP_FILE)],
        check=True,
    )


def main() -> None:
    print("Running CI validation...\n")
    validate_python()
    validate_config()
    run_health_check()
    print("\nCI pipeline validation: PASS")


if __name__ == "__main__":
    main()
