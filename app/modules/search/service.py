from typing import Optional
from app.database import events_collection, event_attendees_collection
from app.modules.events.models import event_helper
from bson import ObjectId

async def search_events(
    user_id: str,
    keyword: Optional[str] = None,
    date: Optional[str] = None,
    role: Optional[str] = None
):
    events = []

    if role == "organizer":
        query = {"organizer_id": user_id}
        if keyword:
            query["title"] = {"$regex": keyword, "$options": "i"}
        if date:
            query["date"] = date
        cursor = events_collection.find(query)

        async for event in cursor:
            events.append(event_helper(event))

    elif role == "attendee":

        attendee_cursor = event_attendees_collection.find({
            "user_id": user_id,
            "role": "attendee"
        })

        async for item in attendee_cursor:
            event = await events_collection.find_one({"_id": ObjectId(item["event_id"])})
            if event:

                if keyword and keyword.lower() not in event["title"].lower():
                    continue
                if date and event["date"] != date:
                    continue
                events.append(event_helper(event))

    else:
        #lw user 3ady
        organizer_cursor = events_collection.find({"organizer_id": user_id})
        async for event in organizer_cursor:
            if keyword and keyword.lower() not in event["title"].lower():
                continue
            if date and event["date"] != date:
                continue
            events.append(event_helper(event))

        attendee_cursor = event_attendees_collection.find({"user_id": user_id, "role": "attendee"})
        async for item in attendee_cursor:
            event = await events_collection.find_one({"_id": ObjectId(item["event_id"])})
            if event:
                if keyword and keyword.lower() not in event["title"].lower():
                    continue
                if date and event["date"] != date:
                    continue
                events.append(event_helper(event))

    return events
