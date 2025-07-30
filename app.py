import streamlit as st
from bewertung import berechne_kennzahlen
from report import erstelle_pdf
from standort import analysiere_standort
from overpass import finde_pois
from PIL import Image
import folium
from streamlit_folium import st_folium

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
        abschicken = st.form_submit_button("✅ Bewertung starten")

    if abschicken:
        result = berechne_kennzahlen(kaufpreis, wohnflaeche, kaltmiete, lage, zustand, zinssatz, laufzeit)
        standortdaten = analysiere_standort(plz)
        st.success("Bewertung abgeschlossen:")
        st.json(result)
        st.subheader("📍 Standortdaten")
        st.json(standortdaten)
        if st.button("📄 Immo360-PDF erstellen"):
            pdf_file = erstelle_pdf(result, standortdaten)
            st.download_button("Download PDF", pdf_file, file_name="immo360_bewertung.pdf")

with tabs[1]:
    st.subheader("🔍 Individuelle Standortanalyse")
    plz_input = st.text_input("Postleitzahl eingeben", "")
    if plz_input:
        result = analysiere_standort(plz_input)
        st.write(result)

with tabs[2]:
    st.subheader("🗺 Standortkarte mit POIs")
    plz_map = st.text_input("PLZ für Karte", "04109")
    ort = analysiere_standort(plz_map)
    if "Latitude" in ort and "Longitude" in ort:
        lat, lon = float(ort["Latitude"]), float(ort["Longitude"])
        m = folium.Map(location=[lat, lon], zoom_start=14)
        folium.Marker([lat, lon], popup=ort.get("Ort", "Standort"), icon=folium.Icon(color="blue")).add_to(m)

        pois = finde_pois(lat, lon)
        for poi in pois:
            icon = "green"
            if poi["typ"] == "supermarket":
                icon = "red"
            elif poi["typ"] in ["school", "kindergarten"]:
                icon = "orange"
            elif poi["typ"] == "platform":
                icon = "gray"
            folium.Marker(
                [poi["lat"], poi["lon"]],
                popup=f"{poi['typ'].capitalize()}: {poi['name']}",
                icon=folium.Icon(color=icon, icon="info-sign")
            ).add_to(m)

        st_folium(m, width=700, height=500)
