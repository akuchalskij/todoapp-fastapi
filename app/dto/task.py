from pydantic import BaseModel


class TaskDTOBase(BaseModel):
    title: str = None
    description: str = None


class TaskCreate(TaskDTOBase):
    title: str


class TaskUpdate(TaskDTOBase):
    pass


class TaskDTO(TaskDTOBase):
    id: int
    title: str
    owner_id: int

    class Config:
        orm_mode = True
