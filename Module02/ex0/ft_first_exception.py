def input_temperature(temp_str: str) -> int:
    number = int(temp_str)
    return number


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print()

    print("Input data is '25'")
    print(f"Temperature is now {input_temperature('25')}°C")
    print()

    print("Input data is 'abc'")
    try:
        input_temperature("abc")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    print()
    print("All tests completed - program didn't crash!")

test_temperature()