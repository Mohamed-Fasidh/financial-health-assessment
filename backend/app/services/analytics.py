def calculate_health_score(data):
    revenue = data["revenue"]
    expenses = data["expenses"]
    receivables = data["receivables"]
    payables = data["payables"]
    inventory = data["inventory"]
    loan = data["loan"]
    tax = data["tax"]

    score = 100

    # Profitability
    margin = (revenue - expenses) / revenue
    if margin < 0.1:
        score -= 20

    # Liquidity
    working_capital = receivables + inventory - payables
    if working_capital < 0:
        score -= 20

    # Leverage
    if loan > revenue * 0.5:
        score -= 15

    # Tax compliance
    expected_tax = revenue * 0.18
    if tax < expected_tax:
        score -= 15

    return max(score, 0), working_capital
