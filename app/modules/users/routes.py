from fastapi import APIRouter, HTTPException, status, Depends
from app.modules.users.service import signUp, loginByEmail, loginByUsername, loginByToken
from app.modules.users.schemas import Signup, Login, userResponse, RegisterResponse, LoginResponse
from app.auth.dependencies import get_current_user

userRouter = APIRouter(prefix="/users", tags=["Users"])

@userRouter.post("/register", response_model= RegisterResponse)
async def register(request: Signup):
    result = await signUp(request.first_name, request.last_name, request.email,
                            request.username, request.password)
    if "token" not in result:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result["message"])
    return result

@userRouter.post("/login", response_model= LoginResponse)
async def login(request: Login):
    if request.email:
        result = await loginByEmail(request.email, request.password)
    elif request.username:
        result = await loginByUsername(request.username, request.password)
    else:
        raise HTTPException(status_code=400, detail="Email or username is required")

    if "token" not in result:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=result["message"])
    return result

@userRouter.post("/login/token")
async def login_by_token_api(user: dict = Depends(get_current_user)):
    user_id = str(user["_id"])
    result = await loginByToken(user_id)
    return result
