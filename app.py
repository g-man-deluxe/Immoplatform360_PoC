import streamlit as st
import uuid

st.set_page_config(page_title="Immo360 – Objektvorrat", layout="wide")
st.title("📁 Objektvorrat – Bewertete Immobilien verwalten")

# Beispiel-Datenbank (Session-State)
if "objekte" not in st.session_state:
    st.session_state.objekte = []

# Funktion zum Rendern einer Zeile
def render_objekt_zeile(objekt):
    col1, col2, col3, col4 = st.columns([3, 2, 4, 1])
    col1.markdown(f"**{objekt['adresse']}**")
    col2.markdown(objekt['stadt'])

    with col3:
        st.markdown("""
        <style>.action-icons button {margin-right: 0.25rem;}</style>
        <div class="action-icons">
        """, unsafe_allow_html=True)
        col3_cols = st.columns(6)
        icons = [
            ("📝", "Finanzierungsbescheinigung"),
            ("👥", "Bewerbungsmappe"),
            ("🕸️", "Beauftragungen"),
            ("§", "Vertragsprüfung"),
            ("🏷️", "Kosten verwalten"),
            ("🏢✅", "Objekt übernehmen")
        ]
        for i, (symbol, tooltip) in enumerate(icons):
            col3_cols[i].button(symbol, key=f"{objekt['id']}_{tooltip}", help=tooltip)

    with col4:
        if col4.button("🗑️", key=f"del_{objekt['id']}", help="Löschen"):
            if st.confirm("Willst du dieses Objekt wirklich löschen?"):
                st.session_state.objekte = [o for o in st.session_state.objekte if o['id'] != objekt['id']]
                st.experimental_rerun()

# Objekt hinzufügen
if st.button("➕ Neues Objekt bewerten"):
    with st.form("Neues Objekt", clear_on_submit=True):
        adresse = st.text_input("Adresse")
        plz = st.text_input("Postleitzahl")
        stadt = st.text_input("Ort")
        titel = st.text_input("Titel (optional)")
        submitted = st.form_submit_button("Speichern")
        if submitted:
            st.session_state.objekte.append({
                "id": str(uuid.uuid4()),
                "adresse": f"{titel + ' – ' if titel else ''}{adresse}, {plz} {stadt}",
                "stadt": stadt,
            })
            st.success("Objekt wurde hinzugefügt")
            st.experimental_rerun()

st.markdown("---")

# Liste anzeigen
if st.session_state.objekte:
    st.subheader("📋 Bewertete Objekte")
    for objekt in st.session_state.objekte:
        render_objekt_zeile(objekt)
else:
    st.info("Noch keine Objekte gespeichert. Bitte füge eines hinzu.")
