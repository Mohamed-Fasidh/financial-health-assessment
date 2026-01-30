from fastapi import APIRouter
from app.integrations.banking.client import BankAPIClient
from app.integrations.banking.service import analyze_cashflow

router = APIRouter(prefix="/bank", tags=["Banking"])

@router.get("/{account_id}")
def bank_analysis(account_id: str):
    client = BankAPIClient()
    bank_data = client.fetch_account_summary(account_id)
    insight = analyze_cashflow(bank_data)

    return {
        "account_id": account_id,
        "bank_data": bank_data,
        "cashflow_status": insight
    }
