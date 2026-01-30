def analyze_cashflow(bank_data):
    if bank_data["monthly_inflow"] < bank_data["monthly_outflow"]:
        return "Negative cash flow detected"
    return "Healthy cash flow"
