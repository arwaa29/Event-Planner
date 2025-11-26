from fastapi import APIRouter, HTTPException, status, Depends
from app.modules.events.service import createEvent , viewOrganizedEvent
from app.modules.events.schemas import CreateEvent, OrganizedEventResponse
from app.auth.dependencies import get_current_user
from typing import List

eventRouter = APIRouter(prefix="/events", tags=["Events"])

@eventRouter.post("/create")
async def creat_event_api(event_data:CreateEvent,
                           user: dict = Depends(get_current_user) #hngeb el user data kolha
                          ):
    user_id = str(user["_id"]) #bngebo mn db (hna5od mn data id bs)
    result = await createEvent(event_data, user_id)
    return result

@eventRouter.get("/organized", response_model=List[OrganizedEventResponse])
async def organized_events_api(user: dict = Depends(get_current_user)):
    user_id = str(user["_id"])
    result = await viewOrganizedEvent(user_id)
    return result



