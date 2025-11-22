from app.database import dataBase
from app.auth.jwt_handler import createAccessToken
from app.modules.events.models import event_helper
from datetime import datetime


async def createEvent(title: str, location: str, description: str):
    dt = datetime.now()

    newEvent = {"title":title, "date":dt.strftime("%Y-%m-%d"),
               "time":dt.strftime("%H:%M:%S"), "location":location,
                "description":description}
    result = await dataBase.Events.insert_one(newEvent)
    createdEvent = await dataBase.Events.find_one({"_id": result.inserted_id})

    token = createAccessToken({"sub":str(createdEvent["_id"])})
    return {"message": "Event Created Successfully", "token": token}