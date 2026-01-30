import requests

class GSTClient:
    def __init__(self):
        self.base_url = "https://gst-sandbox.api.gov.in"  # sandbox-style
        self.api_key = "SANDBOX_GST_KEY"

    def fetch_returns(self, gstin: str):
        # Mocked response – same schema as real GSTN
        return {
            "gstin": gstin,
            "total_turnover": 1200000,
            "tax_paid": 216000,
            "filing_status": "FILED"
        }
