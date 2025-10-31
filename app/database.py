from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = AsyncIOMotorClient(MONGO_URI)
dataBase = client['EventPlanner']

# Collections
user_collection = dataBase["users"]


# import motor.motor_asyncio
# import asyncio
#
# MONGO_URI = "mongodb+srv://nourtarek885_db_user:MyStrongPassword123@cluster0.wknjzi0.mongodb.net/myAppDB?retryWrites=true&w=majority&appName=Cluster0"
#
# async def test_connection():
#     client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI, tls=True, tlsAllowInvalidCertificates=True)
#     db = client["EventPlanner"]
#     try:
#         await db.command("ping")
#         print("✅ Connected successfully to MongoDB Atlas!")
#     except Exception as e:
#         print("❌ Connection failed:", e)
#
# asyncio.run(test_connection())
