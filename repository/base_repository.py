from typing import Optional, List, Any

from config.db import Session


class BaseRepository:
    def __init__(self, db: Session):
        self.db = db

    def find_by(self, *, entity_class: Any, entity_param: Any, variable: Any) -> Optional[Any]:
        return self.db.query(entity_class).filter(entity_param == variable).first()

    def find_all(self, *, entity_class: Any, skip=0, limit=100) -> List[Optional[Any]]:
        return self.db.query(entity_class).offset(skip).limit(limit).all()

    def save(self, entity: Any) -> Any:
        self.db.add(entity)
        self.db.commit()
        self.db.refresh(entity)

        return entity

    def delete(self, entity: Any):
        self.db.delete(entity)
        self.db.commit()
