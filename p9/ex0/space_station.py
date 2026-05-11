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

    stat1 = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance="2026-05-08T15:30:00",  # type: ignore
    )

    print("Valid good station created:")
    print(f"ID: {stat1.station_id}")
    print(f"Name: {stat1.name}")
    print(f"Crew: {stat1.crew_size} people")
    print(f"Power: {stat1.power_level}%")
    print(f"Oxygen: {stat1.oxygen_level}%")
    print(
        f"Status: "
        f"{'Operational' if stat1.is_operational else 'Non-operational'}"
    )

    print("========================================")

    print("NOT Valid good station created:")
    try:
        stat2 = SpaceStation(
            station_id="ISS999",
            name="Broken Station",
            crew_size=99,
            power_level=50.0,
            oxygen_level=50.0,
            last_maintenance="2026-05-08T15:30:00"  # type: ignore
        )
        print(
            f"Status: "
            f"{'Operational' if stat2.is_operational else 'Non-operational'}"
        )

    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
