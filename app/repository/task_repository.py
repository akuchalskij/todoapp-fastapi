from typing import List, Optional, Any

import attr
from injector import inject

from app.entity import Task
from app.repository import BaseRepository


@inject
@attr.dataclass
class TaskRepository(BaseRepository):
    def find_by_id(self, *, entity_class=Task, entity_param=Task.id, variable: Any) -> Optional[Task]:
        return super().find_by(entity_class=entity_class, entity_param=entity_param, variable=variable)

    def find_all(self, *, entity_class=Task, skip=0, limit=100) -> List[Optional[Task]]:
        return super().find_all(entity_class=entity_class)
