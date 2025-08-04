import streamlit as st
from views import quick_check, dashboard, arbeitsvorrat

st.set_page_config(page_title="Immo360", layout="wide")
st.sidebar.image("assets/logo.png", use_column_width=True)
st.sidebar.title("Immo360 Navigation")

page = st.sidebar.radio("Seite auswählen", ["Dashboard", "Quick Check", "Arbeitsvorrat"])

if page == "Dashboard":
    dashboard.show()
elif page == "Quick Check":
    quick_check.show()
elif page == "Arbeitsvorrat":
    arbeitsvorrat.show()
