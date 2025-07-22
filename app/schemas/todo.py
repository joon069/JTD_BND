from pydantic import BaseModel

class TodoCreate(BaseModel):
    task: str
    is_done: bool = False

class TodoResponse(TodoCreate):
    id: int

    class Config:
        from_attributes = True  # orm_mode 대신 최신 방식
