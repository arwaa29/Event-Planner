from fastapi import APIRouter, HTTPException, status
from app.modules.users.service import signUp, loginByEmail, loginByUsername
from app.modules.users.schemas import Signup, Login, userResponse, RegisterResponse, LoginResponse

userRouter = APIRouter(prefix="/users", tags=["Users"])

@userRouter.post("/register", response_model= RegisterResponse)
async def register(request: Signup):
    result = await signUp(request.first_name, request.last_name, request.email,
                            request.username, request.password, request.role)
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