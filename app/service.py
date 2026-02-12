import uuid
from datetime import datetime
from typing import List

from app.model import Task, TaskCreate, TaskUpdate, TaskStatus
from app.repository import TaskRepository


class TaskService:
    def __init__(self, repo: TaskRepository):
        self.repo = repo

    def create_task(self, data: TaskCreate) -> Task:
        now = datetime.utcnow()

        task = Task(
            id=str(uuid.uuid4()),
            title=data.title,
            description=data.description,
            status=TaskStatus.pending,
            priority=data.priority,
            created_at=now,
            updated_at=now,
        )

        return self.repo.create(task)

    def list_tasks(self, skip: int, limit: int) -> List[Task]:
        return self.repo.list(skip, limit)

    def get_task(self, task_id: str):
        return self.repo.get(task_id)

    def update_task(self, task_id: str, data: TaskUpdate):
        task = self.repo.get(task_id)
        if not task:
            return None

        updated = task.copy(update=data.dict(exclude_unset=True))
        updated.updated_at = datetime.utcnow()

        return self.repo.update(task_id, updated)

    def delete_task(self, task_id: str):
        return self.repo.delete(task_id)

    def complete_task(self, task_id: str):
        task = self.repo.get(task_id)
        if not task:
            return None

        task.status = TaskStatus.completed
        task.updated_at = datetime.utcnow()

        return self.repo.update(task_id, task)
