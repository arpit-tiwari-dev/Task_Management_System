from typing import Dict, List
from app.model import Task


class TaskRepository:
    def __init__(self):
        self.tasks: Dict[str, Task] = {}

    def create(self, task: Task):
        self.tasks[task.id] = task
        return task

    def list(self, skip: int = 0, limit: int = 10) -> List[Task]:
        return list(self.tasks.values())[skip: skip + limit]

    def get(self, task_id: str):
        return self.tasks.get(task_id)

    def update(self, task_id: str, task: Task):
        self.tasks[task_id] = task
        return task

    def delete(self, task_id: str):
        return self.tasks.pop(task_id, None)
