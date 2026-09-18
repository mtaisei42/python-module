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
    duration
