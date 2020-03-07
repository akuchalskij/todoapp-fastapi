from typing import List

from fastapi import HTTPException, APIRouter

from app.dto import TaskDTO, TaskCreate, TaskUpdate
from config.container import task_service, task_repository

router = APIRouter()


@router.get("/", response_model=List[TaskDTO])
async def list(skip: int = 0, limit: int = 100):
    """
    List a tasks.
    """
    return task_repository.find_all(skip=skip, limit=limit)


@router.post("/", response_model=TaskDTO)
async def create(request: TaskCreate):
    """
    Create new task.
    """
    return task_service.create(request=request)


@router.put("/{task_id}", response_model=TaskDTO)
async def update(task_id: int, request: TaskUpdate):
    """
    Update an task.
    """
    return task_service.update(task_id=task_id, request=request)


@router.get("/{task_id}", response_model=TaskDTO)
async def retrieve(task_id: int):
    """
    Get task by ID.
    """
    task = task_repository.find_by_id(variable=task_id)

    if not task:
        raise HTTPException(status_code=400, detail="Task not found")

    return task


@router.delete("/{task_id}", response_model=TaskDTO)
async def destroy(task_id: int):
    """
    Delete an task.
    """
    return task_service.remove(task_id=task_id)
