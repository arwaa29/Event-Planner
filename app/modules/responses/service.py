from app.database import dataBase
from bson import ObjectId

async def updateStatus(user: str ,event_id: str ,status: str):
    if status not in ["Going", "Maybe", "Not Going"]:
        return {"message": "Invalid status"}
    event_id = ObjectId(event_id)
    event = await dataBase.Events.find_one({"_id": event_id, "attendees.user": user})
    if not event:
        return {"message": "You are not invited"}

    await dataBase.Events.update_one({"_id": event_id, "attendees.user": user},
                                    {"$set": {"attendees.$.status": status}})
    return {"message": "Status updated successfully"}

async def viewAttendees(user: str, event_id: str):
    event_id = ObjectId(event_id)
    event = await dataBase.Events.find_one({"_id": event_id, "organizer": user})
    if not event :
        return {"message": "You are not authorized to view attendees"}

    return dataBase.Events.find_one("attendees", [])