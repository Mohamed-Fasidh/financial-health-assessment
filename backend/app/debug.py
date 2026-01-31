from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.database import get_db

router = APIRouter()

@router.get("/debug/fix-schema")
def fix_schema(db: Session = Depends(get_db)):
    db.execute(text("""
        ALTER TABLE financial_records
        ADD COLUMN IF NOT EXISTS working_capital DOUBLE PRECISION;
    """))

    db.execute(text("""
        ALTER TABLE financial_records
        ADD COLUMN IF NOT EXISTS recommendation TEXT;
    """))

    db.execute(text("""
        ALTER TABLE financial_records
        ADD COLUMN IF NOT EXISTS created_at TIMESTAMP DEFAULT NOW();
    """))

    db.commit()
    return {"status": "schema updated successfully"}
