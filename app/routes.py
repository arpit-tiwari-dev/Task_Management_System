from fastapi import APIRouter, HTTPException, BackgroundTasks
from typing import List

from app.model import Task, TaskCreate, TaskUpdate
from app.repository import TaskRepository
from app.service import TaskService
from app.services.github_service import GithubService

from app.db.mongo import task_collection

router = APIRouter()

repo = TaskRepository()
service = TaskService(repo)


@router.post("/tasks", response_model=Task)
async def create_task(data: TaskCreate , background_tasks: BackgroundTasks):

    task = await service.create_task(data)

    try:
        github_service = GithubService()
        if data.create_github_issue:
            background_tasks.add_task(
                github_service.create_issue,
                task.id,
                task.title,
                task.description
            )
    except Exception as e:
        print(f"Erorr during github Issue creation - {e}")
    
    return task


@router.get("/tasks", response_model=List[Task])
async def list_tasks(skip: int = 0, limit: int = 10):
    return await service.list_tasks(skip, limit)


@router.get("/tasks/{task_id}", response_model=Task)
async def get_task(task_id: str):
    task = await service.get_task(task_id)
    if not task:
        raise HTTPException(404, "Task not found")
    return task


@router.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: str, data: TaskUpdate):
    task = await service.update_task(task_id, data)
    if not task:
        raise HTTPException(404, "Task not found")
    return task


@router.delete("/tasks/{task_id}")
async def delete_task(task_id: str):
    if not await service.delete_task(task_id):
        raise HTTPException(404, "Task not found")
    return {"message": "Task deleted"}


@router.post("/tasks/{task_id}/complete", response_model=Task)
async def complete_task(task_id: str):
    task = await service.complete_task(task_id)
    if not task:
        raise HTTPException(404, "Task not found")
    return task

@router.get("/health")
async def health_check():
    return {"status": "ok"}

@router.get("/ready")
async def readiness_check():
    try:
        # simple DB ping
        await task_collection.database.command("ping")
        return {"status": "ready"}
    except Exception:
        return {"status": "not ready"}
