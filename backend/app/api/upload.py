from io import BytesIO
import logging
from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
import pandas as pd
import pdfplumber
from sqlalchemy.orm import Session

from app.services.analytics import calculate_health_score
from app.services.recommendations import bank_recommendation
from app.database import get_db
from app.crud import create_financial_record

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
            contents = await file.read()
            excel_file = BytesIO(contents)
            df = pd.read_excel(excel_file)
            logging.info(f"RAW COLUMNS: {df.columns.tolist()}")
            logging.info("RAW DATA PREVIEW:")
            logging.info(df.head().to_dict())
    # 🔧 Normalize column names
            df.columns = (
               df.columns
                .str.strip()
                .str.lower()
                .str.replace(" ", "_")
            ) 
            logging.info(f"NORMALIZED COLUMNS: {df.columns.tolist()}")

    # 🔧 Force numeric conversion
            numeric_cols = [
                "revenue",
                "expenses",
                "receivables",
                "payables",
                "inventory",
                "loan_amount",
                "tax_paid",
         ]

            for col in numeric_cols:
                if col in df.columns:
                    df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

            data = {
                "revenue": float(df.get("revenue", 0).sum()),
                "expenses": float(df.get("expenses", 0).sum()),
                "receivables": float(df.get("receivables", 0).sum()),
                "payables": float(df.get("payables", 0).sum()),
                "inventory": float(df.get("inventory", 0).sum()),
                "loan": float(df.get("loan_amount", 0).sum()),
                "tax": float(df.get("tax_paid", 0).sum()),
            }
            logging.info(f"FINAL PARSED DATA: {data}")


        # ================= PDF =================
        elif filename.endswith(".pdf"):
            pdf_text = ""
            with pdfplumber.open(file.file) as pdf:
                for page in pdf.pages:
                    pdf_text += page.extract_text() or ""

            import re
            def extract(label):
                m = re.search(fr"{label}\s*[:\-]?\s*(\d+)", pdf_text, re.I)
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

        # ✅ STORE INTO POSTGRESQL
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
        print("UPLOAD ERROR:", e)
        raise

