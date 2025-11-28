from fastapi import APIRouter, Depends
from typing import List
from app.auth.dependencies import get_current_user
from app.modules.search.service import search_events
from app.modules.search.schemas import EventSearch
from app.modules.events.schemas import OrganizedEventResponse

searchRouter = APIRouter(prefix="/search", tags=["Search"])

@searchRouter.post("/searchEvent", response_model=List[OrganizedEventResponse])
async def search_events_api(search_data: EventSearch, user: dict = Depends(get_current_user)):
    user_id = str(user["_id"])
    events = await search_events(user_id, search_data.keyword, search_data.date, search_data.role)
    return events
