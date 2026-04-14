from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = AsyncIOMotorClient(MONGO_URI, tls=False)
dataBase = client['EventPlanner']

# Collections
user_collection = dataBase["users"]
events_collection = dataBase["events"]
event_attendees_collection = dataBase["event_attendees"]

# import asyncio
#  # your MongoDB database object
#
# async def print_users():
#     cursor = dataBase["users"].find()
#     async for user in cursor:
#         print(user)
#
# asyncio.run(print_users())

# import asyncio
# #  from motor.motor_asyncio import AsyncIOMotorClient
# #  import os
# # from dotenv import load_dotenv
# #
# # load_dotenv()
# #  MONGO_URI = os.getenv("MONGO_URI")
# #
# async def test_connection():
#     client = AsyncIOMotorClient(MONGO_URI, tls=False)
#     db = client["EventPlanner"]
#     try:
#         await db.command("ping")
#         print("✅ Connected successfully to local MongoDB !")
#     except Exception as e:
#         print("❌ Connection failed:", e)
#
# asyncio.run(test_connection())
