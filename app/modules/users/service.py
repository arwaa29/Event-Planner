from app.database import dataBase
from passlib.context import CryptContext
from app.auth.jwt_handler import createAccessToken
from app.modules.users.models import user_helper

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def signUp(first_name: str, last_name: str, email: str, username: str, password: str,role: str):
    user_exit = await dataBase.users.findone({"email": email})
    if user_exit:
        return {"message": "Email already exists"}

    user_exit = await dataBase.users.find_one({"username": username})
    if user_exit:
        return {"message": "Username already exists"}

    hashed_pass = pwd_context.hash(password)
    newUser = {"email":email, "first_name":first_name,
               "last_name":last_name, "username":username,
               "password":hashed_pass, "role":role}
    result = await dataBase.users.insert_one(newUser)
    createdUser = await dataBase.users.find_one({"_id": result.inserted_id})

    token = createAccessToken({"sub":str(createdUser["_id"])})
    return {"message": "User registered successfully", "token": token}

async def loginByEmail(email: str, password: str):
    user = await dataBase.users.find_one({"email": email})
    if not user:
        return {"message": "Invalid credentials"}
    if not pwd_context.verify(password, user["password"]):
        return {"message": "Invalid credentials"}
    token = createAccessToken({"sub":str(user["_id"])})
    userData = user_helper(user)
    return {"message": "Logged in successfully", "user":userData, "token": token}

async def loginByUsername(username: str, password: str):
    user = await dataBase.users.find_one({"username": username})
    if not user:
        return {"message": "Invalid credentials"}
    if not pwd_context.verify(password, user["password"]):
        return {"message": "Invalid credentials"}
    token = createAccessToken({"sub":str(user["_id"])})
    userData = user_helper(user)
    return {"message": "Logged in successfully", "user":userData, "token": token}