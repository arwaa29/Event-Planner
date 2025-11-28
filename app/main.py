# app/main.py
from fastapi import FastAPI
from app.modules.users.routes import userRouter as user_router
from app.modules.events.routes import eventRouter as event_router
from app.modules.responses.routes import responseRouter as response_router
from app.modules.search.routes import searchRouter as search_router
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(title="EventPlanner API")

# CORS setup should be here before starting Server
origins = [
    "http://127.0.0.1:5173",  # your frontend
    "http://localhost:5173",  # sometimes you use this instead
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow only your frontend URLs
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (POST, GET, etc.)
    allow_headers=["*"],  # Allow all headers
)
# include all routers
app.include_router(user_router)
app.include_router(event_router)
app.include_router(response_router)
app.include_router(search_router)



@app.get("/")
def root():
    return {"message": "FastAPI server is running!"}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)

