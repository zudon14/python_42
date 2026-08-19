def input_temperature(temp_str: str) -> int:
    number = int(temp_str)

    if number > 40:
        raise ValueError(f"{number}°C is too hot for plants (max 40°C)")

    if number < 0:
        raise ValueError(f"{number}°C is too cold for plants (min 0°C)")

    return number


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    print()

    test_values = ["25", "abc", "100", "-50"]

    for value in test_values:
        print(f"Input data is '{value}'")

        try:
            temperature = input_temperature(value)
            print(f"Temperature is now {temperature}°C")
        except Exception as e:
            print(f"Caught input_temperature error: {e}")

        print()

    print("All tests completed - program didn't crash!")


test_temperature()
