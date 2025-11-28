from fastapi import APIRouter, HTTPException, status, Depends
from app.modules.events.service import createEvent , viewOrganizedEvent, viewInvitedEvent, inviteUser, deleteEvent
from app.modules.events.schemas import CreateEvent, OrganizedEventResponse, InvitedEventResponse, InvitedUser, DeleteEvent
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

@eventRouter.get("/organized_events", response_model=List[OrganizedEventResponse])
async def organized_events_api(user: dict = Depends(get_current_user)):
    user_id = str(user["_id"])
    result = await viewOrganizedEvent(user_id)
    return result

@eventRouter.get("/invited_events" , response_model=List[InvitedEventResponse] )
async def invited_events_api(user: dict = Depends(get_current_user)):
    user_id = str(user["_id"])
    result = await viewInvitedEvent(user_id)
    return result

@eventRouter.post("/invite")
async def invite_user_api(invite_data: InvitedUser,
                          user: dict = Depends(get_current_user)):
    inviter_id = str(user["_id"])
    result = await inviteUser(invite_data, inviter_id)
    return result


@eventRouter.delete("/delete")
async def delete_event_api(delete_data: DeleteEvent,
                           user: dict = Depends(get_current_user)):
    user_id = str(user["_id"])
    event_id = delete_data.event_id
    result = await deleteEvent(event_id, user_id)
    return result

