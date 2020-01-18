from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from service import task as task_service
from utils.db import get_db
from security.authenticate import get_current_user
from entity.user import User
from dto.task import Task, TaskCreate, TaskUpdate

router = APIRouter()


@router.get("/", response_model=List[Task])
def read_items(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(get_current_user),
):
    """
    Retrieve items.
    """
    items = task_service.find_all_by_owner(
        db_session=db, owner_id=current_user.id, skip=skip, limit=limit
    )
    return items


@router.post("/", response_model=Task)
def create_item(
    *,
    db: Session = Depends(get_db),
    item_in: TaskCreate,
    current_user: User = Depends(get_current_user),
):
    """
    Create new item.
    """
    item = task_service.create(db_session=db, task_in=item_in, owner_id=current_user.id)
    return item


@router.put("/{id}", response_model=Task)
def update_item(
    *,
    db: Session = Depends(get_db),
    id: int,
    item_in: TaskUpdate,
    current_user: User = Depends(get_current_user),
):
    """
    Update an item.
    """
    item = task_service.find_by_id(db_session=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Task not found")
    if item.owner_id != current_user.id:
        raise HTTPException(status_code=400, detail="Not enough permissions")
    item = task_service.update(db_session=db, task=item, task_in=item_in)
    return item


@router.get("/{id}", response_model=Task)
def read_user_me(
    *,
    db: Session = Depends(get_db),
    id: int,
    current_user: User = Depends(get_current_user),
):
    """
    Get item by ID.
    """
    item = task_service.find_by_id(db_session=db, id=id)
    if not item:
        raise HTTPException(status_code=400, detail="Task not found")
    if item.owner_id != current_user.id:
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return item


@router.delete("/{id}", response_model=Task)
def delete_item(
    *,
    db: Session = Depends(get_db),
    id: int,
    current_user: User = Depends(get_current_user),
):
    """
    Delete an item.
    """
    item = task_service.find_by_id(db_session=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Task not found")
    if item.owner_id != current_user.id:
        raise HTTPException(status_code=400, detail="Not enough permissions")
    item = task_service.remove(db_session=db, id=id)
    return item
