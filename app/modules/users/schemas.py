from pydantic import BaseModel, EmailStr

class Signup(BaseModel):
        first_name: str
        last_name: str
        email: EmailStr
        username: str
        password: str
        confirm_password: str
        role: str

class Login(BaseModel):
    email: EmailStr
    username: str
    password: str