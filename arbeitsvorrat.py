import streamlit as st
import uuid

def show():
    st.title("📁 Arbeitsvorrat")

    if "objekte" not in st.session_state:
        st.session_state.objekte = []

    if st.button("➕ Neues Objekt bewerten"):
        with st.form("Neues Objekt", clear_on_submit=True):
            adresse = st.text_input("Adresse")
            plz = st.text_input("Postleitzahl")
            ort = st.text_input("Ort")
            titel = st.text_input("Titel (optional)")
            submitted = st.form_submit_button("Speichern")
            if submitted:
                st.session_state.objekte.append({
                    "id": str(uuid.uuid4()),
                    "adresse": f"{titel + ' – ' if titel else ''}{adresse}, {plz} {ort}",
                    "stadt": ort
                })
                st.success("Objekt wurde gespeichert")
                st.experimental_rerun()

    st.markdown("---")

    for obj in st.session_state.objekte:
        col1, col2, col3, col4 = st.columns([3, 2, 5, 1])
        col1.markdown(f"**{obj['adresse']}**")
        col2.markdown(obj['stadt'])
        with col3:
            st.button("📝", key=f"{obj['id']}_finanz", help="Finanzierungsbescheinigung")
            st.button("👥", key=f"{obj['id']}_bewerbung", help="Bewerbungsmappe")
            st.button("🕸️", key=f"{obj['id']}_beauftrag", help="Beauftragungen")
            st.button("§", key=f"{obj['id']}_vertrag", help="Vertragsprüfung")
            st.button("🏷️", key=f"{obj['id']}_kosten", help="Kosten verwalten")
            st.button("🏢✅", key=f"{obj['id']}_uebernahme", help="Objekt übernehmen")
        with col4:
            if col4.button("🗑️", key=f"{obj['id']}_delete", help="Löschen"):
                st.session_state.objekte = [x for x in st.session_state.objekte if x['id'] != obj['id']]
                st.experimental_rerun()
