from sqlalchemy import Column, Integer, String

from config.db import Base


class Task(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True, nullable=True)
