from enum import Enum
from pydantic import BaseModel, ValidationError, Field, model_validator
from datetime import datetime


class ContactType(str, Enum):
    Radio ="radio"
    Visual = "visual"
    Physical = "physical"
    Telepathic = "telepathic"

class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_receive: str | None = Field(max_length=500)
    is_varified: bool = Field(default=False)

    @model_validator(mode='after')
    def check_contact(self):
        if ContactType.Physical == self.contact_type and not self.is_varified:
            raise ValidationError("Physical contact reports must be verified")

        elif not self.contact_id.startswith("AC"):
            raise ValidationError("Contact ID must start with AC")

        elif ContactType.Telepathic == self.contact_type and self.witness_count < 3:
            raise ValidationError("Telepathic contact requires at least 3 witnesses")

        elif self.signal_strength > 7.0 and not self.message_receive:
            raise ValidationError("Signals stronger than 7.0 must include a received message")

        return self

def main() -> None:

    print("Alien Contact Log Vallidation")
    print("======================================")
    try:
        contact = AlienContact(contact_id="AC_2024_001",timestamp="2026-06-06 12:30:00",
            location="Area  51, Nevada", contact_type="radio", signal_strength="8.5",
            duration_minutes="45", witness_count="5",
            message_receive="Greetings from Zeta Reticuli")
    except ValidationError as e:
        print(e)
        return

    print("Valid Contact Log Validation")
    print(f"ID: {contact.contact_id}")
    print(f"Type: {contact.contact_type}")
    print(f"Location: {contact.location}")
    print(f"Signal: {contact.signal_strength}/10")
    print(f"Duration: {contact.duration_minutes} minitus")
    print(f"Witnesses: {contact.witness_count}")
    print(f"Message: '{contact.message_receive}'")

    print("\n======================================")
    print("Expected validation error:")
    try:
        contact = AlienContact(contact_id="AC_2024_001",timestamp="2026-06-06 12:30:00",
            location="Area  51, Nevada", contact_type="radio", signal_strength="8.5",
            duration_minutes="45", witness_count="0",
            message_receive="Greetings from Zeta Reticuli")
    except ValidationError as e:
        print(e)


if __name__ == "__main__":
    main()
