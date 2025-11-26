from app.database import dataBase, events_collection, event_attendees_collection
from app.auth.jwt_handler import createAccessToken
from app.modules.events.models import event_helper
from bson import ObjectId

# user = get_current_user(request)
async def createEvent(event_data, user_id: str):

    newEvent = {"title":event_data.title, "date":event_data.date,
               "time": event_data.time, "location":event_data.location,
                "description":event_data.description, "organizer_id":user_id}
    result = await events_collection.insert_one(newEvent)
    event_id = result.inserted_id

    # Add organizer to attendees collection
    await event_attendees_collection.insert_one({
        "event_id": str(event_id),
        "user_id": user_id,
        "role": "organizer",
        "status": "going"
    })

    created_event = await events_collection.find_one({"_id": event_id})

    return {
        "message": "Event created successfully",
        "event": created_event
    }



async def viewOrganizedEvent(user_id: str):
    #we will get all events that this user is an organizer in it
    events_cursor = event_attendees_collection.find({
        "user_id": user_id,
        "role": "organizer"})

    events = []

    #hyrga3 cursor object so we will loop on it to read
    async for item in events_cursor:
        event = await events_collection.find_one({"_id": ObjectId(item["event_id"])})
        if event:
            events.append(event_helper(event))

    return events


async def viewinvitedEvent(user_id: str):
    events_cursor = event_attendees_collection.find({
        "user_id": user_id,
        "role": "attendee"})

    events = []

    async for item in events_cursor:
        event = await events_collection.find_one({"_id": ObjectId(item["event_id"])})
        if event:
            events.append(event_helper(event))

    return events

async def deleteEvent(user,event_id):
    delete = await dataBase.Events.delete_one({"_id": event_id, "organizer":user})
    if delete.deleted_count == 1:
        return {"message": "Event Deleted Successfully"}
    else:
        return {"message": "Not authorized to delete this event or event does not exist"}

async def inviteUser(user,event_id):
    await dataBase.Events.update_one({"_id": event_id},{"$push":{"attendees":{"user": user, "status": "Not Responded"}}})