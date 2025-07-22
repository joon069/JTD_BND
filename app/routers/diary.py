from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.diary import Diary
from app.schemas.diary import DiaryCreate, DiaryResponse
from app.models.user import User
from app.routers.auth import login
router = APIRouter(prefix="/diary", tags=["diary"])

@router.post("/", response_model=DiaryResponse)
def create_diary(diary: DiaryCreate, db: Session = Depends(get_db)):
    db_diary = Diary(**diary.dict())
    db.add(db_diary)
    db.commit()
    db.refresh(db_diary)
    return db_diary

@router.get("/", response_model=list[DiaryResponse])
def get_all_diaries(db: Session = Depends(get_db)):
    return db.query(Diary).all()

@router.get("/{diary_id}", response_model=DiaryResponse)
def get_diary(diary_id: int, db: Session = Depends(get_db)):
    diary = db.query(Diary).filter(Diary.id == diary_id).first()
    if not diary:
        raise HTTPException(status_code=404, detail="Diary not found")
    return diary


@router.delete("/{diary_id}")
def delete_diary(
    diary_id: int,
    db: Session = Depends(get_db)
):
    diary = db.query(Diary).filter(Diary.id == diary_id).first()

    if not diary:
        # 해당 ID의 일기가 없거나, 로그인한 사용자의 일기가 아닌 경우 404 반환
        raise HTTPException(status_code=404, detail="Diary not found or not authorized")

    db.delete(diary)
    db.commit()
    return {"message": "Diary deleted successfully"}