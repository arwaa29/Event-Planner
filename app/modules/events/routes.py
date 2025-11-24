from fastapi import APIRouter, HTTPException, status, Depends
from app.modules.events.service import createEvent
from app.modules.events.schemas import CreateEvent
from app.auth.dependencies import get_current_user

eventRouter = APIRouter(prefix="/events", tags=["Events"])

@eventRouter.post("/create")
async def creat_event_api(event_data:CreateEvent,
                           user: dict = Depends(get_current_user) #hngeb el user data kolha
                          ):
    user_id = str(user["_id"]) #bngebo mn db (hna5od mn data id bs)
    result = await createEvent(event_data, user_id)
    return result


