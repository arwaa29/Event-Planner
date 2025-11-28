from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = AsyncIOMotorClient(MONGO_URI)
dataBase = client['EventPlanner']

# Collections
user_collection = dataBase["users"]
events_collection = dataBase["events"]
event_attendees_collection = dataBase["event_attendees"]


# import asyncio
# from motor.motor_asyncio import AsyncIOMotorClient
# import os
# from dotenv import load_dotenv
#
# load_dotenv()
# MONGO_URI = os.getenv("MONGO_URI")
#
# async def test_connection():
#     client = AsyncIOMotorClient(MONGO_URI, tls=True)
#     db = client["EventPlanner"]
#     try:
#         await db.command("ping")
#         print("✅ Connected successfully to MongoDB Atlas!")
#     except Exception as e:
#         print("❌ Connection failed:", e)
#
# asyncio.run(test_connection())
