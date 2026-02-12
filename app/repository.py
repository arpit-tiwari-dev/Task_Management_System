from typing import Dict, List
from app.model import Task
from app.db.mongo import task_collection


class TaskRepository:

    async def create(self, task: Task):
        await task_collection.insert_one(task.dict())
        return task

    async def list(self, skip: int = 0, limit: int = 10) -> List[Task]:
        cursor = task_collection.find().skip(skip).limit(limit)

        tasks = []
        async for doc in cursor:
            doc.pop("_id", None)
            tasks.append(Task(**doc))
        
        return tasks


    async def get(self, task_id: str):
        task = await task_collection.find_one({"id": task_id})
        if task:
            task.pop("_id", None)
            return Task(**task)

    async def update(self, task_id: str, task: Task):
        await task_collection.update_one(
            {"id": task_id},
            {"$set": task.dict()}
        )
        return task

    async def delete(self, task_id: str):
        result = await task_collection.delete_one({"id": task_id})
        return result.deleted_count > 0
