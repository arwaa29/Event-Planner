#when sed data from back to front ,
#this will help in converting mongoDB into JSON friendly format like response we write in schema.py

from bson import ObjectId

def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "first_name": user["first_name"],
        "last_name": user["last_name"],
        "email": user["email"],
        "username": user["username"],
        "role": user["role"],
    }