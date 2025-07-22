# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# DB 연결 주소
DATABASE_URL = "mysql+pymysql://root:1234@localhost:3307/JOT?charset=utf8mb4"
engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# DB 세션 의존성 (FastAPI용)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_tables():
    from app.models import diary, todo  # 모든 모델 import 필요
    Base.metadata.create_all(bind=engine)
#석석석석석석석석석석석석석석석석석석석석석석석석석석석석석석