
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_report(score, path):
    c = canvas.Canvas(path, pagesize=A4)
    c.drawString(100, 750, f"Financial Health Score: {score}")
    c.save()
