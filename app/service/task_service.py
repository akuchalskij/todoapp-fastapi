import attr
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from injector import inject

from app.dto import TaskCreate, TaskUpdate, TaskDTO
from app.entity import Task
from app.repository import TaskRepository


@inject
@attr.s(auto_attribs=True)
@attr.dataclass
class TaskService:
    _repository: TaskRepository

    def create(self, *, request: TaskCreate) -> TaskDTO:
        request_data = jsonable_encoder(request)
        task = Task(**request_data)

        task = self._repository.save(task)

        return TaskDTO(id=task.id, title=task.title, description=task.description)

    def update(self, *, task_id: int, request: TaskUpdate) -> TaskDTO:
        task: Task = self._repository.find_by_id(variable=task_id)

        if not task:
            raise HTTPException(status_code=400, detail="Task not found")

        task_data = jsonable_encoder(task)
        update_data = request.dict(skip_defaults=True)

        for field in task_data:
            if field in update_data:
                setattr(task, field, update_data[field])

        task = self._repository.save(task)

        return TaskDTO(id=task.id, title=task.title, description=task.description)

    def remove(self, *, task_id: int):
        task = self._repository.find_by_id(variable=task_id)

        if not task:
            raise HTTPException(status_code=404, detail="Task not found")

        return self._repository.delete(task)
