
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Immo360", layout="wide")

st.title("🏡 Immo360")

tabs = st.tabs(["🏘 Objektbewertung", "📍 Standortanalyse & Karte", "💶 Preis-Heatmap", "📈 Analyse & Prognose", "📊 Wertentwicklung (Excel-Modell)"])

with tabs[4]:
    st.subheader("📊 Wertentwicklung (Excel-Modell)")

    st.markdown("Gib die Eckwerte deiner Vermietung ein:")

    startmiete = st.number_input("Startmiete pro Monat (€)", min_value=100, max_value=10000, value=1250, step=50)
    steigerung = st.number_input("Jährliche Mietsteigerung (%)", min_value=0.0, max_value=10.0, value=2.0, step=0.5)
    sanierung_jahr_5 = st.number_input("Sanierungskosten in Jahr 5 (€)", min_value=0, max_value=50000, value=0, step=500)
    investitionskosten = st.number_input("Gesamte Investitionskosten (€)", min_value=50000, max_value=2000000, value=200000, step=1000)

    if st.button("📈 Wertentwicklung berechnen"):
        jahre = list(range(1, 11))
        mieten_monat = [startmiete]
        for i in range(1, 10):
            neue_miete = mieten_monat[-1] * (1 + steigerung / 100)
            mieten_monat.append(round(neue_miete, 2))

        mieten_jahr = [round(m*12, 2) for m in mieten_monat]
        summe_miete = sum(mieten_jahr)
        summe_miete_nach_sanierung = summe_miete - sanierung_jahr_5 if sanierung_jahr_5 else summe_miete
        rendite = summe_miete_nach_sanierung / investitionskosten * 100

        df = pd.DataFrame({
            "Jahr": jahre,
            "Miete pro Monat (€)": mieten_monat,
            "Miete pro Jahr (€)": mieten_jahr
        })

        st.dataframe(df, use_container_width=True)
        st.markdown(f"**📌 Summe Mieteinnahmen (10 Jahre): {summe_miete:,.2f} €**")
        if sanierung_jahr_5:
            st.markdown(f"**🔧 Abzüglich Sanierung: {summe_miete_nach_sanierung:,.2f} €**")
        st.markdown(f"**💰 Rendite bezogen auf {investitionskosten:,.0f} €: {rendite:.2f}%**")
