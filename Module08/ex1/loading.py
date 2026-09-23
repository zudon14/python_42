import importlib
import importlib.metadata
import sys

# Third-party imports are guarded: a missing package must not crash the
# program before it can explain what is wrong (see check_all_dependencies).
# "type: ignore" keeps mypy quiet about missing packages or missing stubs
# (e.g. pandas ships without type information).
try:
    import matplotlib.pyplot as plt  # type: ignore
    import numpy as np  # type: ignore
    import pandas as pd  # type: ignore
except ImportError:
    pass

PACKAGES: dict[str, str] = {
    "pandas": "Data manipulation",
    "numpy": "Numerical computation",
    "matplotlib": "Visualization",
}


def check_dependency(package_name: str) -> tuple[bool, str]:
    """Return (is_importable, installed_version) for a package."""
    try:
        importlib.import_module(package_name)
    except Exception:  # ImportError, or a broken/incompatible install
        return False, "not installed"
    try:
        return True, importlib.metadata.version(package_name)
    except importlib.metadata.PackageNotFoundError:
        return True, "unknown"


def check_all_dependencies() -> dict[str, tuple[bool, str]]:
    return {name: check_dependency(name) for name in PACKAGES}


def print_dependency_report(results: dict[str, tuple[bool, str]]) -> None:
    for name, (ok, version) in results.items():
        if ok:
            print(f"[OK] {name} ({version}) - {PACKAGES[name]} ready")
        else:
            print(f"[MISSING] {name} - {version} "
                  f"({PACKAGES[name]} unavailable)")


def print_missing_instructions() -> None:
    print("\nMissing dependencies detected. Install them with:\n")
    print("pip:")
    print("    python3 -m venv matrix_env")
    print("    source matrix_env/bin/activate")
    print("    pip install -r requirements.txt\n")
    print("Poetry:")
    print("    poetry install")
    print("    poetry run python loading.py")


def sibling_path(filename: str) -> str:
    """Path of a file next to this script, whatever the current directory."""
    folder = __file__.replace("\\", "/").rpartition("/")[0]
    return f"{folder}/{filename}" if folder else filename


def read_requirements() -> dict[str, str]:
    """Parse 'name>=1.0' lines of a pip requirements file."""
    specs: dict[str, str] = {}
    try:
        with open(sibling_path("requirements.txt")) as file:
            lines = file.read().splitlines()
    except OSError:
        return specs
    for raw in lines:
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        cut = len(line)
        for index, char in enumerate(line):
            if char in "<>=!~":
                cut = index
                break
        specs[line[:cut].strip().lower()] = line[cut:].strip() or "any"
    return specs


def read_poetry_dependencies() -> dict[str, str]:
    """Parse the [tool.poetry.dependencies] table of a pyproject.toml."""
    specs: dict[str, str] = {}
    try:
        with open(sibling_path("pyproject.toml")) as file:
            lines = file.read().splitlines()
    except OSError:
        return specs
    in_dependencies = False
    for raw in lines:
        line = raw.strip()
        if line.startswith("["):
            in_dependencies = line == "[tool.poetry.dependencies]"
        elif in_dependencies and "=" in line and not line.startswith("#"):
            name, _, value = line.partition("=")
            specs[name.strip().lower()] = value.strip().strip("\"'")
    return specs


def detect_environment() -> str:
    """Best-effort guess of who manages the current environment."""
    if "pypoetry" in sys.prefix.lower():
        return "Poetry-managed virtual environment"
    if sys.prefix != sys.base_prefix:
        return "pip virtual environment (venv)"
    return "global environment (pip)"


def compare_package_managers(
    installed: dict[str, tuple[bool, str]]
) -> None:
    """Show installed versions next to what pip and Poetry declare."""
    pip_specs = read_requirements()
    poetry_specs = read_poetry_dependencies()

    print("\nPackage manager comparison:")
    print(f"Current environment: {detect_environment()}\n")
    print(f"{'Package':<12}{'Installed':<12}{'pip':<12}{'Poetry'}")
    for name, (_, version) in installed.items():
        pip_spec = pip_specs.get(name, "n/a")
        poetry_spec = poetry_specs.get(name, "n/a")
        print(f"{name:<12}{version:<12}{pip_spec:<12}{poetry_spec}")

    print("\npip    : reads requirements.txt and installs into the active")
    print("         environment. No lock file: two installs on different")
    print("         days can end up with different versions.")
    print("         -> pip install -r requirements.txt")
    print("Poetry : reads pyproject.toml, resolves the whole dependency")
    print("         tree, pins it in poetry.lock and manages its own")
    print("         virtual environment.")
    print("         -> poetry install && poetry run python loading.py")


def generate_matrix_data(size: int = 1000) -> "np.ndarray":
    rng = np.random.default_rng(seed=42)
    return rng.normal(loc=0, scale=1, size=size)


def analyze_data(raw_data: "np.ndarray") -> "pd.DataFrame":
    df = pd.DataFrame({"value": raw_data})
    df["rolling_mean"] = df["value"].rolling(window=10).mean()
    return df


def create_visualization(
    df: "pd.DataFrame", output_path: str = "matrix_analysis.png"
) -> None:
    plt.figure(figsize=(10, 6))
    plt.plot(df["value"], label="raw", alpha=0.5)
    plt.plot(df["rolling_mean"], label="rolling mean")
    plt.legend()
    plt.title("Matrix Data Analysis")
    plt.savefig(output_path)
    plt.close()


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    results = check_all_dependencies()
    print_dependency_report(results)

    if not all(ok for ok, _ in results.values()):
        print_missing_instructions()
        sys.exit(1)

    output_path = "matrix_analysis.png"
    try:
        print("\nAnalyzing Matrix data...")
        raw_data = generate_matrix_data()
        print(f"Processing {len(raw_data)} data points...")

        df = analyze_data(raw_data)

        print("Generating visualization...")
        create_visualization(df, output_path)

        print("\nAnalysis complete!")
        print(f"Results saved to: {output_path}")
    except (ValueError, OSError) as error:
        print(f"ERROR: Analysis failed - {error}")
        sys.exit(1)

    compare_package_managers(results)


if __name__ == "__main__":
    main()
