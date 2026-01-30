
from fastapi import APIRouter
from app.schemas.finance import FinanceInput
from app.services.analytics import calculate_health_score
from app.services.ai_engine import generate_ai_insights

router = APIRouter()

@router.post("/analyze")
def analyze(data: FinanceInput):
    score = calculate_health_score(data.revenue, data.expenses)
    return {
        "score": score,
        "insights": generate_ai_insights(score)
    }
