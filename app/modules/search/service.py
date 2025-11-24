from app.database import dataBase
from app.auth.jwt_handler import createAccessToken

async def searchByName(title: str):
    return await dataBase.Events.find({"title":{"$regex": title, "$options": "i"}}).to_list(length=None)

async def searchByTaskDescrip(task: str):
    return await dataBase.Events.find({"description": {"$regex": task, "$options": "i"}}).to_list(length=None)

async def dateFiltering(date: str):
    return await dataBase.Events.find({"date":{"$regex": date, "$options": "i"}}).to_list(length=None)

async def userFiltering(role: str):
    return await dataBase.Events.find({"attendees.role":role}).to_list(length=None)

async def combination(title = None, description = None, date = None, role = None):

    results = []

    if title:
        results.append(await searchByName(title))
    if description:
        results.append(await searchByTaskDescrip(description))
    if date:
        results.append(await dateFiltering(date))
    if role:
        results.append(await userFiltering(role))