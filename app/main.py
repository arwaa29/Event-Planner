# app/main.py
from fastapi import FastAPI
from app.modules.users.routes import userRouter as user_router
import uvicorn
app = FastAPI(title="EventPlanner API")

# include all routers
app.include_router(user_router)

@app.get("/")
def root():
    return {"message": "FastAPI server is running!"}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)