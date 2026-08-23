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

        content: str = file.read()

        print("---")
        print(content, end="")
        print("---")

        file.close()
        print(f"File '{file_name}' closed.")

    except Exception as error:
        print(f"Error opening file '{file_name}': {error}")
        return

    transformed: str = ""
    for line in content.splitlines():
        transformed += line + "#\n"

    print("Transform data:")
    print("---")
    print(transformed, end="")
    print("---")

    new_file: str = input("Enter new file name (or empty): ")

    if new_file == "":
        print("Not saving data.")
        return

    print(f"Saving data to '{new_file}'")

    try:
        output: IO[str] = open(new_file, "w")
        output.write(transformed)
        output.close()
        print(f"Data saved in file '{new_file}'.")

    except Exception as error:
        print(f"Error opening file '{new_file}': {error}")
        print("Data not saved.")


if __name__ == "__main__":
    ft_archive_creation()