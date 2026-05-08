from datetime import datetime
from pydantic import BaseModel, Field


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(None, max_length=200)


def main() -> None:

    try:
        ss = SpaceStation(
        station_id="ISS-001",
        name="Vabad Station",
        crew_size=25,
        power_level=10.0,
        oxygen_level=14.5,
        last_maintenance="2026-05-08T15:30:00"
    )

    except BaseException as e:
        print(f"MAL {e}")


if __name__ == "__main__":
    main()
