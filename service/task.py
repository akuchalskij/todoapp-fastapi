from typing import List, Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from entity.task import Task
from dto.task import TaskCreate, TaskUpdate


def find_by_id(db_session: Session, *, id: int) -> Optional[Task]:
    return db_session.query(Task).filter(Task.id == id).first()


def find_all(db_session: Session, *, skip=0, limit=100) -> List[Optional[Task]]:
    return db_session.query(Task).offset(skip).limit(limit).all()


def find_all_by_owner(
        db_session: Session, *, owner_id: int, skip=0, limit=100
) -> List[Optional[Task]]:
    return (
        db_session.query(Task)
            .filter(Task.owner_id == owner_id)
            .offset(skip)
            .limit(limit)
            .all()
    )


def create(db_session: Session, *, task_in: TaskCreate, owner_id: int) -> Task:
    task_in_data = jsonable_encoder(task_in)
    task = Task(**task_in_data, owner_id=owner_id)
    db_session.add(task)
    db_session.commit()
    db_session.refresh(task)
    return task


def update(db_session: Session, *, task: Task, task_in: TaskUpdate) -> Task:
    task_data = jsonable_encoder(task)
    update_data = task_in.dict(skip_defaults=True)
    for field in task_data:
        if field in update_data:
            setattr(task, field, update_data[field])
    db_session.add(task)
    db_session.commit()
    db_session.refresh(task)
    return task


def remove(db_session: Session, *, id: int):
    task = db_session.query(Task).filter(Task.id == id).first()
    db_session.delete(task)
    db_session.commit()
    return task
