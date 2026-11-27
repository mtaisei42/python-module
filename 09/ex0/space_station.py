from datetime import datetime

from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    """Validate a station's vital statistics and optional notes."""

    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: str | None = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")

    # model_validate accepts raw input and converts compatible string values.
    station_data: dict[str, object] = {
        "station_id": "ISS001",
        "name": "International Space Station",
        "crew_size": "6",
        "power_level": "85.5",
        "oxygen_level": "92.3",
        "last_maintenance": "2026-06-06 12:30:00",
    }
    try:
        space_station = SpaceStation.model_validate(station_data)
    except ValidationError as e:
        print(e)
        return

    print("Valid station created:")
    print(f"ID: {space_station.station_id}")
    print(f"Name: {space_station.name}")
    print(f"Crew: {space_station.crew_size} people")
    print(f"Power: {space_station.power_level}%")
    print(f"Oxygen: {space_station.oxygen_level}%")
    status = "Operational" if space_station.is_operational else "Offline"
    print(f"Status: {status}")

    print("\n========================================")
    print("Expected validation error:")
    try:
        SpaceStation.model_validate({**station_data, "crew_size": "30"})
    except ValidationError as e:
        print(e)


if __name__ == "__main__":
    main()
