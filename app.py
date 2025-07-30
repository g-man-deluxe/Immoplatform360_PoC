import streamlit as st
from report import erstelle_pdf

st.set_page_config(page_title="Immo360 PDF Test")

st.title("📄 PDF Export testen")

# Dummy-Daten
bewertung = {
    "Kaufpreis pro m²": "4.375 €",
    "Bruttorendite (%)": "2.91",
    "Annuität (€)": "1.847,43",
    "Score-Faktor": "0.56",
    "Einschätzung": "🔴 kritisch"
}

standort = {
    "Ort": "Leipzig, Sachsen",
    "Latitude": "51.34",
    "Longitude": "12.38"
}

if st.button("📄 PDF erstellen"):
    pdf_file = erstelle_pdf(bewertung, standort)
    st.download_button("PDF herunterladen", pdf_file, file_name="immo360_bewertung.pdf")
