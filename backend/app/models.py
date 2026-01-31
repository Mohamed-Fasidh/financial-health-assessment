from sqlalchemy import Column, Integer, Float, DateTime
from datetime import datetime
from app.database import Base

class FinancialRecord(Base):
    __tablename__ = "financial_records"

    id = Column(Integer, primary_key=True, index=True)

    revenue = Column(Float)
    expenses = Column(Float)
    receivables = Column(Float)
    payables = Column(Float)
    inventory = Column(Float)
    loan = Column(Float)
    tax = Column(Float)

    score = Column(Integer)
    working_capital = Column(Float)
    recommendation = Column(Float, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)
