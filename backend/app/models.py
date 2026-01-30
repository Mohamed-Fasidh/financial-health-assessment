from sqlalchemy import Column, Integer, Float, String
from app.database import Base

class FinancialRecord(Base):
    __tablename__ = "financial_records"

    id = Column(Integer, primary_key=True)
    revenue = Column(Float)
    expenses = Column(Float)
    receivables = Column(Float)
    payables = Column(Float)
    inventory = Column(Float)
    loan = Column(Float)
    tax = Column(Float)
    score = Column(Integer)
