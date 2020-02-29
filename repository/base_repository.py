from typing import Optional, List

from config.db import Session
from entity.task import Task


class TaskRepository:
    def __init__(self, db: Session):
        self.db = db

    def find_by_id(self, *, task_id: int) -> Optional[Task]:
        return self.db.query(Task).filter(Task.id == task_id).first()

    def find_all(self,  *, skip=0, limit=100) -> List[Optional[Task]]:
        return self.db.query(Task).offset(skip).limit(limit).all()

    def find_all_by_owner(self, *, owner_id: int, skip=0, limit=100) -> List[Optional[Task]]:
        return (
            self.db.query(Task)
                .filter(Task.owner_id == owner_id)
                .offset(skip)
                .limit(limit)
                .all()
        )

    def save(self, task: Task):
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)

    def delete(self, task: Task):
        self.db.delete(task)
        self.db.commit()
