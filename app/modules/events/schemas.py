from pydantic import BaseModel
from datetime import date, time

class CreateEvent(BaseModel):
        title: str
        date: date
        time: time
        location: str
        description: str


class InviteUser(BaseModel):
    event_id: str
    user: str

class EventResponse(BaseModel):
    message: str

model_config = {
    "from_attributes": True
}
