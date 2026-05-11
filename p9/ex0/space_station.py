from datetime import datetime
from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(default=None, max_length=200)


def main() -> None:

    print("Space Station Data Validation")
    print("========================================")

    good_station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance="2026-05-08T15:30:00",  # type: ignore
    )

    print("Valid good_station created:")
    print(f"ID: {good_station.station_id}")
    print(f"Name: {good_station.name}")
    print(f"Crew: {good_station.crew_size} people")
    print(f"Power: {good_station.power_level}%")
    print(f"Oxygen: {good_station.oxygen_level}%")
    print(
        "Status: "
        f"{'Operational'
            if good_station.is_operational else 'Non-operational'}"
        )

    print("========================================")

    try:
        bad_station = SpaceStation(
            station_id="ISS999",
            name="Broken Station",
            crew_size=99,
            power_level=50.0,
            oxygen_level=50.0,
            last_maintenance="2026-05-08T15:30:00"  # type: ignore
        )

    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
