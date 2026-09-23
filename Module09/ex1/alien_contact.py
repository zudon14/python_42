from datetime import datetime
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field, ValidationError, model_validator


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    """A report of alien contact, checked by field and business rules."""

    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def validate_business_rules(self) -> "AlienContact":
        # Runs after every field passed its own validation, so we can
        # compare several fields with each other.
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")

        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        if self.contact_type == ContactType.TELEPATHIC:
            if self.witness_count < 3:
                raise ValueError(
                    "Telepathic contact requires at least 3 witnesses"
                )

        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals should include received messages")

        return self  # a model_validator(mode="after") must return self


def first_error_message(error: ValidationError) -> str:
    """Return the text of the first validation error.

    Errors raised by our own validators are prefixed by Pydantic with
    'Value error, '; it is removed to show only the rule that failed.
    """
    message: str = error.errors()[0]["msg"]
    return message.removeprefix("Value error, ")


def main() -> None:
    print("Alien Contact Log Validation")
    print("=" * 38)

    # Raw data: the string timestamp and the "radio" string are converted
    # by Pydantic into a datetime and a ContactType member.
    valid_data: dict[str, Any] = {
        "contact_id": "AC_2024_001",
        "timestamp": "2024-03-10T22:15:00",
        "location": "Area 51, Nevada",
        "contact_type": "radio",
        "signal_strength": 8.5,
        "duration_minutes": 45,
        "witness_count": 5,
        "message_received": "Greetings from Zeta Reticuli",
    }
    try:
        contact = AlienContact.model_validate(valid_data)
    except ValidationError as error:
        print(f"Unexpected validation error: {first_error_message(error)}")
        return

    print("Valid contact report:")
    print(f"ID: {contact.contact_id}")
    print(f"Type: {contact.contact_type.value}")
    print(f"Location: {contact.location}")
    print(f"Signal: {contact.signal_strength}/10")
    print(f"Duration: {contact.duration_minutes} minutes")
    print(f"Witnesses: {contact.witness_count}")
    if contact.message_received:
        print(f"Message: '{contact.message_received}'")

    print()
    print("=" * 38)

    # Telepathic contact with a single witness: breaks a business rule.
    invalid_data: dict[str, Any] = {
        "contact_id": "AC_2024_002",
        "timestamp": "2024-03-10T23:00:00",
        "location": "Roswell, NM",
        "contact_type": "telepathic",
        "signal_strength": 6.0,
        "duration_minutes": 10,
        "witness_count": 1,
    }
    try:
        AlienContact.model_validate(invalid_data)
    except ValidationError as error:
        print("Expected validation error:")
        print(first_error_message(error))
    else:
        print("ERROR: the invalid contact report was accepted")


if __name__ == "__main__":
    main()
