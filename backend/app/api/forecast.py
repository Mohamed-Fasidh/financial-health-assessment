def forecast_revenue(df):
    return float(df["revenue"].rolling(3).mean().iloc[-1])
