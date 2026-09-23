from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    """Vital statistics reported by a space station."""

    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: str | None = Field(default=None, max_length=200)


def first_error_message(error: ValidationError) -> str:
    """Return the text of the first validation error.

    Errors raised by our own validators are prefixed by Pydantic with
    'Value error, '; it is removed to show only the rule that failed.
    """
    message: str = error.errors()[0]["msg"]
    return message.removeprefix("Value error, ")


def main() -> None:
    print("Space Station Data Validation")
    print("=" * 40)

    # Raw data, as it would arrive from a data stream. Pydantic converts
    # the ISO string of "last_maintenance" into a datetime by itself.
    valid_data: dict[str, Any] = {
        "station_id": "ISS001",
        "name": "International Space Station",
        "crew_size": 6,
        "power_level": 85.5,
        "oxygen_level": 92.3,
        "last_maintenance": "2024-01-15T10:00:00",
    }
    try:
        station = SpaceStation.model_validate(valid_data)
    except ValidationError as error:
        print(f"Unexpected validation error: {first_error_message(error)}")
        return

    print("Valid station created:")
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    print(f"Status: {'Operational' if station.is_operational else 'Offline'}")
    if station.notes:
        print(f"Notes: {station.notes}")

    print()
    print("=" * 40)

    # Same data, but the crew is bigger than the allowed maximum (20).
    invalid_data = {**valid_data, "station_id": "ISS002", "crew_size": 25}
    try:
        SpaceStation.model_validate(invalid_data)
    except ValidationError as error:
        print("Expected validation error:")
        print(first_error_message(error))
    else:
        print("ERROR: the invalid station was accepted")


if __name__ == "__main__":
    main()
