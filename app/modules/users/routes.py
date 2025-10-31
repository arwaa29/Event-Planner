from fastapi import APIRouter
from app.modules.users.service import userManagement
from app.modules.users.schemas import Signup, Login

userRouter = APIRouter(prefix="/users", tags=["Users"])

@userRouter.post("/signup")
async def signup(User: Signup):
    await userManagement.signUp(User.first_name, User.last_name, User.email, User.username, User.password, User.confirmedPass, User.role)

@userRouter.post("/login")
async def login(User: Login):
    if "@" in User.user:
        await userManagement.loginByEmail(User.email, User.password)
    else:
        await userManagement.loginByUsername(User.username, User.password)
