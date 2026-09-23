import sys
from typing import IO


def ft_stream_management() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
        return

    file_name: str = sys.argv[1]

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{file_name}'")

    try:
        file: IO[str] = open(file_name, "r")
    except OSError as error:
        print(f"[STDERR] Error opening file '{file_name}': {error}",
              file=sys.stderr)
        return

    try:
        content: str = file.read()
    except (OSError, UnicodeError) as error:
        print(f"[STDERR] Error reading file '{file_name}': {error}",
              file=sys.stderr)
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

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    new_file: str = sys.stdin.readline().rstrip("\r\n")

    if new_file == "":
        print("Not saving data.")
        return

    print(f"Saving data to '{new_file}'")

    try:
        output: IO[str] = open(new_file, "w")
    except OSError as error:
        print(f"[STDERR] Error opening file '{new_file}': {error}",
              file=sys.stderr)
        print("Data not saved.")
        return

    try:
        output.write(transformed)
    except (OSError, UnicodeError) as error:
        print(f"[STDERR] Error writing to file '{new_file}': {error}",
              file=sys.stderr)
        print("Data not saved.")
        return
    finally:
        output.close()

    print(f"Data saved in file '{new_file}'.")


if __name__ == "__main__":
    ft_stream_management()
