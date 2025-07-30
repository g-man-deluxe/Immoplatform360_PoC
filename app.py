import streamlit as st
from bewertung import berechne_kennzahlen
from report import erstelle_pdf
from standort import analysiere_standort
from overpass import finde_pois
from PIL import Image
import folium
from streamlit_folium import st_folium
import pandas as pd

st.set_page_config(page_title="Immo360 – Immobilienbewertung", layout="centered")
logo = Image.open("logo.png")
st.image(logo, width=120)
st.title("🏠 Immo360 – Immobilienbewertung für Kleinanleger")

tabs = st.tabs(["🏘 Objektbewertung", "📍 Standortanalyse", "🗺 Karte mit POIs"])

with tabs[0]:
    st.subheader("📥 Objektdaten")
    with st.form("immobilien_formular"):
        kaufpreis = st.number_input("Kaufpreis (€)", 50000, 2000000, 350000, 1000)
        wohnflaeche = st.number_input("Wohnfläche (m²)", 20, 500, 80, 1)
        kaltmiete = st.number_input("Monatliche Kaltmiete (€)", 100, 5000, 850, 50)
        lage = st.selectbox("Lage", ["einfach", "mittel", "gut", "sehr gut"])
        zustand = st.selectbox("Zustand", ["renovierungsbedürftig", "durchschnittlich", "gut", "neuwertig"])
        baujahr = st.number_input("Baujahr", 1900, 2025, 1995)
        zinssatz = st.slider("Zinssatz (%)", 0.5, 10.0, 4.0, 0.1)
        laufzeit = st.slider("Finanzierungslaufzeit (Jahre)", 5, 35, 25, 1)
        plz = st.text_input("Postleitzahl", "04109")
        strasse = st.text_input("Straße", "Augustusplatz")
        hausnr = st.text_input("Hausnummer", "1")
        abschicken = st.form_submit_button("✅ Bewertung starten")

    if abschicken:
        result = berechne_kennzahlen(kaufpreis, wohnflaeche, kaltmiete, lage, zustand, zinssatz, laufzeit)
        standortdaten = analysiere_standort(plz, strasse, hausnr)

        st.success("🏁 Bewertung abgeschlossen")
        st.subheader("📊 Bewertungsergebnisse")
        df_result = pd.DataFrame(result.items(), columns=["Kennzahl", "Wert"])
        st.table(df_result)

        st.subheader("🧠 Bewertung")
        if result["Einschätzung"] == "🔴 kritisch":
            st.error("Die Immobilie wird als *kritisch* eingestuft.")
        else:
            st.success("Die Immobilie erscheint *attraktiv*.")

        st.subheader("📍 Standort")
        st.markdown(f"**Adresse:** {standortdaten.get('Ort', '–')}")
        st.markdown(f"**Koordinaten:** {standortdaten.get('Latitude')} / {standortdaten.get('Longitude')}")

        if st.button("📄 Immo360-PDF erstellen"):
            pdf_file = erstelle_pdf(result, standortdaten)
            st.download_button("Download PDF", pdf_file, file_name="immo360_bewertung.pdf")
