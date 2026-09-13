import sys
import os
import site


def is_in_venv() -> bool:
    return sys.prefix != sys.base_prefix


def get_venv_name() -> str:
    env_path = os.environ.get("VIRTUAL_ENV", sys.prefix)
    return os.path.basename(os.path.normpath(env_path))


def get_site_packages_path() -> str:
    paths = site.getsitepackages()
    return paths[0] if paths else "unknown"


def show_status_outside_venv() -> None:
    print("MATRIX STATUS: You're still plugged in\n")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected\n")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate  # On Unix")
    print("matrix_env\\Scripts\\activate   # On Windows\n")
    print("Then run this program again.")


def show_status_inside_venv() -> None:
    name = get_venv_name()
    packages_path = get_site_packages_path()

    print("MATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {name}")
    print(f"Environment Path: {sys.prefix}\n")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.\n")
    print("Package installation path:")
    print(packages_path)


def main() -> None:
    try:
        if is_in_venv():
            show_status_inside_venv()
        else:
            show_status_outside_venv()
    except OSError as error:
        print(f"ERROR: Could not read environment information: {error}")


if __name__ == "__main__":
    main()