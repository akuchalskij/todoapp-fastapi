from fastapi.encoders import jsonable_encoder

from dto.task import TaskCreate, TaskUpdate
from entity.task import Task
from repository import TaskRepository


class TaskService:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def create(self, *, task_in: TaskCreate, owner_id: int) -> Task:
        task_in_data = jsonable_encoder(task_in)
        task = Task(**task_in_data, owner_id=owner_id)

        return self.repository.save(task)

    def update(self, *, task: Task, task_in: TaskUpdate) -> Task:
        task_data = jsonable_encoder(task)
        update_data = task_in.dict(skip_defaults=True)

        for field in task_data:
            if field in update_data:
                setattr(task, field, update_data[field])

        return self.repository.save(task)

    def remove(self, *, task_id: int):
        task = self.repository.find_by(entity_class=Task, entity_param=Task.id, variable=task_id)

        return self.repository.delete(task)
