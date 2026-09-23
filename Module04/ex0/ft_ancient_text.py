import sys
from typing import IO


def ft_ancient_text() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    file_name: str = sys.argv[1]

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{file_name}'")

    try:
        file: IO[str] = open(file_name, "r")
    except OSError as error:
        print(f"Error opening file '{file_name}': {error}")
        return

    try:
        content: str = file.read()
    except (OSError, UnicodeError) as error:
        print(f"Error reading file '{file_name}': {error}")
        return
    finally:
        file.close()

    print("---")
    print()
    print(content)
    print("---")
    print(f"File '{file_name}' closed.")


if __name__ == "__main__":
    ft_ancient_text()
