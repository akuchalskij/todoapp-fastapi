from typing import Optional, List

from app.entity import Task
from app.repository import BaseRepository


class TaskRepository(BaseRepository):
    def find_all_by_owner(self, *, owner_id: int, skip=0, limit=100) -> List[Optional[Task]]:
        return (
            self.db.query(Task)
                .filter(Task.owner_id == owner_id)
                .offset(skip)
                .limit(limit)
                .all()
        )

