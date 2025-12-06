from pydantic import BaseModel
from typing import Literal

class InvitationResponse(BaseModel):
    event_id: str
    status: Literal["going", "not going", "maybe"]

    class Config:
        orm_mode = True


class AttendeesList(BaseModel):
    event_id: str

class AttendeesResponse(BaseModel):
    username: str
    status: str