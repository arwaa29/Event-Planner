from pydantic import BaseModel, Field
from datetime import date, time

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
    id: str = Field(..., alias="_id")
    title: str
    date: date
    time: time
    location: str
    description: str
    attendee_id: str

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


