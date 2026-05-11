from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from enum import Enum
import json


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def contact_validator(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError('Contact ID must start with "AC"')
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError('Physical contact reports must be verified')
        if (
            self.contact_type == ContactType.TELEPATHIC
            and self.witness_count < 3
        ):
            raise ValueError(
                'Telepathic contact requires at least 3 witnesses'
            )
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                'Strong signals (> 7.0) should include received messages'
            )
        return self


def main() -> None:

    ac_path = ("../generated_data/alien_contacts.json")

    with open(ac_path, "r") as f:
        data = json.load(f)
    for entry in data:
        print("Alien Contact Log Validation")
        try:
            contact = AlienContact(**entry)
            print("======================================")
            print("Valid contact report:")
            print(f"ID: {contact.contact_id}")
            print(f"Type: {contact.contact_type.value}")
            print(f"Location: {contact.location}")
            print(f"Signal: {contact.signal_strength}/10")
            print(f"Duration: {contact.duration_minutes}")
            print(f"Witnesses: {contact.witness_count}")
            print(f"Message: {contact.message_received or 'None'}")
            print()
            print("======================================")
            print()

        except ValidationError as e:
            print("Expected validation error:")
            print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
