import bcrypt
from app.modules.users.models import userTable

class userManagement:

    # All classes have a built-in method called __init__(), which is always executed when the class is being initiated.
    # Without self, Python would not know which object's properties you want to access

    # signup
    async def signUp(self, firstName, lastName, email, username, password, confirmedPass, role):
        if await userTable.find_one({"email": email}):
            return {"error": "User Already Exists"}

        if password != confirmedPass:
            return {"error": "Password Mismatch"}

        if await userTable.find_one({"username": username}):
            return {"error": "Username Already Exists"}

        passwo = bcrypt.hashpw(password.encode("utf8"), bcrypt.gensalt()).decode("utf8")
        user = {
            "first_name": firstName,
            "last_name": lastName ,
            "email": email,
            "username": username,
            "password": passwo,
            "role": role
        }
        await userTable.insert_one(user)
        return {"message": "Sign Up Successfully!"}

    # login email
    async def loginByEmail(self, email, password):
        user = await userTable.find_one({"email": email})
        check = user["password"].encode("utf8")
        if user and bcrypt.checkpw(password.encode("utf8"), check):
            return {"message": "Logged In"}
        else:
            return {"error": "Login Failed"}

    # login username
    async def loginByUsername(self, username, password):
        user = await userTable.find_one({"username": username})
        check = user["password"].encode("utf8")
        if user and bcrypt.checkpw(password.encode("utf8"), check):
            return {"message": "Logged In"}
        else:
            return {"error": "Login Failed"}

userManagement = userManagement()