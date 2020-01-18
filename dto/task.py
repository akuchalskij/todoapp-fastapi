from pydantic import BaseModel


class TaskBase(BaseModel):
    title: str = None
    description: str = None


class TaskCreate(TaskBase):
    title: str


class TaskUpdate(TaskBase):
    pass


class TaskInDBBase(TaskBase):
    id: int
    title: str
    owner_id: int

    class Config:
        orm_mode = True


class Task(TaskInDBBase):
    pass


class TaskInDB(TaskInDBBase):
    pass
