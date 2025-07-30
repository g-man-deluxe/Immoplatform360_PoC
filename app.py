import streamlit as st
from bewertung import berechne_kennzahlen
from report import erstelle_pdf

st.title("🏠 Immobilienbewertung für Kleininvestoren – PoC 2.0")

with st.form("immobilien_formular"):
    st.subheader("📥 Objektdaten")
    kaufpreis = st.number_input("Kaufpreis (€)", 50000, 2000000, 350000, 1000)
    wohnflaeche = st.number_input("Wohnfläche (m²)", 20, 500, 80, 1)
    kaltmiete = st.number_input("Monatliche Kaltmiete (€)", 100, 5000, 850, 50)
    lage = st.selectbox("Lage", ["einfach", "mittel", "gut", "sehr gut"])
    zustand = st.selectbox("Zustand", ["renovierungsbedürftig", "durchschnittlich", "gut", "neuwertig"])
    baujahr = st.number_input("Baujahr", 1900, 2025, 1995)
    zinssatz = st.slider("Zinssatz (%)", 0.5, 10.0, 4.0, 0.1)
    laufzeit = st.slider("Finanzierungslaufzeit (Jahre)", 5, 35, 25, 1)
    abschicken = st.form_submit_button("✅ Bewertung starten")

if abschicken:
    result = berechne_kennzahlen(kaufpreis, wohnflaeche, kaltmiete, lage, zustand, zinssatz, laufzeit)
    st.success("Bewertung abgeschlossen:")
    st.json(result)
    if st.button("📄 PDF erstellen"):
        pdf_file = erstelle_pdf(result)
        st.download_button("Download PDF", pdf_file, file_name="immobilienbewertung.pdf")
