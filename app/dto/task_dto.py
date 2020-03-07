from pydantic import BaseModel


class TaskDTOBase(BaseModel):
    title: str = None
    description: str = None


class TaskDTO(TaskDTOBase):
    id: int
    title: str

    class Config:
        orm_mode = True


class TaskCreate(TaskDTOBase):
    title: str


class TaskUpdate(TaskDTOBase):
    pass
