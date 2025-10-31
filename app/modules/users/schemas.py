from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Signup(BaseModel):
        first_name: str
        last_name: str
        email: EmailStr
        username: str
        password: str = Field(..., min_length=6)
        role: Optional[str] = "attendee"

class Login(BaseModel):
    email: EmailStr
    username: str
    password: str

class userResponse(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: EmailStr
    username: str
    role: str

class RegisterResponse(BaseModel):
    message: str
    token: str

class LoginResponse(BaseModel):
    message: str
    token: str

model_config = {
    "from_attributes": True
}