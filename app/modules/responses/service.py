from app.database import dataBase, event_attendees_collection, events_collection, user_collection
from bson import ObjectId
from fastapi import HTTPException
from app.modules.responses.models import attendee_helper

async def RespondEvent( respond_data, user_id: str):
    attendee = await event_attendees_collection.find_one({
        "event_id": respond_data.event_id,
        "user_id": user_id,
        "role": "attendee"
    })

    if not attendee:
        raise HTTPException(status_code=403, detail="you aren't invited to this event ")

    # going, not going, maybe el user hy5tar fl ui
    await event_attendees_collection.update_one(
        {"event_id": respond_data.event_id, "user_id": user_id},
        {"$set": {"status": respond_data.status}}
    )

    return {"message": f"your response has been set to{respond_data.status}"}

async def viewEventAttendees(event_id: str, user_id:str):
    event = await events_collection.find_one({"_id": ObjectId(event_id)})
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    if str(event["organizer_id"]) != user_id:
        raise HTTPException(status_code=401, detail="Not authorized to view attendees")

    attendees_cursor = event_attendees_collection.find(
        {
            "event_id": event_id,
            "role": "attendee"
        }
    )

    attendees = []
    async for attendee in attendees_cursor:
        user = await user_collection.find_one({"_id": ObjectId(attendee["user_id"])})

        attendees.append(attendee_helper(attendee, user))

    return attendees

