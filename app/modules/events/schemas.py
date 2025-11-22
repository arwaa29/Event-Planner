from pydantic import BaseModel

class CreateEvent(BaseModel):
        title: str
        date: str
        time: str
        location: str
        description: str
        organizer: str
        attendees: list[dict]

class InviteUser(BaseModel):
    event_id: str
    user: str

class EventResponse(BaseModel):
    message: str

model_config = {
    "from_attributes": True
}
