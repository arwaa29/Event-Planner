from app.database import dataBase, events_collection, event_attendees_collection, user_collection
from app.auth.jwt_handler import createAccessToken
from app.modules.events.models import event_helper
from bson import ObjectId
from fastapi import HTTPException

# user = get_current_user(request)
async def createEvent(event_data, user_id: str):

    newEvent = {"title":event_data.title, "date":event_data.date,
               "time": event_data.time, "location":event_data.location,
                "description":event_data.description, "organizer_id":user_id}
    result = await events_collection.insert_one(newEvent)
    event_id = result.inserted_id

    # Add organizer to attendeess collection
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


async def viewInvitedEvent(user_id: str):
    events_cursor = event_attendees_collection.find({
        "user_id": user_id,
        "role": "attendee"})

    events = []

    async for item in events_cursor:
        event = await events_collection.find_one({"_id": ObjectId(item["event_id"])})
        if event:
            events.append(event_helper(event,
                                       attendee_id=user_id,
                                       status=item.get("status", "pending")))


    return events


async def inviteUser(invite_data, inviter_id):
    #hnshof event mwgood wla la
    #hyrg3 b data bt3to kolha
    event = await events_collection.find_one({"_id": ObjectId(invite_data.event_id)})
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    if str(event["organizer_id"]) != inviter_id:
        raise HTTPException(status_code=401, detail="Not authorized to invite users")

    if not invite_data.email and not invite_data.username:
        raise HTTPException(status_code=400, detail="Email or username is required")

    check_user = {}
    if invite_data.email:
        check_user["email"] = invite_data.email
    if invite_data.username:
        check_user["username"] = invite_data.username

    #bgeeb data el user kolha
    invitee = await user_collection.find_one(check_user)
    if not invitee:
        raise HTTPException(status_code=404, detail="User not found")

    existing_invite = await event_attendees_collection.find_one({"event_id": invite_data.event_id,
                                                                 "user_id": str(invitee["_id"])})
    if existing_invite:
        raise HTTPException(status_code=400, detail="User already invited")

    await event_attendees_collection.insert_one({
        "event_id": invite_data.event_id,
        "user_id": str(invitee["_id"]),
        "role": "attendee",
        "status": "pending"
    })
    return {"message": f"{invitee['username']} has been invited successfully."}



async def deleteEvent(event_id, user_id):
    event = await events_collection.find_one({"_id": ObjectId(event_id)})
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    if str(event["organiser_id"]) != user_id:
        raise HTTPException(status_code=401, detail="Not authorized to delete this event")

    await events_collection.delete_one({"_id": ObjectId(event_id)})
    await event_attendees_collection.delete_many({"event_id": event_id})
    return {"message": "Event deleted successfully"}