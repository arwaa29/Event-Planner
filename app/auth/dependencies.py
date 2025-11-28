from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.auth.jwt_handler import verifyAccessToken
from app.database import dataBase
from bson import ObjectId


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/users/login")


async def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    Extracts the user from the JWT token, validates it,
    and returns the full user document from MongoDB.
    """

    #Validate Token
    payload = verifyAccessToken(token)

    if not payload or "sub" not in payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    #hn7tago 3shan el event
    #get user id stored in token
    user_id = payload["sub"]  # user ID inside the token

    #Fetch user from DB
    #fetch user using user id that we got from token
    user = await dataBase.users.find_one({"_id": ObjectId(user_id)})

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return user    # return all user data to routes
