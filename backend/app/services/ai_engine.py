
def generate_ai_insights(score):
    if score < 40:
        return "High financial risk detected. Improve cash flow urgently."
    if score < 70:
        return "Moderate stability. Optimize costs and receivables."
    return "Financially healthy. Eligible for growth funding."
