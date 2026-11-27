from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    Cadet = "cadet"
    Officer = "officer"
    Lieutenant = "lieutenant"
    Captain = "captain"
    Commander = "commander"


class CrewMember(BaseModel):
    """Validate an individual crew member before checking mission safety."""

    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    """Validate mission data, nested crew members, and crew safety rules."""

    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def check(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        if not any(
            member.rank in (Rank.Commander, Rank.Captain)
            for member in self.crew
        ):
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        experienced_count = sum(
            member.years_experience >= 5 for member in self.crew
        )
        # Doubling the count also handles odd-sized crews without rounding.
        if self.duration_days > 365 and experienced_count * 2 < len(self.crew):
            raise ValueError(
                "Long missions (> 365 days) require at least 50% "
                "experienced crew (5+ years)"
            )

        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")

        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")

    # Pydantic turns the nested crew dictionaries into CrewMember instances.
    mission_data: dict[str, object] = {
        'mission_id': 'M2024_TITAN',
        'mission_name': 'Solar Observatory Research Mission',
        'destination': 'Solar Observatory',
        'launch_date': '2024-03-30T00:00:00',
        'duration_days': 451,
        'crew': [
            {
                'member_id': 'CM001',
                'name': 'Sarah Williams',
                'rank': 'captain',
                'age': 43,
                'specialization': 'Mission Command',
                'years_experience': 19,
                'is_active': True
            },
            {
                'member_id': 'CM002',
                'name': 'James Hernandez',
                'rank': 'captain',
                'age': 43,
                'specialization': 'Pilot',
                'years_experience': 30,
                'is_active': True
            },
            {
                'member_id': 'CM003',
                'name': 'Anna Jones',
                'rank': 'cadet',
                'age': 35,
                'specialization': 'Communications',
                'years_experience': 15,
                'is_active': True
            },
            {
                'member_id': 'CM004',
                'name': 'David Smith',
                'rank': 'commander',
                'age': 27,
                'specialization': 'Security',
                'years_experience': 15,
                'is_active': True
            },
            {
                'member_id': 'CM005',
                'name': 'Maria Jones',
                'rank': 'cadet',
                'age': 55,
                'specialization': 'Research',
                'years_experience': 30,
                'is_active': True
            }
        ],
        'mission_status': 'planned',
        'budget_millions': 2208.1,
    }
    try:
        spacemission = SpaceMission.model_validate(mission_data)
    except ValidationError as e:
        print(e)
        return

    print("Valid mission created:")
    print(f"Mission: {spacemission.mission_name}")
    print(f"ID: {spacemission.mission_id}")
    print(f"Destination: {spacemission.destination}")
    print(f"Duration: {spacemission.duration_days} days")
    print(f"Budget: ${spacemission.budget_millions}M")
    print(f"Crew size: {len(spacemission.crew)}")

    print("Crew members:")
    for member in spacemission.crew:
        print(
            f"- {member.name} ({member.rank.value}) - {member.specialization}"
        )

    print("=========================================")
    print("Expected validation error:")

    invalid_data = spacemission.model_dump()
    invalid_data['crew'] = [
        {**member.model_dump(), 'rank': Rank.Cadet}
        for member in spacemission.crew
    ]
    try:
        SpaceMission.model_validate(invalid_data)
    except ValidationError as e:
        print(e)
        return


if __name__ == "__main__":
    main()
