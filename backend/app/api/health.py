from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter()

@router.get("/")
def health(db: Session = Depends(get_db)):
    db.execute("SELECT 1")
    return {"status": "ok"}
