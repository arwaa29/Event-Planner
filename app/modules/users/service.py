from app.database import dataBase, user_collection
from passlib.context import CryptContext
from app.auth.jwt_handler import createAccessToken
from app.modules.users.models import user_helper
from bson import ObjectId
from typing import Optional

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

async def signUp(first_name: str, last_name: str, email: str, username: str, password: str):
    user_exit = await user_collection.find_one({"email": email})
    if user_exit:
        return {"message": "Email already exists"}

    user_exit = await user_collection.find_one({"username": username})
    if user_exit:
        return {"message": "Username already exists"}

    print(password)

    hashed_pass = pwd_context.hash(password)
    newUser = {"email":email, "first_name":first_name,
               "last_name":last_name, "username":username,
               "password":hashed_pass, "role": None}
    result = await user_collection.insert_one(newUser)
    createdUser = await user_collection.find_one({"_id": result.inserted_id})

    token = createAccessToken({"sub":str(createdUser["_id"])})
    return {"message": "User registered successfully", "token": token}

async def loginByEmail(email: str, password: str):
    user = await user_collection.find_one({"email": email})
    if not user:
        return {"message": "Invalid credentials"}
    if not pwd_context.verify(password, user["password"]):
        return {"message": "Invalid credentials"}
    token = createAccessToken({"sub":str(user["_id"])})
    userData = user_helper(user)
    return {"message": "Logged in successfully", "user":userData, "token": token}

async def loginByUsername(username: str, password: str):
    user = await user_collection.find_one({"username": username})
    if not user:
        return {"message": "Invalid credentials"}
    if not pwd_context.verify(password, user["password"]):
        return {"message": "Invalid credentials"}
    token = createAccessToken({"sub":str(user["_id"])})
    userData = user_helper(user)
    return {"message": "Logged in successfully", "user":userData, "token": token}

async def loginByToken(user_id: str):
    user = await user_collection.find_one({"_id": ObjectId(user_id)})
    if user:
        userData = user_helper(user)
        return {"message": "Logged in successfully", "user": userData}
    else:
        return {"message": "Token expired or invalid"}