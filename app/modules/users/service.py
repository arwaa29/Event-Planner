import bcrypt
from app.modules.users.models import userTable
idCounter = 0

class userManagement:

    # All classes have a built-in method called __init__(), which is always executed when the class is being initiated.
    # Without self, Python would not know which object's properties you want to access

    # signup
    async def signUp(self, firstName, lastName, email, username, password, confirmedPass, role):
        if await userTable.find_one({"email": email}):
            return "User Already Exists"

        if password != confirmedPass:
            return "Password Mismatch"

        if await userTable.find_one({"username": username}):
            return "Username Already Exists"

        global idCounter
        passwo = bcrypt.hashpw(password.encode("utf8"), bcrypt.gensalt())
        user = {
            "_id": idCounter,
            "First Name": firstName,
            "Last Name": lastName ,
            "email": email,
            "username": username,
            "password": passwo,
            "Confirmed pass": confirmedPass,
            "role": role
        }
        await userTable.insert_one(user)
        idCounter += 1
        return "Sign Up Successfully!"

    # login email
    async def loginByEmail(self, email, password):
        user = await userTable.find_one({"email": email})
        check = user["password"].encode("utf8")
        if await user and bcrypt.checkpw(password.encode("utf8"), check):
            return "Logged In"
        else:
            return "Login Failed"

    # login username
    async def loginByUsername(self, username, password):
        user = await userTable.find_one({"username": username})
        check = user["password"].encode("utf8")
        if await user and bcrypt.checkpw(password.encode("utf8"), check):
            return "Logged In"
        else:
            return "Login Failed"

userManagement = userManagement()

if "@" in userStr:
    userManagement.loginByEmail(userStr, password)
else:
    userManagement.loginByUsername(userStr, password)