from fastapi import APIRouter, HTTPException
from typing import List

from app.model import Task, TaskCreate, TaskUpdate
from app.repository import TaskRepository
from app.service import TaskService

router = APIRouter()

repo = TaskRepository()
service = TaskService(repo)


@router.post("/tasks", response_model=Task)
def create_task(data: TaskCreate):
    return service.create_task(data)


@router.get("/tasks", response_model=List[Task])
def list_tasks(skip: int = 0, limit: int = 10):
    return service.list_tasks(skip, limit)


@router.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: str):
    task = service.get_task(task_id)
    if not task:
        raise HTTPException(404, "Task not found")
    return task


@router.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: str, data: TaskUpdate):
    task = service.update_task(task_id, data)
    if not task:
        raise HTTPException(404, "Task not found")
    return task


@router.delete("/tasks/{task_id}")
def delete_task(task_id: str):
    if not service.delete_task(task_id):
        raise HTTPException(404, "Task not found")
    return {"message": "Task deleted"}


@router.post("/tasks/{task_id}/complete", response_model=Task)
def complete_task(task_id: str):
    task = service.complete_task(task_id)
    if not task:
        raise HTTPException(404, "Task not found")
    return task
