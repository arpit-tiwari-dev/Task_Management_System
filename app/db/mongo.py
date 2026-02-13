from motor.motor_asyncio import AsyncIOMotorClient
from app.settings import MONGO_URL

MONGO_URL = MONGO_URL

client = AsyncIOMotorClient(MONGO_URL)
database = client.task_db

task_collection = database.get_collection("tasks")