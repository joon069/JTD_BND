from pydantic import BaseModel
from datetime import date

class DiaryCreate(BaseModel):
    title: str
    content: str
    emotion: str
    date: date

class DiaryResponse(DiaryCreate):
    id: int

    class Config:
        from_attributes = True  # orm_mode → from_attributes
