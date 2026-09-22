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
    is_acive: bool = Field(default=True)


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

        experiences = [name for name in self.crew if name.years_experience >= 5]

        if not self.mission_id.startswith("M"):
            raise ValidationError()

        elif not any(Rank.Commander == member.rank or Rank.Capatain == member.rank for member in self.crew):
            raise ValidationError()

        elif self.durarion_days > 365 and len(self.crew /2) > len(experiences):
            raise ValidationError()


        