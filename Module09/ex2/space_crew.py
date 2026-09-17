from enum import Enum
from datetime import datetime
from typing import List
from pydantic import BaseModel, Field, ValidationError, model_validator

class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"

class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)

class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_mission_rules(self) -> 'SpaceMission':
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        has_leadership = any(
            member.rank in (Rank.CAPTAIN, Rank.COMMANDER)
            for member in self.crew
        )
        if not has_leadership:
            raise ValueError("Mission must have at least one Commander or Captain")

        if self.duration_days > 365:
            experientes = sum(1 for member in self.crew if member.years_experience >= 5)
        if experientes < len(self.crew) / 2:
            raise ValueError("Long missions need 50% experienced crew (5+ years)")

        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")

        return self

def main() -> None:
    print("Space Mission Crew Validation")
    print("=" * 41)

    valid_mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date="2024-06-01T08:00:00",
        duration_days=900,
        budget_millions=2500.0,
        crew=[
            {"member_id": "C001", "name": "Sarah Connor", "rank": "commander",
             "age": 45, "specialization": "Mission Command", "years_experience": 20},
            {"member_id": "C002", "name": "John Smith", "rank": "lieutenant",
             "age": 34, "specialization": "Navigation", "years_experience": 8},
            {"member_id": "C003", "name": "Alice Johnson", "rank": "officer",
             "age": 29, "specialization": "Engineering", "years_experience": 6},
        ],
    )
    print("Valid mission created:")
    print(f"Mission: {valid_mission.mission_name}")
    print(f"ID: {valid_mission.mission_id}")
    print(f"Destination: {valid_mission.destination}")
    print(f"Duration: {valid_mission.duration_days} days")
    print(f"Budget: ${valid_mission.budget_millions}M")
    print(f"Crew size: {len(valid_mission.crew)}")
    print("Crew members:")
    for member in valid_mission.crew:
        print(f"- {member.name} ({member.rank.value}) - {member.specialization}")

    print()
    print("=" * 41)

    try:
        SpaceMission(
            mission_id="M2024_FAIL",
            mission_name="No Leadership Mission",
            destination="Europa",
            launch_date="2024-07-01T08:00:00",
            duration_days=100,
            budget_millions=500.0,
            crew=[
                {"member_id": "C010", "name": "Bob Rookie", "rank": "cadet",
                 "age": 22, "specialization": "General", "years_experience": 1},
            ],  # ninguém é captain/commander -> deve falhar
        )
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()