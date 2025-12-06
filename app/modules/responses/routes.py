from fastapi import APIRouter , HTTPException, status, Depends
from app.modules.responses.service import RespondEvent, viewEventAttendees
from app.modules.responses.schemas import InvitationResponse, AttendeesList, AttendeesResponse
from app.auth.dependencies import get_current_user
from typing import List

responseRouter = APIRouter(prefix="/responses", tags=["Responses"])

@responseRouter.put("/status")
async def satus_api(respond_data: InvitationResponse,
                    user: dict = Depends(get_current_user)):
    user_id = str(user["_id"])
    result = await RespondEvent(respond_data, user_id)
    return result

@responseRouter.post("/attendees", response_model=List[AttendeesResponse])
async def atendees_api(attendee_data: AttendeesList,
                       user:dict = Depends(get_current_user)):
    user_id = str(user["_id"])
    event_id = attendee_data.event_id
    result = await viewEventAttendees(event_id, user_id)
    return result
