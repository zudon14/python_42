def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        10 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        # mypy flags this line on purpose: it is what raises the TypeError
        "temperature: " + 25
    else:
        return


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    # Each error type caught by its own except block
    for operation in range(5):
        print(f"Testing operation {operation}...")
        try:
            garden_operations(operation)
            print("Operation completed successfully")
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
    print()

    # Several error types caught together by ONE except block (a tuple)
    print("Testing multiple error types with one try block...")
    for operation in range(4):
        print(f"Testing operation {operation}...")
        try:
            garden_operations(operation)
        except (ValueError, ZeroDivisionError,
                FileNotFoundError, TypeError) as e:
            print(f"Caught an error (handled together): {e}")
    print()

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
