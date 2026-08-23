from typing import Tuple


def secure_archive(filename: str, mode: str = "r",
                    content: str = "") -> Tuple[bool, str]:
    try:
        if mode == "w":
            with open(filename, "w") as archive:
                archive.write(content)
            return (True, "Content successfully written to file")
        else:
            with open(filename, "r") as archive:
                data: str = archive.read()
            return (True, data)

    except OSError as error:
        return (False, str(error))


if __name__ == "__main__":
    print("=== Cyber Archives Security ===\n")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))
    print()

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))
    print()

    print("Using 'secure_archive' to read from a regular file:")
    result = secure_archive("ancient_fragment.txt")
    print(result)
    print()

    print("Using 'secure_archive' to write previous content to a new file:")
    if result[0]:
        print(secure_archive("new_vault_file.txt", "w", result[1]))
    else:
        print("Skipping write: previous read failed.") 