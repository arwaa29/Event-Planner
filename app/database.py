import pymongo
import bcrypt

client = pymongo.MongoClient("mongodb+srv://nourtarek885_db_user:MyStrongPassword123@cluster0.wknjzi0.mongodb.net/myAppDB?retryWrites=true&w=majority&appName=Cluster0")

dataBase = client['EventPlanner']
userTable = dataBase["user"]
eventTable = dataBase["event"]
idCounter = 0

class userManagement:

    # All classes have a built-in method called __init__(), which is always executed when the class is being initiated.
    # Without self, Python would not know which object's properties you want to access

    # signup
    def signUp(self, name, email, username, password):
        if userTable.find_one({"email": email}):
            print("User Already Exists")
            return
        global idCounter
        user = {"_id": idCounter, "name": name, "email": email, "username": username, "password": bcrypt.hashpw(password.encode("utf8"), bcrypt.gensalt())}
        userTable.insert_one(user)
        idCounter += 1
        print("Sign Up Successfully!")

    # login email
    def loginByEmail(self, email, password):
        if userTable.find_one({"email": email}):
            print("Logged In")
        else:
            print("Login Failed")

    # login username
    def loginByUsername(self, username,password):
        if userTable.find_one({"username": username}):
            print("Logged In")
        else:
            print("Login Failed")

# test
# user1 = {"name": "Nour","email":"Nourtarek885@gmail.com", "username": "Nourtarek885","password":""}
# userTable.insert_one(user1)
# userTable.insert_one({"name":"Arwa", "email":"Arwa@gmail.com"})
# eventTable.insert_one({"title":"", "date":"", "time": "", "location": "", "description": ""})
# print(dataBase.list_collection_names())

userManagement = userManagement()
userManagement.signUp("Nour", "nour@gmail.com", "nourtarek885", "NourTarek11")

userStr = input("Enter your username or email: ")
password = input("Enter your password: ")

if "@" in userStr:
    userManagement.loginByEmail(userStr, password)
else:
    userManagement.loginByUsername(userStr, password)