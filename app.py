import streamlit as st
from bewertung import bewerte_immobilie

st.title("🏠 Immobilienbewertung für Kleinanleger")

st.header("🔢 Eingabemaske")

kaufpreis = st.number_input("Kaufpreis (€)", min_value=50000, max_value=2000000, value=350000, step=5000)
wohnfläche = st.number_input("Wohnfläche (m²)", min_value=20, max_value=500, value=80, step=1)
lage = st.selectbox("Lage", ["einfach", "mittel", "gut", "sehr gut"])
zustand = st.selectbox("Zustand", ["renovierungsbedürftig", "durchschnittlich", "gut", "neuwertig"])
mieteinnahmen = st.number_input("Monatliche Nettokaltmiete (€)", min_value=100, max_value=5000, value=850, step=50)

if st.button("Immobilie bewerten"):
    bewertung = bewerte_immobilie(kaufpreis, wohnfläche, lage, zustand, mieteinnahmen)
    st.success(f"💡 Bewertungsergebnis: {bewertung}")
