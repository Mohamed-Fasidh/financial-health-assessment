import pdfplumber
import re

def extract_financials_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text()

    revenue = int(re.search(r"revenue[:\s]+(\d+)", text, re.I).group(1))
    expenses = int(re.search(r"expenses[:\s]+(\d+)", text, re.I).group(1))

    return revenue, expenses
