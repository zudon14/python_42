
import importlib.metadata
import importlib.util
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import numpy as np
    import pandas as pd


def check_dependency(package_name: str) -> tuple[bool, str]:
    spec = importlib.util.find_spec(package_name)
    if spec is None:
        return False, "not installed"
    try:
        version = importlib.metadata.version(package_name)
    except importlib.metadata.PackageNotFoundError:
        version = "unknown"
    return True, version


def check_all_dependencies() -> dict[str, tuple[bool, str]]:
    packages = ["pandas", "numpy", "matplotlib"]
    return {name: check_dependency(name) for name in packages}


def print_dependency_report(
    results: dict[str, tuple[bool, str]]
) -> None:
    labels = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "matplotlib": "Visualization ready",
    }
    for name, (ok, version) in results.items():
        status = "[OK]" if ok else "[MISSING]"
        detail = labels.get(name, "")
        print(f"{status} {name} ({version}) - {detail}")


def print_missing_instructions() -> None:
    print("\nMissing dependencies detected.")
    print("Install with pip:")
    print("    pip install -r requirements.txt")
    print("Install with Poetry:")
    print("    poetry install")


def generate_matrix_data(size: int = 1000) -> "np.ndarray":
    import numpy as np

    rng = np.random.default_rng(seed=42)
    return rng.normal(loc=0, scale=1, size=size)


def analyze_data(raw_data: "np.ndarray") -> "pd.DataFrame":
    import pandas as pd

    df = pd.DataFrame({"value": raw_data})
    df["rolling_mean"] = df["value"].rolling(window=10).mean()
    return df


def create_visualization(
    df: "pd.DataFrame",
    output_path: str = "matrix_analysis.png",
) -> None:
    import matplotlib.pyplot as plt

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

    missing = [name for name, (ok, _) in results.items() if not ok]
    if missing:
        print_missing_instructions()
        return

    try:
        print("\nAnalyzing Matrix data...")
        raw_data = generate_matrix_data()
        print(f"Processing {len(raw_data)} data points...")

        df = analyze_data(raw_data)

        print("Generating visualization...")
        create_visualization(df)

        print("\nAnalysis complete!")
        print("Results saved to: matrix_analysis.png")
    except (ValueError, OSError) as error:
        print(f"ERROR: Analysis failed - {error}")


if __name__ == "__main__":
    main()