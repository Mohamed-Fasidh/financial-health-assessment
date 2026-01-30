
from pydantic import BaseModel

class FinanceInput(BaseModel):
    revenue: float
    expenses: float
