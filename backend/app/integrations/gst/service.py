def analyze_gst_compliance(gst_data):
    expected_tax = gst_data["total_turnover"] * 0.18

    if gst_data["tax_paid"] < expected_tax:
        return "GST risk: underpayment detected"

    if gst_data["filing_status"] != "FILED":
        return "GST risk: return not filed"

    return "GST compliant"
