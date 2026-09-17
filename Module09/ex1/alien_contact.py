from enum import Enum
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ValidationError, model_validator

class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"

class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)


    @model_validator(mode='after')
    def validate_business_rules(self) -> 'AlienContact':
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")

        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        if self.contact_type == ContactType.TELEPATHIC and self.witness_count < 3:
            raise ValueError("Telepathic contact requires at least 3 witnesses")

        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals should include received messages")

        return self

def main() -> None:
    print("Alien Contact Log Validation")
    print("=" * 38)

    contato_valido = AlienContact(
        contact_id="AC_2024_001",
        timestamp="2024-03-10T22:15:00",
        location="Area 51, Nevada",
        contact_type=ContactType.RADIO,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli",
    )
    print("Valid contact report:")
    print(f"ID: {contato_valido.contact_id}")
    print(f"Type: {contato_valido.contact_type.value}")
    print(f"Location: {contato_valido.location}")
    print(f"Signal: {contato_valido.signal_strength}/10")
    print(f"Duration: {contato_valido.duration_minutes} minutes")
    print(f"Witnesses: {contato_valido.witness_count}")
    print(f"Message: '{contato_valido.message_received}'")

    print()
    print("=" * 38)

    try:
        AlienContact(
            contact_id="AC_2024_002",
            timestamp="2024-03-10T23:00:00",
            location="Roswell, NM",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=6.0,
            duration_minutes=10,
            witness_count=1,  # só 1 testemunha, viola a regra 3
        )
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()