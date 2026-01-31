from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
import pandas as pd
import pdfplumber
from sqlalchemy.orm import Session
import logging

from app.services.analytics import calculate_health_score
from app.services.recommendations import bank_recommendation
from app.database import get_db
from app.crud import create_financial_record

logging.basicConfig(level=logging.INFO)

router = APIRouter()

@router.post("/")
async def upload_file(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    try:
        logging.info("UPLOAD ENDPOINT CALLED")
        filename = file.filename.lower()
        logging.info(f"Filename: {filename}")

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

            import re
            def extract(label):
                m = re.search(fr"{label}\s*[:\-]?\s*(\d+)", text, re.I)
                return float(m.group(1)) if m else 0.0

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

        logging.info(f"Parsed data: {data}")

        score, working_capital = calculate_health_score(data)
        recommendation = bank_recommendation(score)

        logging.info(f"Score: {score}")
        logging.info(f"Working Capital: {working_capital}")
        logging.info(f"Recommendation: {recommendation}")

        # 🔍 Verify DB connection
        db_name = db.execute("SELECT current_database()").fetchone()
        logging.info(f"CONNECTED DATABASE: {db_name}")

        # ✅ INSERT
        create_financial_record(
            db=db,
            data=data,
            score=score,
            working_capital=working_capital,
            recommendation=recommendation
        )

        logging.info("INSERT COMPLETED SUCCESSFULLY")

        return {
            "score": int(score),
            "working_capital": working_capital,
            "recommendation": recommendation,
        }

    except Exception as e:
        logging.exception("UPLOAD FAILED")
        raise HTTPException(status_code=500, detail=str(e))
