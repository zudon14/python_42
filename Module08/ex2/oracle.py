import os
import sys

try:
    from dotenv import (  # type: ignore
        dotenv_values,
        find_dotenv,
        load_dotenv,
    )
except ImportError:
    print("ORACLE STATUS: The Oracle cannot read the Matrix\n")
    print("ERROR: the python-dotenv package is not installed.")
    print("Install it inside a virtual environment with:")
    print("    pip install -r requirements.txt")
    sys.exit(1)

REQUIRED_VARS = (
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
)

# Safe fallbacks, used (with a warning) when a variable is not configured.
DEFAULTS = {
    "MATRIX_MODE": "development",
    "DATABASE_URL": "sqlite:///local.db",
    "API_KEY": "",
    "LOG_LEVEL": "INFO",
    "ZION_ENDPOINT": "",
}

VALID_MODES = ("development", "production")
VALID_LOG_LEVELS = ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL")


def load_config() -> tuple[dict[str, str], list[str]]:
    """Read the configuration from os.environ.

    Returns the configuration and the names of the missing variables.
    """
    config: dict[str, str] = {}
    missing: list[str] = []
    for name in REQUIRED_VARS:
        value = os.environ.get(name, "").strip()
        if value:
            config[name] = value
        else:
            config[name] = DEFAULTS[name]
            missing.append(name)
    return config, missing


def collect_warnings(config: dict[str, str], missing: list[str]) -> list[str]:
    warnings = [f"{name} is not set, using default" for name in missing]
    mode = config["MATRIX_MODE"].lower()
    if mode not in VALID_MODES:
        warnings.append(
            f"Unknown MATRIX_MODE '{config['MATRIX_MODE']}', "
            "falling back to development"
        )
    if config["LOG_LEVEL"].upper() not in VALID_LOG_LEVELS:
        warnings.append(f"Unknown LOG_LEVEL '{config['LOG_LEVEL']}'")
    if mode == "production":
        if config["LOG_LEVEL"].upper() == "DEBUG":
            warnings.append("DEBUG log level is not recommended in production")
        endpoint = config["ZION_ENDPOINT"]
        if endpoint and not endpoint.startswith("https://"):
            warnings.append("ZION_ENDPOINT should use https:// in production")
    return warnings


def print_configuration(config: dict[str, str]) -> None:
    mode = config["MATRIX_MODE"].lower()
    if mode not in VALID_MODES:
        mode = "development"

    print("Configuration loaded:")
    print(f"Mode: {mode}")
    # The difference between development and production is visible here.
    if mode == "production":
        print("Database: Connected to production instance")
    else:
        print("Database: Connected to local instance")
    if config["API_KEY"]:
        print("API Access: Authenticated")
    else:
        print("API Access: Not authenticated (API_KEY missing)")
    print(f"Log Level: {config['LOG_LEVEL'].upper()}")
    if config["ZION_ENDPOINT"]:
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline (ZION_ENDPOINT missing)")


def has_hardcoded_secret(api_key: str) -> bool:
    """Look for the API key value inside this very source file."""
    if len(api_key) < 6:
        return False
    try:
        with open(__file__) as source:
            return api_key in source.read()
    except OSError:
        return False


def print_security_check(
    config: dict[str, str],
    env_path: str,
    overridden: list[str],
    warnings: list[str],
) -> None:
    print("\nEnvironment security check:")

    if has_hardcoded_secret(config["API_KEY"]):
        print("[WARNING] API_KEY value is hardcoded in oracle.py")
    else:
        print("[OK] No hardcoded secrets detected")

    if not env_path:
        print("[WARNING] No .env file found (copy .env.example to .env)")
    else:
        file_values = dotenv_values(env_path)
        absent = [name for name in REQUIRED_VARS if name not in file_values]
        if absent:
            names = ", ".join(absent)
            print(f"[WARNING] .env file incomplete, missing: {names}")
        else:
            print("[OK] .env file properly configured")

    # load_dotenv() runs with override=False, so real environment variables
    # always win over the .env file.
    print("[OK] Production overrides available")
    if overridden:
        print(f"[INFO] Overridden by the environment: {', '.join(overridden)}")

    for warning in warnings:
        print(f"[WARNING] {warning}")


def main() -> None:
    # Values already present in the real environment take precedence over
    # the .env file (override=False): this is what allows production
    # overrides such as: MATRIX_MODE=production python3 oracle.py
    before = {n: os.environ[n] for n in REQUIRED_VARS if n in os.environ}
    env_path = find_dotenv()
    file_values: dict[str, str | None] = {}
    if env_path:
        try:
            load_dotenv(env_path, override=False)
            file_values = dict(dotenv_values(env_path))
        except OSError as error:
            print(f"WARNING: could not read {env_path}: {error}")
            env_path = ""
    overridden = [
        name for name, value in before.items()
        if name in file_values and file_values[name] != value
    ]

    print("ORACLE STATUS: Reading the Matrix...\n")

    config, missing = load_config()
    print_configuration(config)
    warnings = collect_warnings(config, missing)
    print_security_check(config, env_path, overridden, warnings)

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
