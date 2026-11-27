from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, ValidationError, model_validator


class ContactType(str, Enum):
    Radio = "radio"
    Visual = "visual"
    Physical = "physical"
    Telepathic = "telepathic"


class AlienContact(BaseModel):
    """Validate contact fields and rules that depend on multiple fields."""

    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def check_contact(self) -> "AlienContact":
        # ValueError is collected into Pydantic's structured ValidationError.
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with AC")

        if self.contact_type == ContactType.Physical and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        if (self.contact_type == ContactType.Telepathic
                and self.witness_count < 3):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )

        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Signals stronger than 7.0 must include a received message"
            )

        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")
    contact_data: dict[str, object] = {
        "contact_id": "AC_2024_001",
        "timestamp": "2026-06-06 12:30:00",
        "location": "Area 51, Nevada",
        "contact_type": "radio",
        "signal_strength": "8.5",
        "duration_minutes": "45",
        "witness_count": "5",
        "message_received": "Greetings from Zeta Reticuli",
    }
    try:
        contact = AlienContact.model_validate(contact_data)
    except ValidationError as e:
        print(e)
        return

    print("Valid contact report:")
    print(f"ID: {contact.contact_id}")
    print(f"Type: {contact.contact_type.value}")
    print(f"Location: {contact.location}")
    print(f"Signal: {contact.signal_strength}/10")
    print(f"Duration: {contact.duration_minutes} minutes")
    print(f"Witnesses: {contact.witness_count}")
    print(f"Message: '{contact.message_received}'")

    print("\n======================================")
    print("Expected validation error:")
    try:
        AlienContact.model_validate({
            **contact_data,
            "contact_type": "telepathic",
            "witness_count": 2,
        })
    except ValidationError as e:
        print(e)


if __name__ == "__main__":
    main()
