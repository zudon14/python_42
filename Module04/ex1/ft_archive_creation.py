import sys
from typing import IO


def ft_archive_creation() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    file_name: str = sys.argv[1]

    print("=== Cyber Archives Recovery & Preservation ===")
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
    print()

    transformed: str = ""
    for line in content.splitlines():
        transformed += line + "#\n"

    print("Transform data:")
    print("---")
    print()
    print(transformed)
    print("---")

    try:
        new_file: str = input("Enter new file name (or empty): ")
    except EOFError:
        print()
        new_file = ""

    if new_file == "":
        print("Not saving data.")
        return

    print(f"Saving data to '{new_file}'")

    try:
        output: IO[str] = open(new_file, "w")
    except OSError as error:
        print(f"Error opening file '{new_file}': {error}")
        print("Data not saved.")
        return

    try:
        output.write(transformed)
    except (OSError, UnicodeError) as error:
        print(f"Error writing to file '{new_file}': {error}")
        print("Data not saved.")
        return
    finally:
        output.close()

    print(f"Data saved in file '{new_file}'.")


if __name__ == "__main__":
    ft_archive_creation()
