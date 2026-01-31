import logging
from sqlalchemy.orm import Session
from app.models import FinancialRecord

def create_financial_record(db: Session, data: dict, score: int, working_capital: float, recommendation: str):
    print(" INSERT FUNCTION CALLED")
    logging.info("INSERT FUNCTION CALLED")
    print("DATA:", data)
    print("SCORE:", score)

    record = FinancialRecord(
        revenue=data["revenue"],
        expenses=data["expenses"],
        receivables=data["receivables"],
        payables=data["payables"],
        inventory=data["inventory"],
        loan=data["loan"],
        tax=data["tax"],
        score=score,
        working_capital=working_capital,
        recommendation=recommendation
    )

    db.add(record)
    print(" BEFORE COMMIT")
    db.flush()  
    db.commit()
    print(" AFTER COMMIT")
    db.refresh(record)
    return record

