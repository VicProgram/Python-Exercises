from pydantic import BaseModel, Field
from datetime import datetime
from Enum import enum


def main() -> None:
    class SpaceStation(BaseModel):
        contact_id: str = Field(..., min)
        timestamp: datetime
        location: str
        contact_type: enum
        signal_strength: float
        duration_minutes: int
        witness_count: int
        message_recieved: str | None = None
        is_verified: bool = False


if __name__ == "__main__":
    main()
