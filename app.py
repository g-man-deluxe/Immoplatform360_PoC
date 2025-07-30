import streamlit as st
import pandas as pd
import json
from PIL import Image
from bewertung import berechne_kennzahlen
from standort import analysiere_standort
from overpass import finde_pois
import folium
from streamlit_folium import st_folium
from folium.plugins import HeatMap

# Login-System
def check_login():
    st.sidebar.title("🔐 Login")
    user = st.sidebar.text_input("Benutzername")
    pw = st.sidebar.text_input("Passwort", type="password")
    with open("users.json") as f:
        user_data = json.load(f)
    if st.sidebar.button("Anmelden"):
        if user in user_data and user_data[user] == pw:
            st.session_state["user"] = user
            st.experimental_rerun()
        else:
            st.sidebar.error("Zugangsdaten ungültig.")

if "user" not in st.session_state:
    check_login()
    st.stop()

# Immo360 UI
st.set_page_config(page_title="Immo360 – Immobilienbewertung", layout="centered")
logo = Image.open("logo.png")
st.image(logo, width=120)
st.title("🏠 Immo360 – Immobilienbewertung für Kleinanleger")

tabs = st.tabs(["🏘 Objektbewertung", "📍 Standortanalyse & Karte", "💶 Preis-Heatmap"])

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

with tabs[1]:
    st.subheader("📍 Adresse eingeben")
    plz_map = st.text_input("PLZ", "04109")
    str_map = st.text_input("Straße", "Augustusplatz")
    nr_map = st.text_input("Hausnummer", "1")

    if plz_map:
        ort = analysiere_standort(plz_map, str_map, nr_map)
        if "Latitude" in ort and "Longitude" in ort:
            st.success(f"📍 Standort: {ort.get('Ort')}")
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
        else:
            st.warning("⚠️ Standort konnte nicht bestimmt werden.")
with tabs[2]:
    st.subheader("💶 Kaufpreis-Heatmap für München & Hamburg")
    selected_city = st.selectbox("Stadt auswählen", ["München", "Hamburg"])
    df = pd.read_csv("preise.csv")
    df_city = df[df["stadt"] == selected_city]
    m = folium.Map(location=[df_city["lat"].mean(), df_city["lon"].mean()], zoom_start=12)
    heat_data = [[row["lat"], row["lon"], row["price"]] for _, row in df_city.iterrows()]
    HeatMap(heat_data, radius=15, blur=10, max_zoom=13).add_to(m)
    st_folium(m, width=700, height=500)
