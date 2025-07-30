from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import io
from PIL import Image

def erstelle_pdf(bewertung, standort):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4
    try:
        logo = Image.open("logo.png")
        logo_path = "/tmp/logo_temp.png"
        logo.save(logo_path)
        c.drawImage(logo_path, 40, height - 100, width=100, preserveAspectRatio=True)
    except:
        pass

    c.setFont("Helvetica-Bold", 16)
    c.drawString(160, height - 70, "Immo360 – Immobilienbewertung")

    c.setFont("Helvetica", 12)
    y = height - 130
    c.drawString(50, y, "🔢 Bewertungsdaten:")
    y -= 20
    for key, value in bewertung.items():
        c.drawString(70, y, f"{key}: {value}")
        y -= 18

    y -= 10
    c.drawString(50, y, "📍 Standortdaten:")
    y -= 20
    for key, value in standort.items():
        c.drawString(70, y, f"{key}: {value}")
        y -= 18

    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer
