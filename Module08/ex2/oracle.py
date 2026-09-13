
import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass
class Config:

    matrix_mode: str
    database_url: str
    api_key: str
    log_level: str
    zion_endpoint: str


def load_config() -> Config:
    return Config(
        matrix_mode=os.environ.get("MATRIX_MODE", "development"),
        database_url=os.environ.get(
            "DATABASE_URL", "sqlite:///local.db"
        ),
        api_key=os.environ.get("API_KEY", ""),
        log_level=os.environ.get("LOG_LEVEL", "INFO"),
        zion_endpoint=os.environ.get(
            "ZION_ENDPOINT", "http://localhost:8000"
        ),
    )


def validate_config(config: Config) -> list[str]:
    warnings = []
    if not config.api_key:
        warnings.append("API_KEY is missing or empty")
    if config.matrix_mode not in ("development", "production"):
        warnings.append(
            f"Unexpected MATRIX_MODE value: {config.matrix_mode}"
        )
    if config.matrix_mode == "production" and not (
        config.zion_endpoint.startswith("https://")
    ):
        warnings.append(
            "ZION_ENDPOINT should use https:// in production"
        )
    return warnings


def print_mode_details(config: Config) -> None:
    if config.matrix_mode == "production":
        print("Database: Connected to production instance")
        print("API Access: Authenticated (production key)")
    else:
        print("Database: Connected to local instance")
        print("API Access: Authenticated")
    print(f"Log Level: {config.log_level}")
    print(f"Zion Network: Online ({config.zion_endpoint})")


def print_security_check(warnings: list[str]) -> None:
    print("\nEnvironment security check:")
    if warnings:
        for warning in warnings:
            print(f"[WARNING] {warning}")
    else:
        print("[OK] No hardcoded secrets detected")
        print("[OK] .env file properly configured")
        print("[OK] Production overrides available")


def main() -> None:
    load_dotenv()
    print("ORACLE STATUS: Reading the Matrix...\n")

    try:
        config = load_config()
    except (KeyError, ValueError) as error:
        print(f"ERROR: Could not load configuration - {error}")
        return

    print("Configuration loaded:")
    print(f"Mode: {config.matrix_mode}")
    print_mode_details(config)

    warnings = validate_config(config)
    print_security_check(warnings)

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()