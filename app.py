import streamlit as st

st.set_page_config(page_title="Immo360 Quick Check", layout="wide")
st.title("🏘 Objektbewertung – Quick Check")

st.markdown("Fülle die Felder aus, um die Brutto-, Nettorendite und den monatlichen Cashflow zu berechnen.")

# Eingabefelder mit Standardwerten
adresse = st.text_input("Adresse des Objekts (optional)", "")
wohnflaeche = st.number_input("Wohnfläche (m²)", min_value=10, max_value=1000, value=80)
kaufpreis = st.number_input("Kaufpreis (€)", min_value=10000, max_value=10000000, value=400000, step=1000)
mieteinnahmen_kalt = st.number_input("Monatliche Kaltmiete (€)", min_value=100, max_value=10000, value=1200, step=50)

kaufnebenkosten_pct = st.slider("Kaufnebenkostenpauschale (%)", min_value=0, max_value=30, value=10)
finanzierungsanteil = st.slider("Finanzierungsanteil (%)", min_value=0, max_value=100, value=90)
zinssatz = st.slider("Zinssatz (%)", min_value=0.0, max_value=20.0, value=4.0, step=0.1)
tilgung = st.slider("Tilgungsrate (%)", min_value=0.0, max_value=5.0, value=1.5, step=0.01)

# Berechnung
kaltmiete_jahr = mieteinnahmen_kalt * 12
bruttorendite = (kaltmiete_jahr / kaufpreis) * 100

kaufpreis_gesamt = kaufpreis + (kaufpreis * kaufnebenkosten_pct / 100)
nettorendite = (kaltmiete_jahr / kaufpreis_gesamt) * 100

darlehen = kaufpreis_gesamt * (finanzierungsanteil / 100)
zinslast_jahr = darlehen * (zinssatz / 100)
cashflow_monat = mieteinnahmen_kalt - (zinslast_jahr / 12)

# Ausgabe
st.markdown("---")
st.subheader("📈 Ergebnis")

col1, col2, col3 = st.columns(3)
col1.metric("Bruttorendite", f"{bruttorendite:.2f} %")
col2.metric("Nettorendite", f"{nettorendite:.2f} %")
col3.metric("Cashflow (monatlich)", f"{cashflow_monat:,.2f} €", delta=None if cashflow_monat >= 0 else "negativ")

# Farbliche Hervorhebung bei negativem Cashflow
if cashflow_monat < 0:
    st.warning(f"🚨 Der monatliche Cashflow ist negativ: {cashflow_monat:,.2f} €")

st.markdown("---")
st.caption("Immo360 – Quick Check zur Erstbewertung deiner Investition")
