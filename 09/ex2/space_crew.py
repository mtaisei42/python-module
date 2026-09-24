from enum import Enum
from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime


class Rank(Enum, str):
    Cadet = "cadit"
    Officer = "officer"
    Lieutenant = "lieutenant"
    Capatain = "captain"
    Commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id:str = Field(min_length=5, max_length=15)
    mission_name:str = Field(min_length=3, max_length=100)
    destination:str = Field(min_length=3, max_length=50)
    launch_date: datetime
    durarion_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status:str = Field(default="planned")
    budget_millions:float = Field(ge=1.0, le=100000.0)

    @model_validator(mode="after")
    def check(self):

        crew_experience = [name for name in self.crew if name.years_experience >= 5]

        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        elif not any(Rank.Commander == member.rank or Rank.Capatain == member.rank for member in self.crew):
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        elif self.durarion_days > 365 and len(self.crew /2) > len(crew_experience):
            raise ValueError(
                    "Long missions (> 365 days) require at least 50% "
                    "experienced crew (5+ years)"
                )

        elif not all(member.is_active == True for member in self.crew):
            raise ValueError("All crew members must be active")




def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")



    try:
        spacemission = SpaceMission.model_validate({'mission_id': 'M2024_TITAN',
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
        'budget_millions': 2208.1})

    except ValidationError as e:
        print(e)
        return

    print("Valid mission created:")
    print(f"Mission: {spacemission.mission_name}")
    print(f"ID: {spacemission.mission_id}")
    print(f"Destination: {spacemission.destination}")
    print(f"Duration: {spacemission.durarion_days} days")
    print(f"Budget: ${spacemission.budget_millions}M")
    print(f"Crew size {len(spacemission.crew)}")

    print("Crew members")
    for member in spacemission.crew:
        print(f"- {member.name} ({member.rank}) - {member.specialization}")

    print("=========================================")
    print("Expected validation error:")

    try:
        spacemission = SpaceMission.model_validate({'mission_id': 'M2024_TITAN',
        'mission_name': 'Solar Observatory Research Mission',
        'destination': 'Solar Observatory',
        'launch_date': '2024-03-30T00:00:00',
        'duration_days': 451,
        'crew': [
            {
                'member_id': 'CM001',
                'name': 'Sarah Williams',
                'rank': 'cadet',
                'age': 43,
                'specialization': 'Mission Command',
                'years_experience': 19,
                'is_active': True
            },
            {
                'member_id': 'CM002',
                'name': 'James Hernandez',
                'rank': 'cadet',
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
                'rank': 'cadet',
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
        'budget_millions': 2208.1})

    except ValidationError as e:
        print(e)
        return