from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO
import os

def erstelle_pdf(bewertung, standort):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    # Titel
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "Immo360 – Immobilienbewertung")

    # Bewertungsdaten
    c.setFont("Helvetica-Bold", 12)
    y = height - 100
    c.drawString(50, y, "📊 Bewertungsergebnisse:")
    c.setFont("Helvetica", 11)
    for key, value in bewertung.items():
        y -= 20
        c.drawString(70, y, f"{key}: {value}")

    # Standortdaten
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
