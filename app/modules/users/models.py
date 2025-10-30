from app.database import client

dataBase = client['EventPlanner']
userTable = dataBase["user"]