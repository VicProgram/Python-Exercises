from enum import Enum
from pydantic import BaseModel, Field, model_validator
from datetime import datetime
import json


class CrewRank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: CrewRank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: list[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def mission_validator(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')

        valid_ranks = [CrewRank.COMMANDER, CrewRank.CAPTAIN]
        has_leader = any(m.rank in valid_ranks for m in self.crew)

        if not has_leader:
            raise ValueError("Must have at least one Commander or Captain")

        if self.duration_days > 365:
            total_exp = sum(1 for m in self.crew if m.years_experience >= 5)

            if total_exp < len(self.crew) / 2:
                raise ValueError(
                    "Long missions (> 365 days) need 50% experienced crew "
                    "(5+ years)"
                )
        if not all(m.is_active for m in self.crew):
            raise ValueError("All crew members must be active")

        return self


def main() -> None:
    ms_path = ("../generated_data/space_missions.json")

    with open(ms_path, "r") as f:
        data = json.load(f)
        print("Space Mission Crew Validation")
        for entry in data:
            try:
                mission = SpaceMission(**entry)
                print("=========================================")
                print("Valid mission created:")
                print(f"Mission: {mission.mission_name}")
                print(f"ID: {mission.mission_id}")
                print(f"Destination: {mission.destination}")
                print(f"Duration: {mission.duration_days}days")
                print(f"Budget: {mission.budget_millions}")
                print(f"Crew size: {len(mission.crew)}")
                print("Crew members:")
                for member in mission.crew:
                    print(
                        f"- {member.name} ({member.rank.value}) - "
                        f"{member.specialization}"
                    )
                print()
                print("=========================================")

            except (ValueError) as e:
                print("Expected validation error:")
                print({e})


if __name__ == "__main__":
    main()
