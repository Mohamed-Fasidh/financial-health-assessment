from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd
import pdfplumber
from app.services.analytics import calculate_health_score
from app.services.recommendations import bank_recommendation

router = APIRouter()

@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    filename = file.filename.lower()

    try:
        # ================= CSV =================
        if filename.endswith(".csv"):
            df = pd.read_csv(file.file, encoding="latin1")

            data = {
                "revenue": float(df["revenue"].sum()),
                "expenses": float(df["expenses"].sum()),
                "receivables": float(df["receivables"].sum()),
                "payables": float(df["payables"].sum()),
                "inventory": float(df["inventory"].sum()),
                "loan": float(df["loan_amount"].sum()),
                "tax": float(df["tax_paid"].sum()),
            }

        # ================= XLSX =================
        elif filename.endswith(".xlsx"):
            df = pd.read_excel(file.file)

            data = {
                "revenue": float(df["revenue"].sum()),
                "expenses": float(df["expenses"].sum()),
                "receivables": float(df["receivables"].sum()),
                "payables": float(df["payables"].sum()),
                "inventory": float(df["inventory"].sum()),
                "loan": float(df["loan_amount"].sum()),
                "tax": float(df["tax_paid"].sum()),
            }

        # ================= PDF =================
        elif filename.endswith(".pdf"):
            text = ""

            with pdfplumber.open(file.file) as pdf:
                for page in pdf.pages:
                    text += page.extract_text() or ""

            # Very important: extract numbers safely
            def extract(label):
                import re
                match = re.search(fr"{label}\s*[:\-]?\s*(\d+)", text, re.I)
                return float(match.group(1)) if match else 0.0

            data = {
                "revenue": extract("revenue"),
                "expenses": extract("expenses"),
                "receivables": extract("receivable"),
                "payables": extract("payable"),
                "inventory": extract("inventory"),
                "loan": extract("loan"),
                "tax": extract("tax"),
            }

        else:
            raise HTTPException(status_code=400, detail="Unsupported file type")

        score, working_capital = calculate_health_score(data)
        recommendation = bank_recommendation(score)

        return {
            "score": int(score),
            "working_capital": working_capital,
            "recommendation": recommendation,
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
