from pydantic import BaseModel, Field, ValidationError
from datetime import datetime

class SpaceStation(BaseModel):
    station_id: str = Field(min_lengh=3, max_lengh=10)
    name: str = Field(min_lengh=1, max_lengh=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: str | None = Field(default=None, max_lengh=200)


def main() -> None:

    print("Space Station Data Validation")
    print("========================================")

    try:
        space_station = SpaceStation(station_id="ISS001",
            name="International Space Station", crew_size="6",
            power_level="85.5", oxygen_level="92.3", is_operational="Ture")
    except ValidationError as e:
        print(e)

    print("Valid station created:")
    print(f"ID: {space_station.station_id}")
    print(f"Name: {space_station.name}")
    print(f"Crew: {space_station.crew_size}")
    print(f"Power: {space_station.power_level}")
    print(f"Oxygen: {space_station.oxygen_level}")
    print(f"Status: {space_station.is_operational}")

    print("\n========================================")
    print("")
