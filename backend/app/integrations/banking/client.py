class BankAPIClient:
    def fetch_account_summary(self, account_id):
        # Sandbox-style data
        return {
            "account_id": account_id,
            "balance": 250000,
            "monthly_inflow": 180000,
            "monthly_outflow": 150000
        }
