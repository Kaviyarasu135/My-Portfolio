import streamlit as st

st.set_page_config(page_title="Page web de Kaviyarasu", page_icon=":material/star:", layout="wide")

# Original text translated into formal French

Digital_resume = st.Page(
    page="views/Digital_Resume.py",
    title="CV numérique",
    icon=":material/digital_wellbeing:",
)
about_page = st.Page(
    page="views/Home.py",
    title="Accueil",
    icon=":material/home:",
    default=True,
)
project_1_page = st.Page(
    page="views/About_me.py",
    title="À propos de moi",
    icon=":material/account_circle:",
)
project_2_page = st.Page(
    page="Views/Experience.py",
    title="Expérience",
    icon=":material/rocket_launch:",
)
project_3_page = st.Page(
    page="views/Projects.py",
    title="Projets",
    icon=":material/smart_toy:",
)
project_4_page = st.Page(
    page="Views/Skills.py",
    title="Compétences",
    icon=":material/tactic:",
)
project_5_page = st.Page(
    page="Views/Core_Competencies.py",
    title="Compétences fondamentales",
    icon=":material/psychology:",
)
project_6_page = st.Page(
    page="Views/Contact_me.py",
    title="Contactez-moi",
    icon=":material/contact_mail:",
)


pg = st.navigation(
        [Digital_resume,about_page,project_1_page, project_2_page, project_3_page, project_4_page, project_5_page, project_6_page],
)

#st.sidebar.image("Assets/Kaviyarasu_LOGO.png",width=200)
st.sidebar.text("Réalisé par Kaviyarasu")
#st.logo("Assets/Kaviyarasu.png")

pg.run()





