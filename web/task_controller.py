from typing import List

from fastapi import Depends, HTTPException, APIRouter

from dto.task import Task, TaskCreate, TaskUpdate
from entity.user import Task as TaskEntity
from repository import TaskRepository
from service import UserService, TaskService
from web import BaseController

router = APIRouter()


class TaskController(BaseController):
    def __init__(self, service: TaskService, user_service: UserService, repository: TaskRepository):
        self.service = service
        self.user_service = user_service
        self.repository = repository
        self.user = Depends(self.user_service.get_current_user)

    @router.get("/", response_model=List[Task])
    def list(self, skip: int = 0, limit: int = 100):
        """
        List a tasks.
        """
        return self.repository.find_all_by_owner(owner_id=self.user.id, skip=skip, limit=limit)

    @router.post("/", response_model=Task)
    def create(self, request: TaskCreate):
        """
        Create new task.
        """
        item = self.service.create(task_in=request, owner_id=self.user.id)

        return item

    @router.put("/{task_id}", response_model=Task)
    def update(self, task_id: int, request: TaskUpdate):
        """
        Update an task.
        """
        task = self.repository.find_by(entity_class=TaskEntity, entity_param=TaskEntity.id, variable=task_id)

        if not task:
            raise HTTPException(status_code=404, detail="Task not found")

        if task.owner_id != self.user.id:
            raise HTTPException(status_code=400, detail="Not enough permissions")

        task = self.service.update(task=task, task_in=request)

        return task

    @router.get("/{task_id}", response_model=Task)
    def retrieve(self, task_id: int):
        """
        Get task by ID.
        """
        task = self.repository.find_by(entity_class=TaskEntity, entity_param=TaskEntity.id, variable=task_id)

        if not task:
            raise HTTPException(status_code=400, detail="Task not found")

        if task.owner_id != self.user.id:
            raise HTTPException(status_code=400, detail="Not enough permissions")

        return task

    @router.delete("/{task_id}", response_model=Task)
    def destroy(self, task_id: int):
        """
        Delete an task.
        """
        task = self.repository.find_by(entity_class=TaskEntity, entity_param=TaskEntity.id, variable=task_id)

        if not task:
            raise HTTPException(status_code=404, detail="Task not found")

        if task.owner_id != self.user.id:
            raise HTTPException(status_code=400, detail="Not enough permissions")

        task = self.repository.delete(task)

        return task
