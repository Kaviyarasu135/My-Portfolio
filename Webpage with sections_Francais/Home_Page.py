import streamlit as st

st.set_page_config(page_title="Kaviyarasu Sakthivel | Portfolio", page_icon="🎓", layout="wide")

home = st.Page("pages/Home.py", title="Accueil", icon=":material/home:", default=True)
research = st.Page("pages/Projects.py", title="Recherche & projets", icon=":material/science:")
journey = st.Page("pages/Experience.py", title="Parcours", icon=":material/school:")
skills = st.Page("pages/Skills.py", title="Compétences", icon=":material/code:")
contact = st.Page("pages/Contact_me.py", title="Contact & CV", icon=":material/mail:")

st.navigation([home, research, journey, skills, contact]).run()
st.sidebar.caption("Kaviyarasu Sakthivel · Orléans, France")
