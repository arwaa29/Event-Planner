from app.database import dataBase
from app.auth.jwt_handler import createAccessToken
from app.modules.events.models import event_helper

# user = get_current_user(request)
async def createEvent(title: str, date: str, time: str, location: str, description: str, user: str):

    newEvent = {"title":title, "date":date,
               "time": time, "location":location,
                "description":description, "organizer":user, "attendees": []}
    result = await dataBase.Events.insert_one(newEvent)
    createdEvent = await dataBase.Events.find_one({"_id": result.inserted_id})

    token = createAccessToken({"sub":str(createdEvent["_id"])})
    return {"message": "Event Created Successfully", "token": token}

async def viewOrganizedEvent(user):
    return dataBase.Events.find({"organizer":user})

async def viewinvitedEvent(user):
    return dataBase.Events.find({"attendees.user":user})

async def deleteEvent(user,event_id):
    delete = await dataBase.Events.delete_one({"_id": event_id, "organizer":user})
    if delete.deleted_count == 1:
        return {"message": "Event Deleted Successfully"}
    else:
        return {"message": "Not authorized to delete this event or event does not exist"}

async def inviteUser(user,event_id):
    await dataBase.Events.update_one({"_id": event_id},{"$push":{"attendees":{"user": user, "status": "Not Responded"}}})