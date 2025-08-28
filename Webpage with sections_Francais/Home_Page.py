import streamlit as st

st.set_page_config(page_title="Page web de Kaviyarasu", page_icon=":material/star:", layout="wide")

# Original text translated into formal French
Digital_resume = st.Page(
    page="pages/Digital_resume.py",
    title="CV numérique",
    icon=":material/digital_wellbeing:",
)
about_page = st.Page(
    page="pages/Home.py",  # Restored as the home page
    title="Accueil",
    icon=":material/home:",
    default=True,  # Set as the default page
)
project_1_page = st.Page(
    page="pages/About_me.py",
    title="À propos de moi",
    icon=":material/account_circle:",
)
project_2_page = st.Page(
    page="pages/Experience.py",
    title="Expérience",
    icon=":material/rocket_launch:",
)
project_3_page = st.Page(
    page="pages/Projects.py",
    title="Projets",
    icon=":material/smart_toy:",
)
project_4_page = st.Page(
    page="pages/Skills.py",
    title="Compétences",
    icon=":material/tactic:",
)
project_5_page = st.Page(
    page="pages/Core_Competencies.py",
    title="Compétences fondamentales",
    icon=":material/psychology:",
)
project_6_page = st.Page(
    page="pages/Contact_me.py",
    title="Contactez-moi",
    icon=":material/contact_mail:",
)

pg = st.navigation(
    [Digital_resume, about_page, project_1_page, project_2_page, project_3_page, project_4_page, project_5_page, project_6_page]
)

st.sidebar.text("Réalisé par Kaviyarasu")
pg.run()

