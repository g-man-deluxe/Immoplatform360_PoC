import streamlit as st

def show():
    st.title("🏠 Quick Check – Objektbewertung")

    adresse = st.text_input("Adresse")
    wohnflaeche = st.number_input("Wohnfläche (m²)", min_value=0.0, format="%.2f")
    kaufpreis = st.number_input("Kaufpreis (€)", min_value=0.0, format="%.2f")
    miete_kalt = st.number_input("Monatliche Mieteinnahme (kalt, €)", min_value=0.0, format="%.2f")

    nebenkosten_pct = st.slider("Kaufnebenkostenpauschale (%)", 0, 30, 10)
    finanzierungsanteil = st.slider("Finanzierungsanteil (%)", 0, 100, 90)
    zinssatz = st.slider("Zinssatz (%)", 0.0, 20.0, 2.5, step=0.1)
    tilgung = st.slider("Tilgung (%)", 0.0, 5.0, 1.5, step=0.05)

    if kaufpreis > 0:
        jahresmiete = miete_kalt * 12
        brutto = (jahresmiete / kaufpreis) * 100

        kaufpreis_gesamt = kaufpreis * (1 + nebenkosten_pct / 100)
        netto = (jahresmiete / kaufpreis_gesamt) * 100

        darlehen = kaufpreis_gesamt * (finanzierungsanteil / 100)
        zinslast = darlehen * (zinssatz / 100)
        cashflow = miete_kalt - (zinslast / 12)

        st.subheader("📊 Ergebnisse")
        st.metric("Bruttorendite", f"{brutto:.2f} %")
        st.metric("Nettorendite", f"{netto:.2f} %")
        st.metric("Monatlicher Cashflow", f"{cashflow:.2f} €")
