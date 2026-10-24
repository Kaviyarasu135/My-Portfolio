from pathlib import Path
import streamlit as st

BASE = Path(__file__).parent
st.markdown("""
<style>
.block-container {max-width: 1120px; padding-top: 2.2rem;}
h1, h2, h3 {letter-spacing: -.025em;}
[data-testid="stSidebar"] {border-right: 1px solid rgba(120,120,120,.17);}
</style>
""", unsafe_allow_html=True)

portrait, intro = st.columns([1, 2], gap="large", vertical_alignment="center")
with portrait:
    st.image(str(BASE / "Assets" / "RCL93391.JPG"), use_container_width=True)
with intro:
    st.caption("PORTFOLIO · RECHERCHE & INGÉNIERIE")
    st.title("Kaviyarasu Sakthivel")
    st.subheader("Doctorant-chercheur à l’ESTP")
    st.write("Génie industriel · Jumeaux numériques · Données géospatiales · Construction durable")
    st.caption("📍 Orléans, France")
    st.write(
        "Je suis doctorant-chercheur à l’ESTP, diplômé d’un master en génie industriel "
        "de Centrale Nantes. Mes travaux portent sur l’étude des ressources minérales "
        "pour la construction et la réhabilitation, en mobilisant les données géospatiales "
        "et les approches de jumeau numérique."
    )
    c1, c2 = st.columns(2)
    with c1:
        if st.button("Découvrir mes recherches", use_container_width=True, type="primary"):
            st.switch_page("pages/Projects.py")
    with c2:
        if st.button("Me contacter", use_container_width=True):
            st.switch_page("pages/Contact_me.py")

st.divider()
st.header("Mes domaines d’intérêt")
a, b, c = st.columns(3)
with a:
    st.markdown("#### 🌍 Ressources & environnement")
    st.write("Données environnementales, fiabilité de l’information et utilisation raisonnée des ressources.")
with b:
    st.markdown("#### 🗺️ Géomatique & données")
    st.write("QGIS, traitement de données spatiales et analyse des territoires.")
with c:
    st.markdown("#### 🏗️ Jumeaux numériques")
    st.write("Méthodes numériques appliquées à l’étude du cadre bâti et des matériaux de construction.")

st.divider()
st.header("En ce moment")
st.info("**2026–2029 · ESTP** — Thèse en cours : projet BASTIR, consacré à l’approvisionnement en ressources minérales issues des sols, des terres et des infrastructures.")
st.write("**2026 · ESTP** — Stage de recherche achevé sur la fiabilité des données climatiques et leur utilisation dans les analyses de matérialité.")
st.caption("Ce site présente des travaux réalisés et des recherches en cours ; les objectifs de thèse ne sont pas présentés comme des résultats acquis.")
