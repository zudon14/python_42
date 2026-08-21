import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        raw = input("Enter new coordinates as floats in format 'x,y,z': ")

        parts = raw.split(",")

        if len(parts) != 3:
            print("Invalid syntax")
            continue

        values = []

        try:
            for part in parts:
                values.append(float(part.strip()))
        except ValueError:
            for part in parts:
                try:
                    float(part.strip())
                except ValueError as err:
                    print(f"Error on parameter '{part.strip()}': {err}")
                    break
            continue

        return values[0], values[1], values[2]


def distance_to_center(position: tuple[float, float, float]) -> float:
    x, y, z = position
    return math.sqrt(x ** 2 + y ** 2 + z ** 2)


def distance_between(
    first: tuple[float, float, float],
    second: tuple[float, float, float]
) -> float:
    x1, y1, z1 = first
    x2, y2, z2 = second

    return math.sqrt(
        (x2 - x1) ** 2 +
        (y2 - y1) ** 2 +
        (z2 - z1) ** 2
    )


def main() -> None:
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    first = get_player_pos()

    print(f"Got a first tuple: {first}")
    print(f"It includes: X={first[0]}, Y={first[1]}, Z={first[2]}")
    print(f"Distance to center: {round(distance_to_center(first), 4)}")

    print("Get a second set of coordinates")
    second = get_player_pos()

    print(
        "Distance between the 2 sets of coordinates: "
        f"{round(distance_between(first, second), 4)}"
    )


if __name__ == "__main__":
    main()
