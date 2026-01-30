def bank_recommendation(score):
    if score >= 75:
        return "Eligible for MSME term loan from banks"
    elif score >= 55:
        return "Eligible for working capital loan from NBFC"
    else:
        return "High risk – loan not recommended"
