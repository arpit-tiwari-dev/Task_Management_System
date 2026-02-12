import uuid
from datetime import datetime
from typing import List

from app.model import Task, TaskCreate, TaskUpdate, TaskStatus
from app.repository import TaskRepository

from app.services.github_service import GithubService


class TaskService:
    def __init__(self, repo: TaskRepository):
        self.repo = repo

    async def create_task(self, data: TaskCreate) -> Task:
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

        github_service = GithubService()

        if data.create_github_issue:
            try:
                issue_id = github_service.create_issue(data.title , data.description)
                task.external_reference_id = str(issue_id)
            except Exception:
                print("Issue Creation on Github Failed")

        return await self.repo.create(task)

    async def list_tasks(self, skip: int, limit: int) -> List[Task]:
        return await self.repo.list(skip, limit)

    async def get_task(self, task_id: str):
        return await self.repo.get(task_id)

    async def update_task(self, task_id: str, data: TaskUpdate):
        task = await self.repo.get(task_id)
        if not task:
            return None

        updated = task.copy(update=data.dict(exclude_unset=True))
        updated.updated_at = datetime.utcnow()

        return await self.repo.update(task_id, updated)

    async def delete_task(self, task_id: str):
        return await self.repo.delete(task_id)

    async def complete_task(self, task_id: str):
        task = await self.repo.get(task_id)
        if not task:
            return None

        task.status = TaskStatus.completed
        task.updated_at = datetime.utcnow()

        return await self.repo.update(task_id, task)
