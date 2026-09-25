from fastapi import FastAPI
from pymongo import AsyncIOMotorClient

app = FastAPI()
client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client["college"]
#select the collection
students_collection = db["students"]
@app.get("/")
async def home():
    return {"message": "FastAPI with MongoDB is running!"}
@app.get("/health") 
async def health():
    result = await db.command("ping")
    return {"mongodb": "Connected","ping": result["ok"]}   