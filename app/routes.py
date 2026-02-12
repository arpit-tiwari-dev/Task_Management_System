from fastapi import APIRouter, HTTPException
from typing import List

from app.model import Task, TaskCreate, TaskUpdate
from app.repository import TaskRepository
from app.service import TaskService

router = APIRouter()

repo = TaskRepository()
service = TaskService(repo)


@router.post("/tasks", response_model=Task)
async def create_task(data: TaskCreate):
    return await service.create_task(data)


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
