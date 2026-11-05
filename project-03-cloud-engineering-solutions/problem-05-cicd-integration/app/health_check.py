def check_service(status_code: int) -> bool:
    return status_code == 200


def main() -> None:
    sample_status = 200

    if check_service(sample_status):
        print("Application health check: PASS")
    else:
        raise SystemExit("Application health check: FAIL")


if __name__ == "__main__":
    main()
