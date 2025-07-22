from sqlalchemy import Column, Integer, String, Text, Date
from app.database import Base

class Diary(Base):
    __tablename__ = "diaries"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    content = Column(Text)
    emotion = Column(String(30))
    date = Column(Date)
