from typing import Optional, List, Any

import attr
from injector import inject

from config.db import Database


@inject
@attr.dataclass
@attr.s(auto_attribs=True)
class BaseRepository(object):
    _db: Database

    def find_by(self, *, entity_class: Any, entity_param: Any, variable: Any) -> Optional[Any]:
        return self._db.session.query(entity_class).filter(entity_param == variable).first()

    def find_all(self, *, entity_class: Any, skip=0, limit=100) -> List[Optional[Any]]:
        return self._db.session.query(entity_class).offset(skip).limit(limit).all()

    def save(self, entity: Any) -> Any:
        self._db.session.add(entity)
        self._db.session.commit()
        self._db.session.refresh(entity)

        return entity

    def delete(self, entity: Any):
        self._db.session.delete(entity)
        self._db.session.commit()
