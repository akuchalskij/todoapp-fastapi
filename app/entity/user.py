from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from config.db import Base
from entity.task import Task


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    tasks = relationship(Task, back_populates="owner")
