from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from config.db import Base


class Task(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="tasks")
