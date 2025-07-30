from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO
import os

def erstelle_pdf(bewertung, standort):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    try:
        logo = "logo.png"
        if os.path.exists(logo):
            c.drawImage(logo, 40, height - 100, width=100, preserveAspectRatio=True)
    except Exception as e:
        print("Logo konnte nicht geladen werden:", e)

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "Immo360 – Immobilienbewertung")

    c.setFont("Helvetica-Bold", 12)
    y = height - 100
    c.drawString(50, y, "📊 Bewertungsergebnisse:")
    c.setFont("Helvetica", 11)
    for key, value in bewertung.items():
        y -= 20
        c.drawString(70, y, f"{key}: {value}")

    y -= 40
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "📍 Standort:")
    c.setFont("Helvetica", 11)
    for key, value in standort.items():
        y -= 20
        c.drawString(70, y, f"{key}: {value}")

    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer
