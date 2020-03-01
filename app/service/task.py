from fastapi.encoders import jsonable_encoder

from app.dto import TaskCreate, TaskUpdate
from app.entity import Task
from app.repository import TaskRepository


class TaskService:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def create(self, *, request: TaskCreate, owner_id: int) -> Task:
        request_data = jsonable_encoder(request)
        task = Task(**request_data, owner_id=owner_id)

        return self.repository.save(task)

    def update(self, *, task: Task, request: TaskUpdate) -> Task:
        task_data = jsonable_encoder(task)
        update_data = request.dict(skip_defaults=True)

        for field in task_data:
            if field in update_data:
                setattr(task, field, update_data[field])

        return self.repository.save(task)

    def remove(self, *, task_id: int):
        task = self.repository.find_by(entity_class=Task, entity_param=Task.id, variable=task_id)

        return self.repository.delete(task)
