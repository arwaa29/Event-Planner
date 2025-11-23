from app.database import dataBase
from app.auth.jwt_handler import createAccessToken

async def searchByName(title: str) -> dict:
    return await dataBase.Events.find({"title":{"$regex": title}})

async def searchByTaskDescrip(task: str) -> dict:
    return await dataBase.Events.find({"description": {"$regex": task}})

async def dateFiltering(date: str) -> dict:
    return await dataBase.Events.find({"date":{"$regex": date}})

async def userFiltering(role: str) -> dict:
    return await dataBase.Events.find({"attendees.role":{"$regex": role}})

async def combination(title = None, description = None, date = None, role = None) -> dict:
    if title:
        searchByName(title)
    if description:
        searchByTaskDescrip(description)
    if date:
        dateFiltering(date)
    if role:
        userFiltering(role)