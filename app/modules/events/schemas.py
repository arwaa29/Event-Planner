from pydantic import BaseModel, Field, EmailStr
from datetime import date, time
from typing import Optional

class CreateEvent(BaseModel):
        title: str
        date: date
        time: time
        location: str
        description: str




class OrganizedEventResponse(BaseModel):
    id: str
    title: str
    date: date
    time: time
    location: str
    description: str
    organizer_id: str

    class Config:
        orm_mode = True
        allow_population_by_field_name = True

class InvitedEventResponse(BaseModel):
    id: str
    title: str
    date: date
    time: time
    location: str
    description: str
    attendee_id: str
    status: str

    class Config:
        orm_mode = True
        allow_population_by_field_name = True

class InvitedUser(BaseModel):
    event_id:str
    email: Optional[EmailStr] = None
    username: Optional[str] = None

    class Config:
        orm_mode = True

class DeleteEvent(BaseModel):
    event_id:str


